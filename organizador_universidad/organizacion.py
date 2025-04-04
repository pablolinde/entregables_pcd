from persona import Profesor, Alumno

class Asignatura:

    def __init__(self, nombre, creditos=6):
        '''Iniciamos la clase Asignatura'''
        self.nombre_as = nombre 
        self.creditos = creditos 
        self.profesore_as = []   
        self.alumnos = [] 

    def asignatura_añadir(self, persona):
        """Agrega un profesor o alumno a la asignatura"""
        if persona not in self.profesore_as and persona not in self.alumnos:
            if isinstance(persona, Alumno):
                self.alumnos.append(persona)
            elif isinstance(persona, Profesor):
                self.profesore_as.append(persona)

    def asignatura_quitar(self, persona):
        """Agrega un profesor o alumno a la asignatura"""
        if isinstance(persona, Alumno) and persona in self.alumnos:
            self.alumnos.remove(persona)
        elif isinstance(persona, Profesor) and persona in self.profesore_as:
            self.profesore_as.remove(persona)
        
    def mostrar_profesores(self):
        """Muestra los profesores de esta asignatura"""
        a='Los profesores de ' + self.nombre_as + ' son:'
        for p in self.profesore_as:
            a += '\n'
            a += p.nombre_per
        return a
    
    def mostrar_alumnos(self):
        """Muestra los alumnos de esta asignatura"""
        a='Los alumnos matriculados de ' + self.nombre_as + ' son:'
        for p in self.alumnos:
            a += '\n'
            a += p.nombre_per
        return a
    
    def __str__(self):
        """Habilita el print"""
        salida=''
        salida += 'Nombre: '+ self.nombre_as
        salida += ', créditos: ' + str(self.creditos)
        salida += ', (Profesores: '
        salida += ', '.join([str(p.nombre_per) for p in self.profesore_as]) + ')'
        salida += ', (Alumnos: '
        salida += ', '.join([str(p.nombre_per) for p in self.alumnos]) + ')'
        return salida

#----------------------------------------------
    
class Departamento:

#    departamentos = [DIS, DITEC, DIS]
    def __init__(self, nombre):
#       if nombre not in Departamento.departamentos:
#           raise ValueError("El departamento no existe. Departamentos existentes: DIIC, DITEC, DIS")
        self.nombre_dep = nombre
        self.profesores_dep = []
        
    def departamento_añadir(self, persona):
        """Agrega un profesor al departamento."""
        if persona in self.profesores_dep:
            print ("El profesor ya pertenecia al departamento")
        elif isinstance(persona, Profesor):
            self.profesores_dep.append(persona)
        else:
            print('El objeto no es una instancia de profesor')
        
    def departamento_quitar(self, persona):
        """Quita un profesor del departamento."""
        if isinstance(persona, Profesor):
            if persona in self.profesores_dep:
                self.profesores_dep.remove(persona)
            else:
                print('Esa persona no se encuentra en este departamento')
        else:
            print('El objeto no es una instancia de profesor')
        
    def __str__(self):
        """Habilita el print"""
        salida=''
        salida += 'Nombre: '+ self.nombre_dep
        salida += ', (Profesores: '
        salida += ', '.join([str(p.nombre_per) for p in self.profesores_dep]) + ')'
        return salida