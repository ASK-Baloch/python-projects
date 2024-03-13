from fastapi import FastAPI
import uvicorn

app = FastAPI()


engine = create_engine('sqlite:///./db.sqlite3', connect_args={'check_same_thread': False})


@app.get('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)