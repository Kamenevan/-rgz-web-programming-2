# Import statement
from flask import (
    Flask,
    render_template,
    Markup,
    url_for,
    flash,
    redirect,
    request
)

# import sendgrid
from datetime import date

# App setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "some_really_long_random_string_here"

# Get details for sendgrid details
sendgrid_file = "sendgrid.txt"
# sendgrid_details = []

# with open(sendgrid_file) as f:
#     sendgrid_details = f.readlines()
#     sendgrid_details = [x.strip("\n") for x in sendgrid_details]

# Global Variables
products_info = [
    {
        "id": "1",
        "name": "Bed, Beige",
        "img": "bed.jpg",
        "price": 25000,
        "paypal": "LFRHBPYZKH4Y",
        "bought" : 0
    },

    {
        "id": "2",
        "name": "Armchair, Blue",
        "img": "armchair.jpg",
        "price": 2500,
        "paypal": "FRHBPYZKH4Y",
        "bought" : 0
    },

    {
        "id": "3",
        "name": "Armchair, White",
        "img": "armchair2.jpg",
        "price": 10000,
        "paypal": "LFRHBPYZH4Y",
        "bought" : 0
    },

    {
        "id": "4",
        "name": "Armchair, Blue",
        "img": "armchair3.jpg",
        "price": 15000,
        "paypal": "LRHBPYZKH4Y",
        "bought" : 0
    },

    {
        "id": "5",
        "name": "Bed, Brown",
        "img": "bed2.jpg",
        "price": 20000,
        "paypal": "LRHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "6",
        "name": "Bed, Green",
        "img": "bed3.jpg",
        "price": 25000,
        "paypal": "LRHBPYZKPR4Y",
        "bought" : 0
    },

    {
        "id": "7",
        "name": "Bedside, White",
        "img": "bedside.jpg",
        "price": 2000,
        "paypal": "LRHBSYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "8",
        "name": "Bookcase, White",
        "img": "bookcase.jpg",
        "price": 7000,
        "paypal": "LRFBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "9",
        "name": "Case, White",
        "img": "case.jpg",
        "price": 3000,
        "paypal": "LRHBDYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "10",
        "name": "Case, White",
        "img": "case2.jpg",
        "price": 3000,
        "paypal": "LRYBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "11",
        "name": "Case, Gray",
        "img": "case3.jpg",
        "price": 3500,
        "paypal": "LRHBPYZKAP4Y",
        "bought" : 0
    },

    {
        "id": "12",
        "name": "Chair, Gray",
        "img": "chair.jpg",
        "price": 1500,
        "paypal": "LRHSPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "13",
        "name": "Chest, Wooden",
        "img": "chest.jpg",
        "price": 4000,
        "paypal": "LTHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "14",
        "name": "Chest, White",
        "img": "chest2.jpg",
        "price": 3500,
        "paypal": "KRHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "15",
        "name": "Chest, White",
        "img": "chest3.jpg",
        "price": 4500,
        "paypal": "LRHBPYZKMP4Y",
        "bought" : 0
    },

    {
        "id": "16",
        "name": "Dresser, White",
        "img": "dresser.jpg",
        "price": 9000,
        "paypal": "LRHAPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "17",
        "name": "Dresser, Wooden",
        "img": "dresser2.jpg",
        "price": 10000,
        "paypal": "LRHBPYZKPP4K",
        "bought" : 0
    },

    {
        "id": "18",
        "name": "Dresser, White",
        "img": "dresser3.jpg",
        "price": 15000,
        "paypal": "LRHRDPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "19",
        "name": "Dresser, White",
        "img": "dresser4.jpg",
        "price": 13000,
        "paypal": "LRHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "20",
        "name": "Dresser, Wooden",
        "img": "dresser5.jpg",
        "price": 12000,
        "paypal": "LRHBPYZKPP5Y",
        "bought" : 0
    },

    {
        "id": "21",
        "name": "Dresser, Wooden",
        "img": "dresser6.jpg",
        "price": 11000,
        "paypal": "LRHBPYZKPP8Y",
        "bought" : 0
    },

    {
        "id": "22",
        "name": "Dresser, White",
        "img": "dresser7.jpg",
        "price": 12000,
        "paypal": "LRHBPQZKPP4Y",
        "bought" : 0
    },

    {
        "id": "23",
        "name": "Shelf, Blue",
        "img": "shelf.jpg",
        "price": 1500,
        "paypal": "LRHBPYZKPP1Y",
        "bought" : 0
    },

    {
        "id": "24",
        "name": "Sofa, Beige",
        "img": "sofa.jpg",
        "price": 25000,
        "paypal": "QRHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "25",
        "name": "Sofa, Beige",
        "img": "sofa2.jpg",
        "price": 35000,
        "paypal": "QRHBPYZKPP7Y",
        "bought" : 0
    },

    {
        "id": "26",
        "name": "Sofa, Brown",
        "img": "sofa3.jpg",
        "price": 23000,
        "paypal": "QRHBSYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "27",
        "name": "Table, Wooden",
        "img": "table.jpg",
        "price": 10000,
        "paypal": "QRHBPAZKPP5Y",
        "bought" : 0
    },

    {
        "id": "28",
        "name": "TVstand, Black",
        "img": "TVstand.jpg",
        "price": 18000,
        "paypal": "QFHBPYZKPP4Y",
        "bought" : 0
    },

    {
        "id": "29",
        "name": "TVstand, White-wooden",
        "img": "TVstand2.jpg",
        "price": 13000,
        "paypal": "QRHBPYZKTT4Y",
        "bought" : 0
    },

    {
        "id": "30",
        "name": "TVstand, Black",
        "img": "TVstand3.jpg",
        "price": 15000,
        "paypal": "QRHBDYZKPP3Y",
        "bought" : 0
    }

]

