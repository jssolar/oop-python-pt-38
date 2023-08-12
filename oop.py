class Persona:
    nombre = None
    apellido = None
    rut = None
    
    def __init__(self, nombre, apellido, rut):
        print("Creando una instancia de Persona")
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
    
    def comer(self):
        pass
    
    def saludar(self):
        pass


class Estudiante(Persona):
    _universidad = None
    
    def __init__(self):
        print("Creando una instancia de Estudiante")
    
    def renunciar(self):
        pass


class EstudianteEscolar(Estudiante):
    
    def __init__(self):
        print("Creando una instancia de Estudiante Escolar")
    

persona1 = Persona() # instanciando la clase Persona (objeto)
persona1.nombre = "John"

persona2 = Persona()
persona2.nombre = "Jane"

persona3 = Persona()
persona3.nombre = "Jane"

persona2.saludar()

print(persona1)

estudiante1 = Estudiante()
print(estudiante1)

estEscolar = EstudianteEscolar()
print(estEscolar.renunciar()) 


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def datos(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}"


class Biblioteca:
    def __init__(self, nombre):
          self.nombre = nombre
          self.libros = []
          
    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        
    def mostrar_catalogo(self):
        print("======= Directorio de Libros ========")
        for libro in self.libros:
            print(libro.datos())
            print("---------------------------------")
            
            
    
libro1 = Libro("100 Años de Soledad", "Garcia Marquez, Gabriel")
libro2 = Libro("Don quijote", "Cervantes, Miguel")

print(libro1.datos())
print(libro2.datos())


biblioteca = Biblioteca("Biblioteca Central de Chile")
# Agrego un libro y muestro el catalogo de libros
biblioteca.agregar_libro(libro1)
biblioteca.mostrar_catalogo()

# Agrego un libro y muestro el catalogo de libros
biblioteca.agregar_libro(libro2)
biblioteca.mostrar_catalogo()
