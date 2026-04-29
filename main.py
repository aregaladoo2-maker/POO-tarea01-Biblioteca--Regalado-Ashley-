from generador_datos import generar_estudiantes, generar_libros
from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca


def main():
    #Crear la biblioteca
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")
    print(f"\n{biblioteca}\n")

    #  GENERAR 100 LIBROS Y ESTUDIANTES CON FAKER
    estudiantes_fake = generar_estudiantes(100)
    libros_fake = generar_libros(100)

    # Agregar estudiantes fake
    for e in estudiantes_fake:
        biblioteca.registrar_estudiante(e)

    # Agregar libros fake
    for l in libros_fake:
        biblioteca.registrar_libro(l)

    print("\n── Datos generados automáticamente ──")
    print(f"Estudiantes generados: {len(estudiantes_fake)}")
    print(f"Libros generados: {len(libros_fake)}")

    # Registrar libros manuales 
    print("\n── Registrando libros ──")
    libro1 = Libro("978-0-13-468599-1", "El Principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("978-0-06-112008-4", "Cien Años de Soledad", "Gabriel García Márquez")
    libro3 = Libro("978-84-376-0494-7", "Don Quijote de la Mancha", "Miguel de Cervantes")

    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_libro(libro3)

    # Registrar estudiantes manuales 
    print("\n── Registrando estudiantes ──")
    est1 = Estudiante("0926400615", "Mishell", "Regalado", "Ingeniería en Sistemas")
    est2 = Estudiante("0912345678", "Israel", "Molina", "Ingeniería Industrial")

    biblioteca.registrar_estudiante(est1)
    biblioteca.registrar_estudiante(est2)

    print(f"\n{biblioteca}\n")

    # Realizar préstamos
    print("── Realizando préstamos ──")
    resultado = biblioteca.prestar_libro(
        "978-0-13-468599-1", "0926400615", "2026-04-15", "2026-04-29"
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        "978-0-06-112008-4", "0926400615", "2026-04-15", "2026-05-01"
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        "978-84-376-0494-7", "0912345678", "2026-04-15", "2026-04-22"
    )
    print(resultado)

    print("\n── Intentando prestar libro ya prestado ──")
    resultado = biblioteca.prestar_libro(
        "978-0-13-468599-1", "0912345678", "2026-04-16", "2026-04-30"
    )
    print(resultado)

    print("\n── Préstamos activos ──")
    prestamos = biblioteca.consultar_prestamos_activos("0926400615")
    for p in prestamos:
        print(f"  → {p}")

    print("\n── Devolviendo un libro ──")
    resultado = biblioteca.devolver_libro("978-0-13-468599-1", "0926400615")
    print(resultado)

    print("\n── Estado final ──")
    print(f"{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()