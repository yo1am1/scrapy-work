import dataclasses
from typing import Optional

import scrapy


@dataclasses.dataclass(frozen=True)
class Vacancy:
    url: str
    title: str
    location: str
    description: str
    salary_min: Optional[str] = None
    salary_max: Optional[str] = None
    vip: bool = False
    workers: Optional[str] = None
    views: Optional[str] = None


class VacancySpider(scrapy.Spider):
    name = "VacanciesSpider"
    start_urls = [
        "https://www.work.ua/jobs-python/",
        "https://www.work.ua/jobs-it-python/",
    ]

    def parse(self, response):
        cards = response.css("h2 a")
        for card in cards:
            job_link = card.attrib["href"]
            yield response.follow(job_link, callback=self.parse_vacancy)

        next_page = response.css("nav li a::attr(href)").extract()[-1]
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_vacancy(self, response):
        url = response.url
        title = get_title(response)
        location = get_location(response)
        description = get_description(response)
        salary = get_salary(response)
        vip = get_vip(response)
        workers = get_workers(response)
        views = response.css("#js-active-users-msg::text").get().strip()

        vacancy_data = Vacancy(
            url=url,
            title=title,
            location=location,
            salary_min=salary["min"],
            salary_max=salary["max"],
            description=description,
            vip=vip,
            workers=workers,
            views=views,
        )
        yield vacancy_data


def get_views(response):
    response.css("#js-active-users-msg::text").get().strip()


def get_workers(response):
    return response.css("span.nowrap::text").get().replace(" ", " ")


def get_vip(response):
    return response.css("div p span::text").extract()[1] == "VIP"


def get_title(response):
    return response.css("h1::text").get()


def get_description(response):
    job_field = response.css("#job-description")
    job_description = job_field.xpath("normalize-space()").get()
    return job_description


def get_location(response):
    for p in response.css("p"):
        try:
            if p.css("span").attrib["title"] == "Адреса роботи":
                return p.xpath("normalize-space()").get().split(".")[0]
            elif p.css("span").attrib["title"] == "Місце роботи":
                return p.xpath("normalize-space()").get()
        except KeyError:
            pass
    return None


def get_salary(response):
    salary = {"min": None, "max": None}
    for par in response.css("p"):
        try:
            if par.css("span").attrib["title"] == "Зарплата":
                salary_info = par.xpath("normalize-space()").get().split(".")[0]
                salary_value = (
                    salary_info.split("грн")[0].replace("\u202f", "_").split("\u2009")
                )
                salary["min"] = f"{int(salary_value[0])} грн"
                salary["max"] = f"{int(salary_value[2])} грн"
        except (KeyError, TypeError, IndexError, ValueError):
            pass
    if salary["max"] is None and salary["min"]:
        salary["max"] = salary["min"]
    return salary
