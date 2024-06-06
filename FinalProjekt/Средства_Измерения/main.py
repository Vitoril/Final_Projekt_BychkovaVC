from Средства_Измерения.СИ import SI
from tkinter import *
if __name__ == '__main__':
    root = Tk()
    root.title("Реестр средств измерний")
    root.geometry("600x400")

    label_name = Label(text="Введите наименование СИ")
    label_name.pack()
    # поле ввода для адреса
    entry_name = Entry()
    entry_name.pack()

    label_tupe = Label(text="Тип СИ")  # текстовая метка
    label_tupe.pack()  # размещение метки в окне
    # поле ввода для адреса
    entry_tupe = Entry()  # поле ввода
    entry_tupe.pack()  # размещение поля ввода в окне

    label_factory_name = Label(text="Заводской номер")  # текстовая метка
    label_factory_name.pack()  # размещение метки в окне
    # поле ввода для адреса
    entry_factory_name = Entry()  # поле ввода
    entry_factory_name.pack()  # размещение поля ввода в окне

    label_subdivision = Label(text="Подразделение организации")  # текстовая метка
    label_subdivision.pack()  # размещение метки в окне
    # поле ввода для адреса
    entry_subdivision = Entry()  # поле ввода
    entry_subdivision.pack()  # размещение поля ввода в окне

    label_responsible = Label(text="Ответсвенный сотрудник")  # текстовая метка
    label_responsible.pack()  # размещение метки в окне
    # поле ввода для адреса
    entry_responsible = Entry()  # поле ввода
    entry_responsible.pack()  # размещение поля ввода в окне

    def add_Si():
        name = entry_name.get()
        tupe = entry_tupe.get()
        factory_name = entry_factory_name.get()
        subdivision = entry_subdivision.get()
        responsible = entry_responsible.get()
        si = SI(name, tupe, factory_name, subdivision, responsible)

        list_sr.append(si)
        list_sr_var.set(list_sr)

    bth_add_Si = Button(text="Добавить Cредство измерения", command=add_Si)
    bth_add_Si.pack()

    list_sr = []
    list_sr_var = Variable(value=list_sr)
    sr_listbox = Listbox(width=50, listvariable=list_sr_var)
    sr_listbox.pack()


    def delete():
        index = sr_listbox.curselection()
        list_sr.remove(list_sr[index[0]])
        list_sr_var.set(list_sr)

    def correct():
        index = sr_listbox.curselection()
        list_sr[index[0]].to_corrected()
        list_sr_var.set(list_sr)


    def repa():
        index = sr_listbox.curselection()
        list_sr[index[0]].repair()
        list_sr_var.set(list_sr)

    bth_add_Si = Button(text="Удалить Cредство измерения", command=delete)
    bth_add_Si.pack()

    bth_add_Si = Button(text="Исправлен", command=correct)
    bth_add_Si.pack()

    bth_add_Si = Button(text="На ремонте", command=repa)
    bth_add_Si.pack()

    root.mainloop()
