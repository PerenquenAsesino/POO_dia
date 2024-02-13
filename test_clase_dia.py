from clase_dia import Dia

def test_inicializar_fecha():
    # Preparo el test, condiciones de inicializacion
    fecha = Dia()
    # Compruebo el resultado esperado
    assert fecha.dia == 1
    assert fecha.mes == 1
    assert fecha.anyo == 1
    assert fecha.dia_semana == 1

def test_inicializar_fecha_concreta():
    # Preparo el test, condiciones de inicializacion
    fecha = Dia(1,1,1970,1)
    # Compruebo el resultado esperado
    assert fecha.dia == 1
    assert fecha.mes == 1
    assert fecha.anyo == 1970
    assert fecha.dia_semana == 1