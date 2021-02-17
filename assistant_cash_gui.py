from tkinter import ttk
# from tkinter import filedialog as fd
from tkinter import *
from tkinter.ttk import Label
from tkinter import messagebox
import calendar


# from datetime import date, time, datetime


class Example(Frame):  # окно открывается

    def __init__(self, parent):
        Frame.__init__(self, parent)  # , background="white"
        self.parent = parent
        self.parent.title("Assistant Cash")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        w = 300
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        variants = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6, "Июль": 7, "Август": 8,
                    "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12}

        date_text = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля",
                     8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}

        # def change_depend(variant):
        #     sub_variants = variants[variant]

        label_dd = Label(self, text="Число:")
        label_dd.place(x=10, y=5)
        entry_dd = Entry(self, bg='white', width=6, font=14)
        entry_dd.place(x=10, y=30)

        label_mm = Label(self, text="Месяц:")
        label_mm.place(x=82, y=5)
        combo_mm = ttk.Combobox(self, values=list(variants.keys()), state="readonly", width=10)
        combo_mm.place(x=82, y=30)

        label_yy = Label(self, text="Год:")
        label_yy.place(x=180, y=5)
        entry_yy = Entry(self, bg='white', width=6, font=14)
        entry_yy.place(x=180, y=30)

        label_balance = Label(self, text="Введите общую сумму оплаты")
        label_balance2 = Label(self, text="(с подарочными):")
        label_balance.place(x=10, y=80)
        label_balance2.place(x=10, y=98)
        entry_balance = Entry(self, bg='white', width=10, font=14)
        entry_balance.place(x=10, y=120)

        label_tarif = Label(self, text="Введите тариф (с доп. оплатами):")
        label_tarif.place(x=10, y=160)
        entry_tarif = Entry(self, bg='white', width=10, font=14)
        entry_tarif.place(x=10, y=182)

        # def test():
        #     pass

        def logic():
            try:
                yy = int(entry_yy.get())
                mm = int(variants[combo_mm.get()])
                dd = int(entry_dd.get())
                balance = int(entry_balance.get())
                tarif = int(entry_tarif.get())

                while True:

                    # days - количество дней в месяце
                    # pay - ежедневный платеж
                    # work_days - дней будет работать за оплату
                    # work_days_pay - сумма за рабочие дни
                    # days_left - дней до конца месяца

                    days = calendar.monthrange(yy, mm)[1]  # 31 день в январе
                    pay = tarif / days  # 22,58₽ за янв

                    print("Проверяю...")
                    if balance / pay <= (days - dd) + 1:  # остаемся в этом месяце
                        print("Остаёмся")
                        work_days = balance / pay
                        print("Будет работать в этом месяце дней", work_days)
                        dd += work_days  # прибавляем к дате оплаченные дни
                        if dd > days:  # если дней получилось больше чем дней в месяце:
                            dd = 1
                            mm += 1
                            if mm > 12:
                                mm = 1
                                yy += 1

                        request = "Отключение {} {} {}".format(int(dd), date_text[mm], yy)
                        print(request)
                        messagebox.showinfo(title="Готово", message=request)
                        break

                    else:  # переходим в след месяц
                        print("Переходим")
                        days_left = (days - dd) + 1
                        work_days_pay = days_left * pay
                        print(dd, mm, yy)
                        print("Баланс на начало месяца:", balance)
                        print("Дней до конца месяца:", days_left)
                        print("Сумма за этот месяц", work_days_pay)
                        balance -= work_days_pay
                        print("Денег осталось", balance)
                        dd = 1
                        mm += 1
                        if mm > 12:
                            mm = 1
                            yy += 1
            except ValueError:
                print("ошибка, введите числа а не буквы")
                messagebox.showinfo(title="Ошибка", message="Ошибка. Введите числовые значения!")

        # Кнопка
        btn = Button(self, width=18, height=2, text="Расчитать число", command=logic, relief=GROOVE)
        btn.place(x=77, y=230)


def main():
    root = Tk()
    root.resizable(False, False)
    # root.iconbitmap('icon.ico')
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
