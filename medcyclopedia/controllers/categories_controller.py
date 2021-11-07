
from typing import List

from ninja.router import Router
from config.utils.schemas import MessageOut
from config.utils.utils import response

from medcyclopedia.models import Category
from medcyclopedia.schemas import ArticleSchema, CategoriesSchema


categories_controller = Router(tags=['categories'])


@categories_controller.get('/', response={200: List[CategoriesSchema], 404: MessageOut})
def get_categories(request):
    categories = Category.objects.all()
    if not categories.exists():
        return response(404, {'message': 'not found'})
    return response(200, categories)


@categories_controller.get('/categories/{id}', response={200: CategoriesSchema, 404: MessageOut})
def get_category(request, id: int):
    category = Category.objects.get(id=id)
    if not category:
        return response(404, {'message': 'not found'})
    return response(200, category)


@categories_controller.post('/', response={201: CategoriesSchema, 400: MessageOut})
def create_category(request, category_in: CategoriesSchema):
    category = Category.objects.create(**category_in.dict())
    category.save()
    return response(201, category)


@categories_controller.put('/{id}', response={200: CategoriesSchema, 404: MessageOut})
def update_category(request, id: int, category: CategoriesSchema):
    category = Category.objects.get(id=id)
    if not category:
        return response(404, {'message': 'not found'})
    category.update(**category.dict())
    return response(200, category)


@categories_controller.delete('/{id}', response={200: MessageOut, 404: MessageOut})
def delete_category(request, id: int):
    category = Category.objects.get(id=id)
    if not category:
        return response(404, {'message': 'not found'})
    category.delete()
    return response(200, {'message': 'deleted'})


@categories_controller.get('/{id}/articles', response={200: List[ArticleSchema], 404: MessageOut})
def get_articles_by_category(request, id: int):
    category = Category.objects.get(id=id)
    if not category:
        return response(404, {'message': 'not found'})
    return response(200, category.articles)
