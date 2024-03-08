from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf


def fetch_data(symbol, ax, canvas):
    df = fetch_stock_data(symbol)
    if df is not None:
        plot_stock_data(df, ax, canvas)


def fetch_stock_data(symbol):
    try:
        start = '2010-01-01'
        end = '2023-12-31'
        df = yf.download(symbol, start=start, end=end)
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None


def plot_stock_data(df, ax, canvas):
    ax.clear()
    ax.plot(df['Close'])
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Closing Price")
    canvas.draw()


def show_chart(symbol, ax, canvas):
    fetch_data(symbol, ax, canvas)


root = Tk()
root.title("Stock List")
root.geometry("900x700")

figure = Figure(figsize=(5, 4))
ax = figure.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

# List of Indian stock symbols
indian_symbols = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS", "LICI.NS", "SBIN.NS",
                  "BHARTIARTL.NS", "HINDUNILVR.NS", "ITC.NS", "LT.NS", "HCLTECH.NS", "BAJFINANCE.NS", "ADANIENT.NS",
                  "SUNPHARMA.NS", "KOTAKBANK.NS", "MARUTI.NS", "ONGC.NS", "AXISBANK.NS", "TITAN.NS", "TATAMOTORS.NS",
                  "COALINDIA.NS", "ASIANPAINT.NS", "WIPRO.NS", "BAJFINANCE.NS", "ULTRACEMCO.NS", "DMART.NS",
                  "NESTLEIND.NS", "IRCTC.NS", "M&M.NS", "FINEORG.NS", "LTIM.NS"]

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
for symbol in indian_symbols:
    stock_info = yf.Ticker(symbol)
    name = stock_info.info['longName']
    listbox.insert(END, f"{symbol} - {name}")
listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)


def on_select(evt):
    index = listbox.curselection()[0]
    symbol = indian_symbols[index]
    show_chart(symbol, ax, canvas)


listbox.bind('<<ListboxSelect>>', on_select)

root.mainloop()
