from flask import Flask
import random

app = Flask(__name__)

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def num(number_list):
    return random.choice(number_list)

@app.route('/get/num')
def get_num():
    return num(numbers)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')