from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <html>
        <head><title>Flask App</title></head>
        <body>
            <h1>Hi, Welcome to My Flask App!</h1>
            <p>Click here for the <a href="/random">random number generator</a> for something fun!</p>
        </body>
    </html>
    """

@app.route('/random')
def random_number():
    number = random.randint(1, 100)
    return f"<h2>Your random number is: {number}</h2>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
