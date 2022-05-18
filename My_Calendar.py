"""
Расчет дня недели
Ввод
1.День
2.Месяц
3.Год
Расчет
Вывод - день недели по дате
"""


class MyData():
    default_day = 1
    default_month = 1
    default_year = 1900
    default_day_of_week=['Воскресенье','Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']

    def __init__(self, day=default_day, month=default_month, year=default_year):
        self.day = day
        self.month = month
        self.year = year
        if self.year % 4 == 0:
            self.days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            self.days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def info(self):
        print(self.day, self.month, self.year)
        if self.year % 4 == 0:
            print('Высокосный год')

    def calculation(self, year):
        amount_year = self.year - self.default_year
        amount_day = 0
        calc_day = 0
        calc_year = self.default_year
        for i in range(amount_year):
            if calc_year % 4 == 0:
                year_day = 366
                amount_day = amount_day + year_day
            else:
                year_day = 365
                amount_day = amount_day + year_day
            calc_year = calc_year+1
        if calc_year == self.default_year:
            calc_month = self.month
            if calc_month > 1:
                for j in range(self.month-1):
                    calc_day = calc_day+self.days_of_month[j]
                amount_day = calc_day + self.day
            else:
                amount_day = self.day
        else:
            calc_month = self.month
            if calc_month > 1:
                for j in range(self.month-1):
                    calc_day = calc_day+self.days_of_month[j]
                amount_day = amount_day+calc_day + self.day
            else:
                amount_day = amount_day+calc_day+self.day

        if calc_year != self.default_year:
            amount_day = amount_day - 1

        print('Кло-во дней с 01.01.1900: ', amount_day)

        return MyData.default_day_of_week[(amount_day) % 7]




data1 = MyData(8, 10, 2005)
data1.info()

print(data1.calculation(data1.year))


