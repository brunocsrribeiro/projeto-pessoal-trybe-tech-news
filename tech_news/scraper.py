import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3)
        response.raise_for_status()
        sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    sel = Selector(html_content)
    news = list()

    for new in sel.css("div.post-inner"):
        url_news = new.css("header.entry-header h2 a::attr(href)").getall()
        news.extend(url_news)
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        sel = Selector(html_content)
        url_next_page = sel.css(
            "div.nav-links > a.next::attr(href)").get()
    except ValueError:
        return None
    else:
        return url_next_page


# Requisito 4
def scrape_noticia(html_content):
    sel = Selector(html_content)

    dict_news = {
        "url": sel.css("link[rel='canonical']::attr(href)").get(),
        "title": sel.css("h1.entry-title::text").get().strip(),
        "timestamp": sel.css("li.meta-date::text").get(),
        "writer": sel.css("span.author a::text").get(),
        "comments_count": len(sel.css("div#comments").getall()),
        "summary": "".join(
            sel.css("div.entry-content > p:nth-of-type(1) *::text").getall()
            ).strip(),
        "tags": sel.css("a[rel='tag']::text").getall(),
        "category": sel.css("div.meta-category a span.label::text").get()
    }

    return dict_news


# Requisito 5
def get_tech_news(amount):
    url_base = "https://blog.betrybe.com/"
    latest_news = list()
    url_news = list()

    while len(latest_news) < amount:
        latest_news.extend(scrape_novidades(fetch(url_base)))
        url_base = scrape_next_page_link(fetch(url_base))

    for url in latest_news[:amount]:
        url_news.append(scrape_noticia(fetch(url)))

    create_news(url_news)

    return url_news
