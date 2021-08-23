import tkinter as tk
import sys

window = tk.Tk()
window.title('Obliczenia dla kredutu hipotecznego')
window.geometry('800x600')


def close_windows():
    sys.exit()


main_menu = tk.Menu(window)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Plik', menu=file_menu)
file_menu.add_command(label='Zamknij', command=close_windows)
window.config(menu=main_menu)


def pk_value():
    pk = entry_pk.get()
    print(pk)


def fo(p, d, r):
    pp = ((p * 100) / (p + d)) / 100
    pd = ((d * 100) / (p + d)) / 100
    rp = int(pp * r)
    rd = int(pd * r)
    wp = int(p - rp)
    wd = int(d - rd)
    print('Wartość raty Pawła: {}'.format(rp))
    print('Wartość raty Danieli: {}'.format(rd))
    print('Wartość wypłaty Pawła: {}'.format(wp))
    print('Wartość wypłaty Danieli: {}'.format(wd))
    return "Zakończenie Obliczeń"


lp = tk.Label(window, text='Wynagrodzenie Pawła: ')
lp.pack()
entry_pk = tk.Entry(window, width="50")
entry_pk.pack()
b_pk = tk.Button(window, text='Dodaj', command=pk_value)
b_pk.pack()


ld = tk.Label(window, text='Wynagrodzenie Danieli: ')
ld.pack()
entry_dk = tk.Entry(window, width="50")
entry_dk.pack()

lr = tk.Label(window, text='Wartość raty: ')
lr.pack()
entry_rt = tk.Entry(window, width="50")
entry_rt.pack()


b_oblicz = tk.Button(window, text="Oblicz", command=pk_value and fo)
b_oblicz.pack()

pk = pk_value()
dk = 2
rk = 2


window.mainloop()
