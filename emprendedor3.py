precio_suscripcion = input('Ingrese precio de suscripción (Ingrese un decimal separado por punto): ')
numero_usuarios = input('Ingrese el número de usuarios (Ingrese un número entero): ')
gasto_total = input('Ingrese el gasto total (Ingrese un decimal separado por punto): ')
utilidad_anho_anterior= input('Ingrese la utilidad del año pasado (Ingrese un número entero): ')

utilidad = float(precio_suscripcion) * int(numero_usuarios) - float(gasto_total)

resultado_razon = utilidad/float(utilidad_anho_anterior)

print(f'La utilidad del año pasado {utilidad_anho_anterior} versus la utilidad actual {utilidad} es: {resultado_razon:.2f}')