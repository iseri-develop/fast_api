from fastapi import FastAPI

app = FastAPI()

# decorator
@app.get('/')
def root():
    return {
        "mensagem": "Olá FastAPI"
    }

@app.get('/profile')
def profile():
    return {
        "nome": "Igor Iseri"
    }
    
@app.post('/profile')
def signup():
    return {
        "mensagem": "Perfil enviado com sucesso"
    }
