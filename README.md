# Facturas

Programa sorteador de facturas, el programa levanta datos de un json que tiene los datos de los [integrantes](#Integrantes). Con esos datos se fija el mes actual, determina cuantos días del mes se debe llevar facturas, con esos datos divide la cantidad de personas por los días que se deben llevar facturas de ese mes.

## Integrantes

Los integrantes seran guardados en un json y tendrán la siguiente estructura:

```json
{
  "team": "Equipo_que_lleva",
  "bdat": "dia_que_se_llevan",
  "persons": [
    {
      "id": "numerador",
      "name": "Nombre Apellido",
      "last": "dd-mm-aaaa",
      "prob": "probabilidad de llevar la próxima"
    }
  ]
  
}
```
