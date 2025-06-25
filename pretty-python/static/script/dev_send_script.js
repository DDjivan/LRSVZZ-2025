function sendPlans() {
    fetch('/dev/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(errorMessage => {
                throw new Error(errorMessage); // Throw the error message to be caught in the catch block
            });
        }
        return response.text(); // Expecting plain text response for success
    })
    .then(data => {
        document.getElementById('response_plans').innerText = data;
        console.log(data);
    })
    .catch(error => {
        document.getElementById('response_plans').innerText = 'JS Error: Could not send plans: \n' + error.message;
        console.error('There was a problem with the fetch operation:', error);
    });
}
