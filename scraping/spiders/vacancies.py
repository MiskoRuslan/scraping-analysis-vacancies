from typing import Iterable

import scrapy
from scrapy import Request


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["parsemachine.com"]
    start_urls = ["https://parsemachine.com"]

    def parse(self, response):
        pass
