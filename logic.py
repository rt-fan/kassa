import calendar

date_text = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}

yy = 2021
mm = 1
dd = 1
balance = 2500
tarif = 700
fix_ip = [0, 2, 6]
ip_index = 2

while True:

  # days - количество дней в месяце
  # pay - ежедневный платеж
  # work_days -  дни за оплату
  # days_left - дней до конца месяца
  # fix_ip - список с оплатой за фиксированный ip-адрес (без оплаты, 2₽, 6₽)
  # ip_index - индекс для списка с фиксированным ip-адресом

  days = calendar.monthrange(yy, mm)[1]  # 31 день в январе
  pay = (tarif / days) + fix_ip[ip_index]  # 22,58₽ за янв + 2₽ за внешний ip

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
    print(fix_ip[2])
    break

  else: # переходим в след месяц
    print("Переходим")
    days_left = (days - dd) + 1
    work_days = days_left * pay
    print(dd, mm, yy)
    print("Баланс на начало месяца:", balance)
    print("Дней до конца месяца:", days_left)
    print("Сумма за этот месяц", work_days)
    balance -= work_days
    print("Денег осталось", balance)
    dd = 1
    mm += 1
    if mm > 12:
      mm = 1
      yy += 1

  print("")
  print("#" * 30)
  print("")
