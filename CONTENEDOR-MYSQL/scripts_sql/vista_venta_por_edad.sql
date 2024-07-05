CREATE VIEW venta_por_edad AS 
SELECT c.RangoEtario, 
       YEAR(vh.Fecha) as Anio,
       MONTH(vh.Fecha) as Mes,
	   SUM(vd.Cantidad * vd.Precio) as Venta
FROM venta_header vh
INNER JOIN venta_detail vd
  ON vd.IdVenta = vh.IdVenta
INNER JOIN cliente c
  ON vh.IdCliente = c.IdCliente
GROUP BY 1,2,3
ORDER BY 2,3;

SELECT * FROM venta_por_edad;