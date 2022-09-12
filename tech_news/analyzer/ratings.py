from operator import itemgetter
from tech_news.database import find_news
from tech_news.database import db


# Requisito 10
def top_5_news():
    ordered_news = list()
    rating_news = sorted(
        find_news(), key=itemgetter("comments_count"), reverse=True)

    for rating in rating_news[:5]:
        ordered_news.append((rating["title"], rating["url"]))
    return ordered_news


# Requisito 11
def top_5_categories():
    ordered_news = list(
        db.news.aggregate(
            list((
                {"$group": {"_id": "$category", "count": {"$sum": 1}}},
                {"$sort": {"count": -1, "_id": 1}},
            ))
        )
    )

    return [category["_id"] for category in ordered_news[:5]]
