Sistema de Gestion de Requerimientos de Sebastián Villero (entrega individual)

Es un sistema para administrar solicitudes de requerimientos internos para que sean distribuidos y 
organizados en las empresas. En el cual se podra realizar lo siguiente

    # Inicio Se muestra el Inicio y detalles
    Url http127.0.0.18000appentrega

	# Login Logearse en el sistema
	Url http127.0.0.18000appentregalogin

	Se debe ingresar Username y Password, luego seleccionar crear.
	Usuario admin, pass admin.
	Usuario no admin. Username martes, pass admin123456

	Una vez que el usuario se logea se muentran todas las opciones a las cuales tiene acceso.
	Un usuario logeado puede ingresar a
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

	#Logout Opcion para cerrar sesion
	Url http127.0.0.18000appentregalogout

	#Registrate Opcion para crear un nuevo usuario del sistema
	Url http127.0.0.18000appentregaregister

	Para un nuevo usuario se solicita
	-Username (no mas de 20 caracteres)
	-Email (con @ y .com)
	-Contraseña  (5 letras + 5 numeros)
	-Confirmar contraseña (5 letras + 5 numeros)

	Luego se selecciona Registraste y si todo es correcto se crea un nuevo usuario.
	Para poder utilizar todas las opciones del sitio, luego de crear el usuario en necesario que seleccione Login

	#Editar usuario Opcion para editar los datos de un usuario ya existente en el sistema
	Url http127.0.0.18000appentregaedit

	Se pueden editar los siguientes datos del usuario
	Correo (Ingrese correo nuevo)
	Contraseña (Ingrese contraseña nueva)
	Repita contraseña

	Luego se selecciona el boton Editar y todos los datos seran cambiados. 

	#Agregar avatar Opción para adjudicarle un avatar a un usuario
	Url http127.0.0.18000appentregaavatar

	Se debe presionar el boton Seleccionar archivo y posteriormente se abre una ventana del Explorer en la cual
	se pueden seleccionar las imagenes que tengamos en el sistema.
	Luego de seleccionar una imagen presionar Abrir, para que el sistema tome la ruta completa de la imagen.
	Y luego seleccionar el boton Cargar. Listo, una vez realizado esto se vera en la esquina superior derecha al lado del 
	nombre del usuario aparecera la nueva imagen.

    # Crear Requerimientos Opcion para crear, editar o borrar un nuevo Requerimiento
    Url http127.0.0.18000appentregarequerimiento
	
	Se debe ingresar
	Numero  Ejemplo 4
	Estado  Ejemplo 99
	Nombre  Ejemplo 'Cambio es Layout'
	Solicitud  Ejemplo '12254'	
	
	Luego presionar 'Crear'
	Nota En la tabla requerimiento se almacenan todos los datos ingresados mas la fecha y hora del alta.
	Para editar o borrar se selecciona el requerimiento deseado y se selecciona la accion Borrar o Editar.
	Para editar se abre una nueva ventana en la cual se piden todos los campos que se desean cambiar.

    # Buscar Requerimientos Opcion para listar los Requerimientos
    Url http127.0.0.18000appentregarequerimientos
	
	Se listan los requerimientos ingresados. 
	Si se ingresa un nombre de un requerimiento y luego se selecciona 'Buscar' se 
	obtiene el o los requerimientos que hagan match con lo buscado.

    # Crear Proyecto Opcion para crear un nuevo Proyecto
    Url http127.0.0.18000appentregaproyecto
	
	Se debe ingresar
	Numero  Ejemplo 77
	Nombre  Ejemplo 'Expansion'
	Pm asignado Ejemplo 'Fede Tres'	
	Fecha entrega Ejemplo '2020-08-08'
	Costo Ejemplo '4110'
	
	Luego presionar 'Crear'
	Nota En la tabla proyecto se almacenan todos los datos ingresados mas la fecha y hora del alta
	Para editar o borrar se selecciona el proyecto deseado y se selecciona la accion Borrar o Editar.
	Para editar se abre una nueva ventana en la cual se piden todos los campos que se desean cambiar.

    # Crear Clientes Opcion para crear un nuevo Cliente
    Url http127.0.0.18000appentregacliente
	
	Se debe ingresar
	Cliente id Ejemplo 44
	Razon social Ejemplo 'Empresa Noble'
	Email  Ejemplo 'empresa@dd.com'	
	
	Luego presionar 'Crear'
	Nota En la tabla cliente se almacenan todos los datos ingresados mas la fecha y hora del alta
	Para editar o borrar se selecciona el cliente deseado y se selecciona la accion Borrar o Editar.
	Para editar se abre una nueva ventana en la cual se piden todos los campos que se desean cambiar.

    # Crear Colaboradores Opcion para crear un nuevo Colaborador
    Url http127.0.0.18000appentregacolaborador
	
	Se debe ingresar
	Numero  Ejemplo 5
	Nombre  Ejemplo 'Carlos'
	Apellido Ejemplo 'Gomez'
	Cargo Ejemplo 'Programador'
	Email Ejemplo 'pg@ffd.com'	
	
	Luego presionar 'Crear'
	Nota En la tabla colaborador se almacenan todos los datos ingresados mas la fecha y hora del alta
	Para editar o borrar se selecciona el colaborador deseado y se selecciona la accion Borrar o Editar.
	Para editar se abre una nueva ventana en la cual se piden todos los campos que se desean cambiar.

	# Crear Mensajes Opcion para crear nuevos mensajes para que los usuarios se puedan comunicar entre si
	http127.0.0.18000appmensajesmensajes

	Se ingresa el texto del mensaje y se presiona crear.

	Se despliega una lista
	Texto del mensaje
	Usuario que lo creo
	Fecha y hora de creacion de los mensajes.


	EN LA SIGUIENTE RUTA SE ENCUENTRA EL VIDEO CON UNA BREVE MUESTRA DEL FUNCIONAMIENTO DEL SITIO

	httpswww.youtube.comwatchv=Z4k6p6lZNhg