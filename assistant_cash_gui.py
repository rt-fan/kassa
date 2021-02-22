from tkinter import ttk
from tkinter import *
from tkinter.ttk import Label
from tkinter import messagebox
import calendar
import datetime


class Example(Frame):  # окно открывается

    def __init__(self, parent):
        Frame.__init__(self, parent, background="#8E9B97")  # , background="white"
        self.parent = parent
        self.parent.title("Assistant Cash")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):

        date_today = datetime.date.today()

        w = 320
        h = 475

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        variants = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6, "Июль": 7,
                    "Август": 8, "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12}

        date_text = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля",
                     8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}

        # Цветовые схемы:
        #  #2C4A52 - сине-зеленый
        #  #537072 - фарватер
        #  #8E9B97 - дымка
        #  #F4EBDB - смог

        # Версия  ====================================================================================================:

        version = Label(self, text="v0.4", background="#8E9B97", foreground="#537072")
        version.place(x=290, y=5)

        # Дата  ======================================================================================================:

        label_dd = Label(self, text="Число:", background="#8E9B97", font=("Arial", 12))
        label_dd.place(x=20, y=15)
        entry_dd = Entry(self, width=6, font=("Arial", 12), selectbackground="#537072", )
        entry_dd.place(x=20, y=40)
        entry_dd.insert(0, date_today.day)

        label_mm = Label(self, text="Месяц:", background="#8E9B97", font=("Arial", 12))
        label_mm.place(x=95, y=15)
        combo_mm = ttk.Combobox(self, values=list(variants.keys()), state="readonly", width=9, font=("Arial", 12))
        combo_mm.place(x=95, y=39)
        combo_mm.current(date_today.month-1)

        label_yy = Label(self, text="Год:", background="#8E9B97", font=("Arial", 12))
        label_yy.place(x=215, y=15)
        entry_yy = Entry(self, width=6, font=("Arial", 12), selectbackground="#537072")
        entry_yy.place(x=215, y=40)
        entry_yy.insert(0, date_today.year)

        # Суммы  =====================================================================================================:

        label_ostatok = Label(self, text="Остаток на балансе:", background="#8E9B97", font=("Arial", 12))
        label_ostatok.place(x=20, y=100)
        entry_ostatok = Entry(self, width=10, font=("Arial", 12), selectbackground="#537072")
        entry_ostatok.place(x=178, y=100)
        entry_ostatok.insert(0, "0")

        label_oplata = Label(self, text="Сумма оплаты:", background="#8E9B97", font=("Arial", 12))
        label_oplata2 = Label(self, text="(с подарочными)", background="#8E9B97", font=("Arial", 9))
        label_oplata.place(x=20, y=140)
        label_oplata2.place(x=20, y=160)
        entry_oplata = Entry(self, width=10, font=("Arial", 12), selectbackground="#537072")
        entry_oplata.place(x=178, y=140)
        entry_oplata.insert(0, "0")

        label_osn_tarif = Label(self, text="Введите тариф:", background="#8E9B97", font=("Arial", 12))
        label_osn_tarif.place(x=20, y=200)
        entry_osn_tarif = Entry(self, width=10, font=("Arial", 12), selectbackground="#537072")
        entry_osn_tarif.place(x=178, y=200)
        entry_osn_tarif.insert(0, "0")

        label_dop_tarif = Label(self, text="Доп. оплаты:", background="#8E9B97", font=("Arial", 12))
        label_dop_tarif.place(x=20, y=240)
        label_dop_tarif2 = Label(self, text="(wi-fi авторизация и др.)", background="#8E9B97", font=("Arial", 9))
        label_dop_tarif2.place(x=20, y=260)
        entry_dop_tarif = Entry(self, width=10, font=("Arial", 12), selectbackground="#537072")
        entry_dop_tarif.place(x=178, y=240)
        entry_dop_tarif.insert(0, "0")

        # Чек-бар c выбором суммы для фиксированного ip-адреса:  =====================================================:

        fix_ip = [0, 2, 6]
        index_fix_ip = IntVar()

        pay_ip_0 = Radiobutton(text="Без фиксированного ip-адреса", value=0,
                               variable=index_fix_ip,  activebackground="#8E9B97",
                               bg="#8E9B97", font=("Arial", 9))
        pay_ip_0.place(x=20, y=300)

        pay_ip_2 = Radiobutton(text="Старый тариф  (2 р/сутки)", value=1,
                               variable=index_fix_ip, activebackground="#8E9B97",
                               bg="#8E9B97", font=("Arial", 9))
        pay_ip_2.place(x=20, y=330)

        pay_ip_6 = Radiobutton(text="Новый тариф  (6  р/сутки)", value=2,
                               variable=index_fix_ip, activebackground="#8E9B97",
                               bg="#8E9B97", font=("Arial", 9))
        pay_ip_6.place(x=20, y=360)

        # # Поле отображения логов  ==================================================================================:
        #
        # c = Canvas(self, width=275, height=120, bg="#8E9B97")
        # c.place(x=20, y=400)
        #
        # #  =========================================================================================================

        def test():
            pass

        def logic():
            try:
                yy = int(entry_yy.get())
                mm = int(variants[combo_mm.get()])
                dd = int(entry_dd.get())
                ostatok = int(entry_ostatok.get())
                oplata = int(entry_oplata.get())
                osn_tarif = int(entry_osn_tarif.get())
                dop_tarif = int(entry_dop_tarif.get())
                pay_fix_ip = fix_ip[index_fix_ip.get()]
                balance = oplata + ostatok
                tarif = osn_tarif + dop_tarif

                while True:
                    # Исключения:
                    if dd == 0:
                        messagebox.showinfo(title="Ошибка", message="Введите корректную дату!")
                        break

                    if dd > calendar.monthrange(yy, mm)[1]:
                        messagebox.showinfo(title="Ошибка", message="Введите корректную дату!")
                        break

                    if yy < 2006:
                        messagebox.showinfo(title="Ошибка", message="Введите корректный год!")
                        break

                    if yy > 2050:
                        messagebox.showinfo(title="Ошибка", message="Введите корректный год!")
                        break

                    if oplata < 0:
                        messagebox.showinfo(title="Ошибка", message="Оплата не может быть отрицательной!")
                        break

                    if osn_tarif <= 0:
                        messagebox.showinfo(title="Ошибка", message="Тариф не может равняться или быть ниже нуля!")
                        break

                    if dop_tarif < 0:
                        messagebox.showinfo(title="Ошибка", message="Доп оплата не может быть отрицательной!")
                        break

                    # days - количество дней в месяце
                    # pay - ежедневный платеж
                    # work_days - дней будет работать за оплату
                    # work_days_pay - сумма за рабочие дни
                    # days_left - дней до конца месяца
                    # fix_ip - список стоймости за фиксированный ip-адрес
                    # index_fix_ip - индекс значения из списка фиксированного ip-адреса

                    days = calendar.monthrange(yy, mm)[1]  # напр. 31 день в январе
                    pay = (tarif / days) + pay_fix_ip  # напр. 22,58₽ за янв + 2р/д

                    if int(balance / pay) <= (days - dd) + 1:  # ОСТАЕМСЯ В ЭТОМ МЕСЯЦЕ
                        print("#" * 30)
                        print("ОСТАЕМСЯ")
                        print("Баланс:  ", balance)
                        print("Количество дней в этом месяце: ", days)
                        print("Ежедневная оплата (осн, внешн): ", pay, "(", tarif / days, ",", pay_fix_ip, ")")
                        work_days = balance / pay  # на столько дней хватает оплаты в этом месяце
                        print("Будет работать дней в этом месяце: ", int(work_days))
                        dd += int(work_days)  # прибавляем к дате оплаченные дни
                        print("Будет работать на сумму: ", int(work_days) * pay)
                        print("Остаток: ", balance - (int(work_days) * pay))
                        print("\n")
                        if dd > days:  # если дней получилось больше чем дней в месяце:
                            dd = 1
                            mm += 1
                            if mm > 12:
                                mm = 1
                                yy += 1

                        ost = round(balance - (int(work_days) * pay), 2)
                        request = "Отключение {} {} {}\nОстаток: {}руб.".format(int(dd), date_text[mm], yy, ost)
                        messagebox.showinfo(title="Готово", message=request)
                        break

                    else:  # ПЕРЕХОДИМ В СЛЕДУЮЩИЙ МЕСЯЦ
                        print("#" * 30)
                        print("ПЕРЕХОДИМ")
                        print("Баланс:  ", balance)
                        days_left = (days - dd) + 1
                        work_days_pay = days_left * pay
                        balance -= work_days_pay
                        dd = 1
                        mm += 1
                        if mm > 12:
                            mm = 1
                            yy += 1

                        print("Количество дней в этом месяце: ", days)
                        print("Ежедневная оплата: ", pay, "(", tarif / days, ",", pay_fix_ip, ")")
                        print("Дней до конца месяца (сегодняшний включительно): ", days_left)
                        print("Расход за месяц", work_days_pay)
                        print("Остаток на следующий месяц: ", balance)
                        print("\n")
            except ValueError:
                messagebox.showinfo(title="Ошибка", message="Ошибка. Введите числовые значения!")

        # Кнопка  ====================================================================================================:
        btn = Button(self, width=22, height=2, text="РАСЧИТАТЬ", command=logic, relief=GROOVE,
                     background="#8E9B97", font=("Arial", 16, "bold"))
        btn.place(x=12, y=400)
        #  ===========================================================================================================


def main():
    root = Tk()
    root.resizable(False, False)
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
