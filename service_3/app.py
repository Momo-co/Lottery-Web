from flask import Flask
import random

app = Flask(__name__)

def num():
    return random.randint(0,9)

@app.route('/get/num')
def get_num():
    return num()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')