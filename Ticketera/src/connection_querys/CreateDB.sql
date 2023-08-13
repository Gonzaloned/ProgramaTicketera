
CREATE TABLE Persona(
  nombre varchar,
  usuario varchar primary key,
  pass varchar,
)

CREATE TABLE turnos_global (
  dni integer,
  hora timestamp,
  primary key(dni, hora),
  tipo integer,
  atiende_nombre varchar,
  FOREIGN KEY(atiende_nombre) REFERENCES Persona(usuario)
)


CREATE TABLE turnos_actual(
  dni integer,
  num integer primary key identity(1,1),
  hora timestamp,
  tipo integer,
  atiende_nombre varchar,
  FOREIGN KEY(atiende_nombre) REFERENCES Persona(usuario),
  status integer, /* creado, 2 llamado, 3 mostrado, 4 retirado.*/

)

