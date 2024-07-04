-- Crear la base de datos
CREATE DATABASE Escuela;

-- Usar la base de datos
USE Escuela;

-- Crear las tablas
CREATE TABLE Estudiantes (
    EstudianteID INT PRIMARY KEY,
    Nombre NVARCHAR(50),
    Apellido NVARCHAR(50),
    FechaNacimiento DATE
);

CREATE TABLE Profesores (
    ProfesorID INT PRIMARY KEY,
    Nombre NVARCHAR(50),
    Apellido NVARCHAR(50),
    Especialidad NVARCHAR(50)
);

CREATE TABLE Cursos (
    CursoID INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Descripcion NVARCHAR(255),
    ProfesorID INT,
    FOREIGN KEY (ProfesorID) REFERENCES Profesores(ProfesorID)
);

CREATE TABLE Asignaturas (
    AsignaturaID INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Creditos INT,
    CursoID INT,
    FOREIGN KEY (CursoID) REFERENCES Cursos(CursoID)
);

CREATE TABLE Clases (
    ClaseID INT PRIMARY KEY,
    Aula NVARCHAR(10),
    HoraInicio TIME,
    HoraFin TIME,
    AsignaturaID INT,
    FOREIGN KEY (AsignaturaID) REFERENCES Asignaturas(AsignaturaID)
);

CREATE TABLE Horarios (
    HorarioID INT PRIMARY KEY,
    DiaSemana NVARCHAR(20),
    HoraInicio TIME,
    HoraFin TIME,
    ClaseID INT,
    FOREIGN KEY (ClaseID) REFERENCES Clases(ClaseID)
);

CREATE TABLE Departamentos (
    DepartamentoID INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Ubicacion NVARCHAR(100)
);

CREATE TABLE Grados (
    GradoID INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Duracion INT,
    DepartamentoID INT,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamentos(DepartamentoID)
);

CREATE TABLE Matriculas (
    MatriculaID INT PRIMARY KEY,
    EstudianteID INT,
    CursoID INT,
    FechaMatricula DATE,
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(EstudianteID),
    FOREIGN KEY (CursoID) REFERENCES Cursos(CursoID)
);

CREATE TABLE Evaluaciones (
    EvaluacionID INT PRIMARY KEY,
    EstudianteID INT,
    AsignaturaID INT,
    Nota DECIMAL(5, 2),
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(EstudianteID),
    FOREIGN KEY (AsignaturaID) REFERENCES Asignaturas(AsignaturaID)
);

CREATE TABLE Asistencias (
    AsistenciaID INT PRIMARY KEY,
    EstudianteID INT,
    Fecha DATE,
    Presente BIT,
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(EstudianteID)
);

CREATE TABLE Pagos (
    PagoID INT PRIMARY KEY,
    EstudianteID INT,
    Monto DECIMAL(10, 2),
    FechaPago DATE,
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(EstudianteID)
);

CREATE TABLE Bibliotecas (
    BibliotecaID INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Ubicacion NVARCHAR(100)
);

CREATE TABLE Libros (
    LibroID INT PRIMARY KEY,
    Titulo NVARCHAR(100),
    Autor NVARCHAR(50),
    AnioPublicacion INT,
    BibliotecaID INT,
    FOREIGN KEY (BibliotecaID) REFERENCES Bibliotecas(BibliotecaID)
);
SELECT * FROM Clases
-- Poblaci�n inicial de datos (opcional)
INSERT INTO Estudiantes VALUES (1, 'Juan', 'P�rez', '2000-01-01');
INSERT INTO Profesores VALUES (1, 'Ana', 'Garc�a', 'Matem�ticas');
INSERT INTO Cursos VALUES (1, 'Matem�ticas B�sicas', 'Introducci�n a las matem�ticas', 1);
INSERT INTO Asignaturas VALUES (1, '�lgebra', 4, 1);
INSERT INTO Clases VALUES (1, 'A101', '08:00:00', '10:00:00', 1);
INSERT INTO Horarios VALUES (1, 'Lunes', '08:00:00', '10:00:00', 1);
INSERT INTO Departamentos VALUES (1, 'Ciencias', 'Edificio A');
INSERT INTO Grados VALUES (1, 'Licenciatura en Matem�ticas', 4, 1);
INSERT INTO Matriculas VALUES (1, 1, 1, '2023-01-15');
INSERT INTO Evaluaciones VALUES (1, 1, 1, 95.5);
INSERT INTO Asistencias VALUES (1, 1, '2023-01-20', 1);
INSERT INTO Pagos VALUES (1, 1, 500.00, '2023-01-05');
INSERT INTO Bibliotecas VALUES (1, 'Biblioteca Central', 'Edificio B');
INSERT INTO Libros VALUES (1, 'Matem�ticas para Todos', 'John Doe', 2010, 1);
