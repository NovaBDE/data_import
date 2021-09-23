#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Passo 1 - Entrar no nosso sistema (Entrar no link: https://www.tse.jus.br/eleitor/estatisticas-de-eleitorado/estatistica-do-eleitorado-por-sexo-e-faixa-etaria)

# Passo 2 - Selecionar o municipio

# Passo 3 - Baixar o arquivo do TRE 


# In[1]:


# Bibliotecas utilizadas

import pyautogui # automatiza o teclado, o mouse e a tela do computador
import pyperclip
import time


# In[6]:


# Passo 1 - Acessar o site
def baixarPlanilhas(qtd):
    print("Entrou na função")
    pyautogui.PAUSE = 1 #tempo de 1 segundo entre cada ação
    pyautogui.hotkey("ctrl","t") # abre uma nova tela utilizando uma combinação de teclas
    link ="https://www.tse.jus.br/eleitor/estatisticas-de-eleitorado/estatistica-do-eleitorado-por-sexo-e-grau-de-instrucao"
    pyperclip.copy(link) #resolve problemas de caracteres especiais no link
    pyautogui.hotkey("ctrl","v") # abre uma nova tela
    # pyautogui.write("") #escreve
    pyautogui.press("enter")  # pressiona a tecla enter
    # pyautogui.press("win") -- pressiona a tecla do windows
    
    # Passo 2 - Navegar no sistema
    while qtd>0:      
        time.sleep(5) # espera 5 segundos
        # seleciona o municipio
        pyautogui.click(x=802, y=534)
        pyautogui.press('down')   # pressiona a tecla enter
        
                
        # Vai para pesquisar
        pyautogui.press('tab')   # pressiona a tecla tab
        pyautogui.press('tab')   # pressiona a tecla tab
        pyautogui.press('tab')   # pressiona a tecla tab
        pyautogui.press('tab')   # pressiona a tecla tab
        
        # Seleciona pesquisar
        pyautogui.press('enter')   # pressiona a tecla enter
        
        # Clica fora da tela
        pyautogui.click(x=1347, y=740) 
        
        # Vai para download
        pyautogui.press('tab')   # pressiona a tecla enter
        
        # Seleciona download
        pyautogui.press('enter')   # pressiona a tecla enter            
        qtd=qtd-1        
    return qtd
    #pyautogui.hotkey("ctrl","w")
    
    


# In[8]:


display(baixarPlanilhas(184))


    


# In[21]:



# Pegar a posição do mouse no local desejado
time.sleep(5) # espera 5 segundos
pyautogui.position()
# Point(x=595, y=506) --> posição do municipio

