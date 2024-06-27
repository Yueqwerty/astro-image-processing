import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ImageUpload.css';
import { Bar } from 'react-chartjs-2';

function ImageUpload() {
    const [files, setFiles] = useState([]);
    const [images, setImages] = useState([]);
    const [classificationFilter, setClassificationFilter] = useState('Todos');
    const [statistics, setStatistics] = useState({});
    const [notification, setNotification] = useState('');

    const handleFileChange = (event) => {
        setFiles(event.target.files);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        Array.from(files).forEach((file) => {
            formData.append('files', file);
        });

        try {
            await axios.post('http://localhost:5000/process_images', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setNotification('Imágenes subidas con éxito');
            setTimeout(() => setNotification(''), 3000);
            fetchImages();
            fetchStatistics();
        } catch (error) {
            console.error('Error uploading images:', error);
            setNotification('Error al subir imágenes');
            setTimeout(() => setNotification(''), 3000);
        }
    };

    const fetchImages = async () => {
        try {
            const response = await axios.get('http://localhost:5000/data');
            setImages(response.data);
        } catch (error) {
            console.error('Error fetching images:', error);
        }
    };

    const fetchStatistics = async () => {
        try {
            const response = await axios.get('http://localhost:5000/statistics');
            setStatistics(response.data);
        } catch (error) {
            console.error('Error fetching statistics:', error);
        }
    };

    useEffect(() => {
        fetchImages();
        fetchStatistics();
    }, []);

    const handleFilterChange = (event) => {
        setClassificationFilter(event.target.value);
    };

    const handleDeleteImage = async (filename) => {
        try {
            await axios.delete(`http://localhost:5000/data/${filename}`);
            fetchImages();
            fetchStatistics();
        } catch (error) {
            console.error('Error deleting image:', error);
        }
    };

    const handleDownloadImage = (url) => {
        const link = document.createElement('a');
        link.href = url;
        link.download = url.split('/').pop();
        link.click();
    };

    const filteredImages = images.filter((image) =>
        classificationFilter === 'Todos' || image.classification === classificationFilter
    );

    const data = {
        labels: ['Espiral', 'Elíptica', 'Irregular'],
        datasets: [
            {
                label: 'Clasificaciones',
                data: [
                    statistics.classifications?.Espiral || 0,
                    statistics.classifications?.Elíptica || 0,
                    statistics.classifications?.Irregular || 0,
                ],
                backgroundColor: ['#6a0dad', '#ffa500', '#00ff00'],
            },
        ],
    };

    return (
        <div className="app-container">
            <nav className="navbar">
                <h1>Procesamiento de Imágenes</h1>
            </nav>
            <div className="upload-card">
                {notification && <p className="notification">{notification}</p>}
                <input type="file" multiple onChange={handleFileChange} />
                <button className="upload-button" onClick={handleUpload}>Subir Imágenes</button>
                <div className="filter-container">
                    <label>Filtrar por clasificación: </label>
                    <select value={classificationFilter} onChange={handleFilterChange}>
                        <option value="Todos">Todos</option>
                        <option value="Espiral">Espiral</option>
                        <option value="Eliptica">Elíptica</option>
                        <option value="Irregular">Irregular</option>
                    </select>
                </div>
                <h2>Imágenes Procesadas</h2>
                <div className="images-grid">
                    {filteredImages.map((image, index) => (
                        <div key={index} className="image-box">
                            <h3>Original:</h3>
                            <img src={`http://localhost:5000/uploads/${image.filename}`} alt="Original" />
                            <h3>Procesada:</h3>
                            <img src={`http://localhost:5000/processed/${image.processed_image_filename}`} alt="Procesada" />
                            <p>Clasificación: {image.classification}</p>
                            <button className="delete-button" onClick={() => handleDeleteImage(image.filename)}>Eliminar</button>
                            <button className="download-button" onClick={() => handleDownloadImage(`http://localhost:5000/processed/${image.processed_image_filename}`)}>Descargar</button>
                        </div>
                    ))}
                </div>
                <h2>Estadísticas</h2>
                <div className="statistics">
                    <p>Total de imágenes: {statistics.total_images}</p>
                    <p>Espirales: {statistics.classifications?.Espiral || 0}</p>
                    <p>Elípticas: {statistics.classifications?.Elíptica || 0}</p>
                    <p>Irregulares: {statistics.classifications?.Irregular || 0}</p>
                </div>
                <div className="chart-container">
                    <Bar data={data} />
                </div>
            </div>
        </div>
    );
}

export default ImageUpload;
