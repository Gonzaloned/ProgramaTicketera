INSERT INTO historial_turnos(dni,hora,tipo,atiende_usuario) 
SELECT a.dni,a.hora,a.tipo,a.atiende_usuario FROM turnos_actual a

DELETE FROM historial_turnos
