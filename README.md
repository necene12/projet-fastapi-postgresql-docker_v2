#### API FastAPI avec PostgreSQL et SQLAlchemy

###### Prérequis
 * Python
 * Docker
 * docker-compose

###### Installation
 * Aller dans le répertoire app/ avec la commande suivante : 
   `cd app`
 * Lancer le script python suivant dans le dossier app/ pour préparer les données à importer dans la base de données postgresql :
   `python3 script_data_prep.py`
 * Lancer le script bash suivant dans le dossier app/ afin de donner les droit d'exécusion au fichier setup.sh :
   `chmod +x setup.sh`
 *  Lander la commande suivante dans le  dossier app/ pour exécuter l'api et la base de données : 
   `./setup.sh`

###### Vérifications:
  * ouvrir sur le navigateur : http://localhost:8000/docs#

###### Test de la dernière route avec le code sql suivant dans le corps

    `{"query": "SELECT * FROM products WHERE brand = 'Acer'"}`
