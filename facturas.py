#
#   Sorteador de facturas de los viernes
#
from datetime import datetime
import json
import calendar

class Persona:
    def __init__(self, id, name, ):
        self.id = id
        self.name = name
        # self.
#     self.name = 
    def get_last_date(self):
        pass


class FacturasApp:
    def __init__(self):
        self.c_month = datetime.now().month
        self.c_year = datetime.now().year

    def get_bring_days(self, day_to_bring):
        
        cal_month = get_cal_month()
        fd_weekday, last_day = calendar.monthrange(2019, 7)
        # Si el primer dia es despues del jueves, se toma el proximo mes
        if fd_weekday >= 3:
            cal_month.pop(0)
        ld_weekday = datetime.today().replace(day = last_day).weekday()
        # Si el ultimo dia es antes del jueves se toma en el  mes
        if ld_weekday < 2:
            cal_month.pop(-1)
        if datetime.weekday(day_to_bring):
            pass
    
    def get_cal_month(self):
        cal_month = calendar.month(self.c_year, self.c_month)
        weeks_lst = cal_month.split('\n')
        # Quita las dos primeras lineas de cabecera:
        #      Month Year
        # Mo Tu We Th Fr Sa Su
        for _ in range(2):
            weeks_lst.pop(0)
        # Elimina la ultima linea que esta vacia
        weeks_lst.pop(-1)
        month_n_days = [week.split(' ') for week in weeks_lst]
        month_clean = []
        for week in month_n_days:
            week_clean = [day for day in week if day != '']
            month_clean.append(week_clean)
        
        return month_clean
        

currentDay = datetime.now().day
currentDayNum = datetime.now().weekday()
currentMonth = datetime.now().month
currentYear = datetime.now().year
currentDate = datetime.now()

print(f'Dia: {currentDay}')
print(f'Dia Num: {currentDayNum}')
print(f'Mes: {currentMonth}')
print(f'Año: {currentYear}')
print(f'Fecha: {currentDate}')
print(f'Dia: {currentDate.strftime("%A")}')
first_day = datetime.today().replace(day = 1)
first_day = first_day.day
cal_month = calendar.month(2019,7)
print(f'Primer dia: {first_day}')
print(f'\nCalendario: \n {cal_month}')
