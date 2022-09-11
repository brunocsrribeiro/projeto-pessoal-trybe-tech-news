from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = list()
    # $regex e "$options": "i" -> encontrados neste link:
    # https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
    get_title = search_news({"title": {"$regex": title, "$options": "i"}})

    for title_news in get_title:
        news.append((title_news["title"], title_news["url"]))
    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
