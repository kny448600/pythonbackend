from flask import flask


app = Flask(__name__)

@app.route('/')
def root():
    return"<h1>root directory</h1>"

from flask import Flask, jsonify, request
app = Flask(__name__)
app.users = {}
app.posts = []
app.idCnt = 1

@app.route('/main', methods=['GET'])
def signUppage():
    return render_template('singup.html')

@app.route('/sing-up', methods=['GET']
           
           )
@app.route('/sing-up', methods=['GET'])

@app.route('/sign-up', methods=['POST'])
def signUp():
    newUser = request.json
    newUser['id'] = app.idCnt
    app.users[app.idCnt] = newUser
    app.idCnt += 1
    return jsonify(newUser)

@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', name="seokjin")



if __name__ == '__name__':
    app.run()