import peewee as pw
from config import BaseModel, db

class assortment(BaseModel):
    id = pw.IntegerField(primary_key=True)
    titles_product = pw.CharField(max_length=255)

class product(BaseModel):
    id = pw.IntegerField(primary_key=True)
    title = pw.CharField(max_length=255)

class city(BaseModel):
    id = pw.IntegerField(primary_key=True)
    name_city = pw.CharField(max_length=255)

class workshop(BaseModel):
    id = pw.IntegerField(primary_key=True)
    adress = pw.CharField(max_length=255)
    phone = pw.CharField(max_length=12)

class manufacturer(BaseModel):
    id = pw.IntegerField(primary_key=True)
    info_manuf = pw.CharField(max_length=255)
    phone = pw.CharField(max_length=12)

# class Customer(BaseModel):
#     id = pw.IntegerField(primary_key=True)
#     contact = pw.ForeignKeyField(Contact, on_delete='CASCADE', null=False, backref='customers')

#(здесь описываем все таблицы)

# Создание таблиц для всех моделей
with db:
    db.create_tables([
        assortment, product, city, workshop, manufacturer
    ])