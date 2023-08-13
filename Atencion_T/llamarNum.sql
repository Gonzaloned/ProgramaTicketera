BEGIN TRANSACTION;

DECLARE @proximo_turno INT;

-- Obtener el próximo turno disponible

SELECT TOP (1) @proximo_turno=num 
FROM turnos_actual 
WHERE (status=1 and tipo=2) 
ORDER BY hora

-- Asignar el turno a una persona específica (supongamos que la persona tiene el ID 1)
        
UPDATE turnos_actual 
SET status = 2
WHERE num = @proximo_turno;

COMMIT TRANSACTION;
