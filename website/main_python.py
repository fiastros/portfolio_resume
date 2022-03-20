from flask import Flask, render_template, request, url_for, redirect
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


"""
#this part of the code was to update automatically my age on the website
from datetime import datetime

def days_between(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2-d1).days)

date_today = str( datetime.date(datetime.now()) )

my_age = int( days_between("1997-09-08", date_today)/365.25 )
print(my_age)
"""