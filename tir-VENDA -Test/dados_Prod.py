# coding: utf-8
import pandas as pd
from pandas.core.frame import DataFrame
import xlrd
import numpy as np


url = (r"C:\tabelaVendas.xlsx")
xls = pd.ExcelFile(url)
plan = pd.read_excel(xls, 'Produto')

linha_coluna = plan.shape
lin = linha_coluna[0]
col = linha_coluna[1]
planilha_dataframe = pd.DataFrame(plan)

CABECALHO = []
COL_A = []
COL_B = []
COL_C = []
COL_D = []
COL_E = []
COL_F = []
COL_G = []
COL_H = []
COL_I = []
COL_J = []
COL_K = []
COL_L = []
COL_M = []
COL_N = []
COL_O = []

contador = 0

for cabecalho_excel in planilha_dataframe:
    
    CABECALHO.append(cabecalho_excel)

    if (contador == 0):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_A.append(coluna)
            i+=1

    if (contador == 1):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_B.append(coluna)
            i+=1
    if (contador == 2):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_C.append(coluna)
            i+=1

    if (contador == 3):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_D.append(coluna)
            i+=1

    if (contador == 4):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_E.append(coluna)
            i+=1

    if (contador == 5):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_F.append(coluna)
            i+=1

    if (contador == 6):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_G.append(coluna)
            i+=1

    if (contador == 7):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_H.append(coluna)
            i+=1

    if (contador == 8):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_I.append(coluna)
            i+=1

    if (contador == 9):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_J.append(coluna)
            i+=1

    if (contador == 10):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_K.append(coluna)
            i+=1

    if (contador == 11):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_L.append(coluna)
            i+=1

    if (contador == 12):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_M.append(coluna)
            i+=1

    if (contador == 13):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_N.append(coluna)
            i+=1

    if (contador == 14):
        i=0
        while i < lin:
            coluna = str(plan[cabecalho_excel][i])#.zfill(6)
            COL_O.append(coluna)
            i+=1

    contador += 1

print('Produtos: {}'.format(lin))