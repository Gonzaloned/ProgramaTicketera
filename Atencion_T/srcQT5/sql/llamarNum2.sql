BEGIN TRANSACTION;
DECLARE @proximo_turno INT;
DECLARE @caja_llamadora INT;
DECLARE @proximo_tipo INT;

-- Obtener el proximo turno disponible
SELECT TOP (1) @proximo_turno=num, @caja_llamadora=atiende_caja, @proximo_tipo=tipo 
FROM turnos_actual 
WHERE (status=2) 
ORDER BY num        
        
SELECT @proximo_turno, @caja_llamadora, @proximo_tipo

UPDATE turnos_actual SET status = 3 WHERE num=@proximo_turno

COMMIT TRANSACTION;