precio_suscripcion = float(input('Ingrese precio de suscripción base: '))
numero_usuarios_normal = int(input('Ingrese el número de usuarios normales: '))
numero_usuarios_premium = int(input('Ingrese el número de usuarios premium: '))
gasto_total = float(input('Ingrese el gasto total: '))

utilidad = (precio_suscripcion * numero_usuarios_normal + (precio_suscripcion * 1.5) * numero_usuarios_premium) - gasto_total


print(f'La utilidad del proyecto es : {utilidad}')