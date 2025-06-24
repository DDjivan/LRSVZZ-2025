const socket = io();

socket.on("new order", (data) => {
    window.location.reload(1);
});
