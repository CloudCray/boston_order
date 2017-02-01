from boston_order_ivr import create_app

app = create_app('development')

app.run(host='localhost', port=8899, debug=True)
