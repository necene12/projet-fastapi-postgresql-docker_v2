from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import csv
from datetime import datetime
from typing import List
from sqlalchemy import text

import models
import database

app = FastAPI()

# Fonction de connexion
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/createdb")
def create_db(db: Session = Depends(get_db)):
    try:
        database.Base.metadata.create_all(bind=database.engine)
        return {"message": "Base de données a été créée avec Succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/insertdata")
def insert_data(db: Session = Depends(get_db)):
    try:
        with open('bdd.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                product = models.ProductCreate(
                    amount_max=float(row['prices.amountMax']) if row['prices.amountMax'] else None,
                    amount_min=float(row['prices.amountMin']) if row['prices.amountMin'] else None,
                    availability=row['prices.availability'] if row['prices.availability'] else None,
                    condition=row['prices.condition'] if row['prices.condition'] else None,
                    currency=row['prices.currency'] if row['prices.currency'] else None,
                    date_seen=row['prices.dateSeen'] if row['prices.dateSeen'] else None,
                    is_sale=bool(row['prices.isSale']) if row['prices.isSale'] else None,
                    merchant=row['prices.merchant'] if row['prices.merchant'] else None,
                    shipping=row['prices.shipping'] if row['prices.shipping'] else None,
                    source_urls=row['prices.sourceURLs'] if row['prices.sourceURLs'] else None,
                    asins=row['asins'] if row['asins'] else None,
                    brand=row['brand'] if row['brand'] else None,
                    categories=row['categories'] if row['categories'] else None,
                    date_added=row['dateAdded'] if row['dateAdded'] else None,
                    date_updated=row['dateUpdated'] if row['dateUpdated'] else None,
                    ean=row['ean'] if row['ean'] else None,
                    image_urls=row['imageURLs'] if row['imageURLs'] else None,
                    keys=row['keys'] if row['keys'] else None,
                    manufacturer=row['manufacturer'] if row['manufacturer'] else None,
                    manufacturer_number=row['manufacturerNumber'] if row['manufacturerNumber'] else None,
                    name=row['name'] if row['name'] else None,
                    primary_categories=row['primaryCategories'] if row['primaryCategories'] else None,
                    upc=row['upc'] if row['upc'] else None,
                    weight=row['weight'] if row['weight'] else None,
                )
                db_product = models.Product(**product.dict())
                db.add(db_product)
            db.commit()
        return {"message": "Données insérées avec succès"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
def query_database(query: str, db: Session = Depends(get_db)):
    result = db.execute(query).fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="Aucun résultat trouvé")
    return JSONResponse(content=result)
