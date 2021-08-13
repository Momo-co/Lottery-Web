from flask import Flask
import random

app = Flask(__name__)

colours = ['Red', 'Yellow', 'Green']

def pick_colour(colour_list):
    return random.choice(colour_list)

@app.route('/get/colour')
def get_colour():
    return pick_colour(colours)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')