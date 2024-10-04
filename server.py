from fastapi import FastAPI

app = FastAPI()

# decorator
@app.get("/")

async def root():
    return {
        "mensagem": "Olá FastAPI"
    }
