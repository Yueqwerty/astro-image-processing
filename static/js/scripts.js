document.addEventListener("DOMContentLoaded", function() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            data.forEach(item => {
                const img = document.createElement('img');
                img.src = '/' + item.result.processed;
                resultsDiv.appendChild(img);
            });
        });
});
