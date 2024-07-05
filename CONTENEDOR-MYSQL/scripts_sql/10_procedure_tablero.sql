TRUNCATE tablero;
TRUNCATE temporal;

DELIMITER $$
DROP PROCEDURE IF EXISTS tablero$$
CREATE PROCEDURE tablero()
BEGIN
    DECLARE perdida FLOAT;
    DECLARE contador_id INT DEFAULT 0;
    DECLARE periodo_var VARCHAR(25);
    DECLARE orden_var INT;
    DECLARE mes_var INT;
    DECLARE anio_var INT;
    DECLARE compras FLOAT;
    DECLARE gastos FLOAT;
    DECLARE ventas FLOAT;
    DECLARE empleado VARCHAR(45);
    DECLARE empleado_venta FLOAT;
    DECLARE empleado_porcentaje FLOAT;
    DECLARE sucursal_mes VARCHAR(45);
    DECLARE sucursal_mes_venta FLOAT;
    DECLARE sucursal_mes_porcentaje FLOAT;
    DECLARE sucursal_anio VARCHAR(45);
    DECLARE sucursal_anio_venta FLOAT;
    DECLARE sucursal_anio_porcentaje FLOAT;
    DECLARE dia_mes VARCHAR(12);
    DECLARE dia_mes_venta FLOAT;
    DECLARE dia_mes_porcentaje FLOAT;
    DECLARE dia_anio VARCHAR(12);
    DECLARE dia_anio_venta FLOAT;
    DECLARE dia_anio_porcentaje FLOAT;
    DECLARE online_mes FLOAT;
    DECLARE presencial_mes FLOAT;
    DECLARE telefono_mes FLOAT;
    DECLARE online_anio FLOAT;
    DECLARE presencial_anio FLOAT;
    DECLARE telefono_anio FLOAT;
    DECLARE venta_outliers FLOAT;
    DECLARE senuelo VARCHAR(20);
    DECLARE senuelo_2 INT;
    DECLARE dias_entrega_ FLOAT;

    -- Llenado de Tabla temporal
     INSERT INTO temporal (periodo, orden, anio, mes)
     SELECT DISTINCT concat(MesNombre," -- ",Anio) as PERIODO,
	   (Anio * 100 + Mes) as ORDEN,
       Anio as ANIO,
       Mes as MES
     FROM calendario
     ORDER BY 2 DESC;

     SET contador_id = (select count(*) from temporal);  
    
	WHILE contador_id >= 1 DO
		-- NO ME ESTA LEYENDO NADA DE LA TABLA `tabla`
	 	  SELECT periodo, anio, mes, orden 
         INTO periodo_var, anio_var, mes_var, orden_var
         FROM temporal  
         WHERE id = contador_id
         limit 1;
	    
    -- Obtengo los Datos del Empleado MES
      SELECT CONCAT(e.IDEmpleado, "-", e.Nombre, " ", e.Apellido) as EMPLEADO, 
                    ROUND(SUM(vd.Cantidad * vd.Precio),2) as VENTA,
                    ROUND(100 * SUM(vd.Cantidad * vd.Precio) / SUM(SUM(vd.Cantidad * vd.Precio))
                      OVER (),2) AS PORCENTAJE 
        INTO empleado, empleado_venta, empleado_porcentaje
        FROM venta_detail vd
        INNER JOIN venta_header vh
          ON vd.IdVenta = vh.IdVenta
        INNER JOIN empleado e
          ON e.IdEmpleado = vh.IdEmpleado  
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) = mes_var
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1;

    -- Obteniendo Compras Acumuladas del año
      SELECT ROUND(SUM(cd.Cantidad * cd.Precio),0) AS COMPRA 
        INTO compras
        FROM compra_detail cd
        INNER JOIN compra_header ch
          ON cd.IdCompra = ch.IdCompra
        WHERE YEAR(ch.Fecha) = anio_var AND MONTH(ch.Fecha) <= mes_var;
      
    -- Obteniendo Gastos Acumuladas del año
      SELECT ROUND(SUM(Monto),0) as GASTO 
        INTO gastos
        FROM gasto
        WHERE YEAR(Fecha) = anio_var AND MONTH(Fecha) <= mes_var;

    -- Obteniendo Ventas Acumuladas del año
      SELECT ROUND(SUM(vd.Cantidad * vd.Precio),0) AS VENTA 
        INTO ventas
        FROM venta_detail vd
        INNER JOIN venta_header vh
          ON vd.IdVenta = vh.IdVenta
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) <= mes_var;


    -- Obteniendo La Sucursal con mas Ventas Dusrante el Mes
      SELECT s.Sucursal as SUCURSAL,  
              ROUND(SUM(vd.Cantidad * vd.Precio),2) as VENTA,
              ROUND(100 * SUM(vd.Cantidad * vd.Precio) / SUM(SUM(vd.Cantidad * vd.Precio))
                OVER (),2) as PORCENTAJE 
        INTO sucursal_mes,
             sucursal_mes_venta,
             sucursal_mes_porcentaje
        FROM venta_detail vd
        INNER JOIN venta_header vh
          ON vd.IdVenta = vh.IdVenta
        INNER JOIN sucursal s 
          ON s.IdSucursal = vh.IdSucursal
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) = mes_var
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1;

    -- Obteniendo La Sucursal con mas Ventas Dusrante lo que va de Año
      SELECT s.Sucursal as SUCURSAL,  
            ROUND(SUM(vd.Cantidad * vd.Precio),2) as VENTA,
            ROUND(100 * SUM(vd.Cantidad * vd.Precio) / SUM(SUM(vd.Cantidad * vd.Precio))
              OVER (),2) as PORCENTAJE 
        INTO sucursal_anio, 
            sucursal_anio_venta,
            sucursal_anio_porcentaje
        FROM venta_detail vd
        INNER JOIN venta_header vh
          ON vd.IdVenta = vh.IdVenta
        INNER JOIN sucursal s 
          ON s.IdSucursal = vh.IdSucursal
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) <= mes_var
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1;

  -- Obteniendo El dia de la Semana que mas Vendio durante el Mes
      SELECT c.DiaNombre as DIA,  
              ROUND(SUM(vd.Cantidad * vd.Precio),2) as VENTA,
              ROUND(100 * SUM(vd.Cantidad * vd.Precio) / SUM(SUM(vd.Cantidad * vd.Precio))
                OVER (),2) as PORCENTAJE 
        INTO dia_mes,
             dia_mes_venta,
             dia_mes_porcentaje
        FROM venta_detail vd
        INNER JOIN venta_header vh
          ON vd.IdVenta = vh.IdVenta
        INNER JOIN calendario c
          ON c.Fecha = vh.Fecha  
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) = mes_var
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1;
                          
  -- Obteniendo El dia de la Semana que mas Vendio durante el Acumulado de Año
      SELECT c.DiaNombre as DIA,  
              ROUND(SUM(vd.Cantidad * vd.Precio),2) as VENTA,
              ROUND(100 * SUM(vd.Cantidad * vd.Precio) / SUM(SUM(vd.Cantidad * vd.Precio))
                OVER (),2) as PORCENTAJE 
        INTO dia_anio,
             dia_anio_venta,
             dia_anio_porcentaje
        FROM venta_detail vd
        INNER JOIN venta_header vh
          ON vd.IdVenta = vh.IdVenta
        INNER JOIN calendario c
          ON c.Fecha = vh.Fecha  
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) <= mes_var
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1;

    -- Venta ONLINE DEL MES
      SELECT cv.Canal as CANAL,
             ROUND(SUM(vd.Cantidad * vd.Precio),2) AS VENTA
        INTO senuelo, online_mes
        FROM venta_detail vd
        INNER JOIN venta_header vh
        ON vd.IdVenta = vh.IdVenta
        INNER JOIN canal_venta cv 
        ON vh.IdCanal = cv.IdCanal
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) = mes_var AND cv.Canal = "OnLine"
        GROUP BY 1;

    -- Venta ONLINE ACUMULADA AÑO
      SELECT cv.Canal as CANAL,
             ROUND(SUM(vd.Cantidad * vd.Precio),2) AS VENTA
        INTO senuelo, online_anio
        FROM venta_detail vd
        INNER JOIN venta_header vh
        ON vd.IdVenta = vh.IdVenta
        INNER JOIN canal_venta cv 
        ON vh.IdCanal = cv.IdCanal
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) <= mes_var AND cv.Canal = "OnLine"
        GROUP BY 1;

    -- Venta PRESENCIAL DEL MES
      SELECT cv.Canal as CANAL,
             ROUND(SUM(vd.Cantidad * vd.Precio),2) AS VENTA
        INTO senuelo, presencial_mes
        FROM venta_detail vd
        INNER JOIN venta_header vh
        ON vd.IdVenta = vh.IdVenta
        INNER JOIN canal_venta cv 
        ON vh.IdCanal = cv.IdCanal
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) = mes_var AND cv.Canal = "Presencial"
        GROUP BY 1;

    -- Venta PRESENCIAL ACUMULADA AÑO
      SELECT cv.Canal as CANAL,
             ROUND(SUM(vd.Cantidad * vd.Precio),2) AS VENTA
        INTO senuelo, presencial_anio
        FROM venta_detail vd
        INNER JOIN venta_header vh
        ON vd.IdVenta = vh.IdVenta
        INNER JOIN canal_venta cv 
        ON vh.IdCanal = cv.IdCanal
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) <= mes_var AND cv.Canal = "Presencial"
        GROUP BY 1;    

    -- Venta TELEFONO DEL MES
      SELECT cv.Canal as CANAL,
             ROUND(SUM(vd.Cantidad * vd.Precio),2) AS VENTA
        INTO senuelo, telefono_mes
        FROM venta_detail vd
        INNER JOIN venta_header vh
        ON vd.IdVenta = vh.IdVenta
        INNER JOIN canal_venta cv 
        ON vh.IdCanal = cv.IdCanal
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) = mes_var AND cv.Canal = "Telefónica"
        GROUP BY 1;

    -- Venta TELEFONO ACUMULADA AÑO
      SELECT cv.Canal as CANAL,
             ROUND(SUM(vd.Cantidad * vd.Precio),2) AS VENTA
        INTO senuelo, telefono_anio
        FROM venta_detail vd
        INNER JOIN venta_header vh
        ON vd.IdVenta = vh.IdVenta
        INNER JOIN canal_venta cv 
        ON vh.IdCanal = cv.IdCanal
        WHERE YEAR(vh.Fecha) = anio_var AND MONTH(vh.Fecha) <= mes_var AND cv.Canal = "Telefónica"
        GROUP BY 1;

     -- Venta Outliers Acumulado
      SELECT YEAR(Fecha) as Anio, 
             SUM(Precio * Cantidad) as Venta
        INTO senuelo_2, venta_outliers
        FROM venta_outliers
        WHERE YEAR(Fecha) = anio_var AND MONTH(Fecha) <= mes_var
        GROUP BY 1;

      -- Perdida Acumulada durante el año a Causa del Producto 42917
      SELECT c.IdProducto, 
             SUM(c.Cantidad * c.Precio) as Perdida
        INTO senuelo_2, perdida     
        FROM compra_detail c
        INNER JOIN compra_header ch
        ON ch.IdCompra = c.IdCompra
        WHERE c.IdProducto = 42917 AND YEAR(ch.Fecha) = anio_var AND MONTH(ch.Fecha) <= mes_var
        GROUP BY 1; 

      -- Promedio de Dias de Entrega en el mes
      SELECT SUM(TiempoEntrega) / 
             (SELECT COUNT(*) FROM despacho
              WHERE anio = anio_var AND mes = mes_var) AS TiempoPromedio
        INTO dias_entrega_      
        FROM despacho
        WHERE anio = anio_var AND mes = mes_var;  


   Insert into tablero(orden, periodo, mes, anio, empleado_mes, empleado_mes_venta, empleado_mes_porcentaje,
                       ventas, compras, gastos, dia_mes, dia_mes_venta, dia_mes_porcentaje, dia_anio,
                       dia_anio_venta, dia_anio_porcentaje, sucursal_mes, sucursal_mes_venta, sucursal_mes_porcentaje,
                       sucursal_anio, sucursal_anio_venta, sucursal_anio_porcentaje, online_mes, online_anio,
                       presencial_mes, presencial_anio, telefono_mes, telefono_anio, ventas_outliers, perdida_42917, dias_entrega)
            VALUES(orden_var, periodo_var, mes_var, anio_var, empleado, empleado_venta, empleado_porcentaje, 
                   ventas, compras, gastos, dia_mes, dia_mes_venta, dia_mes_porcentaje, dia_anio,
                   dia_anio_venta, dia_anio_porcentaje, sucursal_mes, sucursal_mes_venta, sucursal_mes_porcentaje,
                   sucursal_anio, sucursal_anio_venta,sucursal_anio_porcentaje, online_mes, online_anio, 
                   presencial_mes, presencial_anio, telefono_mes, telefono_anio, venta_outliers, perdida, dias_entrega_);     
        
        SET contador_id = contador_id - 1;
    END WHILE;
END $$
DELIMITER ;

CALL tablero();