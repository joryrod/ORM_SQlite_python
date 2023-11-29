import orm
from Tablas.Autores import Autores
from Tablas.Libros import Libros
from Tablas.Usuarios import Usuarios

db=orm.SQLiteORM("db_Biblioteca")
db.crear_tabla(Autores)
db.crear_tabla(Libros)
db.crear_tabla(Usuarios)

# autor_uno={"dni":78451296,"nombre":"quevedo","apellidos":"escoja de los rios"}
# db.insertarUno("Autores",autor_uno)

usuarios_varios=[
    {
        "dni":215474896,
        "nombre":"nadine",
        "apellidos":"ortiz",
        "f_nacimiento":"16/05/2000",
        "estado":"activo"
    },
    {
        "dni":24578963,
        "nombre":"Orlando",
        "apellidos":"lopez",
        "f_nacimiento":"28/06/2001",
        "estado":"activo"
    },
    {
        "dni":32654789,
        "nombre":"mochi",
        "apellidos":"peñafiel",
        "f_nacimiento":"04/06/2002",
        "estado":"activo"
    },
    {
        "dni":98745621,
        "nombre":"edwin",
        "apellidos":"ramos",
        "f_nacimiento":"19/08/1999",
        "estado":"inactivo"
    },
    {
        "dni":98652374,
        "nombre":"yayira",
        "apellidos":"de araña",
        "f_nacimiento":"509 a.c",
        "estado":"momia"
    }
    ]
# db.insertarVarios("Usuarios",usuarios_varios)

# print(db.mostrar("Usuarios"))
# # muestra lista de tuplas
# print(db.mostrar("Usuarios",type="objeto"))
# # muestra un obgeto con sus campos y sus valores
# print(db.mostrar("Usuarios",where="estado='momia'",type="objeto")) 
# # tambien se puede filtrar informacion
# print(db.mostrar("Usuarios",where="nombre LIKE 'ed%'",type="objeto")) 
# # tambien se puede filtrar informacion
# print(db.mostrar("Usuarios",where="dni = 24578963",type="objeto")) 
# # tambien se puede filtrar informacion

# db.actualizar("Usuarios",{"estado":"activo"},where="nombre='yayira'")
# dato_actualizar={"nombre":"yadira","apellidos":"ya es salida"}
# db.actualizar("Usuarios",dato_actualizar,where="dni=98652374")
db.eliminar("Usuarios",where="nombre='mochi'")
db.eliminar("Usuarios",where="dni=98745621")

print(db.mostrar("Usuarios",type="objeto"))