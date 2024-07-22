# IMPORTANDO BIBLIOTECA TKINTER #

from tkinter import *
from tkinter import ttk

# PALETA DE CORES USADAS #

cor1 = "#0f0f0f" # PRETO
cor2 = "#f2f3f5" # BRANCO
cor3 = "#f7a202" # LARANJA
cor4 = "#858483" # CINZA
cor5 = "#200cfa" # AZUL

# CRIANDO TELA PRINCIPAL PARA CALCULADORA #

janela = Tk()
janela.title("Calculadora")
janela.geometry("243x350")
janela.config(bg=cor1)
janela.maxsize(243,350)

#   SEPARANDO TELA, CRIANDO DISPLAY #

display_tela = Frame(janela, width=243, height=50, bg=cor4)
display_tela.grid(row=0, column=0)

display_corpo = Frame(janela, width=243, height=300, bg=cor2)
display_corpo.grid(row=1, column=0)

todos_valores = ""
valor_texto = StringVar()

# CRIANDO FUNÇÃO PARA CALCULAR #

def entrada_valores(event):
    global todos_valores
    if event == '%':
        try:
            if todos_valores:
                todos_valores = str(eval(todos_valores + "/100"))
            else:
                todos_valores = "0"
        except:
            valor_texto.set("Erro")
            todos_valores = ""
    else:
        todos_valores += str(event)
    valor_texto.set(todos_valores)


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

def calcular():
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        todos_valores = ""
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ""


# CRIANDO LABEL #

label_app = Label(display_tela, textvariable=valor_texto, width=23, height=3, padx=10, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 13 bold", bg=cor4, )
label_app.place(x=0, y=0)






# CRIANDO BOTOES #

# PRIMEIRA LINHA DE BOTÕES #

b_1 = Button(display_corpo, command=limpar_tela,text="C", width=10, height=2, bg=cor3, fg=cor2, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=3, y=3)
b_1 = Button(display_corpo, command=lambda: entrada_valores("%"), text="%", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=123, y=3)
b_1 = Button(display_corpo, command=lambda: entrada_valores("/"), text="/", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=183, y=3)

# SEGUNDA LINHA DE BOTÕES #

b_2 = Button(display_corpo, command=lambda: entrada_valores("7"), text="7", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=3, y=63)
b_3 = Button(display_corpo, command=lambda: entrada_valores("8"), text="8", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_3.place(x=63, y=63)
b_4 = Button(display_corpo, command=lambda: entrada_valores("9"), text="9", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=123, y=63)
b_5 = Button(display_corpo, command=lambda: entrada_valores("*"), text="*", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=183, y=60)

# TERCEIRA LINHA DE BOTÕES #

b_6 = Button(display_corpo, command=lambda: entrada_valores("4"), text="4", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=3, y=123)
b_7 = Button(display_corpo, command=lambda: entrada_valores("5"), text="5", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_7.place(x=63, y=123)
b_8 = Button(display_corpo, command=lambda: entrada_valores("6"), text="6", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=123, y=123)
b_9 = Button(display_corpo, command=lambda: entrada_valores("-"), text="-", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=183, y=120)

# QUARTA LINHA DE BOTÕES #

b_10 = Button(display_corpo, command=lambda: entrada_valores("1"), text="1", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_10.place(x=3, y=183)
b_11 = Button(display_corpo, command=lambda: entrada_valores("2"), text="2", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_11.place(x=63, y=183)
b_12 = Button(display_corpo, command=lambda: entrada_valores("3"), text="3", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_12.place(x=123, y=183)
b_13 = Button(display_corpo, command=lambda: entrada_valores("+"), text="+", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_13.place(x=183, y=180)

# QUINTA LINHA DE BOTÕES #

b_14 = Button(display_corpo, command=lambda: entrada_valores("0"), text="0", width=10, height=2, bg=cor2,fg=cor1, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=3, y=241)
b_15 = Button(display_corpo, command=lambda: entrada_valores("."), text=".", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_15.place(x=123, y=241)
b_16 = Button(display_corpo, command=calcular, text="=", width=4, height=2, font="Ivy 14 bold", relief=RAISED, overrelief=RIDGE)
b_16.place(x=183, y=241)


# CRIANDO O LOOP DA INTERFACE GRÁFICA #

janela.mainloop()