bought_products = []

# Functions


def get_list_view_html(product):
    """Function to return html for given shirt

    The product argument should be a dictionary in this structure:
    {
        "id": "shirt_id",
        "name": "name_of_shirt",
        "img": "image_name.jpg",
        "price": price_of_shirt_as_int_or_flat,
        "paypal": "paypal_id"
    }

    The html is returned in this structure:
    <li>
      <a href="shirt/shirt_id">
        <img src="/static/shirt_img" alt="shirt_name">
        <p>View Details</p>
      </a>
    </li>
    """
    output = ""
    image_url = url_for("static", filename=product["img"])
    shirt_url = url_for("shirt", product_id=product["id"])
    output += "<li>"
    output += '<a href="' + shirt_url + '">'
    output = (
        output + '<img src="' + image_url +
        '" al  t="' + product["name"] + '">')
    output += "<p>View Details</p>"
    output += "</a>"
    output += "</li>"

    return output

def get_list_view_html_cart(product):
    """Function to return html for given shirt

    The product argument should be a dictionary in this structure:
    {
        "id": "shirt_id",
        "name": "name_of_shirt",
        "img": "image_name.jpg",
        "price": price_of_shirt_as_int_or_flat,
        "paypal": "paypal_id"
    }

    The html is returned in this structure:
    <li>
      <a href="shirt/shirt_id">
        <img src="/static/shirt_img" alt="shirt_name">
        <p>View Details</p>
      </a>
    </li>
    """
    output = ""
    image_url = url_for("static", filename=product["img"])
    shirt_url = url_for("shirt", product_id=product["id"])
    output += "<li>"
    output += '<a href="' + shirt_url + '">'
    output = (
        output + '<img src="' + image_url +
        '" al  t="' + product["name"] + '">')
    output += "<p>" + str(product["bought"] * product["price"]) + "$ for " + str(product["bought"]) + " shirt(s)</p>"
    output += "</a>"
    output += "</li>"

    return output

# Routes
# All functions should have a page_title variables if they render templates

@app.route("/")
def index():
    """Function for Shirts4Mike Homepage"""
    context = {"page_title": "Shirts 4 Mike", "current_year": date.today().year}
    counter = 0
    product_data = []
    for product in products_info:
        counter += 1
        if counter < 5:  # Get first 4 shirts
            product_data.append(
                Markup(get_list_view_html(product))
            )
    context["product_data"] = Markup("".join(product_data))
    # flash("This site is a demo do not buy anything")
    return render_template("index.html", **context)


