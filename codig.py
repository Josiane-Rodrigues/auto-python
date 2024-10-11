# Passo 1: entra no sistema da empresa
import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 2: Fazer longin
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#dar uma pausa de 3 seg 
time.sleep(3)
pyautogui.click(x=626, y=521)   
pyautogui.write("jos@hormail.com")
pyautogui.press("tab")
pyautogui.write("123589")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# Passo 3: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)
# passo 4 : cadastro de produtos 
# para cada linnha minha tabela 
for linha in tabela.index:

   pyautogui.click(x=609, y=369)
   #codego do produto 
   codigo = tabela.loc[linha, "codigo"]
   pyautogui.write(str(codigo))
   pyautogui.press("tab")

   # marca do produto 
 
   marca = tabela.loc[linha, "marca"]
   pyautogui.write(str(marca))
   pyautogui.press("tab")

   # tipo do produto 
   tipo = tabela.loc[linha,"tipo"]
   pyautogui.write(str(tipo))
   pyautogui.press("tab")

   # categoria de do produto 
   categoria = tabela.loc[linha,"categoria"]
   pyautogui.write(str(categoria))
   pyautogui.press("tab")

    #preço unitario 
   preco = tabela.loc[linha,"preco_unitario"]
   pyautogui.write(str(preco)) 
   
   pyautogui.press("tab")

   # custo do produto
   custo = tabela.loc[linha,"custo"]
   pyautogui.write(str(custo))
   pyautogui.press("tab") 

   # obs
   obs = tabela.loc[linha,"obs"]
   if not pd.isna(obs):
      pyautogui.write(str(obs))
   pyautogui.press("tab") 

   #clicar no botão enviar  
   pyautogui.press("enter")
   pyautogui.scroll(50000)

 
