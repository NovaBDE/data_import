# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
# Ler os dados
TRE_2020 = pd.read_csv('C:/Users/flavia.manhaes.CONDEPEFIDEM.000/OneDrive - Universidade Federal de Pernambuco/BDE/BDE II/DADOS/perfil_eleitor_secao_2020_PE.csv',sep=";", encoding='latin1')
TRE_2020.columns.tolist() # para mostrar todas as colunas


# %%
TRE_2020.head()


# %%
TRE_2020_municipio=TRE_2020.groupby (['NM_MUNICIPIO'],as_index=False).count ()
TRE_2020_municipio.columns.tolist()
TRE_2020_municipio


# %%
# Eleitores por municipio
TRE_2020_ELEITORES=TRE_2020.groupby(['NM_MUNICIPIO'])['NM_MUNICIPIO'].count()
TRE_2020_ELEITORES=pd.DataFrame(TRE_2020_ELEITORES)
TRE_2020_ELEITORES


# %%
# Numero de Eleitores por grupo de idade
TRE_2020_FAIXA_ETARIA=TRE_2020.groupby(['NM_MUNICIPIO', 'DS_FAIXA_ETARIA'])['DS_FAIXA_ETARIA'].count().unstack().fillna(0)
TRE_2020_FAIXA_ETARIA


# %%
# Numero de eleitores por sexo
TRE_2020_GENERO=TRE_2020.groupby(['NM_MUNICIPIO', 'DS_GENERO'])['DS_GENERO'].count().unstack().fillna(0)
TRE_2020_GENERO


# %%
# Percentual de eleitorado, por grau de instrução
TRE_2020_PERC_GRAU_INSTRUC=TRE_2020.groupby(['NM_MUNICIPIO', 'DS_GRAU_ESCOLARIDADE'])['DS_GRAU_ESCOLARIDADE'].count().unstack().fillna(0)


# %%
# Exportar para excel

TRE_2020_ELEITORES.to_excel(r'C:/Users/flavia.manhaes.CONDEPEFIDEM.000/OneDrive - Universidade Federal de Pernambuco/BDE/BDE II/DADOS/DADOS PARA CECY/TRE_2020_ELEITORES.xlsx', sheet_name='Eleitores por município', index = True)
TRE_2020_FAIXA_ETARIA.to_excel(r'C:/Users/flavia.manhaes.CONDEPEFIDEM.000/OneDrive - Universidade Federal de Pernambuco/BDE/BDE II/DADOS/DADOS PARA CECY/TRE_2020_FAIXA_ETARIA.xlsx', sheet_name='Eleitores por município', index = True)
TRE_2020_GENERO.to_excel(r'C:/Users/flavia.manhaes.CONDEPEFIDEM.000/OneDrive - Universidade Federal de Pernambuco/BDE/BDE II/DADOS/DADOS PARA CECY/TRE_2020_GENERO.xlsx', sheet_name='Eleitores por município', index = True)
TRE_2020_PERC_GRAU_INSTRUC.to_excel(r'C:/Users/flavia.manhaes.CONDEPEFIDEM.000/OneDrive - Universidade Federal de Pernambuco/BDE/BDE II/DADOS/DADOS PARA CECY/TRE_2020_PERC_GRAU_INSTRUC.xlsx', sheet_name='Eleitores por município', index = True)


# %%
# Ler os dados
TRE_2020_ELEITORES = pd.read_csv('C:/Users/flavia.manhaes.CONDEPEFIDEM.000/OneDrive - Universidade Federal de Pernambuco/BDE/BDE II/DADOS/DADOS PARA CECY/TRE_2020_ELEITORES.csv',sep=";", encoding='latin1')
TRE_2020_PERC = pd.read_csv('C:/Users/flavia.manhaes.CONDEPEFIDEM.000/OneDrive - Universidade Federal de Pernambuco/BDE/BDE II/DADOS/DADOS PARA CECY/TRE_2020_PERC_GRAU_INSTRUC.csv',sep=";", encoding='latin1')


# %%
TRE_2020_PERC["ANALFABETO"]=(TRE_2020_PERC["ANALFABETO"]/TRE_2020_ELEITORES["Eleitores"])*100
TRE_2020_PERC["ENSINO FUNDAMENTAL COMPLETO"]=(TRE_2020_PERC["ENSINO FUNDAMENTAL COMPLETO"]/TRE_2020_ELEITORES["Eleitores"])*100
TRE_2020_PERC["ENSINO FUNDAMENTAL INCOMPLETO"]=(TRE_2020_PERC["ENSINO FUNDAMENTAL INCOMPLETO"]/TRE_2020_ELEITORES["Eleitores"])*100
TRE_2020_PERC["ENSINO MÉDIO COMPLETO"]=(TRE_2020_PERC["ENSINO MÉDIO COMPLETO"]/TRE_2020_ELEITORES["Eleitores"])*100
TRE_2020_PERC["ENSINO MÉDIO INCOMPLETO"]=(TRE_2020_PERC["ENSINO MÉDIO INCOMPLETO"]/TRE_2020_ELEITORES["Eleitores"])*100
TRE_2020_PERC["LÊ E ESCREVE"]=(TRE_2020_PERC["LÊ E ESCREVE"]/TRE_2020_ELEITORES["Eleitores"])*100
TRE_2020_PERC["NÃO INFORMADO"]=(TRE_2020_PERC["NÃO INFORMADO"]/TRE_2020_ELEITORES["Eleitores"])*100
TRE_2020_PERC["SUPERIOR COMPLETO"]=(TRE_2020_PERC["SUPERIOR COMPLETO"]/TRE_2020_ELEITORES["Eleitores"])*100
TRE_2020_PERC["SUPERIOR INCOMPLETO"]=(TRE_2020_PERC["SUPERIOR INCOMPLETO"]/TRE_2020_ELEITORES["Eleitores"])*100

TRE_2020_PERC.to_excel(r'C:/Users/flavia.manhaes.CONDEPEFIDEM.000/OneDrive - Universidade Federal de Pernambuco/BDE/BDE II/DADOS/DADOS PARA CECY/TRE_2020_PERC.xlsx', sheet_name='Eleitores por município', index = True)


# %%
TRE_2020_PERC_GRAU_INSTRUC.info()


