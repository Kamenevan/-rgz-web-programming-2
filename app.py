from flask import Markup

# Import statement
from flask import Flask, render_template, Markup, url_for, flash, redirect, request,jsonify,session

# from your_module import PaymentError 

# import sendgrid
from datetime import date

# App setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "some_really_long_random_string_here"



# Global Variables
products_info = [
    {
        "id": "101",
        "name": "Кресло, Голубое",
        "img": "armchair.jpg",
        "price": 250,
        "paypal": "LNRBY7XSXS5PA",
        "bought" : 0,
    },

    {
        "id": "102",
        "name": "Кресло-качалка,",
        "img": "armchair2.jpg",
        "price": 1000,
        "paypal": "XP8KRXHEXMQ4J",
        "bought" : 0
    },

    {
        "id": "103",
        "name": "Кресло, Синее",
        "img": "armchair3.jpg",
        "price": 800,
        "paypal": "95C659J3VZGNJ",
        "bought" : 0
    },

    {
        "id": "104",
        "name": "Кровать двуспальная, Бежевая",
        "img": "bed.jpg",
        "price": 1800,
        "paypal": "Z5EY4SJN64SLU",
        "bought" : 0
    },

    {
        "id": "105",
        "name": "Кровать, Коричневая",
        "img": "bed2.jpg",
        "price": 2500,
        "paypal": "RYAGP5EWG4V4G",
        "bought" : 0
    },

    {
        "id": "106",
        "name": "Кровать двуспальная, Темно-зеленая",
        "img": "bed3.jpg",
        "price": 2000,
        "paypal": "QYHDD4N4SMUKN",
        "bought" : 0
    },

    {
        "id": "107",
        "name": "Прикроватная тумба, Белая",
        "img": "bedside.jpg",
        "price": 2000,
        "paypal": "RSDD7RPZFPQTQ",
        "bought" : 0
    },

    {
        "id": "108",
        "name": "Книжный шкаф с стеклянными дверцами, Белыйы",
        "img": "bookcase.jpg",
        "price": 250,
        "paypal": "LFRHBPYZKHV4Y",
        "bought" : 0
    },

    {
        "id": "109",
        "name": "Тумбочка прикроватная, Белая",
        "img": "case.jpg",
        "price": 200,
        "paypal": "RSDD7RPZFPQTQ",
        "bought" : 0
    },

        {
        "id": "110",
        "name": "Case, White",
        "img": "case2.jpg",
        "price": 300,
        "paypal": "LRYBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "111",
        "name": "Case, Gray",
        "img": "case3.jpg",
        "price": 350,
        "paypal": "LRHBPYZKAP4Y",
        "bought" : 0
    },

    {
        "id": "112",
        "name": "Chair, Gray",
        "img": "chair.jpg",
        "price": 150,
        "paypal": "LRHSPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "113",
        "name": "Chest, Wooden",
        "img": "chest.jpg",
        "price": 400,
        "paypal": "LTHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "114",
        "name": "Chest, White",
        "img": "chest2.jpg",
        "price": 350,
        "paypal": "KRHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "115",
        "name": "Chest, White",
        "img": "chest3.jpg",
        "price": 450,
        "paypal": "LRHBPYZKMP4Y",
        "bought" : 0
    },

    {
        "id": "116",
        "name": "Dresser, White",
        "img": "dresser.jpg",
        "price": 900,
        "paypal": "LRHAPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "117",
        "name": "Dresser, Wooden",
        "img": "dresser2.jpg",
        "price": 1000,
        "paypal": "LRHBPYZKPP4K",
        "bought" : 0
    },

    {
        "id": "118",
        "name": "Dresser, White",
        "img": "dresser3.jpg",
        "price": 1500,
        "paypal": "LRHRDPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "119",
        "name": "Dresser, White",
        "img": "dresser4.jpg",
        "price": 1300,
        "paypal": "LRHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "120",
        "name": "Dresser, Wooden",
        "img": "dresser5.jpg",
        "price": 1200,
        "paypal": "LRHBPYZKPP5Y",
        "bought" : 0
    },

    {
        "id": "121",
        "name": "Dresser, Wooden",
        "img": "dresser6.jpg",
        "price": 1100,
        "paypal": "LRHBPYZKPP8Y",
        "bought" : 0
    },

    {
        "id": "122",
        "name": "Dresser, White",
        "img": "dresser7.jpg",
        "price": 1200,
        "paypal": "LRHBPQZKPP4Y",
        "bought" : 0
    },

    {
        "id": "123",
        "name": "Shelf, Blue",
        "img": "shelf.jpg",
        "price": 150,
        "paypal": "LRHBPYZKPP1Y",
        "bought" : 0
    },

    {
        "id": "124",
        "name": "Sofa, Beige",
        "img": "sofa.jpg",
        "price": 2500,
        "paypal": "QRHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "125",
        "name": "Sofa, Beige",
        "img": "sofa2.jpg",
        "price": 3500,
        "paypal": "QRHBPYZKPP7Y",
        "bought" : 0
    },

    {
        "id": "126",
        "name": "Sofa, Brown",
        "img": "sofa3.jpg",
        "price": 2300,
        "paypal": "QRHBSYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "127",
        "name": "Table, Wooden",
        "img": "table.jpg",
        "price": 1000,
        "paypal": "QRHBPAZKPP5Y",
        "bought" : 0
    },

    {
        "id": "128",
        "name": "TVstand, Black",
        "img": "TVstand.jpg",
        "price": 1800,
        "paypal": "QFHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "129",
        "name": "TVstand, White-wooden",
        "img": "TVstand2.jpg",
        "price": 1300,
        "paypal": "QRHBPYZKTT4Y",
        "bought" : 0
    },

    {
        "id": "130",
        "name": "TVstand, Black",
        "img": "TVstand3.jpg",
        "price": 1500,
        "paypal": "QRHBDYZKPP3Y",
        "bought" : 0
    }

]

