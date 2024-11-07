# Proyecto Ética y Seguridad de Datos - Privacidad

---

## A. Clasificación de los Datos de Empleados

### 1. Datos Personales
- **FirstName**: Nombre del empleado.
- **LastName**: Apellido del empleado.
- **DOB**: Fecha de nacimiento.
- **Email**: Dirección de correo electrónico.
- **GenderCode**: Código de género.
- **RaceDesc**: Descripción de la raza.
- **MaritalDesc**: Descripción del estado civil.
- **EmpID**: ID único del empleado.

### 2. Datos Sensibles
- **Password**: Contraseña del empleado (datos de seguridad).
- **Performance Score**: Puntuación de desempeño.
- **Current Employee Rating**: Calificación del empleado.

### 3. Datos Públicos
- **EmployeeType**: Tipo de empleado (puede ser público, como si es permanente o temporal).
- **PayZone**: Zona de pago (aunque se puede considerar público en algunos contextos, es mejor manejarlo con cierta confidencialidad dependiendo de la empresa).
- **DepartmentType**: Tipo de departamento (también puede ser considerado público, dependiendo del contexto organizacional).
- **JobFunctionDescription**: Descripción del puesto de trabajo (aunque es información general, podría ser accesible públicamente dentro de la empresa).

### 4. Datos Confidenciales
- **monthly_salary**: Salario mensual (considerado confidencial debido a su naturaleza económica).

## B. Técnicas de Privacidad 

1. **Pseudonimización**:
   - **Nombres**: Se reemplazaron por "Empleado" seguido de su ID.
   - **Correos electrónicos**: Enmascarada la parte local, manteniendo el dominio.

2. **Eliminación de datos sensibles**:
   - Se eliminaron columnas como `LastName`, `JobFunctionDescription` y `Title` para reducir riesgos de identificación.

3. **Mapeo y anonimización de categorías**:
   - Variables como `EmployeeType`, `PayZone`, `GenderCode`, `Performance Score`, `RaceDesc`, y `MaritalDesc` fueron mapeadas a valores más generales o codificados.

4. **Agregación de edad**:
   - La fecha de nacimiento fue convertida en rangos de edad, evitando la divulgación de la edad exacta.

5. **Privacidad diferencial**:
   - Se utilizó el algoritmo Laplaciano para calcular el salario promedio (`BoundedMean`), añadiendo ruido controlado para proteger la privacidad de los salarios individuales.

Estas técnicas permiten procesar y analizar los datos de empleados manteniendo su privacidad y utilidad para análisis.

