SELECT COUNT(*) FROM Producto; --283 Productos

SELECT COUNT(DISTINCT(IdProducto)) FROM venta_detail; --283 Productos

SELECT IdProducto, Precio
FROM venta_detail
GROUP BY 1,2
ORDER BY 1;
/* En el Resultado se aprecia Claramente que TODOS LOS SKUs de la cadena 
   reportan irregularidades de Precio. Especificamente se observan Ventas en
   TODOS los SKUs donde el Precio es 100 veces el que corresponde.
   SE SOSPECHA
   1.- Poco probable que los clientes hayan pagado 100 Veces lo que cuesta algo,
       y al observarse que no son pocos los errores si no que son TODOS los SKUs
       hace pensar el error haya sido deliverado.
       .- Investigar a profundidad y con mucha discrecion si ese dinero Realmente entro en tienda
       .- Para el caso de Estudio se asumirá que no entro en tienda, y se corregiran 
          los precios, pero antes se debe hacer una tabla backup de como estaba la original 
       .- Tambien se observó que si se excluyen del estudio los casos donde los precioos se multiplicaron
          por 100, no se observa otro cambio en los precios y que los precios coinciden al 100% 
          con los de la tabla `producto` */
         

-- Creacion de la Tabla Backup
CREATE TABLE `henry_mod4`.`venta_detail_backup` (
  `IdVenta` INT NULL,
  `IdProducto` INT NULL,
  `Precio` DECIMAL(15,3) NULL,
  `Cantidad` INT NULL);

-- Llenado de la Tabla Backup
INSERT INTO venta_detail_backup (IdVenta, IdProducto, Precio, Cantidad)
SELECT IdVenta, IdProducto, Precio, Cantidad
FROM venta_detail;

SELECT COUNT(*) FROM venta_detail_backup; --46645 Registros

-- Se Corrigen Los Precios en la Tabla Venta Para un analisis mas objetivo
UPDATE venta_detail v JOIN producto p
ON (v.IdProducto = p.IdProducto)
SET v.Precio = p.Precio;

SELECT IdProducto, Precio
FROM venta_detail
GROUP BY 1,2
ORDER BY 1;
/* El resultado retorno 283 filas que es lo correcto ya que no hubo variacion 
   en los precios de "venta" durante el periodo de estudio  */