#
# Class definitions??
#

from datetime import datetime
import calendar


class FacturasApp:
    def __init__(self):
        self.c_month = datetime.now().month
        self.c_year = datetime.now().year

    def get_day_number(self, day):
        days_lst = [
            "Lunes",
            "Martes",
            "Miercoles",
            "Jueves",
            "Viernes"
        ]

        return days_lst.index(day)

    def get_bring_days(self, day_to_bring):
        
        # day_to_bring debe ser un dia de la semana de lunes a viernes
        # L M X J V  - Debe venir como numérico representanto el valor
        # 0 1 2 3 4  - 

        cal_month = self.get_cal_month()
        fd_weekday, last_day = calendar.monthrange(self.c_year, self.c_month)
        # Si el primer dia es despues del jueves, se toma el proximo mes
        if fd_weekday >= 3:
            cal_month.pop(0)
        ld_weekday = datetime.today().replace(day = last_day).weekday()
        
        if ld_weekday >= 2:
            # Si el ultimo dia es a partir del miercoles se agrega los dias faltantes a esa semana
            missing_days = 7 - len(cal_month[-1])
            for i in range(missing_days):
                cal_month[-1].append(i+1)
        else:
            cal_month.pop(-1)

        days_to_bring = []
        for week in cal_month:
            days_to_bring.append(week[day_to_bring])
        # Si a la ultima fecha es de la primera semana del proximo mes, se asina el proximo mes para ese dia
        if days_to_bring.__len__ != 0:
            dates_to_bring = [[day, self.c_month] for day in days_to_bring]
            if dates_to_bring[-1][0] <= 7:
                dates_to_bring[-1][1] = self.c_month + 1

            dates_p_qty = []
            for day, month in dates_to_bring:
                dates_dict = {'date':f'{day}/{month}/{self.c_year}', 'qty': 0}
                dates_p_qty.append(dates_dict)
            
            return dates_p_qty
        else:
            raise ValueError('No se pudieron encontrar días para traer facturas!')

    
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
            week_clean = [int(day) for day in week if day != '']
            month_clean.append(week_clean)
        
        return month_clean

    def assign_people(self, persons, d2b):
        persons_qty = len(persons)
        # trae la cantidad de personas por semana que deben traer
        d2b_qty_week = self.get_persons_week(d2b, persons_qty)
        # Se multiplica la cantidad de semanas por la cant. de personas por semana
        # se toma el inverso de cada una para calcular su probabilidad de ocurrencia
        counter = 0
        for week in d2b_qty_week:
            qty_p_week = week.get('qty')
            date = week.get('date')
            for i in range(qty_p_week):
                persons[counter]['date'] = date
                counter += 1

        return persons
    
    def get_persons_week(self, d2b, persons_qty):
        weeks_qty = len(d2b)
        remaining_persons = persons_qty
        while remaining_persons > 0:
            for week in d2b:
                qty = week.get('qty')
                if remaining_persons > 0:
                    week['qty'] = qty + 1
                    remaining_persons -= 1
                else:
                    break
        return d2b


class Persona:
    def __init__(self, id, name, mail):
        self.id = id
        self.name = name
        self.mail = mail
    def get_last_date(self):
        pass