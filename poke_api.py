from crud import CRUD

from imports import Flask, CORS

if __name__ == '__main__':
    crud = CRUD()
    crud.open_connection()
    crud.close_connection()