import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Estudante(BaseModel):
    nome: str
    curso: str
    ativo: bool


@app.get("/hello world")
async def root():
  return {"message": "Hello World"}



@app.get("/funcaoteste")
async def funcaoteste():
  return {"teste": True, "num_aleatório": random.randint(0, 20000)}



@app.post("/estudante/cadastro")
async def create_estudante(estudante: Estudante):
  return estudante


@app.put("/estudante/update/{id_estudante}")
async def update_estudante(id_estudante: int):
  return id_estudante > 0


@app.delete("estudante/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
  return id_estudante > 0
