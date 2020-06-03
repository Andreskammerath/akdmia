from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import os
app = Flask(__name__)


app.config['DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formSent", methods=['GET','POST'])
def formSent():
    #if receives get method, just redirect to "/"
    if request.method == 'GET':
        pass
    #Else send the msg to mi inbox
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        content = request.form.get("message")
        print(content)
        msg = Message(content,sender="andreskammerath@gmail.com",
                  recipients=["andreskammerath@gmail.com"])
        mail.send(msg)
    return redirect("/")
if __name__ == '__main__':
    app.run()