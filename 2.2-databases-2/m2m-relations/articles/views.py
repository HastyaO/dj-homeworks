from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    return render(
        request,
        'articles/news.html',
        context={
            'object_list': Article.objects.order_by('-published_at')
        }
    )
