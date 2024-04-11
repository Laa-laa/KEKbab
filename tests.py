import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_affichage_ingredients_borne(self):
        response = requests.get('http://127.0.0.1:5000/borne_commande')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('ingredients', data)

    def test_ajout_ingredient_borne(self):
        ingredient = {'ingredient': 'viande'}
        response = requests.post('http://127.0.0.1:5000/borne_commande', json=ingredient)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'Ingrédient ajouté au ticket')

    def test_affichage_commande_cuisine(self):
        response = requests.get('http://127.0.0.1:5000/ecran_cuisine')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('commande', data)

    def test_effacer_commande_cuisine(self):
        response = requests.delete('http://127.0.0.1:5000/ecran_cuisine')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'Commande effacée de l\'écran')

    def test_calcul_nombre_total_kebab(self):
        ingredients = {'ingredients': ['viande', 'salade', 'tomate']}
        response = requests.post('http://127.0.0.1:5000/kebab', json=ingredients)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('nombre_total', data)


