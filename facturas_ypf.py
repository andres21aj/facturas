#
#   Sorteador de facturas de los viernes
#
from datetime import datetime
import json

class Persona(object):
    name = ''

    def get_last_date(self):
        pass


def get_fridays(currentMonth):

    pass

compas = [ \
        "Gerardo Gaston",
        "Hernan Esmoris",
        "Fernando Martinez",
        "Andres Jacome",
        "Julio Morinigio",
        "Matias Cabo",
        "Francisco Ali",
        "Ignacio Sanchez"
        ]
for compa in compas:
    print(compa)

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
currentDate = datetime.now()

print(f'Dia: {currentDay}')
print(f'Mes: {currentMonth}')
print(f'Año: {currentYear}')
print(f'Fecha: {currentDate}')
dias = { 'Wednesday': 'Miercoles'}
dia_m = dias.get(currentDate.strftime("%A"))
print(f'Dia: {currentDate.strftime("%A")}')
print(f'Dia: {dia_m}')

