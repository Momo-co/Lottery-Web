from flask import Flask
import random

app = Flask(__name__)

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

def num(number_list):
    return random.choice(number_list)

@app.route('/get/num')
def get_num():
    return num(numbers)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')