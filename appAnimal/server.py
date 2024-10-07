from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()


class Animal(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    sexo: str
    cor: str


bd: List[Animal] = []


@app.get("/animais")
def listar_animais():
    return bd


@app.get("/animais/{animal_id}")
def obter_animal(animal_id: str):
    for animal in bd:
        if animal.id == animal_id:
            return animal
    return {"error": "Animal não encontrado"}


@app.post("/animais")
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    bd.append(animal)
    return None


@app.delete("/animais/{animal_id}")
def remover_animal(animal_id: str):
    posicao = -1
    for index, animal in enumerate(bd):
        if animal.id == animal_id:
            posicao = index
            break
    if posicao != -1:
        bd.pop(posicao)
        return {"msg": "Animal removido com sucesso!"}
    else:
        return {"error": "Animal não encontrado"}
