from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import (
    Integer,
    Double,
    String,
    Numeric,
    Date,
    DateTime,
    func,
    ForeignKey,
)
from datetime import datetime, date
from typing import List

Model = declarative_base()


class Tablero(Model):
    __tablename__ = "tablero"
    orden: Mapped[int] = mapped_column(Integer, primary_key=True)
    periodo: Mapped[str] = mapped_column(String(45))
    mes: Mapped[int] = mapped_column(Integer)
    anio: Mapped[int] = mapped_column(Integer)
    empleado_mes: Mapped[str] = mapped_column(String(80))
    empleado_mes_venta: Mapped[float] = mapped_column(Numeric(15, 3))
    empleado_mes_porcentaje: Mapped[float] = mapped_column(Numeric(6, 2))
    dia_mes: Mapped[str] = mapped_column(String(15))
    dia_mes_venta: Mapped[float] = mapped_column(Numeric(15, 2))
    dia_mes_porcentaje: Mapped[float] = mapped_column(Numeric(5, 2))
    dia_anio: Mapped[str] = mapped_column(String(15))
    dia_anio_venta: Mapped[float] = mapped_column(Numeric(15, 2))
    dia_anio_porcentaje: Mapped[float] = mapped_column(Numeric(5, 2))
    sucursal_mes: Mapped[str] = mapped_column(String(80))
    sucursal_mes_venta: Mapped[float] = mapped_column(Numeric(15, 2))
    sucursal_mes_porcentaje: Mapped[float] = mapped_column(Numeric(5, 2))
    sucursal_anio: Mapped[str] = mapped_column(String(80))
    sucursal_anio_venta: Mapped[float] = mapped_column(Numeric(15, 2))
    sucursal_anio_porcentaje: Mapped[float] = mapped_column(Numeric(5, 2))
    online_mes: Mapped[float] = mapped_column(Numeric(15, 2))
    presencial_mes: Mapped[float] = mapped_column(Numeric(15, 2))
    telefono_mes: Mapped[float] = mapped_column(Numeric(15, 2))
    online_anio: Mapped[float] = mapped_column(Numeric(15, 2))
    presencial_anio: Mapped[float] = mapped_column(Numeric(15, 2))
    telefono_anio: Mapped[float] = mapped_column(Numeric(15, 2))
    presencial_mes: Mapped[float] = mapped_column(Numeric(15, 2))
    ventas: Mapped[float] = mapped_column(Numeric(15, 2))
    compras: Mapped[float] = mapped_column(Numeric(15, 2))
    gastos: Mapped[float] = mapped_column(Numeric(15, 2))
    ventas_outliers: Mapped[float] = mapped_column(Numeric(15, 2))
    perdida_42917: Mapped[float] = mapped_column(Numeric(15, 2))
    dias_entrega: Mapped[float] = mapped_column(Numeric(5, 2))


class Temporal(Model):
    __tablename__ = "temporal"
    Id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    periodo: Mapped[str] = mapped_column(String(25), unique=True)
    orden: Mapped[int] = mapped_column(Integer)
    anio: Mapped[int] = mapped_column(Integer)
    mes: Mapped[int] = mapped_column(Integer)


class Despacho(Model):
    __tablename__ = "despacho"
    IdDespacho: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    IdSucursal: Mapped[int] = mapped_column(Integer)
    Sucursal: Mapped[str] = mapped_column(String(45))
    IdCliente: Mapped[int] = mapped_column(Integer)
    FechaPedido: Mapped[str] = mapped_column(Date)
    FechaEntrega: Mapped[str] = mapped_column(Date)
    TiempoEntrega: Mapped[int] = mapped_column(Integer)
    Venta: Mapped[float] = mapped_column(Numeric(15, 2))
    LongitudIni: Mapped[float] = mapped_column(Numeric(13, 10))
    LatitudIni: Mapped[float] = mapped_column(Numeric(13, 10))
    LongitudFinal: Mapped[float] = mapped_column(Numeric(13, 10))
    LatitudFinal: Mapped[float] = mapped_column(Numeric(13, 10))
    Distancia: Mapped[int] = mapped_column(Integer)
    anio: Mapped[int] = mapped_column(Integer)
    mes: Mapped[int] = mapped_column(Integer)
    HoverInf: Mapped[str] = mapped_column(String(150))


