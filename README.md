#### API FastAPI avec PostgreSQL et SQLAlchemy

###### Prérequis
 * Docker
 * docker-compose

###### Installation
 * lancer le script suivant à la racine du fichier app/
   `chmod +x setup.sh`
 * Lancer le script
   `./setup.sh`

###### Vérifications:
  * ouvrir sur le navigateur : http://localhost:8000/docs#

###### Test de la dernière route avec le code sql suivant dans le corps

    `{
  "query": "SELECT * FROM product WHERE brand = 'Nike'"
     }`