bought_products = []

# Functions


def get_list_view_html(product):
    """Function to return html for given furniture

    The product argument should be a dictionary in this structure:
    {
        "id": "furniture_id",
        "name": "name_of_furniture",
        "img": "image_name.jpg",
        "price": price_of_furniture_as_int_or_flat,
        "paypal": "paypal_id"
    }

    The html is returned in this structure:
    <li>
      <a href="furniture/furniture_id">
        <img src="/static/furniture_img" alt="furniture_name">
        <p>View Details</p>
      </a>
    </li>
    """
    output = ""
    image_url = url_for("static", filename=product["img"])
    furniture_url = url_for("furniture", product_id=product["id"])
    output += "<li>"
    output += '<a href="' + furniture_url + '">'
    output = (
        output + '<img src="' + image_url +
        '" al  t="' + product["name"] + '">')
    output += "<p>View Details</p>"
    output += "</a>"
    output += "</li>"

    return output

def get_list_view_html_cart(product):
    """Function to return html for given furniture

    The product argument should be a dictionary in this structure:
    {
        "id": "furniture_id",
        "name": "name_of_furniture",
        "img": "image_name.jpg",
        "price": price_of_furniture_as_int_or_flat,
        "paypal": "paypal_id"
    }

    The html is returned in this structure:
    <li>
      <a href="furniture/furniture_id">
        <img src="/static/furniture_img" alt="furniture_name">
        <p>View Details</p>
      </a>
    </li>
    """
    output = ""
    image_url = url_for("static", filename=product["img"])
    furniture_url = url_for("furniture", product_id=product["id"])
    output += "<li>"
    output += '<a href="' + furniture_url + '">'
    output = (
        output + '<img src="' + image_url +
        '" al  t="' + product["name"] + '">')
    output += "<p>" + str(product["bought"] * product["price"]) + "$ for " + str(product["bought"]) + " furniture</p>"
    output += "</a>"
    output += "</li>"

    return output

# Routes

@app.route("/")
def index():
    """Function for furniture1 Homepage"""
    context = {"page_title": "furniture1 4 Mike", "current_year": date.today().year}
    counter = 0
    product_data = []
    for product in products_info:
        counter += 1
        if counter < 5:  
            product_data.append(
                Markup(get_list_view_html(product))
            )
    context["product_data"] = Markup("".join(product_data))
    return render_template("index.html", **context)


@app.route("/furniture1")
def furniture1():
    """Function for the furniture1 Listing Page"""
    context = {"page_title": "furniture1 4 Mike", "current_year": date.today().year}
    product_data = []
    for product in products_info:
        product_data.append(Markup(get_list_view_html(product)))
    context["product_data"] = Markup("".join(product_data))
    return render_template("furniture1.html", **context)


@app.route("/furniture/<product_id>")
def furniture(product_id):
    """Function for Individual furniture Page"""
    context = {"page_title": "Мебель", "current_year": date.today().year}
    my_product = ""
    for product in products_info:
        if product["id"] == product_id:
            my_product = product
    context["product"] = my_product
    return render_template("furniture.html", **context)

@app.route("/furniture/<product_id>/buy", methods=['POST'])
def buy_furniture(product_id):
    print("You bought: ", product_id)
    context = {"page_title": "Мебель", "current_year": date.today().year}
    my_product = ""
    for product in products_info:
        if product["id"] == product_id:
            my_product = product
            product["bought"] += 1
            if product not in bought_products:
                bought_products.append(product)
    context["product"] = my_product
    flash("Успешно добавлено в корзину: " + my_product["name"])
    return render_template("furniture.html", **context)

@app.route("/contact")
def contact():
    """Function for contact page"""
    context = {"page_title": "Мебель", "current_year": date.today().year}
    return render_template("contact.html", **context)