class VentaOutliers(Model):
    __tablename__ = "venta_outliers"
    IdVenta: Mapped[int] = mapped_column(Integer, primary_key=True)
    Fecha: Mapped[date] = mapped_column(Date)
    FechaEntrega: Mapped[date] = mapped_column(Date)
    IdCanal: Mapped[int] = mapped_column(Integer)
    IdCliente: Mapped[int] = mapped_column(Integer)
    IdSucursal: Mapped[int] = mapped_column(Integer)
    IdEmpleado: Mapped[int] = mapped_column(Integer)
    IdProducto: Mapped[int] = mapped_column(Integer)
    Precio: Mapped[float] = mapped_column(Numeric(15, 3))
    Cantidad: Mapped[int] = mapped_column(Integer)
    Motivo: Mapped[int] = mapped_column(Integer)


class VentaSinOutliers(Model):
    __tablename__ = "venta_sin_outliers"
    IdVenta: Mapped[int] = mapped_column(Integer, primary_key=True)
    Fecha: Mapped[date] = mapped_column(Date)
    FechaEntrega: Mapped[date] = mapped_column(Date)
    IdCanal: Mapped[int] = mapped_column(Integer)
    IdCliente: Mapped[int] = mapped_column(Integer)
    IdSucursal: Mapped[int] = mapped_column(Integer)
    IdEmpleado: Mapped[int] = mapped_column(Integer)
    IdProducto: Mapped[int] = mapped_column(Integer)
    Precio: Mapped[float] = mapped_column(Numeric(15, 3))
    Cantidad: Mapped[int] = mapped_column(Integer)


class AuxCliente(Model):
    __tablename__ = "aux_cliente"
    IdCliente: Mapped[int] = mapped_column(Integer, primary_key=True)
    Latitud: Mapped[float] = mapped_column(Double)
    Longitud: Mapped[float] = mapped_column(Double)


class AuxLocalidad(Model):
    __tablename__ = "aux_localidad"
    LocalidadOriginal: Mapped[str] = mapped_column(String(80))
    ProvinciaOriginal: Mapped[str] = mapped_column(String(50))
    LocalidadNormalizada: Mapped[str] = mapped_column(String(80))
    ProvinciaNormalizada: Mapped[str] = mapped_column(String(50))
    idLocalidad: Mapped[int] = mapped_column(Integer, primary_key=True)


class Calendario(Model):
    __tablename__ = "calendario"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    Fecha: Mapped[int] = mapped_column(Date, unique=True, nullable=False)
    Anio: Mapped[int] = mapped_column(Integer, nullable=False)
    Mes: Mapped[int] = mapped_column(Integer, nullable=False)
    Dia: Mapped[int] = mapped_column(Integer, nullable=False)
    Trimestre: Mapped[int] = mapped_column(Integer, nullable=False)
    Semana: Mapped[int] = mapped_column(Integer, nullable=False)
    DiaNombre: Mapped[str] = mapped_column(String(9), nullable=False)
    MesNombre: Mapped[str] = mapped_column(String(9), nullable=False)


class CanalVenta(Model):
    __tablename__ = "canal_venta"
    IdCanal: Mapped[int] = mapped_column(Integer, primary_key=True)
    Canal: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    # RELATIONS:
    ventas: Mapped[List["VentaHeader"]] = relationship(back_populates="canal_venta")


class TipoProducto(Model):
    __tablename__ = "tipo_producto"
    IdTipoProducto: Mapped[int] = mapped_column(Integer, primary_key=True)
    TipoProducto: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    # RELATIONS:
    productos_tipo: Mapped[List["Producto"]] = relationship(
        back_populates="tipo_producto"
    )


