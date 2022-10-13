from flask import Flask, request, render_template, redirect,url_for

app = Flask(__name__)
app.debug = True

@app.route('/homepage/')
def home():
    return render_template('pagina1.html')


if __name__ == '__main__':
    app.run()