    /**
         * Fonction asynchrone pour récupérer une chaîne de caractères depuis l'API Flask.
         * Utilise l'API Fetch pour faire une requête GET à /get_string.
         */
        async function getStringFromPython() {
            // Effectue une requête GET à l'API Flask
            const response = await fetch('http://127.0.0.1:5000/get_string');

            // Parse la réponse JSON en un objet JavaScript
            const data = await response.json();

            // Affiche la chaîne reçue dans l'élément HTML approprié
            document.getElementById('pythonStringResult').innerText = "Chaîne de Python : " + data.message;
        }
