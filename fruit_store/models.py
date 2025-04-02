# models.py
# models.py

class Fruta:
    def __init__(self, name: str, quantity: int, price: float, family: str, genus: str, order: str, carbohydrates: float, protein: float, fat: float, calories: float, sugar: float):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.family = family
        self.genus = genus
        self.order = order
        self.carbohydrates = carbohydrates
        self.protein = protein
        self.fat = fat
        self.calories = calories
        self.sugar = sugar

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "family": self.family,
            "genus": self.genus,
            "order": self.order,
            "carbohydrates": self.carbohydrates,
            "protein": self.protein,
            "fat": self.fat,
            "calories": self.calories,
            "sugar": self.sugar
        }

# Base de datos de frutas
fruits_db = [
    Fruta("Manzana", 50, 0.5, "Rosaceae", "Malus", "Rosales", 13.81, 0.26, 0.17, 52, 10.39),
    Fruta("Banana", 30, 0.2, "Musaceae", "Musa", "Zingiberales", 22.84, 1.09, 0.33, 89, 12.23),
    Fruta("Naranja", 20, 0.3, "Rutaceae", "Citrus", "Sapindales", 11.75, 0.94, 0.12, 47, 9.35),
    Fruta("Pera", 10, 0.4, "Rosaceae", "Pyrus", "Rosales", 15.23, 0.36, 0.14, 57, 9.75),
    Fruta("Uva", 40, 0.6, "Vitaceae", "Vitis", "Vitales", 18.1, 0.72, 0.16, 69, 15.48),
    Fruta("Fresa", 60, 0.7, "Rosaceae", "Fragaria", "Rosales", 7.68, 0.67, 0.3, 32, 4.89),
    Fruta("Kiwi", 25, 0.8, "Actinidiaceae", "Actinidia", "Ericales", 14.66, 1.14, 0.52, 61, 8.99),
    Fruta("Mango", 15, 1.0, "Anacardiaceae", "Mangifera", "Sapindales", 14.98, 0.82, 0.38, 60, 13.66),
    Fruta("Piña", 10, 1.2, "Bromeliaceae", "Ananas", "Poales", 13.12, 0.54, 0.12, 50, 9.85),
    Fruta("Melón", 5, 2.0, "Cucurbitaceae", "Cucumis", "Cucurbitales", 8.16, 0.84, 0.19, 34, 7.86),
    Fruta("Sandía", 3, 3.0, "Cucurbitaceae", "Citrullus", "Cucurbitales", 7.55, 0.61, 0.15, 30, 6.2),
    Fruta("Papaya", 8, 1.5, "Caricaceae", "Carica", "Brassicales", 10.82, 0.47, 0.26, 43, 7.82),
    Fruta("Cereza", 50, 0.9, "Rosaceae", "Prunus", "Rosales", 16.01, 1.06, 0.2, 63, 12.82),
    Fruta("Coco", 7, 2.5, "Arecaceae", "Cocos", "Arecales", 15.23, 3.33, 33.49, 354, 6.23),
    Fruta("Limón", 35, 0.4, "Rutaceae", "Citrus", "Sapindales", 9.32, 1.1, 0.3, 29, 2.5),
    Fruta("Mandarina", 45, 0.3, "Rutaceae", "Citrus", "Sapindales", 13.34, 0.81, 0.31, 53, 10.58),
    Fruta("Granada", 20, 0.8, "Lythraceae", "Punica", "Myrtales", 18.7, 1.67, 1.2, 83, 13.67),
    Fruta("Higo", 15, 1.0, "Moraceae", "Ficus", "Rosales", 19.18, 0.75, 0.3, 74, 16.26),
    Fruta("Ciruela", 25, 0.7, "Rosaceae", "Prunus", "Rosales", 11.42, 0.7, 0.28, 46, 9.92),
    Fruta("Arándano", 30, 1.5, "Ericaceae", "Vaccinium", "Ericales", 14.49, 0.74, 0.33, 57, 9.96)
]
