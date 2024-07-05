DELIMITER $$
DROP PROCEDURE IF EXISTS historico_sucursales$$
CREATE PROCEDURE historico_sucursales()
BEGIN
  SELECT vh.IdSucursal AS Sucursal,
	       YEAR(vh.Fecha) as Anio,
         MONTH(vh.Fecha) as Mes,
         SUM(vd.Cantidad * vd.Precio) as Venta
  FROM venta_detail vd
  INNER JOIN venta_header vh
   ON vh.IdVenta = vd.IdVenta
  GROUP BY 1,2,3
  ORDER BY 2,3,1;
END $$
DELIMITER ;

CALL historico_sucursales();