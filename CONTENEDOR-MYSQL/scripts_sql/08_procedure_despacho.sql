TRUNCATE despacho;

DELIMITER $$
DROP PROCEDURE IF EXISTS despacho$$
CREATE PROCEDURE despacho()
BEGIN

    INSERT INTO despacho(IdSucursal, Sucursal, IdCliente, FechaPedido, FechaEntrega,
                         TiempoEntrega, Venta, LongitudIni, LatitudIni, LongitudFinal,
                         LatitudFinal, Distancia, Anio, Mes, HoverInf)
    SELECT v.IdSucursal, 
        s.Sucursal,
        v.IdCliente, 
        v.Fecha,  
        v.FechaEntrega,
        TIMESTAMPDIFF(Day, v.Fecha, v.FechaEntrega) as Tiempo_Entrega,
        sum(v.Precio * v.cantidad) as Venta,
        s.Longitud as Longitud_INI,
        s.Latitud as Latitud_INI,
        c.Longitud as Longitud_FIN,
        c.Latitud as Latitud_FIN,
        ROUND(SQRT( (c.Latitud - s.Latitud) * (c.Latitud - s.Latitud) + 
                (c.Longitud - s.Longitud) * (c.Longitud - s.Longitud) ) 
                * 111.1) as Distancia,
        YEAR(v.Fecha) as Anio,
        MONTH(v.Fecha) as Mes,
        CONCAT(s.Sucursal, " ", c.IdCliente, "-",c.NombreApellido, " Fecha: ",
               v.Fecha, " Entrega: ", TIMESTAMPDIFF(Day, v.Fecha, v.FechaEntrega),
               " Venta: ", round(sum(v.Precio * v.cantidad))) as HoverInf
    from venta_sin_outliers v
    inner Join sucursal s
    on s.IdSucursal = v.IdSucursal
    inner Join cliente c
    on c.IdCliente = v.IdCliente
    Group by 1,2,3,4,5,6
    Order by 4;
END $$
DELIMITER ;

CALL despacho();