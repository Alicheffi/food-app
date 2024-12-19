from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, db  # Importing Realtime Database instead of Firestore

# Initialisation de l'application Flask
app = Flask(__name__)

# Initialisation de Firebase
cred = credentials.Certificate("C:/Users/LENOVO/Desktop/food-app-ae7c9-firebase-adminsdk-cmuyt-b2c795c5f5.json")  # Remplacez par le chemin vers votre fichier JSON
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://food-app-ae7c9-default-rtdb.firebaseio.com'  # Remplacez par l'URL de votre Realtime Database
})

# Connexion à Realtime Database
food_ref = db.reference('Foods')  # Référence à la racine "Foods"
category_ref = db.reference('Category')  # Référence à la racine "Categories"
order_ref = db.reference('Orders')  # Référence à la racine "Orders"
time_ref = db.reference('Time')  # Référence à la racine "Times"
location_ref = db.reference('Location')  # Référence à la racine "Locations"
price_ref = db.reference('Price')  # Référence à la racine "Prices"


@app.route('/')
def home():
    return 'Welcome to the Food App API!'
# Routes pour les Foods
@app.route('/food', methods=['GET'])
def get_foods():
    try:
        foods = food_ref.get()
        if foods:
            return jsonify(foods), 200
        else:
            return jsonify({"message": "Aucune donnée trouvée"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/food/add', methods=['POST'])
def add_food():
    data = request.json
    try:
        food_ref.push(data)
        return jsonify({"message": "Food ajouté avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour les Categories
@app.route('/category', methods=['GET'])
def get_categories():
    try:
        categories = category_ref.get()
        if categories:
            return jsonify(categories), 200
        else:
            return jsonify({"message": "Aucune donnée trouvée"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/category/add', methods=['POST'])
def add_category():
    data = request.json
    try:
        category_ref.push(data)
        return jsonify({"message": "Catégorie ajoutée avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour les Orders
@app.route('/order', methods=['GET'])
def get_orders():
    try:
        orders = order_ref.get()
        if orders:
            return jsonify(orders), 200
        else:
            return jsonify({"message": "Aucune donnée trouvée"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/order/add', methods=['POST'])
def add_order():
    data = request.json
    try:
        order_ref.push(data)
        return jsonify({"message": "Order ajouté avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour les Times
@app.route('/time', methods=['GET'])
def get_times():
    try:
        times = time_ref.get()
        if times:
            return jsonify(times), 200
        else:
            return jsonify({"message": "Aucune donnée trouvée"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/time/add', methods=['POST'])
def add_time():
    data = request.json
    try:
        time_ref.push(data)
        return jsonify({"message": "Time ajouté avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour les Locations
@app.route('/location', methods=['GET'])
def get_locations():
    try:
        locations = location_ref.get()
        if locations:
            return jsonify(locations), 200
        else:
            return jsonify({"message": "Aucune donnée trouvée"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/location/add', methods=['POST'])
def add_location():
    data = request.json
    try:
        location_ref.push(data)
        return jsonify({"message": "Location ajoutée avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour les Prices
@app.route('/price', methods=['GET'])
def get_prices():
    try:
        prices = price_ref.get()
        if prices:
            return jsonify(prices), 200
        else:
            return jsonify({"message": "Aucune donnée trouvée"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/price/add', methods=['POST'])
def add_price():
    data = request.json
    try:
        price_ref.push(data)
        return jsonify({"message": "Price ajouté avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour mettre à jour et supprimer des Foods
@app.route('/food/update/<food_id>', methods=['PUT'])
def update_food(food_id):
    data = request.json
    try:
        food_ref.child(food_id).update(data)
        return jsonify({"message": "Food mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/food/delete/<food_id>', methods=['DELETE'])
def delete_food(food_id):
    try:
        food_ref.child(food_id).delete()
        return jsonify({"message": "Food supprimé avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour mettre à jour et supprimer des Categories
@app.route('/category/update/<category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.json
    try:
        category_ref.child(category_id).update(data)
        return jsonify({"message": "Catégorie mise à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/category/delete/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        category_ref.child(category_id).delete()
        return jsonify({"message": "Catégorie supprimée avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour mettre à jour et supprimer des Orders
@app.route('/order/update/<order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    try:
        order_ref.child(order_id).update(data)
        return jsonify({"message": "Order mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/order/delete/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        order_ref.child(order_id).delete()
        return jsonify({"message": "Order supprimé avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour mettre à jour et supprimer des Times
@app.route('/time/update/<time_id>', methods=['PUT'])
def update_time(time_id):
    data = request.json
    try:
        time_ref.child(time_id).update(data)
        return jsonify({"message": "Time mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/time/delete/<time_id>', methods=['DELETE'])
def delete_time(time_id):
    try:
        time_ref.child(time_id).delete()
        return jsonify({"message": "Time supprimé avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour mettre à jour et supprimer des Locations
@app.route('/location/update/<location_id>', methods=['PUT'])
def update_location(location_id):
    data = request.json
    try:
        location_ref.child(location_id).update(data)
        return jsonify({"message": "Location mise à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/location/delete/<location_id>', methods=['DELETE'])
def delete_location(location_id):
    try:
        location_ref.child(location_id).delete()
        return jsonify({"message": "Location supprimée avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Routes pour mettre à jour et supprimer des Prices
@app.route('/price/update/<price_id>', methods=['PUT'])
def update_price(price_id):
    data = request.json
    try:
        price_ref.child(price_id).update(data)
        return jsonify({"message": "Price mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/price/delete/<price_id>', methods=['DELETE'])
def delete_price(price_id):
    try:
        price_ref.child(price_id).delete()
        return jsonify({"message": "Price supprimé avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Lancer le serveur
if __name__ == '__main__':
    app.run(debug=True)
