-- Funciones Sacadas del Homework_Utiles.sql de la Lecture 5
use henry_m3_pandas;

-- PROCEDIMIENTO ALMACENADO QUE SE ENCARGA DE LLENAR EL CALENDARIO.  
-- IMPORTANTISIMO TOMAR SIEMPRE EN CUENTA PARA LOS CALENDARIOS
  DELIMITER $$
  CREATE DEFINER=`root`@`localhost` PROCEDURE `Llenar_dimension_calendario`(IN `startdate` DATE, IN `stopdate` DATE)
    BEGIN
      DECLARE currentdate DATE;
      SET currentdate = startdate;
      WHILE currentdate <= stopdate DO
        INSERT INTO calendario VALUES (
                          YEAR(currentdate)*10000+MONTH(currentdate)*100 + DAY(currentdate),
                          currentdate,
                          YEAR(currentdate),
                          MONTH(currentdate),
                          DAY(currentdate),
                          QUARTER(currentdate),
                          WEEKOFYEAR(currentdate),
                          DATE_FORMAT(currentdate,'%W'),
                          DATE_FORMAT(currentdate,'%M'));
        SET currentdate = ADDDATE(currentdate,INTERVAL 1 DAY);
      END WHILE;
    END$$
  DELIMITER ;

  CALL Llenar_dimension_calendario('2015-01-01', '2020-12-31');