from clase_dia import Dia

class WallCalendar:
    def __init__(self, anyo = 12, mes = 12, dia = 12):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia 
        # Validamos que los parametros sean correctos, si no, lanza ValueError.
        if not isinstance(anyo, int) or anyo < 1:
            raise ValueError("El año debe ser un entero positivo")
        if not isinstance(mes, int) or mes < 1 or mes > 12:
            raise ValueError("El mes debe ser un entero entr 1 y 12")
        if not isinstance(dia, int) or dia < 1:
            raise ValueError("El dia debe ser un entero positivo")
    

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

    # Devuelve año, mes y día ajustados
    def pasar_dias_a_meses(self):
        while self.dia > self.dias_en_mes():
            self.dia -= self.dias_en_mes()
            if self.mes == 12:
                self.mes = 1
                self.anyo += 1
            else:
                self.mes += 1
        return self.anyo, self.mes, self.dia   

    # Devuelve el dia de la semana (lunes, martes...)
    def nombre_dia(self):
        anyo, mes, dia = self.pasar_dias_a_meses()
        clase_dia = Dia(dia, mes, anyo)
        clase_dia.dia_de_la_semana()
        dias = ['sabado', 'domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes']
        return dias[clase_dia.dia_de_la_semana()]
        
    # Guarda la fecha final
    def guardar_fecha(self):
        anyo, mes, dia = self.pasar_dias_a_meses()
        fecha = [anyo, mes, dia]
        return fecha
    
    # Imprime la fecha final
    def mostrar_fecha(self):
        meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
        return f"{self.nombre_dia()}, {self.guardar_fecha()[2]} de {meses[self.guardar_fecha()[1]-1]} de {self.guardar_fecha()[0]}"           
        
    # Avanza un dia de la fecha
    def avanza(self):
        self.dia += 1
        self.pasar_dias_a_meses()
        print("--avanza 1 dia--")
        

# Impresiones de prueba, primero imprime una fecha ajustando dias y meses. Luego imprime avance de dia.
calendario = WallCalendar(2024,1,60)
print(calendario.mostrar_fecha())
calendario.avanza()
print(calendario.mostrar_fecha())

