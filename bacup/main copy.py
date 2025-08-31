from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import connect
import time
from . import models, schemas
from .database import engine , get_db
from sqlalchemy.orm import Session

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
    
@app.get("/")
def root():
    return {"message": "Hello Sam!!!!!!!"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):

#     # posts = db.query(models.Post).all()
#     posts = db.query(models.Post)
#     print(posts)
#     return {"data ": "success"}

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all
    print(posts)
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_Posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # posts = db.query(models.Post)
    # print(**post.dict())
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)

    db.commit()
    db.refresh(new_post)

    return{"data": new_post}
    

@app.get("/posts/latest")
def get_latest_Posts():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

#path parameter
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    # print(post)
    # return {"post details": post}
# def get_post(id: int, response: Response):
# def get_post(id: int):
#     cursor.execute("""SELECT * from posts WHERE id = %s """, (str(id)))
#     post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    print(post)
    return {"post details": post}

# title str, content str,category, bool published

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #deleting post
    #find the index in the array that has requried ID
    #my_posts.pop(index)
    cursor.execute(
        """DELETE FROM posts WHERE id = %s returning * """, (str(id),))
    delete_post = cursor.fetchone()
    conn.commit()
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} does not exists")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_posts(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, 
    #                (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    con.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exists")
    
    return {'data': updated_post}
