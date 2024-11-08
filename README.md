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

---

## B. Técnicas de Privacidad - Datos

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
   - 
![image](https://github.com/user-attachments/assets/d47d1846-0d75-46e0-af3d-90618425e111)

Estas técnicas permiten procesar y analizar los datos de empleados manteniendo su privacidad y utilidad para análisis.

---

## C. Funcionalidades de Privacidad en SalaryBoost

1. **Empleado / "Modificar Contraseña"**:
   - La opción de **modificar contraseña** permite a los empleados gestionar su acceso de manera autónoma, garantizando que solo ellos puedan acceder a sus cuentas. Este control sobre sus credenciales es fundamental para proteger la privacidad de los datos personales y de acceso, alineándose con principios de autonomía y control del usuario que establece el Reglamento General de Protección de Datos (RGPD).
   
2. **Supervisor / "Modificar Datos de Empleados"**:
   - La funcionalidad de **modificar datos de empleados** permite actualizar la información personal de los empleados bajo su solicitud. Esto es importante porque **SalaryBoost** permite que los empleados mantengan sus datos actualizados, lo que es un derecho protegido bajo el RGPD. Los empleados pueden corregir o actualizar cualquier dato erróneo o desactualizado, lo que garantiza que los registros sean precisos y conforme a los principios de integridad y exactitud de los datos.

3. **Supervisor / "Eliminar Empleado"**:
   - Cuando un empleado deja la empresa, **SalaryBoost** ofrece la opción de **eliminar sus datos**. Este procedimiento es crucial para cumplir con el principio de **limitación del almacenamiento** del RGPD, que estipula que los datos personales deben ser eliminados cuando ya no sean necesarios para el propósito para el cual fueron recopilados. Así, se asegura que los datos de los empleados no se mantengan en la plataforma una vez que ya no sean pertinentes, reduciendo el riesgo de exposición de información sensible.

4. **Supervisor / "Modificar Contraseña"**:
   - Los supervisores también pueden modificar la contraseña de un empleado, lo cual puede ser útil para situaciones de seguridad o cuando un empleado olvida sus credenciales. Esto asegura que el acceso al sistema se mantenga controlado y seguro. Esta función está alineada con las medidas de seguridad requeridas bajo el RGPD, que establece que los datos deben ser protegidos mediante medidas técnicas y organizativas adecuadas para evitar el acceso no autorizado.

### Cumplimiento con el RGPD:
Las funcionalidades mencionadas son esenciales para **SalaryBoost** al cumplir con varios principios clave del **RGPD**, como:
- **Control del usuario**: Brindar al empleado la capacidad de modificar su contraseña y actualizar sus datos personales, asegurando su autonomía sobre la información que se recopila y gestiona.
- **Precisión de los datos**: Permitir la modificación de datos garantiza que la información almacenada en el sistema esté siempre actualizada y sea precisa, cumpliendo con el principio de exactitud.
- **Limitación del almacenamiento**: La opción de eliminar los datos de un empleado cuando ya no es necesario para el propósito original (cuando deja la empresa) asegura que la empresa no retenga información más allá de lo permitido por la ley.
- **Seguridad de los datos**: La capacidad de modificar contraseñas, tanto por parte del empleado como del supervisor, asegura que el acceso a los datos personales esté protegido y que los datos no sean accesibles sin la debida autorización.

Estas medidas garantizan que **SalaryBoost** no solo protege la privacidad de los empleados, sino que también cumple con las normativas internacionales de protección de datos, como el RGPD.

---

## D. Conclusión 
En resumen, SalaryBoost garantiza la privacidad de los empleados mediante técnicas como pseudonimización, eliminación de datos sensibles y privacidad diferencial, alineándose con el RGPD. Las funcionalidades clave, como la capacidad de modificar contraseñas, actualizar datos y eliminar registros, permiten a los empleados controlar su información personal, asegurando su precisión, seguridad y limitación del almacenamiento. Estas medidas protegen la privacidad de los empleados y aseguran el cumplimiento de normativas internacionales de protección de datos.
