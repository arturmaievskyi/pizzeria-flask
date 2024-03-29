from flask import Flask, render_template, request, flash, redirect, url_for
from seetings import SECRET_KEY
from sql_queries import*

#________________________________________________________________________________________#

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY 
db_pizzas = ShopDB_Pizzas()
db_drinks = ShopDB_Drinks()

#________________________________________________________________________________________#

@app.route("/index")
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
    return render_template('own_pizza.html', title="Online Pizzeria", pizza = pizza_obj)


@app.route("/drink/<drink_id>")
def drink(drink_id):
    drink_obj = db_drinks.get_drink(drink_id)
    return render_template('own_drink.html', title="Online Pizzeria", drink = drink_obj)


@app.route("/pizza")
def pizzaPage():
    pizzas_obj = db_pizzas.get_all_pizzas()
    print(pizzas_obj)
    return render_template('pizza.html', title="Online Pizzeria", pizzas = pizzas_obj)


@app.route("/drink")
def drinkPage():
    drink_obj = db_drinks.get_all_drinks()
    print(drink_obj)
    return render_template('drink.html',title="Online Pizzeria",  drinks = drink_obj)

@app.route("/pizza/<pizza_id>/buy", methods = ["GET", "POST"])
def order_pizza(pizza_id):
    pizza_obj = db_pizzas.get_pizza(pizza_id)
    if request.method == 'POST':
        try:
            db_pizzas.add_order_pizza(pizza_obj[0], 
                    request.form["name"],
                    request.form["email"],
                    request.form["phone"],
                    request.form["city"],
                    request.form["address"], 
                        pizza_obj[5])
            flash("New order was given!", "alert-light") #надсилаємо швидкі сповіщення у браузер
            return redirect(url_for("pizzaria")) #перенаправляємо на головну сторінку
        except:
            flash("Fail to make!", "alert-danger") #надсилаємо швидкі сповіщення у браузер
            return redirect(url_for("pizzaria"))
    return render_template('new_order_pizza.html', title="Online Pizzeria", pizza = pizza_obj)

@app.route("/drink/<drink_id>/buy", methods = ["GET", "POST"])
def order_drink(drink_id):
    drink_obj = db_drinks.get_drink(drink_id)
    if request.method == 'POST':
        # try:
            db_drinks.add_order_drink(drink_obj[0], 

                    request.form["phone"],
                    request.form["name"],
                    request.form["email"],
                    request.form["city"],
                    drink_obj[4])
            flash("Додано замовлення!", "alert-light") #надсилаємо швидкі сповіщення у браузер
            return redirect(url_for('pizzaria')) #перенаправляємо на головну сторінку
        # except:
            flash("Помилка оформлення замовлення!", "alert-danger") #надсилаємо швидкі сповіщення у браузер
    return render_template('new_order_drink.html', title="Online Pizzeria", drink = drink_obj)


@app.route("/suppoort_me")
def support_me():
    return render_template("suppoort_me.html", title="Online Pizzeria")

@app.route("/about")
def about():
    return render_template("about.html", title="Online Pizzeria")



#________________________________________________________________________________________#
if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True