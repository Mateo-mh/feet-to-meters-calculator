from tkinter import *

root = Tk()
root.title('Pies a Metros')

def calcular(*arg): # arg significa que la funcion tomara los argumentos, con sus respectivos parametros
    try:
        value = float(pies.get())
        m = int(0.3048 * value * 10000 + 0.5)/10000
        metros.set(m)
    except ValueError:
        metros.set('ERROR')    

frame = Frame(root, padx=12, pady=3)
frame.grid(row=0, column=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)

pies_input.grid(row=0, column=1)

metros = StringVar()
Label(frame, textvariable=metros).grid(row=1, column=1)

Button(frame, text='calcular', command=calcular).grid(row=2, column=2)

Label(frame, text='pies').grid(row=0, column=0)
Label(frame, text='es igual a').grid(row=1, column=0)
Label(frame, text='metros').grid(row=1, column=2)

pies_input.focus() # focus selecciona el campo de texto del input automaticamente
root.bind('<Return>', calcular) # bind permite escuchar eventos y dependiendo de lo que ocurra ejecuta una funcion
# en este caso a bind le pasamos la accion <Return> que permite que el usuario de enter y se ejecute una funcion, que en este caso es la funcion de calcular
root.mainloop()
