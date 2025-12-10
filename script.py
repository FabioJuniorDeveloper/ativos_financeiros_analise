import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (14, 6)

def baixar_dados(tickers, period="5y"):

    df = yf.download(tickers, period=period, progress=False)

    
    df = df["Close"]

    
    if isinstance(df, pd.Series):
        df = df.to_frame()

    return df.dropna(how="all")

def normalizar(df):
    """Normaliza para 100 no primeiro dia."""
    return df.div(df.iloc[0]).mul(100)


tickers = ["^BVSP", "AAPL", "VALE3.SA", "PETR4.SA"]


dados = baixar_dados(tickers, period="5y")
print(dados.head())


dados_norm = normalizar(dados)


dados_norm.plot(title="Comparação — Evolução Normalizada (Base 100)")
plt.ylabel("Evolução")
plt.grid(alpha=0.3)
plt.show()