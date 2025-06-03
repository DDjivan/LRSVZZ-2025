const links = document.querySelectorAll('a');

links.forEach(link => {
    const img = document.createElement('img');
    img.src = svgIconPath; // var defined in the HTML
    img.alt = 'Icon'; // alt attribute for accessibility
    img.className = 'icon'; // icon class for CSS 
    link.appendChild(img);
});
