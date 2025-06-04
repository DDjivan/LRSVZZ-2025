function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// function executeScript() {
async function executeScript() {
    // temp optional loading message
    document.getElementById('response').innerText = 'Executing...';  

    await sleep(1000); // milliseconds    

    // actual execution 
    fetch('/execute_script')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('response').innerText = data;
        })
        .catch(error => {
            document.getElementById('response').innerText = 'Error: ' + error.message;
        });
}


// function executeScript() {
async function moteurMarche() {
    // temp optional loading message
    document.getElementById('response').innerText = 'Executing...';

    await sleep(1000); // milliseconds

    // actual execution
    fetch('/moteurMarche')
}
