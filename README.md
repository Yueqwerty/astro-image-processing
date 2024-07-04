# Aplicación de Procesamiento y Clasificación de Imágenes Astronómicas

Este proyecto implica la construcción de una aplicación web que procesa imágenes astronómicas, las clasifica y almacena los resultados utilizando Flask para el backend y React para el frontend. Los datos procesados se almacenan en una base de datos MongoDB.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Configuración](#configuración)
- [Uso](#uso)
- [Endpoints de la API](#endpoints-de-la-api)
- [Estructura de Archivos](#estructura-de-archivos)

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
   ```bash
   git clone https://github.com/tu_usuario/astro-image-processing.git
   cd astro-image-processing

2. Configura el backend.
   ```bash
   cd backend
   pip install -r requirements.txt

3. Configura el frontend.
   ```bash
   cd frontend
   npm install

4. Iniciar MongoDB localmente.


