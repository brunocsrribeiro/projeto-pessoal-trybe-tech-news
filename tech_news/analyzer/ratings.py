# Requisito 10
from operator import itemgetter
from tech_news.database import find_news


def top_5_news():
    ordered_news = list()
    rating_news = sorted(
        find_news(), key=itemgetter("comments_count"), reverse=True)

    for rating in rating_news[:5]:
        ordered_news.append((rating["title"], rating["url"]))
    return ordered_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
