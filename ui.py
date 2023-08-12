import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # create a main window
        self.menu = tk.Menu()
        self.title("LITE LIS")
        self.state("zoomed")



if __name__ == '__main__':
    app = App()
    app.mainloop()