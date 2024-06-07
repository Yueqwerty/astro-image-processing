import React, { useState } from 'react';
import axios from 'axios';
import './ImageUpload.css';

function ImageUpload() {
    const [file, setFile] = useState(null);
    const [imageURL, setImageURL] = useState('');
    const [results, setResults] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:5000/process_image', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setImageURL(`http://localhost:5000/uploads/${response.data.filename}`);
            setResults(response.data);
        } catch (error) {
            console.error('Error uploading image:', error);
        }
    };

    return (
        <div className="app-container">
            <div className="upload-card">
                <h1>Procesamiento de imágenes</h1>
                <input type="file" onChange={handleFileChange} />
                <button className="upload-button" onClick={handleUpload}>Upload Image</button>
                <div className="image-container">
                    {imageURL && (
                        <div className="image-box">
                            <h3>Original Image:</h3>
                            <img src={imageURL} alt="Uploaded" />
                        </div>
                    )}
                    {results && (
                        <div className="image-box">
                            <h3>Processed Image:</h3>
                            <img src={`http://localhost:5000/processed/${results.result.processed}`} alt="Processed" />
                            <p>Classification: {results.result.classification}</p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default ImageUpload;
