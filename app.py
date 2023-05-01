from flask import Flask, render_template, request
from utils import get_dogecoin_price, get_current_time
from time import ctime

app = Flask(__name__)

@app.route('/')
def home_page():
    dp = get_dogecoin_price()
    ct = get_current_time()
    return render_template("home_page.html", dogecoin_price=dp, time=ct)

@app.route('/news')
def news_page():
    return render_template("news_page.html")

@app.route('/time')
def time_page():
    return render_template("time_page.html", my_current_time=ctime())

@app.route('/my first post', methods=['POST'])
def post_hendler():
    print(request.get_json())
    return "Ok"

if __name__ == '__main__':
    app.run()
