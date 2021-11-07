from typing import List
from ninja import Schema
from rest_auth.schemas.email_account_schemas import AccountOut


class TagSchema(Schema):
    id: str = None
    # drugs: List['DrugSchemaOut'] = None
    name: str


class TagSchemaOut(Schema):
    id: str = None
    # drugs: List['DrugSchemaOut'] = None
    name: str


class ArticleSchema(Schema):
    id: str = None
    title: str
    body: str
    img: str
    tag: List[TagSchema] = None
    author: AccountOut


class ArticleSchemaIn(Schema):
    title: str
    body: str
    img: str
    tag: List[int] = None
    author_id: str = "507e2215e5cd449c9ab6af252522e9bb"


class CategoriesSchema(Schema):
    id: str = None
    name: str
    img: str = None


class DrugSchemaOut(Schema):
    id: str = None
    name: str
    genericName: str
    brandName: str
    federalSchedule: str
    availability: str
    img: str
    description: str
    primaryIndications: str
    tags: List[TagSchema] = None
    # drugClasses: List['DrugClassSchemaOut'] = None


class DrugSchemaIn(Schema):
    name: str
    genericName: str
    brandName: str
    federalSchedule: str
    availability: str
    img: str
    description: str
    primaryIndications: str
    tags: List[int] = None
    drugClasses: List[int] = None


class DrugClassSchemaOut(Schema):
    id: str = None
    name: str
    # description: str
    img: str = None
    drugs: List[DrugSchemaOut] = None


class DrugClassSchemaIn(Schema):
    name: str
    # description: str
    img: str = None
