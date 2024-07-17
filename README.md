# Aplicación de Procesamiento y Clasificación de Imágenes Astronómicas

Este proyecto implica la construcción de una aplicación web que procesa imágenes astronómicas, las clasifica y almacena los resultados utilizando Flask para el backend y React para el frontend. Los datos procesados se almacenan en una base de datos MongoDB.

## Tabla de Contenidos

- Características
- Tecnologías
- Configuración
- Uso
- Endpoints de la API
- Estructura de Archivos

## Características

- **Carga de Imágenes:** Permite cargar múltiples imágenes astronómicas para su procesamiento.
- **Procesamiento de Imágenes:** Detecta bordes y contornos en las imágenes y clasifica las galaxias como 'Espiral', 'Elíptica' o 'Irregular'.
- **Almacenamiento en Base de Datos:** Almacena imágenes originales y procesadas junto con los resultados de la clasificación en MongoDB.
- **Visualización de Resultados:** Muestra las imágenes cargadas, procesadas y las estadísticas de clasificación.
- **Filtrado de Imágenes:** Filtra las imágenes procesadas por su clasificación.
- **Descarga de Imágenes:** Permite descargar imágenes procesadas.
- **Eliminación de Imágenes:** Elimina imágenes y sus datos asociados de la base de datos.

## Tecnologías

- **Backend:** Flask, Python, OpenCV, scikit-image, MongoDB, GridFS
- **Frontend:** React, Axios, Chart.js, CSS

## Configuración

### Prerrequisitos

- Python 3.x
- Node.js y npm
- MongoDB

### Instalación

1. Clona el repositorio:
   git clone https://github.com/tu_usuario/astro-image-processing.git
   cd astro-image-processing

2. Configura el backend:
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. Configura el frontend:
   cd my-astronomy-app
   npm install

4. Inicia MongoDB localmente.

### Ejecutar la aplicación

1. Backend:
   python app.py

2. Frontend:
   npm start

## Uso

### Carga de Imágenes

Permite subir múltiples imágenes para su procesamiento y clasificación. Las imágenes se procesan para detectar bordes y contornos, y se clasifican en tres categorías: 'Espiral', 'Elíptica' o 'Irregular'.

### Visualización de Resultados

Muestra las imágenes cargadas y procesadas, junto con las estadísticas de clasificación. Permite filtrar las imágenes por su clasificación y descargar las imágenes procesadas.

### Eliminación de Imágenes

Permite eliminar imágenes y sus datos asociados de la base de datos.

## Endpoints de la API

### Subir imágenes

- **Endpoint:** /process_images
- **Método:** POST
- **Descripción:** Permite subir múltiples imágenes para su procesamiento y clasificación.

Ejemplo de uso en Postman:
1. Seleccionar el método POST.
2. Usar la URL: http://localhost:5000/process_images.
3. En la pestaña Body, seleccionar form-data.
4. Añadir una llave files con tipo File y seleccionar las imágenes a subir.
5. Enviar la solicitud.

### Obtener datos de imágenes

- **Endpoint:** /data
- **Método:** GET
- **Descripción:** Recupera la información de todas las imágenes procesadas.

Ejemplo de uso en Postman:
1. Seleccionar el método GET.
2. Usar la URL: http://localhost:5000/data.
3. Enviar la solicitud.

### Obtener una imagen original

- **Endpoint:** /uploads/<filename>
- **Método:** GET
- **Descripción:** Recupera la imagen original subida.

Ejemplo de uso en Postman:
1. Seleccionar el método GET.
2. Usar la URL: http://localhost:5000/uploads/<nombre_del_archivo>.
3. Enviar la solicitud.

### Obtener una imagen procesada

- **Endpoint:** /processed/<filename>
- **Método:** GET
- **Descripción:** Recupera la imagen procesada.

Ejemplo de uso en Postman:
1. Seleccionar el método GET.
2. Usar la URL: http://localhost:5000/processed/<nombre_del_archivo_procesado>.
3. Enviar la solicitud.

### Eliminar datos de una imagen

- **Endpoint:** /data/<filename>
- **Método:** DELETE
- **Descripción:** Elimina los datos de una imagen específica.

