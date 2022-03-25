from flask import Flask, jsonify, request, \
    redirect, url_for, make_response, render_template
import flask
import sqlite3
from CONNECTION import conn, cur

app = Flask(__name__)

db = sqlite3.connect('token.db')
sql = db.cursor()
token_db = sql.execute('''select token from users where login='dxarid' ''').fetchall()[0][0]
data = []

products_data = []
main_data = []


def insert_prod(data):
    cur.executemany('''insert into test_post.products values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', data)
    conn.commit()


def insert_main(data):
    cur.executemany('''insert into test_post.main values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                    data)
    conn.commit()


def get_req(data):
    for item in data:
        '''collection lot_info'''
        lot_info = item.get('lot_info', 'null')
        l_date_end = lot_info.get('date_end', 'null')
        l_dateini = lot_info.get('dateini', 'null')
        l_id = lot_info.get('id', 'null')
        l_item_group_name = lot_info.get('item_group_name', 'null')
        l_name = lot_info.get('name', 'null')
        l_status_name = lot_info.get('status_name', 'null')

        ''' collection products'''
        products = item.get('products', 'null')
        for prod in products:
            all_price = prod.get('all_price', 'null')
            art_id = prod.get('art_id', 'null')
            descript = prod.get('descript', 'null')
            expend_id = prod.get('expend_id', 'null')
            measure_gnk = prod.get('measure_gnk', 'null')
            one_price = prod.get('one_price', 'null')
            p_product_name = prod.get('p_product_name', 'null')
            plan_position_id = prod.get('plan_position_id', 'null')
            quantity = prod.get('quantity', 'null')
            tnvd_code = prod.get('tnvd_code', 'null')
            products_data.append((l_id, all_price, art_id, descript, expend_id, measure_gnk, one_price,
                                  p_product_name, plan_position_id, quantity, tnvd_code))
        insert_prod(products_data)
        '''seller collection'''
        seller = item.get('seller', 'null')
        s_address = seller.get('address', 'null')
        s_inn = seller.get('inn', 'null')
        s_name = seller.get('name', 'null')
        s_rayon = seller.get('rayon', 'null')
        s_region = seller.get('region', 'null')

        '''collection buyer'''
        buyer = item.get('buyer', 'null')
        b_account = buyer.get('account', 'null')
        b_address = buyer.get('address', 'null')
        b_inn = buyer.get('inn', 'null')
        b_name = buyer.get('name', 'null')
        b_rayon = buyer.get('rayon', 'null')
        b_region = buyer.get('region', 'null')

        main_data.append((s_address, s_inn, s_name, s_rayon, s_region, b_account, b_address,
                          b_inn, b_name, b_rayon, b_region, l_date_end, l_dateini,
                          l_id, l_item_group_name, l_name, l_status_name))
        insert_main(main_data)


@app.route('/dxarid', methods=['POST', 'GET'])
def addOne():
    if flask.request.method != 'POST':
        return render_template('index.html')
    elif flask.request.method == 'POST':
        token_ars = request.args.get('token')
        if token_ars != token_db or token_ars is None:
            return 'Invalid token'
        else:
            data.append(request.json)
            get_req(data)
            return jsonify(data)


if __name__ == '__main__':
    app.run(port=7070)
