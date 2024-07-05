/* Tomando en cuenta que las ventas vienen individualizadas por Producto 
   es decir: Si un cliente compra 5 productos en una tienda genera 5 ventas
   creo conveniente adoptar un nuevo término "Despacho" donde se incluyan
   a todas las ventas de la MISMA FECHA donde este involucrado el mismo
   IdCliente*/

/* Partiendo de la Suposicion de que los pedidos que representen un Outlier 
   o venta importante, se les prestara especial atencion Basare el estudio en
   los despachos del dia a dia.  
   
Store Procedures asociados al analisis
   1.- llenar_dimension_calendario
       Crea un calendario completo para el periodo en estudio
   2.- create_venta_outliers 
       Llena las tablas venta_outliers y venta_sin_outliers (Tablas para analisis) 
   3.- despacho    
       Llena la tabla despacho */

-- Estructura tabla despacho
+---------------+----------------+------+-----+---------+----------------+
| Field         | Type           | Null | Key | Default | Extra          |
+---------------+----------------+------+-----+---------+----------------+
| IdDespacho    | int            | NO   | PRI | NULL    | auto_increment |
| IdSucursal    | int            | NO   |     | NULL    |                |
| Sucursal      | varchar(45)    | NO   |     | NULL    |                |
| IdCliente     | int            | NO   |     | NULL    |                |
| FechaPedido   | date           | NO   |     | NULL    |                |
| FechaEntrega  | date           | NO   |     | NULL    |                |
| TiempoEntrega | int            | NO   |     | NULL    |                |
| Venta         | decimal(15,2)  | NO   |     | NULL    |                |
| LongitudIni   | decimal(13,10) | NO   |     | NULL    |                |
| LatitudIni    | decimal(13,10) | NO   |     | NULL    |                |
| LongitudFinal | decimal(13,10) | NO   |     | NULL    |                |
| LatitudFinal  | decimal(13,10) | NO   |     | NULL    |                |
| Distancia     | int            | NO   |     | NULL    |                |
| anio          | int            | NO   |     | NULL    |                |
| mes           | int            | NO   |     | NULL    |                |
| HoverInf      | varchar(150)   | NO   |     | NULL    |                |
+---------------+----------------+------+-----+---------+----------------+

SELECT SUM(TiempoEntrega) / 
(SELECT COUNT(*) FROM despacho) AS TiempoPromedio
FROM despacho;
-- 4.8594 Casi 5 dias es el promedio de Domora en La entregas



SELECT COUNT(*) /
       (SELECT COUNT(*) FROM despacho) 
       AS Porcentaje_Pedidos
FROM despacho
WHERE Distancia < 2000 and Venta <= 10000;
-- Resultado 0.7897 
-- 78.97% de los pedidos (casi 80%) estan en un rango de 2KM 
-- Con un Valor de Menos de 10000 Pesos. 
-- Se DEBERIA PROPONER ESTABLECER UNA POLITICA DE DESPACHOS 
-- CAMINANDO PARA MEJORAR LA METRICA

-- Se debe Proponer empezar a medir el CHURN RATE en la Cadena
-- Es probable que esta Demora este afectando la fidelidad de los
-- clientes para con la tienda 






SELECT SUM(TiempoEntrega) / 
(SELECT COUNT(*) FROM despacho
WHERE anio = 2018 AND mes = 4) AS TiempoPromedio
FROM despacho
WHERE anio = 2018 AND mes = 4;
-- Esta query nos dara el indicativo de Tiempo Promedio de dias que tardan en despachar
-- un pedido en un mes determinado