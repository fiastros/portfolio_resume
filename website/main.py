from flask import render_template, request, redirect, flash, Blueprint
import smtplib
from email.message import EmailMessage
import json

main = Blueprint("main", __name__)

# retrieve your gmail personal information
with open("website/confidential.json") as f:
    confidential_info = json.load(f)

#print(confidential_info.get("your_email"))

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/sendemail/", methods=["POST"])
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
            flash("Message sent ! Expect an answer under 48 hour. Thank you !")
            server.send_message(msg)
        except:
            flash(f"There has been an issue sending your mail. Please contact : {receiver_email}")
            redirect("/")

    return redirect("/")