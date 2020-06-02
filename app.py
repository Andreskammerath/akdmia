from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pepito", methods=['GET','POST'])
def pepito():
    if request.method == 'GET':
        pass
    else:
        name = request.form.get("name")
        mail = request.form.get("email")
        content = request.form.get("message")
        print(str(content))        
    return redirect("/")
if __name__ == '__main__':
    app.run()