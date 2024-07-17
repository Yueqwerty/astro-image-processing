# Aplicación de Procesamiento y Clasificación de Imágenes Astronómicas

Este proyecto implica la construcción de una aplicación web que procesa imágenes astronómicas, las clasifica y almacena los resultados utilizando Flask para el backend y React para el frontend. Los datos procesados se almacenan en una base de datos MongoDB.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Configuración](#configuración)
- [Uso](#uso)
- [Endpoints de la API](#endpoints-de-la-api)
- [Estructura de Archivos](#estructura-de-archivos)
- [Documentación del Código](#documentación-del-código)

## Características

- **Carga de Imágenes:** Permite cargar múltiples imágenes astronómicas para su procesamiento.
- **Procesamiento de Imágenes:** Detecta bordes y contornos en las imágenes y clasifica las galaxias como 'Espiral', 'Elíptica' o 'Irregular'.
- **Almacenamiento en Base de Datos:** Almacena imágenes originales y procesadas junto con los resultados de la clasificación en MongoDB.
- **Visualización de Resultados:** Muestra las imágenes cargadas, procesadas y las estadísticas de clasificación.
- **Filtrado de Imágenes:** Filtra las imágenes procesadas por su clasificación.
- **Descarga de Imágenes:** Permite descargar imágenes procesadas.
- **Eliminación de Imágenes:** Elimina imágenes y sus datos asociados de la base de datos.

## Tecnologías

### Backend

- **Flask:** Microframework de Python para construir aplicaciones web. Se utiliza para gestionar las solicitudes HTTP y conectar la lógica del servidor con el frontend.
- **OpenCV:** Biblioteca de visión por computadora para el procesamiento de imágenes. Se utiliza para leer, manipular y detectar características en las imágenes astronómicas.
- **scikit-image:** Biblioteca de procesamiento de imágenes en Python. Se utiliza para aplicar filtros y técnicas de procesamiento avanzadas a las imágenes.
- **MongoDB:** Base de datos NoSQL para almacenar datos de imágenes y resultados de clasificación. Se utiliza para almacenar tanto los metadatos de las imágenes como las propias imágenes procesadas utilizando GridFS.
- **GridFS:** Especificación para almacenar y recuperar archivos que exceden el tamaño de un solo documento en MongoDB. Se utiliza para manejar el almacenamiento de imágenes procesadas.

### Frontend

- **React:** Biblioteca de JavaScript para construir interfaces de usuario. Se utiliza para construir la interfaz de usuario interactiva de la aplicación.
- **Axios:** Cliente HTTP basado en promesas para realizar solicitudes al servidor. Se utiliza para enviar y recibir datos entre el frontend y el backend.
- **Chart.js:** Biblioteca para crear gráficos y visualizaciones de datos. Se utiliza para mostrar estadísticas y datos de clasificación de manera visual.
- **CSS:** Hojas de estilo en cascada para dar estilo a la aplicación. Se utiliza para diseñar y estilizar la interfaz de usuario.

## Configuración

### Prerrequisitos

- **Python 3.x:** Lenguaje de programación utilizado para el backend.
- **Node.js y npm:** Entorno de ejecución de JavaScript y su administrador de paquetes, utilizados para el frontend.
- **MongoDB:** Base de datos NoSQL utilizada para almacenar los datos de las imágenes.

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/astro-image-processing.git
   cd astro-image-processing
   ```

2. **Configurar el backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configurar el frontend:**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Iniciar MongoDB localmente.**

5. **Ejecutar el servidor Flask:**
   ```bash
   cd backend
   python app.py
   ```

6. **Ejecutar la aplicación React:**
   ```bash
   cd ../my-astronomy-app
   npm start
   ```

## Uso

1. **Abrir el navegador web:** Navega a `http://localhost:3000`.
2. **Cargar imágenes astronómicas:** Utiliza la interfaz para cargar las imágenes.
3. **Visualizar resultados:** Observa las imágenes procesadas y sus clasificaciones.
4. **Filtrar imágenes:** Filtra las imágenes por su clasificación.
5. **Descargar imágenes:** Descarga las imágenes procesadas si es necesario.
6. **Eliminar imágenes:** Elimina imágenes y sus datos asociados de la base de datos.

## Endpoints de la API

- **`POST /process_images`**: Procesa las imágenes cargadas y las clasifica.
- **`GET /data`**: Obtiene todos los datos de imágenes procesadas.
- **`DELETE /data/:filename`**: Elimina una imagen y sus datos asociados.
- **`GET /report`**: Genera un reporte de las imágenes procesadas y sus clasificaciones.
- **`GET /statistics`**: Obtiene estadísticas de las imágenes clasificadas.
- **`GET /image/:filename`**: Obtiene los detalles de una imagen específica.

## Estructura de Archivos

```
astro-image-processing/
│
├── app.py                         # Script principal para iniciar el servidor Flask
├── requirements.txt               # Archivo con las dependencias de Python necesarias
├── data/                          # Carpeta para almacenar datos de imágenes
│   ├── images/                    # Imágenes originales cargadas
│   ├── processed_images/          # Imágenes procesadas
│   └── training_images/           # Imágenes clasificadas para entrenamiento
│       ├── Espiral/               # Carpeta para imágenes clasificadas como Espiral
│       ├── Elíptica/              # Carpeta para imágenes clasificadas como Elíptica
│       └── Irregular/             # Carpeta para imágenes clasificadas como Irregular
├── astro_utils/                   # Utilidades para procesamiento de imágenes
│   └── image_processing.py        # Script para procesamiento y clasificación de imágenes
└── my-astronomy-app/              # Aplicación frontend en React
    ├── public/                    # Archivos estáticos públicos
    ├── src/                       # Código fuente de React
    │   ├── components/            # Componentes de React
    │   │   └── ImageUpload.js     # Componente para cargar y procesar imágenes
    │   ├── App.js                 # Componente principal de la aplicación
    │   ├── index.js               # Punto de entrada de la aplicación React
    │   └── ImageUpload.css        # Estilos CSS para el componente ImageUpload
    ├── package.json               # Archivo de configuración de npm con las dependencias del proyecto
    └── package-lock.json          # Archivo de bloqueo de versiones de npm
```

## Documentación del Código

### Frontend

#### `ImageUpload.js`

- **Descripción:** Este componente permite a los usuarios cargar imágenes astronómicas para su procesamiento. Utiliza `axios` para enviar las imágenes al backend y muestra los resultados procesados y clasificados. Incluye funcionalidades para filtrar imágenes por clasificación, descargar imágenes procesadas y eliminar imágenes.
- **Principales Funcionalidades:**
  - Carga de imágenes múltiples.
  - Envío de imágenes al backend para procesamiento.
  - Visualización de imágenes originales y procesadas.
  - Filtro de imágenes por clasificación.
  - Descarga de imágenes procesadas.
  - Eliminación de imágenes de la base de datos.

#### `App.js`

- **Descripción:** Componente principal de la aplicación React que organiza y renderiza el componente `ImageUpload`.
- **Principales Funcionalidades:**
  - Renderiza la estructura principal de la aplicación.
  - Incluye el componente `ImageUpload`.

#### `index.js`

- **Descripción:** Punto de entrada de la aplicación React que renderiza el componente `App` en el DOM.
- **Principales Funcionalidades:**
  - Renderiza el componente principal `App` en el elemento raíz del HTML.

#### `ImageUpload.css`

- **Descripción:** Archivo de estilos CSS para el componente `ImageUpload`.
- **Principales Funcionalidades:**
  - Define estilos visuales para el componente de carga de imágenes.
  - Mejora la presentación y la disposición de los elementos en la interfaz de usuario.

### Backend

#### `app.py`

- **Descripción:** Configura el servidor Flask y define los endpoints de la API. Incluye la lógica para procesar imágenes, clasificarlas y almacenarlas en MongoDB.
- **Principales Funcionalidades:**
  - Define los endpoints para el procesamiento y clasificación de imágenes.
  - Gestiona las solicitudes HTTP para obtener datos de imágenes, generar reportes y estadísticas, y eliminar imágenes.
  - Conecta con la base de datos MongoDB y utiliza GridFS para almacenar imágenes grandes.

#### `requirements.txt`

- **Descripción:** Lista de dependencias de Python necesarias para ejecutar el backend.
- **Principales Dependencias:**
  - Flask: Microframework para construir aplicaciones web.
  - Flask-CORS: Para manejar solicitudes entre dominios.
  - pymongo: Para conectar y operar con MongoDB.
  - gridfs: Para manejar el almacenamiento de archivos grandes en MongoDB.
  - opencv-python: Para procesamiento de imágenes.
  - scikit-image: Para procesamiento avanzado de imágenes.

### Persistencia

#### MongoDB

- **Descripción:** Base de datos NoSQL utilizada para almacenar los datos de las imágenes y los resultados de la clasificación.
- **GridFS:** Especificación utilizada para almacenar y recuperar archivos que

 exceden el tamaño de un solo documento en MongoDB. Utilizada para manejar el almacenamiento de imágenes procesadas.
- **Colecciones:**
  - **`images`**: Almacena metadatos de las imágenes procesadas, incluyendo el nombre del archivo, la ruta de la imagen procesada y la clasificación.
  - **`fs.files` y `fs.chunks`**: Utilizados por GridFS para almacenar y recuperar archivos grandes.
