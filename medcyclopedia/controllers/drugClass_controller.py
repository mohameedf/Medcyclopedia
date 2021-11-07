from typing import List
from config.utils.utils import response
from ninja.router import Router
from config.utils.schemas import MessageOut
from medcyclopedia.models import DrugClass

from medcyclopedia.schemas import DrugClassSchemaIn, DrugClassSchemaOut, DrugSchemaOut


drugClass_controller = Router(tags=['drugClass'])


@drugClass_controller.get('/', response={200: List[DrugClassSchemaOut], 404: MessageOut})
def get_drugClasses(request):
    drugClass = DrugClass.objects.all()
    if not drugClass.exists():
        return response(404, {'message': 'not found'})
    return response(200, drugClass)


@drugClass_controller.post('/', response={201: DrugClassSchemaOut, 400: MessageOut})
def create_drugClass(request, drugClass_in: DrugClassSchemaIn):
    drugClass = DrugClass.objects.create(**drugClass_in.dict())
    drugClass.save()
    return response(201, drugClass)


@drugClass_controller.get('/{id}', response={200: DrugClassSchemaOut, 404: MessageOut})
def get_drugClass(request, id: int):
    drugclass = DrugClass.objects.get(id=id)
    if not drugclass:
        return response(404, {'message': 'not found'})
    return response(200, drugclass)


@drugClass_controller.put('/{id}', response={200: DrugClassSchemaOut, 404: MessageOut})
def update_drugClass(request, id: int, drugClass_in: DrugClassSchemaIn):
    drugClass = DrugClass.objects.get(id=id)
    if not drugClass:
        return response(404, {'message': 'not found'})
    drugClass.name = drugClass_in.name
    drugClass.drugClass = drugClass_in.description
    drugClass.save()
    return response(200, drugClass)


@drugClass_controller.delete('/{id}', response={200: MessageOut, 404: MessageOut})
def delete_drugClass(request, id: int):
    drugClass = DrugClass.objects.filter(id=id).first()
    if not drugClass:
        return response(404, {'message': 'not found'})
    drugClass.delete()
    return response(200, {'message': 'deleted'})


@drugClass_controller.get('/{id}/drugs', response={200: List[DrugSchemaOut], 404: MessageOut})
def get_drugs(request, id: int):
    drugClass = DrugClass.objects.get(id=id)
    if not drugClass:
        return response(404, {'message': 'not found'})
    return response(200, drugClass.drugs)
