from flask import Flask
app = Flask(__name__)

from genai import genAi

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/genai/<prompt>')
def call_genai(prompt):
    result = genAi(prompt)
    return result

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True,port=8080)

