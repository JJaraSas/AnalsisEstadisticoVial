# Manuar de Utilizacion

Explicaremos como se instala la aplicacion y su utilizacion


## Pre-requisitos 📋

Debemos tener Python 3.7 o superior instalado en el sistema y configurado en las variables de entorno [aqui](https://tutorial.djangogirls.org/es/python_installation/)

## Instalación 🔧

Para la **Instalacion** debemos descargar primero esta carpeta del repositorio **PaginaWeb**. Una vez descargada abriremos una linea de comandos (CMD, PowerShell,..) y nos hubicamos subre el directorio de la carpeta la carpeta descargada.

Iniciaremos creando un entrono virtual para la aplicacion y asi no afectar nuestro sistema, asi que en la consola ejecutamos el siguiente comando, escogiendo el _nombre_entorno virtual_ que deseemos (**venv** por lo general)

```
python -m venv nombre_entorno virtual
```

Esperamos que se realice lainstalacion, cuando termine activamos el entorno virtual.

```
.\nombre_entorno virtual\Scripts\activate
```

Nos aparecera al inicio de la linea de comando el nombre del entorno virtual, por ejemplo, en este caso llamamos al entorno virtua **test**.

```
(test) PS C:\PaginaWeb> 
```

Para desactivar el entorno virtual usaremos.

```
deactivate
```

Finalmente instalamos los requisitos necesarios con el comando.

```
pip install -r requirements.txt
```

## Ejecucion 🚀

Ahora ejecutaremos flask para poder acceder a la pagina, asi que con el entorno virtual activado y los requerimientos instalados procedemos a escribir lo siguiente.

```
flask run 
```

Si todo es correcto veremos que podemos acceder a nuestro desarrollo por medio de localhost.

```
* Running on http://127.0.0.1:5000/
```

### Ejecutando las pruebas ⚙️

Ahora accederemos al navegador web y escribimos la direccion de arriba en la barra de direcciones.

```
http://127.0.0.1:5000/
```

Y podremos acceder a la pagina web con la informacion recolectada.

![Pagina Inicio](https://github.com/SebastianMancera/AnalisisEstadisticoVial/blob/pagina_web/PaginaWeb/imagenesmanual/principal.PNG?raw=true)

En la pagina principal tendremos una breve descripcion del proyecto, y un menu a la izquierda que puede quitarse o mostrarse presionando el boton de las tres lineas.

![Boton Menu](https://github.com/SebastianMancera/AnalisisEstadisticoVial/blob/pagina_web/PaginaWeb/imagenesmanual/ocultarmenu.PNG?raw=true)

Ahora para navegar por la pagina tendremos el sisguiente menu.

![Menu](https://github.com/SebastianMancera/AnalisisEstadisticoVial/blob/pagina_web/PaginaWeb/imagenesmanual/menu.PNG?raw=true)

Alli encontraremos las categorias de los diferentes analsis que se obtubieron por medio del [registro de siniestros viales](https://github.com/SebastianMancera/AnalisisEstadisticoVial/blob/pagina_web/Data/2015_2019_siniestralidad_vial.xlsx)

Algunas de las opciones del menu pueden expandirse para entrar mas en detalle de los datos analizados.

![Menu Deplegable](https://github.com/SebastianMancera/AnalisisEstadisticoVial/blob/pagina_web/PaginaWeb/imagenesmanual/menuexpandido.PNG?raw=true)

Al acceder a las secciones seremos llevados a una nueva pagina con la informacion que esta contiene.

![Nueva Ventana](https://github.com/SebastianMancera/AnalisisEstadisticoVial/blob/pagina_web/PaginaWeb/imagenesmanual/nuevaseccion.PNG?raw=true)

Finalemente podemos cerrar el navegador para salir de la pagina y acceder siempre que lo deseemos activando Flask como se menciono con anterioridad.

### Desinstalacion 🔩

Para quitar la aplicacion simplemente debemos ejecutar el comando de desactivar el entorno virtual

```
deactivate
```

Y eliminar el directorio donde se extrajo la informacion.


## Herramientas 📌

Las siguientes herraientas fueron usadas en el proyecto:


[Pandas](https://pandas.pydata.org/) Pandas es una biblioteca de software escrita como extensión de NumPy para manipulación y análisis de datos.  
[Numpy](https://numpy.org/) Da soporte para crear vectores y matrices grandes multidimensionales.  
[Geopandas](https://geopandas.org/) Facilita el trabajo con datos geoespaciales en python.  
[Matplotlib](https://matplotlib.org/stable/index.html) Es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays.  
[Flask](https://flask.palletsprojects.com/en/1.1.x/) Permite crear aplicaciones web rápidamente y con un mínimo número de líneas de código.  
[Seaborn](https://seaborn.pydata.org/) Biblioteca de visualización de datos de Python basada en matplotlib.  
[datetime](https://docs.python.org/es/3/library/datetime.html) Incluye funciones y clases para hacer análisis, formateo y aritmética de fecha y hora.  

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Sebastian Mancera** - *Analisis Estadistico* - [SebastianMancera](https://github.com/SebastianMancera)
* **Jeison Jara** - *Pagina Web* - [JJaraSas](https://github.com/JJaraSas)

