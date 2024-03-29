from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def get():
    return 'Hello World!'


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
