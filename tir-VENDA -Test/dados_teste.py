import xlwt
import shutil

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()