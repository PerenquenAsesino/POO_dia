from clase_dia import Dia

def test_inicializar_fecha_concreta():
    # Preparo el test, condiciones de inicializacion
    fecha = Dia(1,1,1970,4)
    # Compruebo el resultado esperado
    assert fecha.dia == 1
    assert fecha.mes == 1
    assert fecha.anyo == 1970
    assert fecha.dia_semana == 4


def test_es_bisiesto():
    fecha = Dia(14,2,2024)  # Selecciono un año bisiesto
    fecha2 = Dia(14,2,2023) # Selecciono un año NO bisiesto
    # Compruebo el resultado esperado
    assert fecha.es_bisiesto() == True
    assert fecha2.es_bisiesto() == False


def test_dias_mes():
    fecha1 = Dia(14,1,2024)  # Enero tiene 31 dias
    fecha2 = Dia(14,2,2024)  # Febrero tiene 29 dias
    fecha3 = Dia(14,4,2024)  # Abril tiene 30 dias
    # Compruebo el resultado esperado
    assert fecha1.dias_en_mes() == 31
    assert fecha2.dias_en_mes() == 29
    assert fecha3.dias_en_mes() == 30


def test_zeller():
    fecha1 = Dia(22,2,2024) # Jueves                
    fecha2 = Dia(23,2,2024) # Viernes    
    fecha3 = Dia(24,2,2024) # Sabado    
    # Compruebo el resultado esperado
    assert fecha1.dia_de_la_semana() == 5
    assert fecha2.dia_de_la_semana() == 6
    assert fecha3.dia_de_la_semana() == 0