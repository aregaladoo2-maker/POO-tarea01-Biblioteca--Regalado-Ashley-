<<<<<<< HEAD
# POO-tarea01-Biblioteca--Regalado-Ashley-
=======
NOMBRE: Ashley Mishell Regalado Oroñez 
CARRERA: Ing.de Software
SEMESTRE: 4to Semestre 
                           
                           DOCUMENTACIÓN

Esta estructura contiene :
- personas.py -> En si es la base del sisitema, contine a :
clase persona - que funciona como una clase madre
define datos básicos de cualquier persona como cédula,nombre y apellido
ESTRUCTURA: usa propiedades como @property para leer datos y mmetodo como __str__ para mostrarinformación 

- estudiantes.py -> Define la clase estudiante que herencia de (persona), ademas de lo que herreda añade el atributo carrera
ESTRUCTURA: Llama al constructor de la clase madre mediante super().__init__ para no repetir código. 

Su representación visual incluye los datos de la persona más su carrera universitaria.
- libro.py -> Gestiona el recurso principal (clase)
Almacena el ISBN, título y autor. Incluye un indicador de disponibilidad (_disponible) que por defecto es verdadero.

ESTRUCTURA: Tiene métodos clave como prestar() (cambia estado a falso) y devolver() (cambia estado a verdadero). Su formato de impresión muestra si el libro está "Disponible" o "Prestado"

- prestamo.py -> Este archivo une a los protagonistas mediante la clase Prestamo
Registra qué Libro se le entregó a qué Estudiante, junto con la fecha de salida y la de entrega.

ESTRUCTURA: Maneja un estado activo (_activo). Incluye el método registrar_devolucion(), que marca el préstamo como finalizado y libera el libro automáticamente.
- biblioteca.py -> es el cerebro de todo este caso de estudio 
Registra qué Libro se le entregó a qué Estudiante, junto con la fecha de salida y la de entrega.

- El archivo main.py funciona como el punto de ejecución principal del sistema.
Su rol es integrar todos los módulos que revisamos anteriormente para simular un escenario real de uso en la "Biblioteca Central UNEMI".

- ESTRUCTURA Y CONTENIDO
- INICIALIZACIÓN DEL ENTORNO:
 Importa las clases Libro, Estudiante y Biblioteca para poder crear objetos.

Lo primero que hace es crear la instancia central: 
biblioteca = Biblioteca("Biblioteca Central UNEMI")
Carga de Datos (Fase de Registro):
- LIBROS: 
Instancia 3 libros y los añade al sistema usando registrar_libro

- ESTUDIANTES: 
Crea dos perfiles de estudiantes con sus respectivas cédulas y carreras, registrándolos con registrar_estudiante.

- EJECUCIÓN DE NEGOCIOS :
- PRESTAMOS: 
Llama al método prestar_libro enviando el ISBN del libro, la cédula del estudiante y las fechas de entrega/devolución.

- VALIDACIONES: Intenta prestar un libro que ya está ocupado para demostrar que el sistema arroja un error y protege el inventario.

- DEVOLUCIONES: 
Utiliza el método devolver_libro para liberar un ejemplar y cambiar su estado de "Prestado" a "Disponible".

- CONSULTAS Y REPORTES :
Filtra y muestra en pantalla los préstamos que tiene activos un estudiante específico en diferentes momentos del tiempo.
Imprime el estado de la biblioteca al inicio, durante y al final del proceso para verificar que los contadores de libros y préstamos coincidan.
>>>>>>> ff34d75 (primer commit)
