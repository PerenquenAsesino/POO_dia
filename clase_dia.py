
# Inicializamos la clase
class Dia:
    def __init__(self,dia=1, mes=1, anyo=1970,  dia_semana=4):
        self.dia = dia
        self.mes = mes
        self.anyo = anyo
        self.dia_semana = dia_semana        
        # Validamos que los parametros sean correctos.
        if not isinstance(anyo, int) or anyo < 1:
            raise ValueError("El año debe ser un entero positivo")
        if not isinstance(mes, int) or mes < 1 or mes > 12:
            raise ValueError("El mes debe ser un entero entre 1 y 12")
        if not isinstance(dia, int) or dia < 1 or dia > self.dias_en_mes():
            raise ValueError("El dia debe ser un entero entre 1 y el numero de dias del mes")
        self.dia_semana = self.dia_de_la_semana()

    # Devuelve True si es bisiesto.
    def es_bisiesto(self):
        return self.anyo % 4 == 0 and (self.anyo % 100 != 0 or self.anyo % 400 == 0)

    # Devuelve el numero de dias segun el mes.
    def dias_en_mes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes == 2:
            return 29 if self.es_bisiesto() else 28
        else:
            return 30

    # Calcula el dia de la semana (Algoritmo de Zeller).        
    def dia_de_la_semana(self):
        if self.mes < 3:
            mes_modificado = self.mes + 12
            anyo_modificado = self.anyo - 1
        else:
            mes_modificado = self.mes
            anyo_modificado = self.anyo

        a = anyo_modificado % 100
        b = anyo_modificado // 100
        c = 2 - b + (b // 4)
        d = a // 4
        e = 13 * (mes_modificado + 1) // 5
        f = a + c + d + e + self.dia - 1
        g = f % 7 
        return g
       
    # Metodo especial para imprimir todos los valores del objeto.
    def __str__(self):
        return f"Dia: {self.dia}, Mes: {self.mes}, Año: {self.anyo}, Dia de la semana: {self.dia_semana}"

# Impresiones de prueba  
d = Dia(28, 12, 2024)
print(d)
d = Dia(29, 12, 2024)
print(d)
d = Dia(30, 12, 2024)
print(d)
d = Dia(31, 12, 2024)
print(d)
