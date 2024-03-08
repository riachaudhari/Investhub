from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import yfinance as yf


def fetch_data():
    symbol1 = e1.get()
    symbol2 = e2.get()

    df1 = fetch_stock_data(symbol1)
    df2 = fetch_stock_data(symbol2)

    if df1 is not None and df2 is not None:
        plot_stock_data(df1, df2)


def fetch_stock_data(symbol):
    try:
        start = '2010-01-01'
        end = '2023-12-31'
        df = yf.download(symbol, start=start, end=end)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def plot_stock_data(df1, df2):
    ax.clear()  # Clear previous plot
    ax.plot(df1['Close'], color='red', label='Stock 1')
    ax.plot(df2['Close'], color='blue', label='Stock 2')
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Closing Price")
    ax.legend()

    # Toolbar
    toolbar.update()
    canvas.draw()


root = Tk()
root.title("Compare Stocks")
root.geometry("900x700")

l1 = Label(root, text="Enter Stock Symbol 1:", font=("Trebuchet MS", 12, "bold"))
l1.pack(pady=10)
e1 = Entry(root, font=("Trebuchet MS", 12))
e1.pack(pady=10)

l2 = Label(root, text="Enter Stock Symbol 2:", font=("Trebuchet MS", 12, "bold"))
l2.pack(pady=10)
e2 = Entry(root, font=("Trebuchet MS", 12))
e2.pack(pady=10)

b1 = Button(root, text="Fetch Data", command=fetch_data, font=("Trebuchet MS", 10, "bold"), width=15, pady=4, background="black", foreground="white")
b1.pack(pady=10)


figure = Figure(figsize=(5, 4))
ax = figure.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
toolbar.pack(side=TOP, fill=X)

root.mainloop()
