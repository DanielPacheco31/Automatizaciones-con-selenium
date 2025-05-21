Pruebas de aceptacion con Selenium.

Pasos del Taller:

Inicialización del WebDriver:
Escriban el código para inicializar una instancia del WebDriver para el navegador que estén utilizando (ej., Chrome).
Naveguen a la URL del formulario de práctica de DemoQA: https://demoqa.com/automation-practice-form.
Maximicen la ventana del navegador para una mejor visualización.
Llenar el Nombre y Apellido:
Localizar el campo "First Name": Inspeccionen el elemento en la página web utilizando las herramientas de desarrollo del navegador (clic derecho > Inspeccionar o Inspect Element). Identifiquen un localizador único y robusto (ID, nombre, XPath, CSS Selector).
Escriban el código para localizar este campo utilizando el método find_element() de Selenium.
Utilicen el método send_keys() para ingresar un nombre de prueba (ej., "Juan").
Localizar el campo "Last Name": Realicen el mismo proceso para el campo "Last Name" e ingresen un apellido de prueba (ej., "Pérez").
Seleccionar el Género:
Localizar los botones de radio de género: Inspeccionen los elementos de los botones de radio (Male, Female, Other). Observen sus atributos (tipo, valor, etc.).
Elijan uno de los géneros (ej., "Male") y localicen su correspondiente botón de radio o el label asociado que al hacer clic selecciona el botón.
Escriban el código para hacer clic en el botón de radio seleccionado utilizando el método click().
Ingresar el Número de Teléfono:
Localizar el campo "Mobile(10 Digits)": Inspeccionen el elemento y encuentren un localizador adecuado.
Escriban el código para localizar este campo.
Utilicen el método send_keys() para ingresar un número de teléfono de 10 dígitos (ej., "1234567890").
Seleccionar la Fecha de Nacimiento:
Localizar el campo "Date of Birth": Inspeccionen el campo que al hacer clic abre el calendario.
Escriban el código para hacer clic en este campo para abrir el selector de fechas.
Interactuar con el selector de fechas:
Localicen el selector del mes y el año (generalmente dropdowns).
Seleccionen un mes y un año deseados utilizando la clase Select si son elementos <select>, o haciendo clic en los elementos correspondientes.
Localicen el día deseado en la cuadrícula del calendario (pueden necesitar usar XPath o CSS Selectors basados en el texto del día).
Hagan clic en el día seleccionado.
Seleccionar las Materias (Subjects):
Localizar el campo "Subjects": Inspeccionen el campo que al escribir muestra sugerencias.
Escriban el código para ingresar las primeras letras de una materia (ej., "Math"). Observen cómo aparecen las sugerencias.
Localicen la sugerencia deseada (ej., "Maths") y hagan clic en ella para seleccionarla.
Repitan este proceso para seleccionar otra materia (ej., "Physics").
Seleccionar los Hobbies:
Localizar los checkboxes de hobbies: Inspeccionen los checkboxes (Sports, Reading, Music) o sus labels asociados.
Elijan uno o varios hobbies y localicen sus correspondientes checkboxes o labels.
Escriban el código para hacer clic en los checkboxes seleccionados utilizando el método click().
Subir un Archivo (Opcional si tienen un archivo de prueba):
Localizar el botón "Choose File": Inspeccionen el elemento de tipo input con el atributo type="file".
Escriban el código para localizar este elemento.
Utilicen el método send_keys() para especificar la ruta completa a un archivo de prueba en su sistema. Nota: Por razones de seguridad del navegador, esta es la forma estándar de interactuar con los campos de carga de archivos.
Ingresar la Dirección Actual:
Localizar el campo "Current Address": Inspeccionen el elemento <textarea>.
Escriban el código para localizar este campo.
Utilicen el método send_keys() para ingresar una dirección de prueba.
Seleccionar el Estado y la Ciudad:
Localizar el dropdown de "State": Inspeccionen el elemento que al hacer clic muestra las opciones de estado. Puede ser un elemento <select> o un elemento interactivo que muestra una lista.
Hagan clic en el campo para abrir las opciones.
Localicen y hagan clic en un estado de su elección (ej., "NCR").
Localizar el dropdown de "City": Realicen el mismo proceso para el campo de "City" después de haber seleccionado un estado (las opciones de ciudad dependen del estado seleccionado).
Seleccionen una ciudad de su elección (ej., "Delhi").
Enviar el Formulario:
Localizar el botón "Submit": Inspeccionen el botón para enviar el formulario.
Escriban el código para localizar este botón.
Utilicen el método click() para enviar el formulario.
Cerrar el Navegador:
Finalmente, escriban el código para cerrar la instancia del WebDriver (driver.quit()).
