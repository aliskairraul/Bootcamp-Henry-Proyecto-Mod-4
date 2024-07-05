SELECT IdProducto, Precio
FROM compra_detail
GROUP BY 1,2
ORDER BY 1;

/* Se Observa que aunque TODOS los Skus han sido comprados a Varios Precios
   Las Variaciones de los mismos son MUY LEVES, lo cual es un comportamiento
   que se asume como normal ya que pudiera bien atribuirse a 
   .- Descuentos por Volumen en algun momento dado, Tomar en cuenta que pudieran
      haber diversas ESCALAS y por ende diversos DESCUENTOS.
   .- Oferta Estacionaria del Proveedor, que quiera renovar su stock
   .- Ligero incremento por costo de envio, en algun momento que se haya 
      solicitado mercancia con URGENCIA, etc*/


/* Para un Analisi de Margen de Comercializacion o Profit en Ventas se recomienda
   Obtener un Precio Promedio de Compra por Sku, para asi poder facilitar y mejorar 
   el análisis*/

/* Creare unas Columnas Extras que contendran los valores de `compra` individual de cada
   transaccion y una de `costo promedio` del sku */   

-- Creo la columna `Compra`
ALTER TABLE `compra_detail` ADD `Compra` DECIMAL(13,3) DEFAULT 0.00 AFTER `Precio`;

-- lleno a `Compra` con el valor de `Cantidad` * `Precio`
UPDATE compra_detail SET Compra = Cantidad * Precio;

-- Creo La Columna `CostoPromedio`
ALTER TABLE `compra_detail` ADD `CostoPromedio` DECIMAL(13,3) DEFAULT 0.00 AFTER `Compra`;
   
-- Creo una Tabla Auxiliar para comodidad en los calculos
CREATE TABLE `compra_aux` (
  `IdProducto` int DEFAULT NULL,
  `SumaCompra` decimal(15,3) DEFAULT NULL,
  `SumaCantidad` decimal(15,3) DEFAULT NULL,
  `CostoPromedio` decimal(15,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

-- Genero la Informacion Necesaria y la Vacio en la tabla auxiliar
INSERT INTO compra_aux (IdProducto, SumaCompra, SumaCantidad, CostoPromedio)
SELECT IdProducto,       
       SUM(Compra) as SumaCompra, 
       SUM(Cantidad) as SumaCantidad,
       SUM(Compra) / SUM(Cantidad) as CostoPromedio
FROM compra_detail
GROUP BY 1;

SELECT * FROM compra_aux;  -- obtengo los 283 CostosPromedio


/* Traslado esos costos Promedios a la Tabla `compra_detail`*/
UPDATE compra_detail c JOIN compra_aux ca
ON (c.IdProducto = ca.IdProducto)
SET c.CostoPromedio = ca.CostoPromedio;

SELECT IdProducto, CostoPromedio
FROM compra_detail
GROUP BY 1,2
ORDER BY 1;
-- Arroja los 283 Costos Promedios




-- Por ultimo Importante analizar el Peso de los Proveedores
SELECT p.IdProveedor,
       p.Nombre,
       SUM(cd.Cantidad * cd.Precio) as Compra,
       ROUND(100 * SUM(cd.Cantidad * cd.Precio) / SUM(SUM(cd.Cantidad * cd.Precio))
          OVER (),2) AS PORCENTAJE
FROM compra_detail cd 
INNER JOIN compra_header ch 
  ON cd.IdCompra = ch.IdCompra
INNER JOIN proveedor p 
  ON p.IdProveedor = ch.IdProveedor
GROUP BY 1,2
ORDER BY 3 DESC;

+-------------+------------------------+-------------+------------+
| IdProveedor | Nombre                 | Compra      | PORCENTAJE |
+-------------+------------------------+-------------+------------+
|           9 | Via Chile Containers   | 11220344.23 |       9.54 |
|          11 | Via Chile Containers   | 10757888.08 |       9.15 |
|           8 | Sin Dato               | 10488291.33 |       8.92 |
|           3 | Bell S.A.              |  9997136.80 |       8.50 |
|           6 | Importadora Mann Kloss |  9979226.54 |       8.49 |
|           2 | San Cirano             |  8837968.25 |       7.52 |
|          10 | Full Toner             |  8700250.00 |       7.40 |
|           7 | Fletes y Logistica     |  8584865.83 |       7.30 |
|          13 | María Rivarola         |  8494756.31 |       7.23 |
|           5 | Laprida Computacion    |  8035251.34 |       6.83 |
|           4 | Rivero Insumos         |  7007805.61 |       5.96 |
|          12 | Central Rosario SRL    |  6749610.19 |       5.74 |
|          14 | Río Full Net           |  5039489.28 |       4.29 |
|           1 | Sin Dato               |  3672986.28 |       3.12 |
+-------------+------------------------+-------------+------------+
-- No hay Proveedor con Gran Peso