@app.route("/shirts")
def shirts():
    """Function for the Shirts Listing Page"""
    context = {"page_title": "Shirts 4 Mike", "current_year": date.today().year}
    product_data = []
    for product in products_info:
        product_data.append(Markup(get_list_view_html(product)))
    context["product_data"] = Markup("".join(product_data))
    # flash("This site is a demo do not buy anything")
    return render_template("shirts.html", **context)


@app.route("/shirt/<product_id>")
def shirt(product_id):
    """Function for Individual Shirt Page"""
    context = {"page_title": "Shirts 4 Mike", "current_year": date.today().year}
    my_product = ""
    for product in products_info:
        if product["id"] == product_id:
            my_product = product
    context["product"] = my_product
    # flash("This site is a demo do not buy anything")
    return render_template("shirt.html", **context)

@app.route("/shirt/<product_id>/buy", methods=['POST'])
def buy_shirt(product_id):
    print("You bought: ", product_id)
    context = {"page_title": "Shirts 4 Mike", "current_year": date.today().year}
    my_product = ""
    for product in products_info:
        if product["id"] == product_id:
            my_product = product
            product["bought"] += 1
            if product not in bought_products:
                bought_products.append(product)
    context["product"] = my_product
    flash("Successfully bought " + my_product["name"])
    return render_template("shirt.html", **context)



@app.route("/cart")
def cart():
    """Function to display receipt after purchase"""
    context = {"page_title": "Shirts 4 Mike", "current_year": date.today().year}
    product_data = []
    for product in bought_products:
        product_data.append(Markup(get_list_view_html_cart(product)))
    context["product_data"] = Markup("".join(product_data))
    return render_template("cart.html", **context)

# @app.route("/receipt")
# def receipt():
#     """Function to display receipt after purchase"""
#     context = {"page_title": "Shirts 4 Mike", "current_year": date.today().year}
#     return render_template("receipt.html", **context)


@app.route("/contact")
def contact():
    """Function for contact page"""
    context = {"page_title": "Shirts 4 Mike", "current_year": date.today().year}
    return render_template("contact.html", **context)


# Route to send email
@app.route("/send", methods=['POST'])
def send():
    """Function to send email using sendgrid API"""
    # sendgrid_object = sendgrid.SendGridClient(
    #     sendgrid_details[0], sendgrid_details[1])
    message = sendgrid.Mail()
    sender = request.form["email"]
    subject = request.form["name"]
    body = request.form["message"]
    message.add_to("charlie.thomas@attwoodthomas.net")
    message.set_from(sender)
    message.set_subject(subject)
    message.set_html(body)
    # sendgrid_object.send(message)
    # flash("Email sent.")
    return redirect(url_for("contact"))


# Run application
if __name__ == "__main__":
    app.run(debug=True)

# @lab7.route('/lab7/api', methods=['POST'])
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


# #    return price

# # def pay(params):
# #     card_num = params['card']
# #     if len(card_num) != 16 or not str(card_num).isdigit():
# #         return {"result": None, "error": "Неверный номер карты"} 

# #     cvv = params['cvv']
# #     if len(cvv) != 3 or not cvv.isdigit():
# #         return {"result": None, "error": "Неверный номер CVV/CVC"}
    
# #     price = params['price']  # Используем переданную цену

# #     return {"result": f'С карты {card_num} списано {price} руб', "error": None}

# # def refund(params):
# #     card_num = params['card']
# #     if len(card_num) != 16 or not str(card_num).isdigit():
# #         return {"result": None, "error": "Неверный номер карты"}

# #     cvv = params['cvv']
# #     if len(cvv) != 3 or not cvv.isdigit():
# #         return {"result": None, "error": "Неверный номер CVV/CVC"}

# #     return {"result": f'Деньги возвращены на карту {card_num}', "error": None}
