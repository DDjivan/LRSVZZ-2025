document.addEventListener('DOMContentLoaded', function() {
    fetchTickets();

    function fetchTickets() {
        fetch('/tickets')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#ticketTable tbody');
            tableBody.innerHTML = '';
        data.forEach(ticket => {
            const row = document.createElement('tr');
            row.innerHTML = `
            <td>${ticket.id}</td>
            <td>${ticket.status}</td>
            <td>
            <button onclick="updateTicket(${ticket.id}, 'Completed')">Complete</button>
            </td>
            `;
            tableBody.appendChild(row);
        });
        });
    }

    window.updateTicket = function(ticketId, newStatus) {
        fetch(`/update_ticket/${ticketId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ status: newStatus })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                fetchTickets(); // Refresh the ticket list
            }
        });
    };
});
