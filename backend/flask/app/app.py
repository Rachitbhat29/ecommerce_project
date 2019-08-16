from flask import Flask, render_template, request
from os import path as p,walk

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

cart_products = []
products = []

@app.route('/')
def home():
	#read_products()
	products.append({'name':'1','mrp':'24','sp':'20'})
	products.append({'name':'2','mrp':'34','sp':'20'})
	products.append({'name':'3','mrp':'44','sp':'20'})
	products.append({'name':'4','mrp':'54','sp':'20'})
	products.append({'name':'5','mrp':'64','sp':'20'})
	products.append({'name':'6','mrp':'74','sp':'20'})
	products.append({'name':'7','mrp':'84','sp':'20'})
	products.append({'name':'8','mrp':'94','sp':'20'})
	products.append({'name':'9','mrp':'44','sp':'20'})
	cart_products.append({'name':'1','mrp':'24','sp':'20'})
	cart_products.append({'name':'2','mrp':'34','sp':'20'})
	cart_products.append({'name':'3','mrp':'44','sp':'20'})
	
	return render_template('index.html',title = 'Home',products=products, cart= cart_products)


@app.route('/contact')
def contact():
	return render_template('contact.html', title = 'Contact US')

@app.route('/checkout')
def checkout():	
	return render_template('checkout.html', title = 'Checkout')

@app.route('/customer-login')
def customerlogin():	
	return render_template('customer-login.html', title = 'Customer-Login')

@app.route('/customer-account')
def customeraccount():	
	return render_template('user_accountpage.html', title = 'Account')	

@app.route('/wishlist')
def wishlist():	
	return render_template('wishlist.html', title = 'Wishlist')

@app.route('/product-details')
def productdetails():
	reqname = request.args.get('name')
	productdetail = [d for d in products if d.get('name') == reqname]
	return render_template('product-details.html', title = 'Product Details', productdetail= productdetail)

@app.route('/shop')
def shop():	
	return render_template('shop.html', title = 'Shop')	

@app.route('/cart')
def cart():	
	return render_template('cart.html', title = 'Cart')
	
@app.route('/addtocart')	
def addtocart():
	reqname = request.args.get('name')
	reqsp = request.args.get('sp')
	reqmrp = request.args.get('mrp')
	cart_products.append({'name':reqname,'sp':reqsp,'mrp':reqmrp})
	return render_template('index.html',title = 'Home',products=products, cart= cart_products)

@app.route('/removefromcart')	
def removefromcart():
	reqname = request.args.get('name')
	reqsp = request.args.get('sp')
	reqmrp = request.args.get('mrp')
	cart_products[:] = [d for d in cart_products if d.get('name') != reqname]
	return render_template('index.html',title = 'Home',products=products, cart= cart_products)	

	

# def read_products():
# 	path = p.abspath(p.dirname(__file__))

# 	files = []
# 	# r=root, d=directories, f = files
# 	for r, d, f in os.walk(path):
# 		for file in f:
# 			if '.jpg' in file:
#             	files.append(os.path.join(r,file))



# 	for f in files:
#     	print(f)

# 	return path 
