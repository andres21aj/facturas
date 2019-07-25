# Facturas

Programa sorteador de facturas, el programa levanta datos de un json que tiene los datos de los [integrantes](#Integrantes). Con esos datos se obtiene el `bdat` que es el día del mes que se llevaran las facturas cada semana. El campo `persons` contiene el total de integrantes por equipo o grupo.

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
