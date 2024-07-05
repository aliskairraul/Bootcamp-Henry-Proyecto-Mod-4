

/* Nota: La Query a continuacion muestra el Profit acumulativo de los Productos
         (Cantidad * (PrecioVenta-CostoCompra)) de cada Sku, pero no contempla 
         otros costos asociados, como pueden ser Impuestos (No es este el caso,
         pero en ocasiones la naturaleza de los productos hace que paguen impuestos
         distintos), costos de Almacenaje (No es lo mismo el costo de almacenaje de
         un Pendrive al de una Mesa o Centro Gaming), y otros costos asociados (en 
         ocasiones hay mercancias que por su naturaleza los dueños de Negocio prefieren
         pagarles algun tipo de seguro), etc.... */     

/* Nota 2: En el Profit Acumulado el último valor debe llegar a 100% ó (99,algo% por los
            redondeos), En este caso al tener un sku con margen negativo, es normal que supere 
            el 100% y luego el reste profit para llegar a 100.  Cuanto Exceda de 100% es lo que
            nos indicara que tanto afecta ese Sku con Margen Negativo */           

-- Profit acumulado
SELECT IdProducto, Profit, Porcentaje,
       SUM(Porcentaje) OVER 
       (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS Acumulado,
       ROW_NUMBER() OVER () AS NumeroFila
FROM(select v.IdProducto,  
       ROUND(SUM((v.Precio-c.CostoPromedio) * v.Cantidad),2) as Profit,
       ROUND(100 * SUM((v.Precio-c.CostoPromedio) * v.Cantidad) / 
                   SUM(SUM((v.Precio-c.CostoPromedio) * v.Cantidad))
                   OVER(),2) as Porcentaje
FROM venta_detail v
INNER JOIN compra_detail c
ON v.IdProducto = c.IdProducto
GROUP BY 1
ORDER BY 2 DESC ) as subquery
ORDER BY 2 DESC;

/*  173 =======> 273 
     X  =======> 100       el 63% del Profit se lo esta llevando este articulo
    
    Lo del Articulo con el codigo no es un caso puntual aislado ya por la magnitud, se presume
    comportamiento corrupto pero NO SE SABE si en el departamento de Compras o Ventas */  

-- Nota: Evaluo si Ocurre la casualidad de que el producto siempre es vendido por el mismo Proveedor
SELECT cd.IdProducto,
       ch.IdProveedor,    
       pv.Nombre As Proveedor,
       SUM(cd.Cantidad * cd.Precio) as Compra
FROM compra_detail cd
INNER JOIN compra_header ch
  ON ch.IdCompra = cd.IdCompra
INNER JOIN proveedor pv
  ON pv.IdProveedor = ch.IdProveedor  
WHERE cd.IdProducto = 42917
GROUP BY 1,2,3;

+------------+-------------+------------------------+------------+
| IdProducto | IdProveedor | Proveedor              | Compra     |
+------------+-------------+------------------------+------------+
|      42917 |          13 | María Rivarola         | 1733812.50 |
|      42917 |           8 | Sin Dato               | 3583030.60 |
|      42917 |          11 | Via Chile Containers   | 4410722.70 |
|      42917 |           7 | Fletes y Logistica     | 2325309.70 |
|      42917 |           4 | Rivero Insumos         |  401902.70 |
|      42917 |           5 | Laprida Computacion    | 1012587.60 |
|      42917 |           9 | Via Chile Containers   | 3885306.20 |
|      42917 |          14 | Río Full Net           | 1945293.40 |
|      42917 |           2 | San Cirano             | 1827531.20 |
|      42917 |           3 | Bell S.A.              | 2506926.90 |
|      42917 |           6 | Importadora Mann Kloss | 2686412.20 |
|      42917 |          10 | Full Toner             | 1986951.00 |
|      42917 |           1 | Sin Dato               |  395178.40 |
+------------+-------------+------------------------+------------+

SELECT COUNT(*) FROM proveedor; -- 14 Proveedores en Total

/* Nota: El Producto se está Comprando a 13 de los 14 Proveedores de la Cadena,
         Es muy Díficil que todos los Proveedores se pongan de acuerdo para hacer
         un acto de Corrupcion.
         Toca Averiguar El costo y Precio de Mercado del Articulo a ver si lo que 
         ocurre es que mas bien el comportamiento corrupto este en la parte administrativa
         junto con clientes que lleguen a la Tienda a Comprar. */



SELECT vd.IdProducto,
       vh.IdCliente,
       cl.NombreApellido,
       SUM(vd.Cantidad * vd.Precio) as Venta,
       ROUND(100 *SUM(vd.Cantidad * vd.Precio) / SUM(SUM(vd.Cantidad * vd.Precio))
         OVER(),2) as Porcentaje,
         SUM(vd.Cantidad) AS Unidades
FROM venta_detail vd
INNER JOIN venta_header vh
  ON vd.IdVenta = vh.IdVenta
INNER JOIN cliente cl  
  ON cl.IdCliente = vh.IdCliente
WHERE vd.IdProducto = 42917
GROUP BY 1,2,3
ORDER BY 5 DESC;

+------------+-----------+-------------------------------+-----------+------------+----------+
| IdProducto | IdCliente | NombreApellido                | Venta     | Porcentaje | Unidades |
+------------+-----------+-------------------------------+-----------+------------+----------+
|      42917 |      1594 | Julio Halty                   | 36486.450 |       9.28 |       27 |
|      42917 |      2887 | Marcelo Adan De Polsi         | 22972.950 |       5.84 |       17 |
|      42917 |      3245 | Jorge Raul Rodriguez          | 18918.900 |       4.81 |       14 |
|      42917 |       850 | Ana Maria Barajas Rivera      | 13513.500 |       3.44 |       10 |
|      42917 |      1290 | Osvaldo Rodolfo Fernandez     | 13513.500 |       3.44 |       10 |
|      42917 |        39 | Richard Ronald Servan         | 13513.500 |       3.44 |       10 |
|      42917 |      1495 | Luis Eduardo Goggia           | 12162.150 |       3.09 |        9 |
|      42917 |      1453 | Graciela Corina Garin         | 12162.150 |       3.09 |        9 |
|      42917 |       487 | Sallovitz, Francisco A.       | 12162.150 |       3.09 |        9 |
|      42917 |      1195 | Mauricio Cusano               | 10810.800 |       2.75 |        8 |
|      42917 |      3004 | Maria Noel Padron             | 10810.800 |       2.75 |        8 |
|      42917 |       643 | Freddato, Octavio Jose D.     | 10810.800 |       2.75 |        8 |
|      42917 |      2124 | Clever Daniel Montiel         | 10810.800 |       2.75 |        8 |
|      42917 |      1351 | Francisco Fleitas             |  9459.450 |       2.41 |        7 |
|      42917 |       898 | Andres Felipe Muñoz Ceballos  |  9459.450 |       2.41 |        7 |
|      42917 |      1534 | Adriana Maria Gonzalez        |  9459.450 |       2.41 |        7 |
|      42917 |       813 | De Chiaria, Claudio Victor    |  8108.100 |       2.06 |        6 |
|      42917 |      1051 | Felipe Carballo               |  8108.100 |       2.06 |        6 |
|      42917 |       951 | Naileth Montenegro Mendez     |  8108.100 |       2.06 |        6 |
|      42917 |       583 | Aiello, Mario S.              |  8108.100 |       2.06 |        6 |
|      42917 |      2606 | Ruperto Long                  |  6756.750 |       1.72 |        5 |
|      42917 |      1243 | Graciela Beatriz Espina       |  6756.750 |       1.72 |        5 |
|      42917 |       817 | Impini, Luis Fabian           |  6756.750 |       1.72 |        5 |
|      42917 |       388 | Alvarado, Agustin Enrique     |  6756.750 |       1.72 |        5 |
|      42917 |      3143 | Alberto Brause                |  6756.750 |       1.72 |        5 |
|      42917 |       681 | Knichnik, Armando             |  6756.750 |       1.72 |        5 |
|      42917 |      1094 | Juanpablo Cesio               |  5405.400 |       1.37 |        4 |
|      42917 |       437 | Merele, Jorge Marcelo         |  5405.400 |       1.37 |        4 |
|      42917 |      3401 | Maria Eugenia Rolla           |  5405.400 |       1.37 |        4 |
|      42917 |      3392 | Gilberto Rodriguez            |  4054.050 |       1.03 |        3 |
|      42917 |      1408 | Jorge Luis Gamarra            |  4054.050 |       1.03 |        3 |
|      42917 |       953 | Liceth Yurani Quintero Suarez |  4054.050 |       1.03 |        3 |
|      42917 |      2586 | Mario Nelgar Diaz             |  4054.050 |       1.03 |        3 |
|      42917 |      2224 | Luis Eduardo Odriozola        |  4054.050 |       1.03 |        3 |
|      42917 |      1253 | Daniel Esteves                |  4054.050 |       1.03 |        3 |
|      42917 |       789 | Espinoza , Gonzalo Gabriel    |  4054.050 |       1.03 |        3 |
|      42917 |      1794 | Luis Eduardo Raffo            |  4054.050 |       1.03 |        3 |
|      42917 |      2114 | Domingo Antonio Montaldo      |  4054.050 |       1.03 |        3 |
|      42917 |      2854 | Marcelo Daniel Cabral         |  2702.700 |       0.69 |        2 |
|      42917 |       118 | Juan Carlos Souza             |  2702.700 |       0.69 |        2 |
|      42917 |      3405 | Jose Luis Ruocco              |  2702.700 |       0.69 |        2 |
|      42917 |       594 | Bombelli, Juan A.             |  2702.700 |       0.69 |        2 |
|      42917 |      1863 | Maria Del Carmen Roybal       |  2702.700 |       0.69 |        2 |
|      42917 |      1147 | Nery Mauro Corbo              |  2702.700 |       0.69 |        2 |
|      42917 |       674 | Preta, Ricardo A              |  2702.700 |       0.69 |        2 |
|      42917 |       760 | Pineda, Dario Octavio         |  2702.700 |       0.69 |        2 |
|      42917 |       557 | Correa, Gustavo Rafael        |  2702.700 |       0.69 |        2 |
|      42917 |      1782 | Alberto German Queijo         |  2702.700 |       0.69 |        2 |
|      42917 |       368 | Carbone, Juan Carlos          |  2702.700 |       0.69 |        2 |
|      42917 |       407 | Basi, Jose Luis               |  1351.350 |       0.34 |        1 |
|      42917 |      1382 | Heber Freitas                 |  1351.350 |       0.34 |        1 |
|      42917 |      2039 | Gustavo Ricardo Mayola        |  1351.350 |       0.34 |        1 |
|      42917 |      3181 | Leonardo Leon                 |  1351.350 |       0.34 |        1 |
|      42917 |       303 | Edgar Fernando Vignoli        |  1351.350 |       0.34 |        1 |
|      42917 |      1503 | José María Gomez              |  1351.350 |       0.34 |        1 |
|      42917 |        45 | Jonny Barcich Silbermann      |  1351.350 |       0.34 |        1 |
|      42917 |      1625 | Adela Isabel Hounie           |  1351.350 |       0.34 |        1 |
+------------+-----------+-------------------------------+-----------+------------+----------+

/* Nota: El Articulo en cuestion es una FUNDA PARA NOTEBOOK HP CROSSHATCH 15.6, es Atipico
         que personas Naturales (No JURIDICAS o NEGOCIOS) compren mas de 1 UNidad, toca 
         informar al dueño de la Cadena y que el Tome la decision de si desea Investigar
         si existen Nexos entre los primeros de la Lista y sus empleados... 