#!/bin/bash

# Démarrer les conteneurs Docker pour Postgres et l'API
docker-compose up --build

# Attendre que le conteneur Postgres soit prêt
#while ! docker exec api_db psql -U metoo -c '\q' &>/dev/null; do
#    sleep 1
#done

#docker exec -it api_db createdb -U metoo db_product

#docker exec -it api_api python /app/inject_data.py

#echo "Le service est disponible à l'adresse http://localhost:8000/docs"