@app.route("/cart")
def cart():
    """Функция для отображения чека после покупки"""
    context = {"page_title": "Мебель", "current_year": date.today().year}
    product_data = []
    total_cost = 0
    for product in bought_products:
        product_data.append(Markup(get_list_view_html_cart(product)))
        total_cost += product["price"]
    context["product_data"] = Markup("".join(product_data))
    context["total_cost"] = total_cost
    return render_template("cart.html", **context)


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        card_number = request.form['card_number']
        expiry_date = request.form['expiry_date']
        cvv = request.form['cvv']

        # Проверка наличия данных карты, срока действия и CVV
        if not card_number or not expiry_date or not cvv:
            flash("Пожалуйста, заполните все платежные реквизиты")
            return redirect(url_for('cart'))

        # Отправка данных на сервер платежной системы
        # Обработка ответа от сервера
        try:
            # код для обработки оплаты
            flash("Оплата прошла успешно")
            return redirect(url_for('cart'))
        except PaymentError as e:
            flash("Ошибка при оплате: " + str(e))
            return redirect(url_for('cart'))
    else:
        return redirect(url_for('cart'))


@app.route("/sum", methods=['GET'])
def sum():
    total_cost = sum(product["price"] for product in bought_products)
    return jsonify(total_cost=total_cost)


@app.route('/login')
def login():
    session.clear()
    return redirect('/contact')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/contact')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     errors = []
#     if request.method == 'GET':
#         return render_template('login.html')

#     username_form = request.form.get('username')
#     password_form = request.form.get('password')

#     my_user = users.query.filter_by(username=username_form).first()

#     if my_user is not None:
#         if check_password_hash(my_user.password, password_form):
#             login_user(my_user, remember = False)
#             return redirect('/products')
#         else: 
#             errors.append("Неправильный пароль")
#             return render_template('login.html', errors=errors)
        
#     if not (username_form or password_form):
#         errors.append("Пожалуйста заполните все поля")
#         return render_template("login.html", errors=errors)
#     if username_form == '':
#         errors.append("Пожалуйста заполните все поля")
#         print(errors)
#         return render_template('login.html', errors=errors)
#     if password_form == '':
#         errors.append("Пожалуйста заполните все поля")
#         print(errors)
#         return render_template('login.html', errors=errors)
#     else: 
#         errors.append('Пользователя не существует')
#         return render_template('login.html', errors=errors)
    

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     errors = []
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
        
#         existing_user = users.query.filter_by(username=username).first()
#         if existing_user:
#             errors.append("Пользователь уже существует")
#             return render_template('contact.html', errors=errors)


#         hashed_password = generate_password_hash(password)
#         new_user = users(username=username, password=hashed_password)

#         db.session.add(new_user)
#         db.session.commit()

#         return redirect('/login')
#     return render_template('contact.html')
        

# @app.route('/app/api', methods=['POST'])
# def api():
#     data = request.json
#     global paid  # Используем глобальную переменную paid

#     if data['method'] == 'get-price':
#         return get_price(data['params'])
    
#     if data['method'] == 'pay':
#         response = pay(data['params'])
#         if not response.get("error"):
#             paid = True  # Обновляем состояние оплаты после успешной оплаты
#         return response
    
#     if data['method'] == 'refund':
#         if paid:  # Проверяем состояние оплаты
#             response = refund(data['params'])
#             paid = False  # Обновляем состояние оплаты после успешного возврата
#             return response
#         else:
#             return {"result": None, "error": "Оплата еще не выполнена"}
    
#     abort(400)

# def get_price(params):
#     return {'result': calculate_price(params), "error": None}


# def pay(params):
#     card_num = params['card']
#     if len(card_num) != 16 or not str(card_num).isdigit():
#         return {"result": None, "error": "Неверный номер карты"} 

#     cvv = params['cvv']
#     if len(cvv) != 3 or not cvv.isdigit():
#         return {"result": None, "error": "Неверный номер CVV/CVC"}
    
#     price = params['price']  # Используем переданную цену

#     return {"result": f'С карты {card_num} списано {price} руб', "error": None}

# def refund(params):
#     card_num = params['card']
#     if len(card_num) != 16 or not str(card_num).isdigit():
#         return {"result": None, "error": "Неверный номер карты"}

#     cvv = params['cvv']
#     if len(cvv) != 3 or not cvv.isdigit():
#         return {"result": None, "error": "Неверный номер CVV/CVC"}

#     return {"result": f'Деньги возвращены на карту {card_num}', "error": None}




# Route to send email
@app.route("/send", methods=['POST'])
def send():
    """Function to send email using sendgrid API"""
   
    message = sendgrid.Mail()
    subject = request.form["name"]
    body = request.form["message"]
    message.set_from(sender)
    message.set_subject(subject)
    message.set_html(body)
    return redirect(url_for("contact"))


# Run application
if __name__ == "__main__":
    app.run(debug=True)
