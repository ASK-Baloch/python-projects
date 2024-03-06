from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from models import Blog, showBlog, User, ShowUser
from database import engine
from typing import Annotated
from hashing import Hash


# Create the FastAPI application
app = FastAPI()

# Create all tables
Blog.metadata.create_all(engine)


def get_deb():
    with Session(engine) as session:
        yield session


@app.get("/blog", status_code=status.HTTP_200_OK)
def get_all(db: Annotated[Session, Depends(get_deb)]):
    blogs = db.exec(select(Blog)).all()
    return blogs


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(req: Blog, db: Session = Depends(get_deb)):
    new_blog = Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=list[showBlog])
def show(id, db: Annotated[Session, Depends(get_deb)]):
    blog = db.get(Blog, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {id} not found")
    return blog


@app.patch("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def updating(id: int, req: Blog, db: Session = Depends(get_deb)):
    blog = db.get(Blog, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found",
        )
    if req.title is not None and req.title != blog.title:
        blog.title = req.title

    if req.body is not None and req.body != blog.body:
        blog.body = req.body

    db.add(blog)
    db.commit()
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Annotated[Session, Depends(get_deb)]):
    blog = db.get(Blog, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {id} not found")
    db.delete(blog)
    db.commit()
    return f'Blog with id:{id} deleted'


#                            NOW CREATING USER ROUTES...

@app.post('/user', response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Annotated[Session, Depends(get_deb)]):

    new_user = User(name=request.name, email=request.email,
                    password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Ensure response is a dictionary
    return new_user.dict()  # Convert model instance to a dictionary


@app.get('/user/{id}', response_model=ShowUser, status_code=status.HTTP_200_OK)
def get_user(id: str, db: Annotated[Session, Depends(get_deb)]):
    user = db.get(User, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found")
    return user