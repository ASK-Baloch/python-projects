from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from models import Blog
from database import engine
from typing import Annotated


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


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(id, db: Annotated[Session, Depends(get_deb)]):
    blog = db.get(Blog, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {id} not found")
    return blog


@app.patch("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def updating(id: int, req: Blog, db: Session = Depends(get_deb)):
    with db.begin() as session:
        try:
            blog = session.get(Blog, id)
            if not blog:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Blog with id {id} not found",
                )

            # Update model attributes directly
            blog.title = req.title
            blog.body = req.body

            session.add(blog)  # Mark model for update
            session.commit()  # Commit changes
            return blog
        except Exception as e:
            session.rollback()  # Rollback if any error occurs
            raise HTTPException(status_code=500, detail=f"Error updating blog: {str(e)}")



@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Annotated[Session, Depends(get_deb)]):
    blog = db.get(Blog, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {id} not found")
    db.delete(blog)
    db.commit()
    return f'Blog with id:{id} deleted'
