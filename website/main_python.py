from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage
import json

with open("confidential.json") as f:
    confidential_info = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sendemail/", methods=["POST"])
def sendemail():
    if request.method == "POST":
        #retrieving the information typed in the form by the user
        sender_name = request.form["name"]
        sender_subject = request.form["Subject"]
        sender_email = request.form["_replyto"]
        sender_message = request.form["message"]

        #retrieving our personnal information from the confindential.json file
        receiver_name = confidential_info.get("your_name")
        receiver_email = confidential_info.get("your_email")
        receiver_password = confidential_info.get("your_password")

        #loggin in to our email account
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(receiver_email,receiver_password)

        #writing the mail
        msg = EmailMessage()
        msg.set_content("First Name: " + str(sender_name) +
                        "\nEmail: " + str(sender_email) +
                        "\nSubject: " + str(sender_subject) +
                        "\n Message: " + str(sender_message)
                        )
        msg["Subject"] = "New Response on Personal Website"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        #Send the mail
        try:
            flash("Message. Expect an answer under 48 hour. Thank you !")
            server.send_message(msg)
        except:
            flash(f"There has been an issue sending your mail. Please contact : {receiver_email}")
            redirect("/")

    return redirect("/")

if __name__ == "__main__":
    app.run(threaded=True, debug=True, host = "127.0.0.1", port=5000)


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