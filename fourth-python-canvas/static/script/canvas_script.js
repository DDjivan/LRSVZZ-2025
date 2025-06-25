const canvas = document.getElementById('bitmapCanvas');
const ctx = canvas.getContext('2d');
const undoStack = [];
const redoStack = [];
let currentTool = 'pixel';
let startPoint = null;
const scaleFactor = 10;
const pixelCursor = document.getElementById('pixelCursor');

function initCanvas() {
    const img = new Image();
    img.src = '/static/plans/1.png';

    img.onload = function() {
        ctx.drawImage(img, 0, 0);
    };

    img.onerror = function() {
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    };
}
initCanvas();

canvas.addEventListener('mousemove', (event) => {
    const rect = canvas.getBoundingClientRect();
    // Calculate the mouse position relative to the canvas
    const x = Math.floor((event.clientX - rect.left) / scaleFactor);
    const y = Math.floor((event.clientY - rect.top) / scaleFactor);

    // Update the position of the pixel cursor to snap to the grid
    pixelCursor.style.left = `${(x * scaleFactor) + rect.left}px`; // Align with the grid
    pixelCursor.style.top = `${(y * scaleFactor) + rect.top}px`; // Align with the grid
    pixelCursor.style.display = 'block'; // Show the cursor
});

canvas.addEventListener('mouseleave', () => {
    pixelCursor.style.display = 'none'; // Hide the cursor when leaving the canvas
});

canvas.addEventListener('click', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = Math.floor((event.clientX - rect.left) / scaleFactor);
    const y = Math.floor((event.clientY - rect.top) / scaleFactor);

    if (currentTool === 'pixel') {
        drawPixel(x, y);
    } else if (currentTool === 'rectangle') {
        if (!startPoint) {
            startPoint = { x, y };
        } else {
            drawRectangle(startPoint.x, startPoint.y, x, y);
            startPoint = null; // Reset for next rectangle
        }
    }
});

function drawPixel(x, y) {
    // ctx.fillStyle = 'black';
    ctx.fillStyle = '#000000';
    ctx.fillRect(x, y, 1, 1);
    saveState();
}

function drawBasicRectangle(x1, y1, x2, y2, color) {
    ctx.fillStyle = color;

    const x0 = Math.min(x1, x2);
    const y0 = Math.min(y1, y2);
    const x_size = Math.abs(x2 - x1) +1;
    const y_size = Math.abs(y2 - y1) +1;

    ctx.fillRect(x0, y0, x_size, y_size);
}

function drawRectangle(x1, y1, x2, y2) {
    const color_fill = '#000000';
    const color_border = '#55ff7f';
    const color_corner = '#55aa7f';

    // fill
    ctx.fillStyle = color_fill;
    drawBasicRectangle(x1, y1, x2, y2, color_fill);

    // border
    ctx.fillStyle = color_border;
    drawBasicRectangle(x1, y1, x2, y1, color_border);
    drawBasicRectangle(x2, y1, x2, y2, color_border);
    drawBasicRectangle(x1, y1, x1, y2, color_border);
    drawBasicRectangle(x1, y2, x2, y2, color_border);

    // corner
    ctx.fillStyle = color_corner;
    ctx.fillRect(x1, y1, 1, 1);
    ctx.fillRect(x2, y1, 1, 1);
    ctx.fillRect(x1, y2, 1, 1);
    ctx.fillRect(x2, y2, 1, 1);

    saveState();
}

function clearCanvas() {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    saveState();
}

function saveState() {
    undoStack.push(canvas.toDataURL());
    redoStack.length = 0;
}

document.getElementById('clearButton').addEventListener('click', clearCanvas);
document.getElementById('undoButton').addEventListener('click', undo);
document.getElementById('redoButton').addEventListener('click', redo);

function undo() {
    if (undoStack.length > 0) {
        redoStack.push(undoStack.pop());
        const lastState = undoStack[undoStack.length - 1];
        if (lastState) {
            const img = new Image();
            img.src = lastState;
            img.onload = () => ctx.drawImage(img, 0, 0);
        } else {
            initCanvas(); // Clear if no more states
        }
    }
}

function redo() {
    if (redoStack.length > 0) {
        const redoState = redoStack.pop();
        undoStack.push(redoState);
        const img = new Image();
        img.src = redoState;
        img.onload = () => ctx.drawImage(img, 0, 0);
    }
}

document.getElementById('pixelToolButton').addEventListener('click', () => {
    currentTool = 'pixel';
});

document.getElementById('rectangleToolButton').addEventListener('click', () => {
    currentTool = 'rectangle';
});

// document.getElementById('sendButton').addEventListener('click', () => {
//     const imageData = canvas.toDataURL('image/png');
//     fetch('/upload', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ image: imageData }),
//     })
//     .then(response => {
//         if (response.ok) {
//             alert('Image sent successfully!');
//         } else {
//             alert('Error sending image.');
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });

document.getElementById('sendButton').addEventListener('click', () => {
    canvas.toBlob((blob) => {
        const formData = new FormData();
        formData.append('image', blob, 'canvas-image.png');

        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (response.ok) {
                alert('Image sent successfully!');
            } else {
                alert('Error sending image.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }, 'image/png');
});
