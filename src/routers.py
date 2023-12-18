from config import app
from flask import request, render_template, jsonify, redirect
from . import services, models


# GET: Получение всех записей
@app.route('/tables', methods=['GET'])
def get_assortment():
    assortment_data = models.assortment.select()
    product_data = models.product.select()
    workshop_data = models.workshop.select()
    return render_template('all_tables.html', assortment_data=assortment_data, product_data=product_data, workshop_data=workshop_data)

@app.route('/assortment', methods=['GET'])
def show_assortment():
    assortment_data = models.assortment.select()
    return render_template('assortment.html', assortment_data=assortment_data)

# Маршрут для отображения таблицы Product
@app.route('/product', methods=['GET'])
def show_product():
    product_data = models.product.select()
    return render_template('product.html', product_data=product_data)


@app.route('/workshop', methods=['GET'])
def show_workshop():
    workshop_data = models.workshop.select()
    return render_template('workshop.html', workshop_data=workshop_data)

# GET: Получение определенной записи по ID
@app.route('/assortment/<pk>', methods=['GET'])
def get_assortment_detail(pk: int):
    return services.get_assortment_detail(pk)

@app.route('/add_assortment', methods=['POST'])
def add_assortment():
    if request.method == 'POST':
        titles_product = request.form['titles_product']
        # Создание новой записи
        new_item = {
            'titles_product': titles_product
        }
        created_item = services.create_assortment(new_item)  # Используйте вашу функцию создания записи
        if created_item:
            return redirect('/assortment')  # Перенаправление на страницу ассортимента после добавления
        else:
            return "Failed to add assortment item"  # Сообщение об ошибке

@app.route('/update_assortment/<int:pk>', methods=['POST'])
def update_assortment(pk):
    if request.method == 'POST':
        updated_titles_product = request.form['updated_titles_product']
        updated_item = {
            'titles_product': updated_titles_product
        }
        updated = services.update_assortment(pk, updated_item)  # Используйте вашу функцию обновления записи
        if updated:
            return redirect('/assortment')  # Перенаправление на страницу ассортимента после обновления
        else:
            return "Failed to update assortment item"  # Сообщение об ошибке


@app.route('/delete_assortment/<int:pk>', methods=['POST'])
def delete_assortment(pk):
    deleted = services.delete_assortment(pk)  # Используйте вашу функцию удаления записи
    if deleted:
        return redirect('/assortment')  # Перенаправление на страницу ассортимента после удаления
    else:
        return "Failed to delete assortment item"  # Сообщение об ошибке



##################

@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        title = request.form['title']
        # Создание новой записи
        new_item = {
            'title': title
        }
        created_item = services.create_product(new_item)  # Используйте вашу функцию создания записи
        if created_item:
            return redirect('/product')  # Перенаправление на страницу ассортимента после добавления
        else:
            return "Failed to add assortment item"  # Сообщение об ошибке

@app.route('/update_product/<int:pk>', methods=['POST'])
def update_product(pk):
    if request.method == 'POST':
        updated_title = request.form['updated_title']
        updated_item = {
            'title': updated_title
        }
        updated = services.update_product(pk, updated_item)  # Используйте вашу функцию обновления записи
        if updated:
            return redirect('/product')  # Перенаправление на страницу ассортимента после обновления
        else:
            return "Failed to update assortment item"  # Сообщение об ошибке


@app.route('/delete_product/<int:pk>', methods=['POST'])
def delete_product(pk):
    deleted = services.delete_product(pk)  # Используйте вашу функцию удаления записи
    if deleted:
        return redirect('/product')  # Перенаправление на страницу ассортимента после удаления
    else:
        return "Failed to delete assortment item"  # Сообщение об ошибке


#########################33


@app.route('/add_workshop', methods=['POST'])
def add_workshop():
    if request.method == 'POST':
        adress = request.form['adress']
        phone = request.form['phone']
        # Создание новой записи
        new_item = {
            'adress': adress,
            'phone': phone
        }
        created_item = services.create_workshop(new_item)  # Используйте вашу функцию создания записи
        if created_item:
            return redirect('/workshop')  # Перенаправление на страницу с мастерскими после добавления
        else:
            return "Failed to add workshop item"  # Сообщение об ошибке

@app.route('/update_workshop/<int:pk>', methods=['POST'])
def update_workshop(pk):
    if request.method == 'POST':
        updated_adress = request.form['updated_adress']
        updated_phone = request.form['updated_phone']
        updated_item = {
            'adress': updated_adress,
            'phone': updated_phone
        }
        updated = services.update_workshop(pk, updated_item)  # Используйте вашу функцию обновления записи
        if updated:
            return redirect('/workshop')  # Перенаправление на страницу с мастерскими после обновления
        else:
            return "Failed to update workshop item"  # Сообщение об ошибке

@app.route('/delete_workshop/<int:pk>', methods=['POST'])
def delete_workshop(pk):
    deleted = services.delete_workshop(pk)  # Используйте вашу функцию удаления записи
    if deleted:
        return redirect('/workshop')  # Перенаправление на страницу с мастерскими после удаления
    else:
        return "Failed to delete workshop item"  # Сообщение об ошибке


