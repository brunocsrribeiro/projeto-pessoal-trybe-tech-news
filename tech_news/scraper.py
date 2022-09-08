import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news = list()

    for new in selector.css("div.post-inner"):
        url_news = new.css("header.entry-header h2 a::attr(href)").getall()
        news.extend(url_news)
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector = Selector(html_content)
        url_next_page = selector.css(
            "div.nav-links > a.next::attr(href)").get()
    except ValueError:
        return None
    else:
        return url_next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
