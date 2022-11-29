from tkinter import Tk
from ui.ui import UI

def main():
	window = Tk()
	window.title("Ohjelmoijan laskin")
	window.geometry("500x300")

	ui = UI(window)
	ui.start()

	window.mainloop()

if __name__ == "__main__":
	main()
