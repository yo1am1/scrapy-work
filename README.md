# Scrapy-work: Work.ua Scraper for Python Developer Vacancies

## Installation and Usage 🧠
🥐 **Note: At the moment, the scraper only supports Work.ua. Updates and additional website support are coming soon!**


1. **_Clone_** the repository:
    ```bash
    git clone https://github.com/yo1am1/scrapy-work.git
    ```

2. **_Navigate_** to the project directory and either open it in PyCharm or use the terminal.

3. **_Install_** the [requirements.txt](requirements.txt):
    ```bash
    pip install -r requirements.txt
    ```
    > The `requirements.txt` file contains all the dependencies needed to run the scraper locally.
    
4. **_Run_** web scrapper with command:
    ```bash
    scrapy crawl VacanciesSpider -O data.json
    ```
    > Where `VacanciesSpider` - is the name of the scrapper, `-O data.json` - rewrites our data to [data.json](/workua/data.json) file.
    
    > ⚠️ Use this command inside the project folder

5. ### _Good luck at finding job_!

## License
This project is licensed under the [MIT License](LICENSE.md).
