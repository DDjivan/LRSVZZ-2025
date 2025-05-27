function executeScript() {
    fetch('/execute_script')
    .then(response => response.text())
    .then(data => {
        document.getElementById('response').innerText = data;
    });
}
