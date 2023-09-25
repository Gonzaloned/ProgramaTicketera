BEGIN TRANSACTION

--REGISTRAR USUARIO
INSERT INTO Persona(nombre,usuario,pass) VALUES('gonzalo','zalito','Seguridad123');

COMMIT TRANSACTION


BEGIN TRANSACTION

--LOGIN ATTEMPT RESPONSE
DECLARE @status INT;

SELECT TOP (1) @status=usuario
FROM Persona
WHERE (usuario='zalito' and pass='Seguridad123')

if (@status <> null) THEN @STATUS='True';

COMMIT TRANSACTION


