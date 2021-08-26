import tkinter as tk
import sys
from tkinter.constants import END

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


def fo():
    pk = float(entry_pk.get())
    dk = float(entry_dk.get())
    r = float(entry_rt.get())
    pp = float(round(((pk * 100) / (pk + dk)) / 100, 2))
    pd = float(round(((dk * 100) / (pk + dk)) / 100, 2))
    rp = float(round(pp * r, 2))
    rd = float(round(pd * r, 2))
    wp = float(round(pk - rp, 2))
    wd = float(round(dk - rd, 2))
    pokaz_rp = entry_s_pk.insert(0, round(rp, 2))
    print(pokaz_rp)
    pokaz_rd = entry_s_dk.insert(0, round(rd, 2))
    print(pokaz_rd)
    pokaz_w_rp = entry_w_pk.insert(0, round(wp, 2))
    print(pokaz_w_rp)
    pokaz_w_rd = entry_w_dk.insert(0, round(wd, 2))
    print(pokaz_w_rd)
    return None


def clear():
    entry_s_pk.delete(0, END)
    entry_s_dk.delete(0, END)
    entry_w_pk.delete(0, END)
    entry_w_dk.delete(0, END)


lp = tk.Label(window, text='Wynagrodzenie Pawła: ')
lp.pack()
entry_pk = tk.Entry(window, width="50")
entry_pk.pack()

ld = tk.Label(window, text='Wynagrodzenie Danieli: ')
ld.pack()
entry_dk = tk.Entry(window, width="50")
entry_dk.pack()

lr = tk.Label(window, text='Wartość raty: ')
lr.pack()
entry_rt = tk.Entry(window, width="50")
entry_rt.pack()

b_oblicz = tk.Button(window, text="Oblicz", command=fo)
b_oblicz.pack()

lsp = tk.Label(window, text='Kwota kredytu Paweł: ')
lsp.pack()
entry_s_pk = tk.Entry(window, width="50")
entry_s_pk.pack()

lsd = tk.Label(window, text='Kwota kredytu Daniela: ')
lsd.pack()
entry_s_dk = tk.Entry(window, width="50")
entry_s_dk.pack()

lwp = tk.Label(window, text='Kwota do wypłaty Paweł: ')
lwp.pack()
entry_w_pk = tk.Entry(window, width="50")
entry_w_pk.pack()

lwd = tk.Label(window, text='Kwota do wypłaty Daniela: ')
lwd.pack()
entry_w_dk = tk.Entry(window, width="50")
entry_w_dk.pack()

b_wyczysc = tk.Button(window, text="Wyczyść", command=clear)
b_wyczysc.pack()

window.mainloop()
