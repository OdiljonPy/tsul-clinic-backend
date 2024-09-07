from django.core.paginator import Paginator
from django.db.models import Count

from ..serializers import NewsSerializer


def get_news(context: dict, page: int, page_size: int, response):
    news_query = response.order_by('-created_at')
    total_count = news_query.aggregate(total_count=Count('id'))['total_count']

    paginator = Paginator(news_query, page_size)
    balance = paginator.get_page(page)

    responses = {
        "totalElements": total_count,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(balance),
        "first": not balance.has_previous(),
        "last": not balance.has_next(),
        "empty": total_count == 0,
        "content": NewsSerializer(balance, many=True, context=context).data,
    }
    return responses
