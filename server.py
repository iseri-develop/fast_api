from fastapi import FastAPI

app = FastAPI()


# decorator
@app.get("/")
def root():
    return {"mensagem": "Olá FastAPI"}


@app.get("/profile")
def profile():
    return {"nome": "Igor Iseri"}


@app.post("/profile")
def signup():
    return {"mensagem": "Perfil enviado com sucesso"}


@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    text = f"Ola {nome}, tudo bem?"
    return {"mensagem": text}


@app.get("/quadrado/{numero}")
def quadrado(numero: int):
    result = numero * numero
    text = f"O quadrado de {numero} é {result}"

    return {"mensagem": text}

# param Query
@app.get('/dobro')
def dobro(valor: int):
    result = 2 * valor
    return {"mensagem": f"O dobro do valor {valor} é {result}"}
