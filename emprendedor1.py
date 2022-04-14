precio_suscripcion = input('Ingrese precio de suscripción: ')
numero_usuarios = input('Ingrese el número de usuarios: ')
gasto_total = input('Ingrese el gasto total: ')

utilidad = int(precio_suscripcion) * int(numero_usuarios) - int(gasto_total)


print(f'La utilidad del proyecto es : {utilidad}')