    ##Néstor González Suárez Clase_Dia##
#Prueba final POO, TDD, Python#


##1 Enunciado del Ejercicio: Creación de la Clase Dia en Python##

Objetivo: Desarrollar una clase Dia en Python que represente una fecha, la cual puede ser inicializada con valores por defecto (1 de enero de 1970) o con valores específicos de fecha (año, mes, día) proporcionados por el usuario. Esta clase debe ser implementada sin utilizar ninguna librería estándar o no estándar de Python, apoyándose únicamente en cálculos numéricos para todas sus operaciones.

#Requisitos de la Clase Dia:#

• **Inicialización:** La clase debe poder inicializarse tanto con valores por defecto (1 de enero de 1970) como con una fecha específica proporcionada por el usuario. Debe validar que la fecha es correcta, considerando años bisiestos.
Es decir si creas una instancia de Día tal que asi d = Dia(), eso significara que d tendra los valores d.dia = 1, d.mes = 1, d.anyo = 1970.
Si intentas crear una fecha tal que d = Dia(1970, 4, 31) debe lanzar una excepcion
de tipo ValueError con el mensaje que desees, ya que abril solo tiene 30 días.
Si intentas crear una fecha tal que d = Dia(1970, 4, 7) d tendrá los siguientes atributos d.dia = 7, d.mes = 4, d.anyo = 1970.

**• Atributos:** La clase tendrá los atributos:
– **dia:** dia del mes
– **mes:** numero del mes, 1 enero, 12 diciembre
– **anyo:** numero del año. Siempre después de cristo (desde el 1 en adelante)
– **dia_semana:** numero del dia de la semana siendo 0 el sabado y el 6 el viernes
representada.

**• Verificación de Fecha Correcta:** Incluir lógica para verificar la validez de la fecha, incluyendo la correcta identificación de años bisiestos.

**• Cálculo del Día de la Semana:** Implementar el algoritmo de Zeller dentro de la clase para determinar el día de la semana de la fecha.

**Restricciones:** - No se permite el uso de librerías estándar o no estándar de Python para el manejo de fechas o cualquier otro cálculo relacionado con la clase. Todos los cálculos deben realizarse de manera numérica.