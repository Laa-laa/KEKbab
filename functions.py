from flask import Flask, request, jsonify

app = Flask(__name__)

# Borne de commande
ingredients_borne = []

# Écran dans la cuisine
commande_cuisine = []

@app.route('/borne_commande', methods=['GET'])
def affichage_ingredients():
    return jsonify({'ingredients': ingredients_borne})

@app.route('/borne_commande', methods=['POST'])
def ajout_ingredient():
    ingredient = request.json.get('ingredient')
    ingredients_borne.append(ingredient)
    return jsonify({'message': 'Ingrédient ajouté au ticket'})

@app.route('/ecran_cuisine', methods=['GET'])
def affichage_commande_cuisine():
    return jsonify({'commande': commande_cuisine})

@app.route('/ecran_cuisine', methods=['DELETE'])
def effacer_commande_cuisine():
    commande_cuisine.clear()
    return jsonify({'message': 'Commande effacée de l\'écran'})

@app.route('/kebab', methods=['POST'])
def calcul_nombre_total():
    ingredients = request.json.get('ingredients')
    nombre_total = len(ingredients)
    return jsonify({'nombre_total': nombre_total})

if __name__ == '__main__':
    app.run(debug=True)
