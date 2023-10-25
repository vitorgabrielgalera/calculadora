from tkinter import *
root = Tk()

#defina o nome da janela
root.title("calculadora")
#define um ícone
root.iconbitmap("robot.ico")

#deifine o visor
visor = Entry(root, width=27)
#posiciona o visor
visor.grid(row=0, column=0, columnspan=3)

#definir a função para os botoes numericos
def click_numero(numero):
    num_visor = visor.get() + str(numero)
    visor.delete(0, END)
    visor.insert(0, num_visor)

#definir os botões numéricos
btn_1 = Button(root, text="1", padx=20, pady=20, command=lambda : click_numero(1))
btn_2 = Button(root, text="2", padx=20, pady=20, command=lambda : click_numero(2))
btn_3 = Button(root, text="3", padx=20, pady=20, command=lambda : click_numero(3))
btn_4 = Button(root, text="4", padx=20, pady=20, command=lambda : click_numero(4))
btn_5 = Button(root, text="5", padx=20, pady=20, command=lambda : click_numero(5))
btn_6 = Button(root, text="6", padx=20, pady=20, command=lambda : click_numero(6))
btn_7 = Button(root, text="7", padx=20, pady=20, command=lambda : click_numero(7))
btn_8 = Button(root, text="8", padx=20, pady=20, command=lambda : click_numero(8))
btn_9 = Button(root, text="9", padx=20, pady=20, command=lambda : click_numero(9))
btn_0 = Button(root, text="0", padx=20, pady=20, command=lambda : click_numero(0))

#posicionar os botoes
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

#definir botao limpar
def click_limpar():
    visor.delete(0, END)

#definir função igual
def click_equal():
    second_number = int(visor.get())
    visor.delete(0, END)
    ans = 0
    if math == "adição":
        ans = first_number + second_number
    elif math == "subtração":
        ans = first_number - second_number
    elif math == "multiplicação":
        ans = first_number*second_number
    elif math == "divisão":
        ans = first_number / second_number
    visor.insert(0, str(ans))

#definir botoes de igual e clear
btn_equal = Button(root, text="=", padx=20, pady=20, command=click_equal)
btn_clear = Button(root, text="C", padx=20, pady=20, command=click_limpar)

#posicionar botoes de igual e limpar
btn_equal.grid(row=4, column=1)
btn_clear.grid(row=4, column=2)

#defini a função do botão adição
def click_add():
    global first_number
    first_number = int(visor.get())
    global math
    math = "adição"
    visor.delete(0, END)

#defini a função do botão subtração
def click_sub():
    global first_number
    first_number = int(visor.get())
    global math
    math = "subtração"
    visor.delete(0, END)

#defini a função do botão multiplicação
def click_mul():
    global first_number
    first_number = int(visor.get())
    global math
    math = "multiplicação"
    visor.delete(0, END)

#defini a função do botão divisão
def click_div():
    global first_number
    first_number = int(visor.get())
    global math
    math = "divisão"
    visor.delete(0, END)

#definir os botoes das operações
btn_add = Button(root, text="+", padx=20, pady=20, command=click_add)
btn_sub = Button(root, text="-", padx=20, pady=20, command=click_sub)
btn_mul = Button(root, text="*", padx=20, pady=20, command=click_mul)
btn_div = Button(root, text="/", padx=20, pady=20, command=click_div)

#posicionar os botoes
btn_add.grid(row=5, column=0)
btn_sub.grid(row=5, column=1)
btn_mul.grid(row=5, column=2)
btn_div.grid(row=6, column=0)

root.mainloop()