import MySQLdb
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

class Conexion:
    database = 'gestion_inventario'
    username = 'root'
    password = 'admin'
    port = 3306
    host = 'localhost'
    pool_size = 10
    pool_name = 'gestion_inventario_pool'
    pool = None
    
    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = [MySQLdb.connect(
                    host=cls.host,
                    user=cls.username,
                    passwd=cls.password,
                    db=cls.database,
                    port=cls.port,
                    cursorclass=DictCursor) for _ in range(cls.pool_size)]
                return cls.pool
            except OperationalError as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool
        
    @classmethod
    def obtener_conexion(cls):
        pool = cls.obtener_pool()
        if pool:
            return pool.pop()
        return None
    
    @classmethod
    def liberar_conexion(cls, conexion):
        pool = cls.obtener_pool()
        if pool is not None:
            pool.append(conexion)