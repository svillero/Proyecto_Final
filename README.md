Sistema de Gestion de Requerimientos de Sebastián Villero (entrega individual)

EN LA SIGUIENTE RUTA SE ENCUENTRA EL VIDEO CON UNA BREVE MUESTRA DEL FUNCIONAMIENTO DEL SITIO

#https://youtu.be/Z4k6p6lZNhg

Es un sistema para administrar solicitudes de requerimientos internos para que sean distribuidos y 
organizados en las empresas. En el cual se podra realizar lo siguiente:

    # Inicio Se muestra el Inicio y detalles
    #Url http://127.0.0.1:8000/appentrega/

	#About - Se cuenta sobre el dueño de la pagina
	#Url http://127.0.0.1:8000/appentrega/about/

	# Login -Logearse en el sistema
	#Url http://127.0.0.1:8000/appentrega/login/

	Se debe ingresar Username y Password, luego seleccionar crear.
	Usuario admin, pass admin.
	Usuario no admin. Username martes, pass admin123456
	Usuario no admin. Username jueves, pass admin123456

	Una vez que el usuario se logea se muestran todas las opciones a las cuales tiene acceso.
	Un usuario logeado puede ingresar a:
	-Requerimientos
	-Buscar Requerimientos
	-Proyectos
	-Clientes
	-Colaboradores
	-Mensajes
	-Editar usuario
	-Agregar avatar
	-Logout

	Tambien se muestra el nombre y la imagen del avatar cuando el usuario se logea.

	#Logout - Opcion para cerrar sesion
	#Url http://127.0.0.1:8000/appentrega/logout/

	Se cierra la sesion del usuario

	#Registrate - Opcion para crear un nuevo usuario del sistema
	#Url http://127.0.0.1:8000/appentrega/register/

	Para un nuevo usuario se solicita
	-Username (no mas de 20 caracteres)
	-Email (con @ y .com)
	-Contraseña  (5 letras + 5 numeros)
	-Confirmar contraseña (5 letras + 6 numeros)

	Luego se selecciona Registraste y si todo es correcto se crea un nuevo usuario.
	Para poder utilizar todas las opciones del sitio, luego de crear el usuario en necesario que seleccione Login

	#Editar usuario - Opcion para editar los datos de un usuario ya existente en el sistema
	#Url http://127.0.0.1:8000/appentrega/edit/

	Se pueden editar los siguientes datos del usuario
	Correo (Ingrese correo nuevo)
	Contraseña (Ingrese contraseña nueva)
	Repita contraseña

	Luego se selecciona el boton Editar y todos los datos seran cambiados. 

	#Agregar avatar - Opción para adjudicarle un avatar a un usuario
	#Url http://127.0.0.1:8000/appentrega/avatar/

	Se debe presionar el boton Seleccionar archivo y posteriormente se abre una ventana del Explorer en la cual
	se pueden seleccionar las imagenes que tengamos en el sistema.
	Luego de seleccionar una imagen presionar Abrir, para que el sistema tome la ruta completa de la imagen.
	Y luego seleccionar el boton Cargar. Listo, una vez realizado esto se vera en la esquina superior derecha al lado del 
	nombre del usuario aparecera la nueva imagen.

    # Crear Requerimientos- Opcion para crear, editar o borrar un nuevo Requerimiento
    #Url http://127.0.0.1:8000/appentrega/requerimiento/
	
	Se debe ingresar
	Numero  Ejemplo 4
	Estado  Ejemplo 99
	Nombre  Ejemplo 'Cambio es Layout'
	Solicitud  Ejemplo '12254'	
	
	Luego presionar 'Crear'
	Nota En la tabla requerimiento se almacenan todos los datos ingresados mas la fecha del alta.
	Para editar o borrar se selecciona el requerimiento deseado y se selecciona la accion Borrar o Editar.
	Para editar se abre una nueva ventana en la cual se piden todos los campos que se desean cambiar.

	Casos cargados en appentrega_requerimiento
	id	numero	estado	nombre					solicitud	fecha_alta	fecha_cierre
	1	1		1		Cambio en usuario.java	1425		2022-08-06	
	2	2		2		Cambio en C#			47785		2022-08-06	
	12	99		63		testing					1111		2022-09-05	

    # Buscar Requerimientos - Opcion para listar los Requerimientos
    #Url http://127.0.0.1:8000/appentrega/requerimientos/
	
	Se listan los requerimientos ingresados. 
	Si se ingresa un nombre de un requerimiento y luego se selecciona 'Buscar' se 
	obtiene el o los requerimientos que hagan match con lo buscado.

    # Crear Proyecto - Opcion para crear un nuevo Proyecto
    #Url http://127.0.0.1:8000/appentrega/proyecto/
	
	Se debe ingresar
	Numero  Ejemplo 77
	Nombre  Ejemplo 'Expansion'
	Pm asignado Ejemplo 'Fede Tres'	
	Fecha entrega Ejemplo '2020-08-08'
	Costo Ejemplo '4110'
	
	Luego presionar 'Crear'
	Nota En la tabla proyecto se almacenan todos los datos ingresados mas la fecha del alta
	Para editar o borrar se selecciona el proyecto deseado y se selecciona la accion Borrar o Editar.
	Para editar se abre una nueva ventana en la cual se piden todos los campos que se desean cambiar.

	Casos cargados en appentrega_proyecto
	id	numero	nombre				pm_asignado			fecha_alta	fecha_entrega	costo
	17		99	Cambio funcional	Nicolas Torres		2022-08-31	2022-08-02		66
	21		66	Modificacion BD		Juan Gomez			2022-09-05	2022-01-02		8400
	22		55	Pase a produccion	Luis Battle			2022-09-05	2200-01-02		8900	

    # Crear Clientes - Opcion para crear un nuevo Cliente
    #Url http://127.0.0.1:8000/appentrega/cliente/
	
	Se debe ingresar
	Cliente id Ejemplo 44
	Razon social Ejemplo 'Empresa Noble'
	Email  Ejemplo 'empresa@dd.com'	
	
	Luego presionar 'Crear'
	Nota En la tabla cliente se almacenan todos los datos ingresados mas la fecha del alta
	Para editar o borrar se selecciona el cliente deseado y se selecciona la accion Borrar o Editar.
	Para editar se abre una nueva ventana en la cual se piden todos los campos que se desean cambiar.

	Casos cargados en appentrega_cliente
	id	rut			razon_social		email			fecha_alta
	1	1			Distribuidora		assa@ee.com		2020-07-08
	10	333222		ole					coder@ar.com	2011-01-01
	11	45215665	Nuevo Testing Sa	ddd@ssd.com		2022-09-05
	12	78945662	Coder nuevo srl		ddd@ssd.com		2022-09-05

    # Crear Colaboradores - Opcion para crear un nuevo Colaborador
    #Url http://127.0.0.1:8000/appentrega/colaborador/
	
	Se debe ingresar
	Numero  Ejemplo 5
	Nombre  Ejemplo 'Carlos'
	Apellido Ejemplo 'Gomez'
	Cargo Ejemplo 'Programador'
	Email Ejemplo 'pg@ffd.com'	
	
	Luego presionar 'Crear'
	Nota En la tabla colaborador se almacenan todos los datos ingresados mas la fecha del alta
	Para editar o borrar se selecciona el colaborador deseado y se selecciona la accion Borrar o Editar.
	Para editar se abre una nueva ventana en la cual se piden todos los campos que se desean cambiar.

	Casos cargados en appentrega_colaborador
	id	numero	nombre		apellido	cargo		email		fecha_alta
	1	1	Juan		Prueba		analista	sd@fm.com	2022-08-06
	7	45	Sebastian	Villero		Programador	ddd@ssd.com	2022-09-05
	10	45	Pedro		Paez		junior		ddd@ssd.com	2022-09-05		

	# Crear Mensajes - Opcion para crear nuevos mensajes para que los usuarios se puedan comunicar entre si
	#url http://127.0.0.1:8000/appmensajes/mensajes/ -- Para esta funcionalidad se crea appmensajes

	Se ingresa el texto del mensaje y se presiona crear.

	Se despliega una lista
	Texto del mensaje
	Usuario que lo creo
	Fecha y hora de creacion de los mensajes.

	Casos cargados en appmensajes_mensaje
	id	texto							usuario			fecha_alta
	17	Hola							admin			2022-09-05 14:38:00.930364
	18	Mensaje de prueba para video	viernes			2022-09-05 15:54:27.134484
	19	hola como estas?				martes			2022-09-05 15:56:24.376464


	