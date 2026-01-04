#%%
import pandas as pd
import yfinance as yf

#%%
#============================Análise Ação=======================
acao = yf.Ticker("BBSE3.SA")
acao

#%%
#============================Histórico de Preços=======================
historico_preco = acao.history(period="5y").reset_index()
historico_preco

#%%
historico_preco = historico_preco.drop(columns=["Dividends", "Stock Splits"])

#%%
historico_preco

#%%
#============================Análise Dividendos=======================
data_corte = pd.Timestamp.now(tz='UTC') - pd.DateOffset(years=5)

#%%
dividendos = acao.dividends[acao.dividends.index >= data_corte]

#%%
dados_dividendos = pd.DataFrame(dividendos).reset_index()
dados_dividendos