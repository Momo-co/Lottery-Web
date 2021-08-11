from application import app, db
from flask import redirect, request, render_template, url_for
from application.models import Record

@app.route('/')
@app.route('/home')
def home():
    colour = requests.get('http://service-2:5000/get/colour').text 
    number = requests.get('http://service-3:5000/get/num').text 

    lucky_input = {'colour': colour, 'number': number}
    prize = requests.post('http://service-4:5000/gen.prize', json=lucky_input).json() 

    new_lotto = Record(colour=colour, number=number, prize=prize)
    db.session.add(new_lotto)
    db.session.commit()

    all_record = Record.query.all()
    total_prize = func.sum(Record.prize)

    return render_template("home.html", all_record=all_record, colour=colour, number=number, prize=prize, total_prize=total_prize)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')