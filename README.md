Sistema de Gestion de Requerimientos by Sebastián Villero

Es un sistema para administrar solicitudes de requerimientos internos para que sean distribuidos y 
organizados en las empresas. En el cual se podra realizar lo siguiente:

    # Inicio: Se muestra el Inicio y detalles
    Url http://127.0.0.1:8000/inicio/ 

    # Crear Requerimientos: Opcion para crear un nuevo Requerimiento
    Url http://127.0.0.1:8000/inicio/crear_requerimiento/
	
	Se debe ingresar:
	Numero : Ejemplo 4
	Estado : Ejemplo 99
	Nombre : Ejemplo 'Cambio es Layout'
	Solicitud : Ejemplo '12254'
	Fecha alta: Ejemplo '2020-01-01'
	
	Luego presionar 'Crear'

    # Buscar Requerimientos: Opcion para listar los Requerimientos
    Url http://127.0.0.1:8000/inicio/requerimientos/
	
	Se listan los requerimientos ingresados. 
	Si se ingresa un nombre de un requerimiento y luego se selecciona 'Buscar' se 
	obtiene el o los requerimientos que hagan match con lo buscado.

    # Crear Proyecto: Opcion para crear un nuevo Proyecto
    Url http://127.0.0.1:8000/inicio/crear_proyecto/
	
	Se debe ingresar:
	Numero : Ejemplo 77
	Nombre : Ejemplo 'Expansion'
	Pm asignado: Ejemplo 'Fede Tres'
	Fecha alta: Ejemplo '2001-01-01'
	Fecha entrega: Ejemplo '2020-08-08'
	Costo: Ejemplo '4110'
	
	Luego presionar 'Crear'

    # Crear Clientes: Opcion para crear un nuevo Cliente
    Url http://127.0.0.1:8000/inicio/crear_cliente/
	
	Se debe ingresar:
	Cliente id: Ejemplo 44
	Razon social: Ejemplo 'Empresa Noble'
	Email : Ejemplo 'empresa@dd.com'
	Fecha alta: '2019-05-05'
	
	Luego presionar 'Crear'

    # Crear Colaboradores: Opcion para crear un nuevo Colaborador
    Url http://127.0.0.1:8000/inicio/crear_colaborador/
	
	Se debe ingresar:
	Numero : Ejemplo 5
	Nombre : Ejemplo 'Carlos'
	Apellido: Ejemplo 'Gomez'
	Cargo: Ejemplo 'Programador'
	Email: Ejemplo 'pg@ffd.com'
	Fecha alta: '2022-05-05'
	
	Luego presionar 'Crear'
