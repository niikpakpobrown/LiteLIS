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
        ttk.Label(self.parent_frame, text=self.unit, font=("Helvetica", 12, "bold")).grid(row=self.row, column=8, padx=20, pady=5)
        ttk.Label(self.parent_frame, text=self.r_range, font=("Helvetica", 12, "bold")).grid(row=self.row, column=10, padx=10, pady=5, columnspan=2)
       
class InsertResult:
    def __init__(self, patient_id, patient_name, age, sex, test_date, t_bil_result, d_bil_result, alt_result, ast_result, alp_result, ggt_result, tp_result, alb_result):
        self.patient_id = patient_id.get()
        self.patient_name = patient_name.get()
        self.age = int(age.get())
        self.sex = sex.get()
        self.test_date = date.get()
        self.t_bil_result = float(t_bil.result_entry.get())
        self.d_bil_result = float(d_bil.result_entry.get())
        self.alt_result = float(alt.result_entry.get())
        self.ast_result = float(ast.result_entry.get())
        self.alp_result = float(alp.result_entry.get())
        self.ggt_result = float(ggt.result_entry.get())
        self.tp_result = float(tp.result_entry.get())
        self.alb_result = float(alb.result_entry.get())


    def insert_data(self):
         # SQL INSERT query
        insert_query = """
        INSERT INTO LabTestResults (patient_id, patient_name, age, sex, test_date, t_bil_result, d_bil_result, alt_result, ast_result, alp_result, ggt_result, tp_result, alb_result)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data = (
            self.patient_id, self.patient_name, self.age, self.sex, self.test_date, self.t_bil_result, self.d_bil_result, self.alt_result, self.ast_result, self.alp_result, self.ggt_result, self.tp_result, self.alb_result
        )

        # Execute the INSERT query
        cursor.execute(insert_query, data)

        # Commit the changes
        conn.commit()
        print("Data inserted successfully.")



