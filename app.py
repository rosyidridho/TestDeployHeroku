from flask import Flask, render_template, request, json, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST','GET'])
def signUp():
    if request.method == 'POST':
        _name = request.POST['inputName']
        _email = request.POST['inputEmail']
        _password = request.POST['inputPassword']
        print("Berhasill");

    return render_template('index.html')

if __name__=="__main__":
        app.run()
