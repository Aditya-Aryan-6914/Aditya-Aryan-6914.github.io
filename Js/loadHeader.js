// Function to load external HTML content using the Fetch API (more modern than XMLHttpRequest)
function loadHeader(url, targetElementId) {
    fetch(url)
        .then(response => {
            // Check if the request was successful (status 200)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text(); // Get the HTML content as text
        })
        .then(html => {
            // Find the placeholder and insert the fetched HTML
            document.getElementById(targetElementId).innerHTML = html;
        })
        .catch(error => {
            console.error('Error loading the header:', error);
        });
}

// *** IMPORTANT: You may need to adjust the path to '/header.html' based on your repository structure.
loadHeader('/header.html', 'header-placeholder');