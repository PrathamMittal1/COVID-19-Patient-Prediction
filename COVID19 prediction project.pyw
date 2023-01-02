import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import tkinter as tk


def run():
    symptoms_list = []
    for i in symptoms:
        symptoms_list.append(i.get())
    classifier = KNeighborsClassifier()
    classifier.fit(x, y)
    predict = classifier.predict(np.array([symptoms_list]))
    print(predict)

    if predict == 1:
        print('\nCaution: Patient is corona positive!\nStay away from patient.')
        l.config(text='Caution: Patient is corona positive!\nStay away from patient.')
    else:
        print('\nWooho! Patient is corona negative, patient is safe.')
        l.config(text='Wooho! Patient is corona negative, patient is safe.')
    _l = tk.Label(root, text='The result is just a prediction, it may be false also.'
                             '\nSo, it is best to consult a doctor for accurate results.')
    _l.place(x=90, y=460)


data = pd.read_excel(r"data\COVID19 data.xlsx", sheet_name='Sheet1')
# print(data)
x = data.iloc[0:, 0:-1].values
y = data.iloc[0:, -1].values

root = tk.Tk()
root.title('COVID-19 Prediction')
root.geometry('500x500-100+100')
root.resizable(False, False)
l1 = tk.Label(root, text='Enter patient symptoms...\nSelect for yes and leave for no.')
l1.place(x=100, y=10)
canvas = tk.Canvas(root, bg='white', height=400, width=500)
canvas.place(y=50)

check = dict()
symptoms = []
for i in range(8):
    symptoms.append(tk.IntVar())
check[0] = tk.Checkbutton(root, text='Cough', onvalue=1, offvalue=0, variable=symptoms[0], bg='white')
check[1] = tk.Checkbutton(root, text='Running nose', onvalue=1, offvalue=0, variable=symptoms[1], bg='white')
check[2] = tk.Checkbutton(root, text='Breathing difficulty', onvalue=1, offvalue=0, variable=symptoms[2], bg='white')
check[3] = tk.Checkbutton(root, text='Fever', onvalue=1, offvalue=0, variable=symptoms[3], bg='white')
check[4] = tk.Checkbutton(root, text='Body pain', onvalue=1, offvalue=0, variable=symptoms[4], bg='white')
check[5] = tk.Checkbutton(root, text='Red head and skin', onvalue=1, offvalue=0, variable=symptoms[5], bg='white')
check[6] = tk.Checkbutton(root, text='High B.P.', onvalue=1, offvalue=0, variable=symptoms[6], bg='white')
check[7] = tk.Checkbutton(root, text='Weakness', onvalue=1, offvalue=0, variable=symptoms[7], bg='white')
for i in range(0, 8):
    check[i].place(x=100, y=70 + 25 * i)
button = tk.Button(root, text='SUBMIT', command=run)
button.place(x=200, y=290)
l = tk.Label(root, bg='white')
l.place(x=150, y=340)
root.mainloop()
