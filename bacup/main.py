from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import connect
import time
from . import models, schemas, utils
from .database import engine , get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Databse connection was sucesfull!")
#         break
#     except Exception as error:
#         print("Connecting to databse failed")
#         print("Error :", error)
#         time.sleep(2)

my_posts = [{"title": "title of post 1", "content" : "content of post 1", "id": 1}, 
            {"title": "fevorite food", "content" : "I like Pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

    
@app.get("/")
def root():
    return {"message": "Hello Sam!!!!!!!"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):

#     # posts = db.query(models.Post).all()
#     posts = db.query(models.Post)
#     print(posts)
#     return {"data ": "success"}



