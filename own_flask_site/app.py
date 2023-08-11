from flask import Flask, render_template
from seetings import SECRET_KEY
from sql_queries import*

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
db = ShopDB()

@app.route("/")
def pizzaria():
    items = db.get_all()
    print(items)
    return render_template('index.html', title="Online Pizzaria", items = items)
if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True