from conexion import Conexion
from producto import Producto

class GestionInventario:
    AGREGAR = 'INSERT INTO productos(nombre, cantidad, precio, categoria) VALUES (%s, %s, %s, %s)'
    MOSTRAR = 'SELECT * FROM productos'
    BUSCAR = 'SELECT * FROM productos WHERE id=%s'
    ACTUALIZAR = 'UPDATE productos SET nombre=%s, cantidad=%s, precio=%s, categoria=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM productos WHERE id=%s'
    
    
    @classmethod
    def agregar(cls, producto):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            cursor.execute(cls.AGREGAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al agregar un producto: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def mostrar(cls):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.MOSTRAR)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro['id'], registro['nombre'], registro['cantidad'], registro['precio'], registro['categoria'])
                productos.append(producto)
            return productos
        except Exception as e:
            print(f'Ocurrió un error al mostrar los productos: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
  
    @classmethod
    def buscar(cls, id_producto):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.BUSCAR, (id_producto,))
            registro = cursor.fetchone()
            if registro:
                return Producto(registro['id'], registro['nombre'], registro['cantidad'], registro['precio'], registro['categoria'])
            return None
        except Exception as e:
            print(f'Ocurrió un error al buscar el producto: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)

                
    @classmethod
    def actualizar(cls, producto):
        conexion = None
        
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria, producto.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar un producto: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def eliminar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar un producto: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