class Producto(Model):
    __tablename__ = "producto"
    IdProducto: Mapped[int] = mapped_column(Integer, primary_key=True)
    Producto: Mapped[str] = mapped_column(String(100), nullable=False)
    Precio: Mapped[float] = mapped_column(Numeric(15, 3), nullable=False)
    IdTipoProducto: Mapped[int] = mapped_column(
        Integer, ForeignKey("tipo_producto.IdTipoProducto"), nullable=False
    )
    # RELATIONS:
    tipo_producto: Mapped["TipoProducto"] = relationship(
        back_populates="productos_tipo"
    )
    compra_detail_producto: Mapped[List["CompraDetail"]] = relationship(
        back_populates="producto_detail_compra"
    )
    venta_detail_producto: Mapped[List["VentaDetail"]] = relationship(
        back_populates="productos_detail_venta"
    )


class CompraHeader(Model):
    __tablename__ = "compra_header"
    IdCompra: Mapped[int] = mapped_column(Integer, primary_key=True)
    Fecha: Mapped[date] = mapped_column(Date, nullable=False)
    IdProveedor: Mapped[int] = mapped_column(
        Integer, ForeignKey("proveedor.IdProveedor"), nullable=False
    )
    # RELATIONS:
    proveedor: Mapped["Proveedor"] = relationship(back_populates="compras_proveedor")
    details_compra: Mapped[List["CompraDetail"]] = relationship(
        back_populates="header_compa"
    )


class CompraDetail(Model):
    __tablename__ = "compra_detail"
    IdCompra: Mapped[int] = mapped_column(
        Integer, ForeignKey("compra_header.IdCompra"), primary_key=True
    )
    IdProducto: Mapped[int] = mapped_column(
        Integer, ForeignKey("producto.IdProducto"), primary_key=True
    )
    Cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    Precio: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    # RELATIONS:
    header_compa: Mapped["CompraHeader"] = relationship(back_populates="details_compra")
    producto_detail_compra: Mapped["Producto"] = relationship(
        back_populates="compra_detail_producto"
    )

    # __table_args__ = (PrimaryKeyConstraint('idVenta', 'idProducto'),)


class Proveedor(Model):
    __tablename__ = "proveedor"
    IdProveedor: Mapped[int] = mapped_column(Integer, primary_key=True)
    Nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    Domicilio: Mapped[str] = mapped_column(String(150), nullable=False)
    IdLocalidad: Mapped[int] = mapped_column(
        Integer, ForeignKey("localidad.IdLocalidad"), nullable=False
    )
    Pais: Mapped[str] = mapped_column(String(20), nullable=False)
    Departamento: Mapped[str] = mapped_column(String(80), nullable=False)
    # RELATIONS:
    compras_proveedor: Mapped[List["CompraHeader"]] = relationship(
        back_populates="proveedor"
    )
    localidad_proveedor: Mapped["Localidad"] = relationship(
        back_populates="proveedores"
    )


class Empleado(Model):
    __tablename__ = "empleado"
    IdEmpleado: Mapped[int] = mapped_column(Integer, primary_key=True)
    CodigoEmpleado: Mapped[int] = mapped_column(Integer, nullable=False)
    Apellido: Mapped[str] = mapped_column(String(100), nullable=False)
    Nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    IdSucursal: Mapped[int] = mapped_column(
        Integer, ForeignKey("sucursal.IdSucursal"), nullable=False
    )
    IdSector: Mapped[int] = mapped_column(
        Integer, ForeignKey("sector.IdSector"), nullable=False
    )
    IdCargo: Mapped[int] = mapped_column(
        Integer, ForeignKey("cargo.IdCargo"), nullable=False
    )
    Salario: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    # RELATIONS:
    sector: Mapped["Sector"] = relationship(back_populates="empleados_sector")
    cargo: Mapped["Cargo"] = relationship(back_populates="empleados_cargo")
    sucursal: Mapped["Sucursal"] = relationship(back_populates="empleados_sucrsal")
    ventas_empleado: Mapped[List["VentaHeader"]] = relationship(
        back_populates="empleado_venta"
    )


