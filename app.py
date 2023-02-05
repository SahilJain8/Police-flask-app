from flask import Flask,render_template,request,jsonify,flash,redirect,url_for


app=Flask(__name__,static_folder="assets")

 

app.secret_key = "secret key"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/oct.html')
def oct():
    return render_template("oct.html")


@app.route('/contacts.html')
def contacts():
    return render_template("contacts.html")



@app.route('/login.html')
def login():
    return render_template("login.html")

    
@app.route('/contribute.html')
def contribute():
    return render_template("contribute.html")



    
@app.route('/api.html')
def api():
    return render_template("api.html")
@app.route('/monkeypox.html')
def monkey():
    return render_template('monkeypox.html')

@app.route('/Brain tumor.html')
def brain():
    return render_template('Brain tumor.html')





    
if __name__=="__main__":
    app.run(debug=True)




