from flask import Flask
from pymongo import MongoClient
from datetime import date
try:
    from user import user, password
except:
    user = 'Stephane'
    password = 'isenbrest'

class Connexion:
    @classmethod
    # Se connecter à Atlas
    def connect(cls):
        cls.user = user
        cls.password = password
        return MongoClient(f"mongodb+srv://{cls.user}:{cls.password}@bel-cluster.1cbyc.mongodb.net/?retryWrites=true&w=majority")
    
    @classmethod
    # Se connecter à la base de données
    def open_connexion(cls):
        cls.client = cls.connect()
        cls.collection = cls.client.flask.dons

    @classmethod
    # Se déconnecter de la base de données
    def close_connexion(cls):
        cls.client.close()

    @classmethod
    def insert(cls, prenom, nom, email, telephone, montant):
        cls.open_connexion()
        cls.collection.insert_one({'prenom': prenom, 'nom': nom, 'email': email,
                                'telephone': telephone, 'date': date.today().strftime("%Y/%m/%d"), 'montant': int(montant)})
        cls.close_connexion()
    
    @classmethod
    def get_dons(cls):
        cls.open_connexion()
        dons = list(cls.collection.find({}, {'_id': 0, 'prenom': 1, 'nom': 1, 'montant': 1, 'date': 1}).sort('date', -1).limit(10))
        print(dons)
        cls.close_connexion()
        return dons