from loguru import logger

logger.add('meu_app.log')
def soma(a, b):
    logger.info(f'Somando {a} + {b}')
    return a + b

logger.info(soma(1, '2'))