from tkinter import *
root = Tk()

#defina o nome da janela
root.title("calculadora")

#define um ícone
root.iconbitmap("robot.ico")

#deifine o visor
visor = Entry(root, width=10, borderwidth=3, font=("System", 20), justify="right", state="readonly")
#posiciona o visor
visor.grid(row=0, column=0, columnspan=3)

#definir a função para os botoes numericos
def click_numero(numero):
    visor.configure(state="normal")
    num_visor = visor.get() + str(numero)
    visor.delete(0, END)
    visor.insert(0, num_visor)
    visor.configure(state="readonly")

#definir os botões numéricos
btn_1 = Button(root, text="1", command=lambda : click_numero(1), font=("System", 20))
btn_2 = Button(root, text="2", command=lambda : click_numero(2), font=("System", 20))
btn_3 = Button(root, text="3", command=lambda : click_numero(3), font=("System", 20))
btn_4 = Button(root, text="4", command=lambda : click_numero(4), font=("System", 20))
btn_5 = Button(root, text="5", command=lambda : click_numero(5), font=("System", 20))
btn_6 = Button(root, text="6", command=lambda : click_numero(6), font=("System", 20))
btn_7 = Button(root, text="7", command=lambda : click_numero(7), font=("System", 20))
btn_8 = Button(root, text="8", command=lambda : click_numero(8), font=("System", 20))
btn_9 = Button(root, text="9", command=lambda : click_numero(9), font=("System", 20))
btn_0 = Button(root, text="0", command=lambda : click_numero(0), font=("System", 20))

#posicionar os botoes
btn_1.grid(row=3, column=0, sticky=E + W)
btn_2.grid(row=3, column=1, sticky=E + W)
btn_3.grid(row=3, column=2, sticky=E + W)

btn_4.grid(row=2, column=0, sticky=E + W)
btn_5.grid(row=2, column=1, sticky=E + W)
btn_6.grid(row=2, column=2, sticky=E + W)

btn_7.grid(row=1, column=0, sticky=E + W)
btn_8.grid(row=1, column=1, sticky=E + W)
btn_9.grid(row=1, column=2, sticky=E + W)

btn_0.grid(row=4, column=0, sticky=E + W)

#definir botao limpar
def click_limpar():
    visor.configure(state="normal")
    visor.delete(0, END)
    visor.configure(state="readonly")

#definir função igual
def click_equal():
    visor.configure(state="normal")
    second_number = int(visor.get())
    visor.configure(state="readonly")
    visor.configure(state="normal")
    visor.delete(0, END)
    visor.configure(state="readonly")
    ans = 0
    if math == "adição":
        ans = first_number + second_number
    elif math == "subtração":
        ans = first_number - second_number
    elif math == "multiplicação":
        ans = first_number*second_number
    elif math == "divisão":
        ans = first_number / second_number
    visor.configure(state="normal")
    visor.insert(0, str(ans))
    visor.configure(state="readonly")

#definir botoes de igual e clear
btn_equal = Button(root, text="=", command=click_equal, font=("System", 20))
btn_clear = Button(root, text="C", command=click_limpar, font=("System", 20))

#posicionar botoes de igual e limpar
btn_equal.grid(row=4, column=1, sticky=E + W)
btn_clear.grid(row=4, column=2, sticky=E + W)

#defini a função do botão adição
def click_add():
    global first_number
    visor.configure(state="normal")
    first_number = int(visor.get())
    visor.configure(state="readonly")
    global math
    math = "adição"
    visor.configure(state="normal")
    visor.delete(0, END)
    visor.configure(state="readonly")

#defini a função do botão subtração
def click_sub():
    global first_number
    visor.configure(state="normal")
    first_number = int(visor.get())
    visor.configure(state="readonly")
    global math
    math = "subtração"
    visor.configure(state="normal")
    visor.delete(0, END)
    visor.configure(state="readonly")

#defini a função do botão multiplicação
def click_mul():
    global first_number
    visor.configure(state="normal")
    first_number = int(visor.get())
    visor.configure(state="readonly")
    global math
    math = "multiplicação"
    visor.configure(state="normal")
    visor.delete(0, END)
    visor.configure(state="readonly")

#defini a função do botão divisão
def click_div():
    global first_number
    visor.configure(state="normal")
    first_number = int(visor.get())
    visor.configure(state="readonly")
    global math
    math = "divisão"
    visor.configure(state="normal")
    visor.delete(0, END)
    visor.configure(state="readonly")

#definir os botoes das operações
btn_add = Button(root, text="+", command=click_add, font=("System", 20))
btn_sub = Button(root, text="-", command=click_sub, font=("System", 20))
btn_mul = Button(root, text="*", command=click_mul, font=("System", 20))
btn_div = Button(root, text="/", command=click_div, font=("System", 20))

#posicionar os botoes
btn_add.grid(row=5, column=0, sticky=E + W)
btn_sub.grid(row=5, column=1, sticky=E + W)
btn_mul.grid(row=5, column=2, sticky=E + W)
btn_div.grid(row=6, column=0, sticky=E + W)

root.mainloop()