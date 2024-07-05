/* La siguiente Query Obtiene los Margenes Con respecto al precio de venta
   de los distintos SKU's */

-- MARGENES DE COMERCIALIZACION
SELECT DISTINCT p.IdProducto, ROUND( 1 - (c.CostoPromedio / p.Precio),2) as Margen
FROM producto p
INNER JOIN compra_detail c
ON p.IdProducto = c.IdProducto;

/* Se observa un Margen de 30% con una pequeña variacion maxima de 2% para arriba o para
   abajo de todos los Sku's excepto 1 El Sku con el codigo `IdProducto` 42917 el cual tiene 
   un margen de -70.03 */


/* Obtengo el Costo Promedio y Precio de Venta del Sku 42917*/    
SELECT p.IdProducto,
       p.Producto,
       v.Precio as "Se Vende en",
       c.CostoPromedio as "Se Compra en"
FROM producto p  
INNER JOIN venta_detail as v 
  ON v.IdProducto = p.IdProducto
INNER JOIN compra_detail c  
  ON c.IdProducto = p.IdProducto
WHERE c.IdProducto = 42917
LIMIT 1;   

+------------+----------------------------------------+-------------+--------------+
| IdProducto | Producto                               | Se Vende en | Se Compra en |
+------------+----------------------------------------+-------------+--------------+
|      42917 | FUNDA PARA NOTEBOOK HP CROSSHATCH 15.6 |    1351.350 |    95989.850 |
+------------+----------------------------------------+-------------+--------------+


/* Conclusiones:
1.- Aunque (excluyendo al 42917) todos los Skus tienen un margen de aprox 30% es muy probable,
    como todo Negocio que existan Productos mas y menos Importantes. Hay que realizar un estudio
    del Profit Individualizado para ver que productos le aportan mas al negocio
    
2.- Aunque el Id 42917 tiene un Margen muy desfavorable Todavia es Temprano para sacar conclusiones
    Es necesario ver el profit de este Sku en Particular y evaluar si lo que ocurre con el fue algo
    `puntual` o por el contrario sea una situación rutinaria, donde entonce se debe prender una alarma      */