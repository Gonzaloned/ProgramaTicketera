DECLARE @proximo_tipo INT;
DECLARE @numero INT;
DECLARE @advice_num INT;

-- ESTA QUERY DEVUELVE EL PROXIMO NUMERO y EL TIPO
SELECT TOP (1) @proximo_tipo=t.tipo, @numero=t.num
FROM turnos_actual t INNER JOIN advice a ON t.num=a.num
WHERE (status=2) ORDER BY t.num;


-- ESTA DEVUELVE EL CONTADOR ESPECIFICO DEL TIPO Y LO GUARDA EN @advice_num

IF @proximo_tipo=1
    SELECT TOP (1) @advice_num=contador_tipo_CT 
    FROM turnos_actual 
    WHERE (status=2) 
    ORDER BY num;
ELSE
    SELECT TOP (1) @advice_num=contador_tipo_ST 
    FROM turnos_actual 
    WHERE (status=2) 
    ORDER BY num;    

-- Eliminar aviso
DELETE  FROM advice WHERE num=@numero;

SELECT @advice_num;