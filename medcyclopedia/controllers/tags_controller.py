from typing import List
from config.utils.utils import response
from ninja.router import Router

from config.utils.schemas import MessageOut
from medcyclopedia.models import Tag

from medcyclopedia.schemas import TagSchema, TagSchemaOut


tags_controller = Router(tags=['tags'])


@tags_controller.get('/', response={200: List[TagSchemaOut], 404: MessageOut})
def get_tags(request):
    tag = Tag.objects.all()
    if not tag.exists():
        return response(404, {'message': 'not found'})
    return response(200, tag)


@tags_controller.post('/', response={201: TagSchema, 400: MessageOut})
def create_tag(request, tag_in: TagSchema):
    tag = Tag.objects.create(**tag_in.dict())
    tag.save()
    return response(201, tag)


@tags_controller.get('/{id}', response={200: TagSchema, 404: MessageOut})
def get_tag(request, id: int):
    tag = Tag.objects.get(id=id)
    if tag == None:
        return response(404, {'message': 'not found'})
    return response(200, tag)


@tags_controller.put('/{id}', response={200: TagSchema, 404: MessageOut})
def update_tag(request, id: int, tag: TagSchema):
    tag = Tag.objects.filter(id=id)
    if not tag.exists():
        return response(404, {'message': 'not found'})
    tag.update(**tag.dict())
    return response(200, tag)


@tags_controller.delete('/{id}', response={200: MessageOut, 404: MessageOut})
def delete_tag(request, id: int):
    tag = Tag.objects.filter(id=id)
    if not tag.exists():
        return response(404, {'message': 'not found'})
    tag.delete()
    return response(200, {'message': 'deleted'})


@tags_controller.get('/{id}/articles', response={200: List[TagSchema], 404: MessageOut})
def get_articles_by_tag(request, id: int):
    tag = Tag.objects.filter(id=id)
    if not tag.exists():
        return response(404, {'message': 'not found'})
    return response(200, tag.articles)


@tags_controller.get('/{id}/drugs', response={200: TagSchema, 404: MessageOut})
def get_drugs_by_tag(request, id: int):
    tag = Tag.objects.filter(id=id)
    if not tag.exists():
        return response(404, {'message': 'not found'})
    return response(200, tag.drugs)
