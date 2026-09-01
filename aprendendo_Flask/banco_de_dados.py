import psycopg2 as pg
from psycopg2 import Error
import os

def conectar():
    try:
        conect = pg.connect(
            user = "postgres",
            password = "sua_senha_aqui",
            host = "127.0.0.1",
            port = "5432",
            database = "controlefinanceiro"

        )
        return conect
    except Error as e:
        print(f"Ocorreu um erro ao se conectar ao banco de dados: {e}")

def encerrar_conexao(conect):
    if conect:
        conect.close()
