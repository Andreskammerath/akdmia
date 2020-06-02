from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/hello", methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")


if __name__ == '__main__':
    app.run()