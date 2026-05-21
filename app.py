import os
from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) # Isse ab koi website error nahi aayega

# 1. DUKAAN KA NAAM AUR TAGLINE
DUKAAN_INFO = {
    "name": "🛍️ Fresh Kart 🛍️",
    "tagline": "Fresh items, directly connected to Python Back-end"
}

# 2. DUKAAN KA SAMAAN
PRODUCTS = [
    {
        "id": 1, 
        "name": "Billionaire Gaming Phone 📱", 
        "price": "₹49,999", 
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 2, 
        "name": "Superstar Sports Shoes 👟", 
        "price": "₹4,999", 
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 3, 
        "name": "Royal Luxury Watch ⌚", 
        "price": "₹12,500", 
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&auto=format&fit=crop&q=60"
    }
]

# Yeh handle karega jab website khulegi aur saamaan mangegi
@app.route('/get-shop-data', methods=['GET'])
def get_shop_data():
    return jsonify({
        "info": DUKAAN_INFO,
        "products": PRODUCTS
    })

# Yeh handle karega jab koi 'Buy Now' button dabayega
@app.route('/buy-product', methods=['POST'])
def buy_product():
    data = request.json
    product_name = data.get('product_name', 'Unknown Item')
    print(f"\n🚨 ALERT: Kisi customer ne '{product_name}' par click kiya hai!\n")
    return jsonify({
        "status": "success", 
        "message": f"Success! '{product_name}' ka order Python Backend tak pahunch gaya!"
    })

if __name__ == '__main__':
    print("Server shuru ho raha hai... Port 5000 par.")
    app.run(debug=True, port=5000)