
CREATE TABLE Persona(
  nombre varchar(30),
  usuario varchar(10) primary key,
  pass varchar(max),
)

CREATE TABLE turnos_global (
  dni int,
  hora datetime,
  primary key(dni, hora),
  tipo int,
  atiende_usuario varchar(10),
  FOREIGN KEY(atiende_usuario) REFERENCES Persona(usuario)
)


CREATE TABLE turnos_actual(
  dni int,
  num int primary key identity(1,1),
  hora datetime,
  tipo int,
  atiende_usuario varchar(10),
  FOREIGN KEY(atiende_usuario) REFERENCES Persona(usuario),
  status int, /* creado, 2 llamado, 3 mostrado, 4 retirado.*/

)
