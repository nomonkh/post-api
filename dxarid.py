from flask import Flask, jsonify, request, \
    redirect, url_for, make_response, render_template
import flask
import sqlite3
app = Flask(__name__)

db = sqlite3.connect('token.db')
sql = db.cursor()
token_db = sql.execute('''select token from users where login='dxarid' ''').fetchall()[0][0]

@app.route('/dxarid', methods=['POST', 'GET'])

def addOne():
    if flask.request.method != 'POST':
        return render_template('index.html')
    elif flask.request.method == 'POST':
        token_ars = request.args.get('token')
        if token_ars != token_db or token_ars is None:
            return 'Invalid token'
        else:
            data = []
            item = {'products': request.json['products'],
                    'lot_info': request.json['lot_info'],
                    'seller': request.json['seller'],
                    'buyer': request.json['buyer']
                    }
            data.append(item)
            return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=7070)
