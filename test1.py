from tkinter import *
from tkinter import ttk
import yfinance as yf
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fetch_data():
    symbol = entry_symbol.get()
    df = fetch_stock_data(symbol)
    if df is not None:
        plot_stock_data(df)

def fetch_stock_data(symbol):
    try:
        start = '2010-01-01'
        end = '2023-12-31'
        df = yf.download(symbol, start=start, end=end)
        df = df.reset_index()
        df = df.drop(['Date', 'Adj Close'], axis=1)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def plot_stock_data(df):
    figure = Figure(figsize=(5, 4))
    ax = figure.add_subplot(111)
    ax.plot(df['Close'])
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Closing Price")

    plot_canvas.figure = figure
    plot_canvas.draw()

def show_earnings_calendar():
    symbol = entry_symbol.get()
    earnings_data = fetch_earnings_calendar(symbol)
    if earnings_data:
        display_earnings_calendar(earnings_data)

def fetch_earnings_calendar(symbol):
    try:
        stock = yf.Ticker(symbol)
        earnings_df = stock.calendar
        return earnings_df
    except Exception as e:
        print(f"Error fetching earnings calendar: {e}")
        return None

def display_earnings_calendar(earnings_data):
    earnings_window = Toplevel(root)
    earnings_window.title("Earnings Calendar")
    earnings_window.geometry("400x200")

    earnings_date = earnings_data['Earnings Date'][0]
    text_widget = Text(earnings_window, wrap="word", font=("Helvetica", 12))
    text_widget.pack(expand=YES, fill=BOTH)
    text_widget.insert(INSERT, f"Earnings Date: {earnings_date}")

root = Tk()
root.title("Analyze Stock")
root.geometry("800x600")

label_symbol = Label(root, text="Enter Stock Symbol:")
entry_symbol = Entry(root)
button_fetch_data = Button(root, text="Fetch Data", command=fetch_data)
button_earnings_calendar = Button(root, text="Earnings Calendar", command=show_earnings_calendar)
plot_canvas = FigureCanvasTkAgg(Figure(figsize=(5, 4)), master=root)
plot_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

label_symbol.pack(pady=10)
entry_symbol.pack(pady=10)
button_fetch_data.pack(pady=10)
button_earnings_calendar.pack(pady=10)

# Timeframe dropdown menu
timeframes = ['Daily', 'Weekly', 'Monthly']
timeframe_var = StringVar()
timeframe_var.set(timeframes[0])  # Default to daily
timeframe_menu = OptionMenu(root, timeframe_var, *timeframes)
timeframe_menu.pack(pady=10)

root.mainloop()
