from log import log_decorator

@log_decorator # esse é um decorator para capturar o log da funcao
def soma(a, b):
    return a + b

soma(1, 3)
soma(1, '2')