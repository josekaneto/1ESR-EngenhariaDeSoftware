import os
import logging

# directory_name = "my_new_directory"
# os.mkdir(directory_name)
#
# with open ('my_new_directory/exemplo.py', 'w')  as arquivo:
#     print("Arquivo criado")

# with open ('exemplo.txt', 'w')  as arquivo:
#     arquivo.write('Olá, este é um exemplo de escrita em arquivo.\n')
#     arquivo.write('Python é poderoso e versátil!\n')
#     arquivo.write('Fechando o arquivo automaticamente com o bloco "with".\n')

# with open('exemplo.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# with open('exemplo.txt', 'a') as arquivo:
#     # Escrever algumas linhas no arquivo sem sobrescrever o conteúdo existente
#     arquivo.write('Esta linha será adicionada ao conteúdo existente.\n')
#     arquivo.write('Adicionando outra linha.\n')

# with open('exemplo.txt', 'r') as arquivo:
#     for linha in arquivo:
#         print(linha.strip())

# caminho_arquivo = 'exemplo.txt'
#
# if os.path.exists(caminho_arquivo):
#     print(f'O arquivo {caminho_arquivo} existe.')
# else:
#     print(f'O arquivo {caminho_arquivo} não existe.')

# caminho_arquivo = 'exemplo.txt'
# # Verificar se o arquivo existe antes de tentar excluí-lo
# if os.path.exists(caminho_arquivo):
#     os.remove(caminho_arquivo)
#     print(f'O arquivo {caminho_arquivo} foi excluído.')
# else:
#     print(f'O arquivo {caminho_arquivo} não existe.')


# Configurando o logger
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')
# logging.debug('Isso é uma mensagem de depuração')
# logging.info('Isso é uma mensagem informativa')
# logging.warning('Isso é um alerta')
# logging.error('Ocorreu um erro!')
# logging.critical('Erro crítico! O sistema pode parar de funcionar.')

# Configurando o logger
# logging.basicConfig(filename='log.log', level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
# Realizando as operações de log
# logging.debug("Executing program")
# logging.debug("Processing data...")
# logging.info("Server started successfully.")
# logging.warning("Invalid configuration detected.")
# logging.error("Failed to connect to the database.")
# logging.critical("Unexpected system error occurred. Shutting down.\n")

logging.basicConfig(filename='log.log', level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Iniciando Programa")

try:
    print(10/0)
    logging.info("Operação Realizada")
except Exception as e:
    logging.error(f"Ocorreu um erro inesperado {e}")