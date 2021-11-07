from typing import List
from ninja.router import Router
from config.utils.schemas import MessageOut
from medcyclopedia.models import Drug, DrugClass, Tag
from config.utils.utils import response


from medcyclopedia.schemas import DrugSchemaIn, DrugSchemaOut


drug_controller = Router(tags=['drugs'])


@drug_controller.get('/', response={200: List[DrugSchemaOut], 404: MessageOut})
def get_drugs(request):
    drugs = Drug.objects.all()
    if not drugs.exists():
        return response(404, {'message': 'not found'})
    return response(200, drugs)


@drug_controller.get('/{id}', response={200: DrugSchemaOut, 404: MessageOut})
def get_drug(request, id: int):
    drug = Drug.objects.get(id=id)
    if not drug:
        return response(404, {'message': 'not found'})
    return response(200, drug)


@drug_controller.post('/', response={201: DrugSchemaOut, 400: MessageOut})
def create_drug(request, drug_in: DrugSchemaIn):
    drug = Drug.objects.create(**drug_in.dict())
    tags = drug_in.tag
    del drug_in.tags
    for tag in tags:
        drug.tag.add(Tag.objects.get(id=tag))

    drugClasses = drug_in.drugClasses
    del drug_in.drugClasses
    for drugClass in drugClasses:
        drug.drugClass.add(DrugClass.objects.get(id=drugClass))

    drug.save()

    return response(201, drug)


@drug_controller.put('/{id}', response={200: DrugSchemaOut, 404: MessageOut})
def update_drug(request, id: int, drug_in: DrugSchemaIn):
    drug = Drug.objects.get(id=id)
    if not drug:
        return response(404, {'message': 'not found'})
    drug.tag.clear()
    if drug_in.tag != None:
        for tag in drug_in.tag:
            drug.tag.add(Tag.objects.get(id=tag))

    drug.drugClass.clear()
    if drug_in.drugClass != None:
        for drugClass in drug_in.drugClass:
            drug.drugClass.add(DrugClass.objects.get(id=drugClass))

    drug.save()
    return response(200, drug)


@drug_controller.delete('/{id}', response={200: MessageOut, 404: MessageOut})
def delete_drug(request, id: int):
    drug = Drug.objects.get(id=id)
    if not drug:
        return response(404, {'message': 'not found'})
    drug.delete()
    return response(200, {'message': 'deleted'})
