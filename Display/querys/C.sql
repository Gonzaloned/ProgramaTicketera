BEGIN TRANSACTION;
DECLARE @proximo_turno INT;
DECLARE @caja_llamadora INT;
DECLARE @proximo_tipo INT;
DECLARE @num_llamado INT;

-- Obtener proximo tipo
SELECT TOP (1) @proximo_tipo=tipo 
FROM turnos_actual 
WHERE (status=2) ORDER BY num  

-- Obtener el proximo turno disponible
IF @proximo_tipo=1
    SELECT TOP (1) @proximo_turno=contador_tipo_CT, @caja_llamadora=atiende_caja, @proximo_tipo=tipo, @num_llamado=num 
    FROM turnos_actual 
    WHERE (status=2) 
    ORDER BY num
ELSE
    SELECT TOP (1) @proximo_turno=contador_tipo_ST, @caja_llamadora=atiende_caja, @proximo_tipo=tipo, @num_llamado=num 
    FROM turnos_actual 
    WHERE (status=2) 
    ORDER BY num         
        
SELECT @proximo_turno, @caja_llamadora, @proximo_tipo

UPDATE turnos_actual SET status = 3 WHERE num=@num_llamado

COMMIT TRANSACTION;