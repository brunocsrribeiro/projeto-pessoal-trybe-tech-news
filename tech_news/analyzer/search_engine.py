from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search_news_title = list()
    # $regex e "$options": "i" -> encontrados neste link:
    # https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
    get_title = search_news({"title": {"$regex": title, "$options": "i"}})

    for title_news in get_title:
        search_news_title.append((title_news["title"], title_news["url"]))
    return search_news_title


# Requisito 7
def search_by_date(date):
    try:
        search_news_date = list()
        format_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        get_date = search_news({"timestamp": format_date})

        for date_news in get_date:
            search_news_date.append((date_news["title"], date_news["url"]))

        return search_news_date
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    search_news_tags = list()
    get_tags = search_news({"tags": {"$regex": tag, "$options": "i"}})

    for tags_news in get_tags:
        search_news_tags.append((tags_news["title"], tags_news["url"]))
    return search_news_tags


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