class Sector(Model):
    __tablename__ = "sector"
    IdSector: Mapped[int] = mapped_column(Integer, primary_key=True)
    Sector: Mapped[str] = mapped_column(String(50), nullable=False)
    # RELATIONS:
    empleados_sector: Mapped[List["Empleado"]] = relationship(back_populates="sector")


class Cargo(Model):
    __tablename__ = "cargo"
    IdCargo: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cargo: Mapped[str] = mapped_column(String(50), nullable=False)
    # RELATIONS:
    empleados_cargo: Mapped[List["Empleado"]] = relationship(back_populates="cargo")


class Sucursal(Model):
    __tablename__ = "sucursal"
    IdSucursal: Mapped[int] = mapped_column(Integer, primary_key=True)
    Sucursal: Mapped[str] = mapped_column(String(40), nullable=False)
    Domicilio: Mapped[str] = mapped_column(String(150), nullable=False)
    IdLocalidad: Mapped[int] = mapped_column(
        Integer, ForeignKey("localidad.IdLocalidad"), nullable=False
    )
    Latitud: Mapped[float] = mapped_column(Numeric(13, 10))
    Longitud: Mapped[float] = mapped_column(Numeric(13, 10))
    # RELATIONS:
    empleados_sucursal: Mapped[List["Empleado"]] = relationship(
        back_populates="sucursal"
    )
    gastos_sucursal: Mapped[List["Gasto"]] = relationship(
        back_populates="sucursal_gasto"
    )
    ventas_sucursal: Mapped[List["VentaHeader"]] = relationship(
        back_populates="sucursal_venta"
    )
    localidad_sucursal: Mapped["Localidad"] = relationship(back_populates="sucursales")


class TipoGasto(Model):
    __tablename__ = "tipo_gasto"
    IdTipoGasto: Mapped[int] = mapped_column(Integer, primary_key=True)
    TipoGasto: Mapped[str] = mapped_column(String(100), nullable=False)
    MontoAproximado: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    # RELATIONS:
    gastos: Mapped[List["Gasto"]] = relationship(back_populates="tipo_gasto")


class Gasto(Model):
    __tablename__ = "gasto"
    IdGasto: Mapped[int] = mapped_column(Integer, primary_key=True)
    IdSucursal: Mapped[int] = mapped_column(
        Integer, ForeignKey("sucursal.IdSucursal"), nullable=False
    )
    IdTipoGasto: Mapped[int] = mapped_column(
        Integer, ForeignKey("tipo_gasto.IdTipoGasto"), nullable=False
    )
    Fecha: Mapped[date] = mapped_column(Date, nullable=False)
    Monto: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    # RELATIONS:
    tipo_gasto: Mapped["TipoGasto"] = relationship(back_populates="gastos")
    sucursal_gasto: Mapped["Sucursal"] = relationship(back_populates="gastos_sucursal")


class Cliente(Model):
    __tablename__ = "cliente"
    IdCliente: Mapped[int] = mapped_column(Integer, primary_key=True)
    NombreApellido: Mapped[str] = mapped_column(String(80), nullable=False)
    Domicilio: Mapped[str] = mapped_column(String(150), nullable=False)
    Telefono: Mapped[str] = mapped_column(String(30), nullable=False)
    Edad: Mapped[int] = mapped_column(Integer, nullable=False)
    RangoEtario: Mapped[str] = mapped_column(String(20), default="1_Hasta 30 años")
    IdLocalidad: Mapped[int] = mapped_column(
        Integer, ForeignKey("localidad.IdLocalidad"), nullable=False
    )
    Latitud: Mapped[float] = mapped_column(Numeric(13, 10))
    Longitud: Mapped[float] = mapped_column(Numeric(13, 10))
    FechaAlta: Mapped[date] = mapped_column(Date)
    UsuarioAlta: Mapped[str] = mapped_column(String(20))
    FechaUpdate: Mapped[datetime] = mapped_column(
        DateTime, onupdate=func.now(), default=func.now()
    )
    UsuarioUpdate: Mapped[str] = mapped_column(String(20), default="usuario_anónimo")
    MarcaBaja: Mapped[int] = mapped_column(Integer)
    # RELATIONS:
    ventas_cliente: Mapped[List["VentaHeader"]] = relationship(
        back_populates="cliente_venta"
    )
    localidad_cliente: Mapped["Localidad"] = relationship(back_populates="clientes")


