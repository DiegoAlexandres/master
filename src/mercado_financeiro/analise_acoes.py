#%%
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#%%
#============================Análise da Ações TAEE11=======================
acoes = yf.Ticker("TAEE11.SA")

#%%
#============================Histórico de Preços=======================
historico = acoes.history(period="5y")
historico

#%%
#Data Corte últimos 5 anos
data_corte = pd.Timestamp.now(tz='UTC') - pd.DateOffset(years=5)

#%%
#Histórico de Dividendos
dividendos = acoes.dividends[acoes.dividends.index >= data_corte]
dados = pd.DataFrame(dividendos).reset_index()
dados

#%%
#Soma dos Dividendos
soma_dividendos = dados["Dividends"].sum()
soma_dividendos

#%%
#Média dos Dividendos
pagamento_medio = soma_dividendos / 5
pagamento_medio

#%%
#Gráfico dos Dividendos
plt.figure(figsize=(10, 5))
plt.plot(dados['Date'], dados['Dividends'])
plt.title('Dividendos da TAEE11')
plt.xlabel('Data')
plt.ylabel('Dividendos')
plt.show()

#%%
#Calculo do Preço Teto
def calcula_preco_teto(media_dividendos, taxa_retorno_esperada):
    preco_teto = media_dividendos / taxa_retorno_esperada
    return preco_teto

#%%
calcula_preco_teto(pagamento_medio, 0.08)