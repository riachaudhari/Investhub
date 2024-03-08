from tkinter import *
import yfinance as yf


def fetch_data():
    symbol = e.get()
    stock_info = fetch_stock_info(symbol)
    if stock_info is not None:
        display_stock_info(stock_info)


def fetch_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        # print(stock.info)
        info = {
            "Name": stock.info.get('longName', 'N/A'),
            "Type": stock.info.get('quoteType', 'N/A'),
            "Current Price": stock.info.get('currentPrice', 'N/A'),
            "Industry": stock.info.get('industry', 'N/A'),
            "Market Cap": stock.info.get('marketCap', 'N/A'),
            "PE Ratio": stock.info.get('trailingPE', 'N/A'),
            "PB Ratio": stock.info.get('priceToBook', 'N/A'),
            "EBITDA": stock.info.get('ebitda', 'N/A'),
            "Total Debt": stock.info.get('totalDebt', 'N/A'),
            "Total Revenue": stock.info.get('totalRevenue', 'N/A'),
        }
        return info
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def display_stock_info(info):
    info_text.delete(1.0, END)
    for key, value in info.items():
        info_text.insert(END, f"{key}: {value}\n")


root = Tk()
root.title("Stock Information")
root.geometry("900x700")

l = Label(root, text="Enter Stock Symbol:")
l.pack(pady=10)
e = Entry(root)
e.pack(pady=10)

b = Button(root, text="Fetch Data", command=fetch_data)
b.pack(pady=10)

info_text = Text(root)
info_text.pack(pady=10)

root.mainloop()
