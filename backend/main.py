from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Hello, world!"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)