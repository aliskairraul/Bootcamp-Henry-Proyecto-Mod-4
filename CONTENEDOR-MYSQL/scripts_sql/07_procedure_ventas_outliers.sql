truncate table aux_venta;


DELIMITER $$
CREATE PROCEDURE create_venta_outliers()
BEGIN
	TRUNCATE TABLE venta_outliers;
  TRUNCATE TABLE venta_sin_outliers;
  SET @media_venta = (SELECT AVG(Cantidad * Precio) FROM venta_detail);
  SET @desv_venta = (SELECT STDDEV(Cantidad * Precio) FROM venta_detail);
  SET @maximo = @media_venta + 3 * @desv_venta;
  SET @minimo = @media_venta - 3 * @desv_venta;

  -- LLENADO TABLA CON VENTAS OUTLIERS
  INSERT INTO venta_outliers (IdVenta, Fecha, FechaEntrega, IdCanal, IdCliente,
              IdSucursal, IdEmpleado, IdProducto, Precio, Cantidad, Motivo)
  SELECT vh.IdVenta, vh.Fecha, vh.FechaEntrega, vh.IdCanal, vh.IdCliente, vh.IdSucursal,
          vh.IdEmpleado, vd.IdProducto, vd.Precio, vd.Cantidad, 2
  FROM venta_header vh
  INNER JOIN venta_detail vd
  ON vh.IdVenta = vd.IdVenta
  WHERE (vd.Cantidad * vd.Precio) >= @maximo;
  
  -- LLENADO TABLA VENTA SIN OUTLIERS
  INSERT INTO venta_sin_outliers (IdVenta, Fecha, FechaEntrega, IdCanal, IdCliente,
              IdSucursal, IdEmpleado, IdProducto, Precio, Cantidad)
  SELECT vh.IdVenta, vh.Fecha, vh.FechaEntrega, vh.IdCanal, vh.IdCliente, vh.IdSucursal,
          vh.IdEmpleado, vd.IdProducto, vd.Precio, vd.Cantidad 
  FROM venta_header vh
  INNER JOIN venta_detail vd
  ON vh.IdVenta = vd.IdVenta
  WHERE (vd.Cantidad * vd.Precio) < @maximo;
END$$
DELIMITER ;

CALL create_venta_outliers();