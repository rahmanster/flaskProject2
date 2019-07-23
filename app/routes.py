from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    userData = dict(request.form)
    return render_template("index.html")
        
@app.route("/bill", methods = ["GET", "POST"])
def bill():
    if request.method == "GET":
        return "You didn't fill out the form."
    else:
        userData = dict(request.form)
        total = float(userData['total'][0])
        tip = float(userData['tip'][0])
        people = float(userData['people'][0])
        finalTotal = model.totalBill(total,tip)
        finalTip = model.tip(total,tip)
        finalSplit = model.split(total,tip,people)
        return render_template("bill.html", finalTip = finalTip, finalTotal = finalTotal, finalSplit = finalSplit)