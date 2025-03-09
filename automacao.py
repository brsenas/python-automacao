import pyautogui
import pandas as pd
import time

#define tempo de espera entre os comandos
pyautogui.PAUSE = 0.6
tabela = pd.read_csv("produtos.csv")

#passo a passo abertura do sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#espera para carregar
time.sleep(5)

#fazendo login no sistema
pyautogui.click(x=784, y=529)
pyautogui.write("brunosena@gmail.com")
pyautogui.press("tab")
pyautogui.write("senabruno")
pyautogui.click(x=963, y=747)

#aqui percorreremos as linhas da tabela
#para cada linha vamos cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=881, y=380)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]): #verifica se existe informação em obs, contrario n preenche
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

