// Function to load external HTML content using the Fetch API.
// Inserts the fetched HTML into the target element and executes any inline/external scripts.
async function loadHeader(url, targetElementId) {
    try {
        const response = await fetch(url, { cache: 'no-cache' });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const html = await response.text();

        const container = document.getElementById(targetElementId);
        if (!container) {
            console.error(`Element with id "${targetElementId}" not found.`);
            return;
        }

        // Insert HTML
        container.innerHTML = html;

        // Execute any scripts contained in the fetched HTML.
        // Note: scripts added via innerHTML do not execute automatically.
        const scripts = container.querySelectorAll('script');
        scripts.forEach(oldScript => {
            const newScript = document.createElement('script');

            // copy attributes like type, async, defer
            if (oldScript.type) newScript.type = oldScript.type;
            if (oldScript.async) newScript.async = true;
            if (oldScript.defer) newScript.defer = true;

            if (oldScript.src) {
                // External script: copy the src so browser fetches and executes it
                newScript.src = oldScript.src;
                // Append to head to preserve global scope and execution behavior
                document.head.appendChild(newScript);
            } else {
                // Inline script: copy text and append to the container
                newScript.textContent = oldScript.textContent;
                container.appendChild(newScript);
            }

            // Remove the original script tag to avoid duplication
            oldScript.remove();
        });
    } catch (error) {
        console.error('Error loading header:', error);
    }
}

// Use a relative path (no leading slash) so the loader works on GitHub Pages project pages.
// Call after DOM is ready to ensure the placeholder element exists.
document.addEventListener('DOMContentLoaded', () => {
    loadHeader('header.html', 'header-placeholder');
});