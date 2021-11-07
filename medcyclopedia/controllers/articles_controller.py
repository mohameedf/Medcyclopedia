from typing import List
from config.utils.utils import response
# from django.shortcuts import render
from ninja import Router

from config.utils.schemas import MessageOut
from medcyclopedia.models import Article, Tag
from medcyclopedia.schemas import ArticleSchema, ArticleSchemaIn
# from config.utils import status


articles_controller = Router(tags=['articles'])


@articles_controller.get('/', response={200: List[ArticleSchema], 404: MessageOut})
def get_articles(request):
    articles = Article.objects.all()
    if not articles.exists():
        return response(404, {'message': 'not found'})
    return response(200, articles)


@articles_controller.post('/', response={201: ArticleSchema, 400: MessageOut})
def create_article(request, article_in: ArticleSchemaIn):
    tags = article_in.tag
    del article_in.tags
    article = Article.objects.create(**article_in.dict())
    article.save()
    for tag in tags:
        article.tag.add(Tag.objects.get(id=tag))
    article.save()
    return response(201, article)


@articles_controller.get('/{id}', response={200: ArticleSchema, 404: MessageOut})
def get_article(request, id):
    article = Article.objects.filter(id=id)
    if not article.exists():
        return response(404, {'message': 'not found'})

    return response(200, article)


@articles_controller.put('/{id}', response={200: ArticleSchema, 404: MessageOut})
def update_article(request, id, article_in: ArticleSchemaIn):
    article = Article.objects.get(id=id)
    if article == None:
        return response(404, {'message': 'not found'})
    article.tag.clear()
    if article_in.tag != None:
        for tag in article_in.tag:
            article.tag.add(Tag.objects.get(id=tag))

    article.save()

    return response(200, article)


@articles_controller.delete('/{id}', response={200: MessageOut, 404: MessageOut})
def delete_article(request, id):
    article = Article.objects.filter(id=id)
    if not article.exists():
        return response(404, {'message': 'not found'})

    article.delete()

    return response(200, {'message': 'deleted'})
