from flask import Flask, request, jsonify

app = Flask(__name__)

prizes = {
    'colour': {
        'Red': 1,
        'Yellow': 50,
        'Green': 100
    },
    'number': {
        'Zero': 0,
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five':5,
        'Six':6,
        'Seven':7,
        'Eight':8,
        'Nine':9
    }
}

@app.route('/gen/prize', methods=['POST'])
def gen_prize():
    colour = request.json['colour']
    number = request.json['number']

    prize = prizes['colour'][colour] * prizes['number'][number]
    

    return jsonify(prize) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')