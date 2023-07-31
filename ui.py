import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # create a menu
        self.menu = tk.Menu()



if __name__ == '__main__':
    app = App()
    app.title = 'LiteLIS'
    app.mainloop()