class VentaHeader(Model):
    __tablename__ = "venta_header"
    IdVenta: Mapped[int] = mapped_column(Integer, primary_key=True)
    Fecha: Mapped[date] = mapped_column(Date, nullable=False)
    FechaEntrega: Mapped[date] = mapped_column(Date, nullable=False)
    IdCanal: Mapped[int] = mapped_column(
        Integer, ForeignKey("canal_venta.IdCanal"), nullable=False
    )
    IdCliente: Mapped[int] = mapped_column(
        Integer, ForeignKey("cliente.IdCliente"), nullable=False
    )
    IdSucursal: Mapped[int] = mapped_column(
        Integer, ForeignKey("sucursal.IdSucursal"), nullable=False
    )
    IdEmpleado: Mapped[int] = mapped_column(
        Integer, ForeignKey("empleado.IdEmpleado"), nullable=False
    )
    # RELATIONS:
    canal_venta: Mapped["CanalVenta"] = relationship(back_populates="ventas")
    empleado_venta: Mapped["Empleado"] = relationship(back_populates="ventas_empleado")
    sucursal_venta: Mapped["Sucursal"] = relationship(back_populates="ventas_sucursal")
    cliente_venta: Mapped["Cliente"] = relationship(back_populates="ventas_cliente")
    deatils_venta: Mapped[List["VentaDetail"]] = relationship(
        back_populates="header_venta"
    )


class VentaDetail(Model):
    __tablename__ = "venta_detail"
    IdVenta: Mapped[int] = mapped_column(
        Integer, ForeignKey("venta_header.IdVenta"), primary_key=True
    )
    IdProducto: Mapped[int] = mapped_column(
        Integer, ForeignKey("producto.IdProducto"), primary_key=True
    )
    Precio: Mapped[float] = mapped_column(Numeric(15, 3), nullable=False)
    Cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    # RELATIONS:
    header_venta: Mapped["VentaHeader"] = relationship(back_populates="deatils_venta")
    productos_detail_venta: Mapped["Producto"] = relationship(
        back_populates="venta_detail_producto"
    )


class Localidad(Model):
    __tablename__ = "localidad"
    IdLocalidad: Mapped[int] = mapped_column(Integer, primary_key=True)
    Localidad: Mapped[str] = mapped_column(String(80), nullable=False)
    IdProvincia: Mapped[int] = mapped_column(
        Integer, ForeignKey("provincia.IdProvincia"), nullable=False
    )
    # RELATIONS:
    provincia: Mapped["Provincia"] = relationship(back_populates="localidades")
    clientes: Mapped[List["Cliente"]] = relationship(back_populates="localidad_cliente")
    sucursales: Mapped[List["Sucursal"]] = relationship(
        back_populates="localidad_sucursal"
    )
    proveedores: Mapped[List["Proveedor"]] = relationship(
        back_populates="localidad_proveedor"
    )


class Provincia(Model):
    __tablename__ = "provincia"
    IdProvincia: Mapped[int] = mapped_column(Integer, primary_key=True)
    Provincia: Mapped[str] = mapped_column(String(50), nullable=False)
    # RELATIONS:
    localidades: Mapped[List["Localidad"]] = relationship(back_populates="provincia")
