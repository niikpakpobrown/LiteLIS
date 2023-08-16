import tkinter as tk
from tkinter import ttk

class TestElement:
    def __init__(self, parent_frame, row, test_name, r_range, unit):
        self.parent_frame = parent_frame
        self.row = row
        self.test_name = test_name
        self.r_range = r_range
        self.unit = unit

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.parent_frame, text=self.test_name, font=("Helvetica", 12, "bold")).grid(row=self.row, column=0, padx=5, pady=5, columnspan=4)
        ttk.Entry(self.parent_frame, font=("Helvetica", 12, "bold")).grid(row=self.row, column=4, padx=50, pady=5, columnspan=4)
        ttk.Label(self.parent_frame, text=self.r_range, font=("Helvetica", 12, "bold")).grid(row=self.row, column=8, padx=10, pady=5, columnspan=2)
        ttk.Label(self.parent_frame, text=self.unit, font=("Helvetica", 12, "bold")).grid(row=self.row, column=10, padx=20, pady=5)
