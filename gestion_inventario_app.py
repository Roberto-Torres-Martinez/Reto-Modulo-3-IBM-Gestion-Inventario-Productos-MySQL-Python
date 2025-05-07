from gestion_inventario import GestionInventario
from producto import Producto

print('Inventario De Productos')

opcion = None
while opcion != 6:
    print(f'''Menu:
          1. Agregar Productos
          2. Mostrar Productos
          3. Buscar Producto
          4. Actualizar Producto
          5. Eliminar Producto
          6. Salir
          '''),
    opcion = int(input('Elige tu opcion (1-6): '))
    
    if opcion ==1:
        nombre_producto = input('Escribe el nombre del producto: ')
        cantidad_producto = input('Elige la cantidad del producto: ')
        precio_producto = input('Escribe el precio del producto: ')
        categoria_producto = input('Escribe la categoría del producto: ')
        producto = Producto(nombre=nombre_producto, cantidad=cantidad_producto, precio=precio_producto, categoria=categoria_producto)
        productos_insertados = GestionInventario.agregar(producto)
        print(f'Productos Agregados: {productos_insertados}')
    elif opcion == 2:
        productos = GestionInventario.mostrar()
        print('\n*** Listado de Productos ***')
        for producto in productos:
            print(producto)
    elif opcion == 3:
        id_producto = int(input('Escribe el ID del producto que quieres buscar: '))
        producto = GestionInventario.buscar(id_producto)
        if producto:
            print(f'\n*** Producto Encontrado ***\n{producto}')
        else:
            print('No se encontró un producto con ese ID.')
    elif opcion == 4:
        id_producto = int(input('Escribe el id del producto que quieres actualizar: '))
        nombre_producto = input('Escribe el nombre del producto: ')
        cantidad_producto = input('Escribe la cantidad del producto: ')
        precio_producto = input('Escribe el precio del producto: ')
        categoria_producto = input('Escribe la categoría del producto: ')
        producto = Producto(id=id_producto, nombre=nombre_producto, cantidad=cantidad_producto, precio=precio_producto, categoria=categoria_producto)
        productos_actualizados = GestionInventario.actualizar(producto)
        print(f'Productos actualizados: {productos_actualizados}')
    elif opcion == 5:
        id_producto = int(input('Escribe el id del producto a eliminar: '))
        producto = Producto(id=id_producto)
        productos_eliminados = GestionInventario.eliminar(producto)
        print(f'Productos eliminados: {productos_eliminados}')
    else:
        print('Saliste de la aplicacion...')