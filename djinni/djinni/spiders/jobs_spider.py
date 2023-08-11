import dataclasses
from typing import Optional

import scrapy


@dataclasses.dataclass(frozen=True)
class VacancyDjinni:
    url: str
    title: str
    location: str
    additional: list
    publication_date: str
    description: str = None
    views: Optional[str] = None
    calls: Optional[str] = None


class VacancySpider(scrapy.Spider):
    name = "DjinniSpider"
    start_urls = [
        "https://djinni.co/jobs/?primary_keyword=Python",
    ]

    def parse(self, response, **kwargs):
        cards: list = response.css(".col-md-8 > main a.profile::attr(href)").getall()

        for card in cards:
            job_link = card
            yield response.follow(job_link, callback=self.parse_vacancy)

        next_page: str = response.css("a.page-link::attr(href)").extract()[-1]
        print(next_page)
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_vacancy(self, response) -> VacancyDjinni:
        url = response.url
        title = get_title(response)
        location = get_location(response)
        additional = get_additional_info(response)
        calls = get_calls(response)
        publication_date = get_publication_date(response)
        views = get_views(response)
        description = get_description(response)

        vacancy_data = VacancyDjinni(
            url=url,
            title=title,
            location=location,
            additional=additional,
            calls=calls,
            publication_date=publication_date,
            views=views,
            description=description,
        )
        yield vacancy_data


def get_title(response):
    title = response.css("h1::text").getall()[0].strip().replace(" ", "")
    return title


def get_location(response):
    location = (
        response.css("span.location-text::text")
        .extract()[-1]
        .strip()
        .replace(" ", "")
        .replace("\n", "")
    )

    return location


def get_additional_info(response):
    job_info = response.css(".card > ul > li > div::text").getall()

    answer = []
    for string in job_info:
        string = string.strip()
        if string not in ["", "\n", ","]:
            answer.append(string)

    return answer


def get_calls(response):
    calls = response.css("p.text-muted::text").extract()[-1].strip()

    return calls


def get_publication_date(response):
    publication_date = (
        response.css("p.text-muted::text")
        .extract()[1]
        .strip()
        .replace(" ", "")
        .replace("\n", "")
        .split("опублікована")[-1]
        .strip()
    )

    return publication_date


def get_views(response):
    views = response.css("p.text-muted::text").extract()[3].strip()

    return views


def get_description(response):
    job_description: list = response.css(".mb-4::text").getall()
    for string in job_description:
        string = string.strip()
        if string not in ["", "\n", ","]:
            return string

    return None
