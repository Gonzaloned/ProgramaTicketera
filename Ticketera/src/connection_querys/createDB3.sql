
CREATE TABLE Persona(
  nombre varchar(30),
  usuario varchar(10) primary key,
  pass varchar(max),
)

CREATE TABLE historial_turnos (
  dni int,
  hora datetime,
  tipo int,
  atiende_usuario varchar(10),
  FOREIGN KEY(atiende_usuario) REFERENCES Persona(usuario)
)


CREATE TABLE turnos_programados(
  dni int,
  num int primary key identity(1,1),
  hora datetime,
  tipo int,
  atiende_usuario varchar(10),
  atiende_caja int,
  FOREIGN KEY(atiende_usuario) REFERENCES Persona(usuario),
  status int, /* creado, 2 llamado, 3 mostrado, 4 retirado.*/

)

CREATE TABLE turnos_llegada(
  dni int,
  num int primary key identity(1,1),
  hora datetime,
  tipo int,
  atiende_usuario varchar(10),
  atiende_caja int,
  FOREIGN KEY(atiende_usuario) REFERENCES Persona(usuario),
  status int, /* creado, 2 llamado, 3 mostrado, 4 retirado.*/

)

CREATE TABLE video(
	num int primary key identity(1,1),
	ipnum varchar(max),
	dir varchar(max)
)

CREATE TABLE advice(
	num int primary key,
	hora datetime
)