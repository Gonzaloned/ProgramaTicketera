BEGIN TRANSACTION;
DECLARE @advice_num INT;

-- Obtener el proximo turno disponible

SELECT TOP (1) @advice_num=num 
FROM advice
ORDER BY num        
        
SELECT @advice_num

DELETE  FROM advice WHERE 

COMMIT TRANSACTION;
