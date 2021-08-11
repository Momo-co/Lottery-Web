from flask import Flask, request, jsonify

app = Flask(__name__)

prizes = {
    'colour': {
        'Red': 1,
        'Yellow': 50,
        'Green': 100
    },
    'number': {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9
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