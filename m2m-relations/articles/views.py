from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    articles = Article.objects.all().prefetch_related('scopes').order_by('-published_at')
    for article in articles:
        for scope in article.scopes.all():
            articleset = scope.articlesection_set.get(article=article)
            scope.common_section = articleset.common_section
    context = {'object_list': articles}

    return render(request, template, context)