Ejemplo de uso en Postman:
1. Seleccionar el método DELETE.
2. Usar la URL: http://localhost:5000/data/<nombre_del_archivo>.
3. Enviar la solicitud.

### Generar reporte de clasificación

- **Endpoint:** /report
- **Método:** GET
- **Descripción:** Genera un reporte con la cantidad de imágenes por cada clasificación.

Ejemplo de uso en Postman:
1. Seleccionar el método GET.
2. Usar la URL: http://localhost:5000/report.
3. Enviar la solicitud.

### Obtener estadísticas

- **Endpoint:** /statistics
- **Método:** GET
- **Descripción:** Obtiene estadísticas generales de las imágenes clasificadas.

Ejemplo de uso en Postman:
1. Seleccionar el método GET.
2. Usar la URL: http://localhost:5000/statistics.
3. Enviar la solicitud.

### Obtener detalles de una imagen

- **Endpoint:** /image/<filename>
- **Método:** GET
- **Descripción:** Recupera los detalles de una imagen específica.

Ejemplo de uso en Postman:
1. Seleccionar el método GET.
2. Usar la URL: http://localhost:5000/image/<nombre_del_archivo>.
3. Enviar la solicitud.

## Estructura de Archivos

astro-image-processing/
│
├── app.py
├── requirements.txt
├── data/
│   ├── images/
│   ├── processed_images/
│   └── training_images/
│       ├── Espiral/
│       ├── Eliptica/
│       └── Irregular/
├── astro_utils/
│   └── image_processing.py
└── my-astronomy-app/
    ├── public/
    ├── src/
    │   ├── components/
    │   │   └── ImageUpload.js
    │   ├── App.js
    │   ├── index.js
    │   └── ImageUpload.css
    ├── package.json
    └── package-lock.json

## Documentación del Código

### Backend

#### app.py

Maneja las rutas y la lógica de procesamiento de imágenes y clasificación. Utiliza Flask como framework web y MongoDB para la persistencia de datos.

- Configuración de MongoDB: Establece la conexión con la base de datos MongoDB y configura GridFS para almacenar las imágenes.
- Rutas de carpetas: Define las rutas para almacenar las imágenes originales, procesadas y de entrenamiento.
- Endpoints de la API: Define los endpoints para subir imágenes, obtener datos de imágenes, eliminar imágenes, generar reportes y obtener estadísticas.

### Frontend

#### src/components/ImageUpload.js

Componente principal de React que maneja la carga, visualización y eliminación de imágenes, así como la visualización de estadísticas de clasificación.

- **Carga de imágenes:** Permite la selección y subida de múltiples imágenes.
- **Visualización de imágenes:** Muestra las imágenes originales y procesadas, junto con su clasificación.
- **Eliminación de imágenes:** Permite eliminar imágenes y actualizar las estadísticas.
- **Visualización de estadísticas:** Muestra estadísticas generales de las imágenes clasificadas utilizando Chart.js para gráficos.

#### src/ImageUpload.css

Define los estilos CSS para el componente ImageUpload, incluyendo la disposición de los elementos y la apariencia de los botones y las tarjetas de imagen.

## Persistencia

### MongoDB

Se utiliza MongoDB para almacenar los datos de las imágenes y sus clasificaciones. GridFS se utiliza para almacenar las imágenes procesadas.

- **images_collection:** Colección que almacena los metadatos de las imágenes, incluyendo el nombre del archivo original, el nombre del archivo procesado y la clasificación.
- **fs.files y fs.chunks:** GridFS utiliza estas colecciones para almacenar las partes de los archivos de imagen procesados.

### Configuración y uso

- **Configurar MongoDB:** Asegúrate de que MongoDB esté corriendo en localhost:27017. La configuración de la conexión está en el archivo app.py.
- **Insertar imágenes:** Las imágenes se insertan en MongoDB después de ser procesadas y clasificadas, junto con sus metadatos.
- **Eliminar imágenes:** Las imágenes y sus datos asociados se eliminan de MongoDB cuando se llama al endpoint de eliminación.
