class OlaMundo:
    def __enter__(self):
        print("precionei enter para começar")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("finalizei")

with OlaMundo() as ola:
    print("executando!!")