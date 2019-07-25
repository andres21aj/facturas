#
#   Sorteador de facturas para 'x' día de la semana
#   levanta los datos de un json, lee los datos y determina
#   de acuerdo al día parametrizado y la cantidad de gente,
#   los días que se debe llevar facturas y quien las lleva

import json
# from datetime import datetime
import modules.facturas_classes as fClasses


fApp = fClasses.FacturasApp()

# Logica para levantar los datos del archivo
with open('participantes.json') as json_file:
    participantes = json.load(json_file)
    day_to_bring = fApp.get_day_number(participantes.get('bdat'))
    persons_lst = participantes.get('persons')

try:
    d2b = fApp.get_bring_days(day_to_bring)
    asigned_dates = fApp.assign_people(persons_lst, d2b)
except ValueError as ex_las_fechas:
    print(ex_las_fechas)
