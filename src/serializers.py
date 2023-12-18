# def serialize_customer(model):
#     return {
#         'id': model.id,
#         'contact': {
#             'id': model.contact.id,
#             'fcs': model.contact.fcs,
#             'phone': model.contact.phone,
#             'address': model.contact.address,
#         }
#     }

def serialize_assortment(model):
    return {
        'id': model.id,
        'titles_product': model.titles_product
    }

def serialize_product(model):
    return {
        'id': model.id,
        'title': model.title
    }

def serialize_city(model):
    return {
        'id': model.id,
        'name_city': model.name_city
    }

def serialize_workshop(model):
    return {
        'id': model.id,
        'adress': model.addres,
        'phone': model.phone
    }

def serialize_manufacturer(model):
    return {
        'id': model.id,
        'info_manuf': model.info_manuf,
        'phone': model.phone
    }