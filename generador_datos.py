from faker import Faker
from modelo.estudiante import Estudiante
from modelo.libro import Libro

fake = Faker('es_ES')

def generar_estudiantes(cantidad):
    estudiantes = []
    for _ in range(cantidad):
        estudiante = Estudiante(
            str(fake.random_number(digits=10, fix_len=True)),  # cédula
            fake.first_name(),                                 # nombre
            fake.last_name(),                                  # apellido
            fake.random_element(elements=[
                "Ingeniería en Sistemas",
                "Ingeniería Industrial",
                "Administración",
                "Contabilidad"
            ])  # carrera
        )
        estudiantes.append(estudiante)
    return estudiantes


def generar_libros(cantidad):
    libros = []
    for _ in range(cantidad):
        libro = Libro(
            fake.isbn13(),            # ISBN
            fake.sentence(nb_words=3),# título
            fake.name()               # autor
        )
        libros.append(libro)
    return libros