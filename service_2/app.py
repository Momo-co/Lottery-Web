from flask import Flask
import random

app = Flask(__name__)

colour = ['Red', 'Yellow', 'Green']

@app.route('/get/colour')
def home():
    return random.choice(colour)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')