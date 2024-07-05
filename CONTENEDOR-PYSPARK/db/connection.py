from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

host = "mod4_mysql"
user = "root"
password = "root"
db_name = "henry_mod4"
motor_sql = "mysql"
connector_used = "pymysql"
port = 3306


# UTILIZANDO SQLALCHEMY
def connec_db() -> object:
    """Conecta a Mysql Usando sqlAlchemy

    Returns:
        object: Conexion a Base de Datos
    """
    try:
        engine = create_engine(
            f"{motor_sql}+{connector_used}://{user}:{password}@{host}:{port}/{db_name}"
        )
        return engine
    except OperationalError as e:
        print(f"Error de la conexion {e}")
        return False
