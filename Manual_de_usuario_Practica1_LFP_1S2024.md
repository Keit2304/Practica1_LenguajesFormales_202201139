# Lenguajes Formales y de Programación (Sección B-)
## Práctica 1 PetManager
### Primer Semestre 2024
```js
Universidad San Carlos de Guatemala
Programador: Keitlyn Valentina Tunchez Castañeda
Carne: 202201139
Correo: 2986847560101@ingenieria.usac.edu.gt
```
---
## Descripción del Proyecto
El Consejo Nacional de Áreas Protegidas ha lanzado el programa educativo "PetWorld Manager", destinado a niños de 6 a 12 años, con el objetivo de inculcar valores de cuidado y responsabilidad en la tenencia de mascotas. En colaboración con la Universidad de San Carlos de Guatemala, el curso de Lenguajes Formales y de Programación se ha comprometido a ofrecer su apoyo a este proyecto socialmente responsable.
"PetWorld Manager" no solo es un programa de entretenimiento y educación, sino también una herramienta pedagógica diseñada para concientizar a los niños sobre el compromiso y cuidado necesario al tener una mascota. Este proyecto se alinea estrechamente con la misión del Consejo Nacional de Áreas Protegidas de fomentar la responsabilidad social y ambiental desde una edad temprana.

## Objetivos
* Objetivo General
    * Desarrollar un sistema de gestión integral de mascotas virtuales (gatos), incorporando módulos de almacenamiento de palabras, utilizando principios de programación en Python y aplicando paradigmas de programación orientada a objetos y funcional.
* Objetivos Específicos
    * Desarrollar las clases y funciones necesarias para la creación, interacción y gestión de mascotas virtuales.
    * Asegurar que la aplicación pueda interpretar y ejecutar los comandos contenidos en estos archivos.

---
## Ejecución del Programa
### Requisitos Previos:
- Python instalado en su sistema.
- Instalación de las bibliotecas necesarias: graphviz y PIL.
- Asegúrese de tener los archivos de entrada con la extensión .petmanager en el mismo directorio que el programa.

### Inicio del Programa:
- Ejecute el programa en su entorno Python preferido.

### Menú Principal:

Al ejecutar el programa, se presentará un menú principal con las siguientes opciones:
- Módulo PetManager: Acceda a las funcionalidades principales del programa.
- Salir: Finaliza la ejecución del programa.

![principal](https://i.ibb.co/rd5nDT8/menu-principal.png)

### Módulo PetManager:

En este módulo, puede realizar diversas operaciones con archivos .petmanager. Al seleccionar el módulo PetManager, se presentará un submenú con las siguientes opciones:

![PetManager](https://i.ibb.co/4RTdQrg/modulo-petmanager.png)
- Cargar Archivo:
Seleccione la opción "Cargar Archivo" para cargar uno de los archivos disponibles con extensión .petmanager en el directorio.

El programa leerá el contenido del archivo, mostrará el contenido en pantalla y procesará las acciones especificadas en él.
Se generarán resúmenes de acciones para cada mascota presente en el archivo. Además, se creará un archivo de resultados llamado gatos.petworld_result, donde se almacenará un resumen global de todas las acciones realizadas en los gatos presentes en el archivo.

![Lectura](https://i.ibb.co/kcw8Rqv/lectura-de-archivo.png)

- Salir:
Puede seleccionar la opción "Salir" tanto del menú principal como del submenú PetManager para finalizar la ejecución del programa.

# Resultados del Programa:

El programa realizará acciones como alimentar y jugar con los gatos según las especificaciones del archivo .petmanager.
- Se generará un resumen detallado de las acciones realizadas para cada mascota.
- Se creará un archivo de resultados (gatos.petworld_result) con un resumen global de todas las acciones realizadas en los gatos presentes en el archivo cargado.

![Result](https://i.ibb.co/JHQby6v/petworld-result.png)
- Se generarán imágenes de grafos para visualizar el estado de los gatos después de realizar las acciones correspondientes. Estas imágenes se combinarán en un solo archivo llamado imagenes_combinadas.png.

![Result](https://i.ibb.co/WKHDYkJ/graficas.png)

# En conclusión
 PetManager es un sistema fácil de utilizar que permite interactuar de manera eficiente con los Gatos del archivo de entrada. A través de una interfaz amigable y opciones claras en el menú, como usuarios pueden cargar archivos de configuración, realizar acciones como alimentar y jugar con los gatos, y obtener informes detallados sobre el estado y las actividades de sus mascotas virtuales. Además, la limpieza automática de archivos de imagen y la creación de un archivo de resultados simplifican el proceso de gestión de los Gatos.
### ¡Disfruta utilizando PetManager para interactuar con tus Gatos!