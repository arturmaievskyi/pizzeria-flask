from flask import Flask, render_template
from seetings import SECRET_KEY
from sql_queries import*


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY 


db_pizzas = ShopDB_Pizzas()
db_drinks = ShopDB_Drinks()


@app.route("/templates/index.html")
@app.route("/")
def pizzaria():
    pizzas_obj = db_pizzas.get_all_pizzas()
    drinks_obj = db_drinks.get_all_drinks()
    print(pizzas_obj)
    print(drinks_obj)
    return render_template('index.html', title="Online Pizzaria", pizzas = pizzas_obj, drinks = drinks_obj)


@app.route("/pizza/<pizza_id>")
def pizza(pizza_id):
    pizza_obj = db_pizzas.get_pizza(pizza_id)
    return render_template('own_pizza.html', pizza = pizza_obj)


@app.route("/drink/<drink_id>")
def drink(drink_id):
    drink_obj = db_drinks.get_drink(drink_id)
    return render_template('own_drink.html', drink = drink_obj)


@app.route("/templates/pizza.html")
def pizzaPage():
    pizzas_obj = db_pizzas.get_all_pizzas()
    print(pizzas_obj)
    return render_template('pizza.html',  pizzas = pizzas_obj)


@app.route("/templates/drink.html")
def drinkPage():
    drink_obj = db_drinks.get_all_drinks()
    print(drink_obj)
    return render_template('drink.html',  drinks = drink_obj)


@app.route("/templates/about.html")
def About():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True