📝 Descripción
Este proyecto implementa una automatización completa del formulario "Practice Form" de DemoQA utilizando Selenium WebDriver y Python. La automatización incluye la navegación al sitio, el llenado de todos los campos del formulario, la selección de opciones en menús desplegables, la interacción con calendarios, la carga de archivos y el envío del formulario.

🛠️ Tecnologías Utilizadas

Python: Lenguaje de programación principal
Selenium WebDriver: Framework para automatización de navegadores web
Chrome WebDriver: Driver específico para el navegador Chrome

🚀 Características

Inicialización automática del WebDriver con opciones personalizadas
Navegación a la URL del formulario y maximización de la ventana
Llenado de campos de texto (nombre, apellido, email, número de teléfono)
Selección de género mediante radio buttons
Selección de fecha de nacimiento con interacción en calendario
Ingreso y selección de materias con autocompletado
Selección de múltiples hobbies mediante checkboxes
Carga de archivos
Selección de estado y ciudad dependientes
Captura de pantallas antes y después de enviar el formulario
Cierre controlado del navegador

📋 Requisitos Previos

Python 3.6 o superior
Navegador Chrome instalado
ChromeDriver compatible con tu versión de Chrome

⚙️ Instalación

Clona este repositorio:
bashgit clone https://github.com/tu-usuario/automatizacion-formularios-selenium.git
cd automatizacion-formularios-selenium

Instala las dependencias:
bashpip install selenium

Asegúrate de tener ChromeDriver instalado y accesible en tu PATH o especifica su ubicación en el script.

🖥️ Uso
Para ejecutar la automatización, simplemente ejecuta el script principal:
python main.py
La automatización realizará las siguientes acciones:

Abrirá Chrome en modo incógnito
Navegará a https://demoqa.com/automation-practice-form
Llenará todos los campos del formulario
Tomará capturas de pantalla antes y después de enviar
Cerrará el navegador al finalizar

📁 Estructura del Proyecto
automatizacion-formularios-selenium/
│
├── main.py                    # Script principal de automatización
├── README.md                  # Este archivo
├── antes_de_enviar.png        # Captura antes de enviar el formulario (generada durante la ejecución)
└── despues_de_enviar.png      # Captura después de enviar el formulario (generada durante la ejecución)

🧪 Funciones Principales

get_driver(): Inicializa y configura el WebDriver
datos_texto_formulario(driver): Llena los campos de texto del formulario
seleccionar_genero(driver): Selecciona la opción de género
seleccionar_hobbies(driver): Marca las casillas de hobbies
seleccionar_fecha_nacimiento(driver): Interactúa con el calendario para seleccionar fecha
seleccionar_imagen(driver): Carga un archivo al formulario
seleccionar_estado_y_ciudad(driver): Selecciona opciones en menús desplegables
enviar_formulario(driver): Envía el formulario y captura pantallas
main(): Función principal que coordina la ejecución

📞 Contacto
Daniel Pacheco - danielpacosta93@gmail.com

⭐️ Proyecto creado como parte de de una actividad de la clase Pruebas de Software dirijida por el Profesor Sebastian Martinez https://github.com/JuanS3 de automatización con Selenium WebDriver y Python ⭐️
