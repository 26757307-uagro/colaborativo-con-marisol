'''
Programa que permite vender bebidas
Programa que permite vender bebidas
Solicita una opción para elegir la bebida
Pregunta cantidad de bebida
Muestra total a pagar
'''

print('Aguas de litro UAGro')
print('=================================')
print('1. Agua de mango - $ 40')
print('2. Agua de jamaica - $ 45')
print('3. Agua de horchata - $ 35')
print('==================================')
opcion = int(input('elige una opción del menú: '))
cantidad = int(input('¿Cuántos litros quieres?: '))

if opcion == 1:
    bebida = 'Agua de mango'
    precio = 40
elif opcion == 2:
    bebida = 'Agua de jamaica'
    precio = 45
elif opcion == 3:
    bebida = 'Agua de horchata'
    precio = 35
else:
    bebida = 'No existe bebida'
    precio = 0

if precio > 0:
    total = precio * cantidad
    print(f'{cantidad} de {bebida}')
    print(f'Total a pagar: $ {total}')
else:
    print('No existe la bebida, solo hay de mango, jamaica y horchata')
    print("mensaje de prueba en mi rama")