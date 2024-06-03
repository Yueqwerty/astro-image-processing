document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData();
    var fileInput = document.getElementById('fileInput');
    formData.append('file', fileInput.files[0]);

    fetch('/process_image', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        var resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <p>Original Image: <a href="/data/images/${data.filename}" target="_blank">View</a></p>
            <p>Processed Image: <a href="/data/processed_images/${data.result.processed.split('/').pop()}" target="_blank">View</a></p>
            <p>Classification: ${data.result.classification}</p>
        `;
    })
    .catch(error => console.error('Error:', error));
});
