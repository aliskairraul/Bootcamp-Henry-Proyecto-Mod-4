from models.tables import Model
from db.connection import connec_db

# Importacion de Modelos de Tablas del Proyecto
from models.tables import (
    Tablero,
    Temporal,
    Despacho,
    VentaOutliers,
    VentaSinOutliers,
    AuxCliente,
    AuxLocalidad,
    Calendario,
    CanalVenta,
    VentaHeader,
    VentaDetail,
    TipoProducto,
    Producto,
    TipoGasto,
    Gasto,
    CompraHeader,
    CompraDetail,
    Proveedor,
    Empleado,
    Cargo,
    Sector,
    Sucursal,
    Cliente,
    Localidad,
    Provincia,
)

# Creacion del Engine
engine = connec_db()

# Creacion de Todas las Tablas del Proyecto
Model.metadata.drop_all(engine)
Model.metadata.create_all(engine)
