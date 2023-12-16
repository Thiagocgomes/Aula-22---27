import tkinter as tk
from tkinter import messagebox

def calcular_imc():
  try:
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())

    imc = peso // (altura ** 2)
    resultado.config(text = f'Seu IMC é: {imc: .2f}')
  except ValueError:
    messagebox.showerror('Erro', 'Inserir valores válidos para altura e peso!')

janela = tk.Tk()
janela.geometry('400x400')
janela.title('Calculadora de IMC')

label_peso = tk.Label(janela, text ='Peso(kg): ')
label_peso.pack()
entry_peso = tk.Entry(janela)
entry_peso.pack()

label_altura = tk.Label(janela, text ='Altura: ')
label_altura.pack()
entry_altura = tk.Entry(janela)
entry_altura.pack()

button_calcular = tk.Button(janela, text = 'Calcular', command = calcular_imc)
button_calcular.pack()

resultado = tk.Label(janela, text = 'Seu IMC é: ')
resultado.pack()

janela.mainloop()


  