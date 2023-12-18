from . import models
from flask import jsonify
from .serializers import *

def where_filters(query, model: models.BaseModel, **filters):
    _filters = [
        getattr(model, key) == value
        for key, value in filters.items() if value is not None
    ]
    if _filters:
        return query.where(*_filters)
    return query

# для вывода в json
# def execute_get_all(model, serializer, **filters):
#     query = model.select()
#     query = where_filters(query, model, **filters)
#     return jsonify([serializer(model) for model in query])
#
# def execute_get_one(pk, model, serializer):
#     return serializer(model.select().where(model.id == int(pk)).get())

#вывод списком строк
def execute_get_all(model, serializer, **filters):
    query = model.select()
    query = where_filters(query, model, **filters)
    result = [serializer(model) for model in query]
    return "\n".join(str(row) + "\n" for row in result)

def execute_get_one(pk, model, serializer):
    result = serializer(model.select().where(model.id == int(pk)).get())
    return str(result) + "\t"

def get_assortment_detail(pk):
    item = models.assortment.get_or_none(id=pk)
    if item:
        return {
            'id': item.id,
            'titles_product': item.titles_product
        }
    return None

def create_assortment(data):
    new_item = models.assortment.create(**data)
    return {
        'id': new_item.id,
        'titles_product': new_item.titles_product
    }

def update_assortment(pk, data):
    item = models.assortment.get_or_none(id=pk)
    if item:
        item.titles_product = data.get('titles_product', item.titles_product)
        item.save()
        return {
            'id': item.id,
            'titles_product': item.titles_product
        }
    return None

def delete_assortment(pk):
    item = models.assortment.get_or_none(id=pk)
    if item:
        item.delete_instance()
        return {'message': 'Deleted successfully'}
    return None

def get_product_detail(pk):
    item = models.product.get_or_none(id=pk)
    if item:
        return {
            'id': item.id,
            'title': item.title
        }
    return None

def create_product(data):
    new_item = models.product.create(**data)
    return {
        'id': new_item.id,
        'title': new_item.title
    }

def update_product(pk, data):
    item = models.product.get_or_none(id=pk)
    if item:
        item.title = data.get('title', item.title)
        item.save()
        return {
            'id': item.id,
            'title': item.title
        }
    return None

def delete_product(pk):
    item = models.product.get_or_none(id=pk)
    if item:
        item.delete_instance()
        return {'message': 'Deleted successfully'}
    return None

def get_workshop_detail(pk):
    item = models.workshop.get_or_none(id=pk)
    if item:
        return {
            'id': item.id,
            'adress': item.titles_product,
            'phone': item.phone
        }
    return None

def create_workshop(data):
    new_item = models.workshop.create(**data)
    return {
        'id': new_item.id,
        'adress': new_item.adress,
        'phone': new_item.phone
    }

def update_workshop(pk, data):
    item = models.workshop.get_or_none(id=pk)
    if item:
        item.adress = data.get('adress', item.adress)
        item.phone = data.get('phone', item.phone)
        item.save()
        return {
            'id': item.id,
            'adress': item.adress,
            'phone': item.phone

        }
    return None

def delete_workshop(pk):
    item = models.workshop.get_or_none(id=pk)
    if item:
        item.delete_instance()
        return {'message': 'Deleted successfully'}
    return None