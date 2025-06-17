const myDomain = window.location.hostname; 

const links = document.querySelectorAll('a');

links.forEach(link => {
    const img = document.createElement('img');

    img.className = 'icon'; // icon class for CSS 

    const href = link.getAttribute('href');

    if (href.startsWith('http://') || href.startsWith('https://')) {

        const linkDomain = new URL(href).hostname; 

        if (linkDomain == myDomain) {
            img.src = svgIconLinkInternal;
            img.alt = 'Internal Link';

        } else {
            img.src = svgIconLinkExternal;
            img.alt = 'External Link';

    }
    } else if (href.startsWith('appstream:')) {
        img.src = svgIconLinkFlathub;
        img.alt = 'Flathub Link'; 

    } else if (href.startsWith('mailto:')) {
        img.src = svgIconLinkEmail;
        img.alt = 'Email Link'; 

    } else {
        // img.src = svgIconLink; // var defined in the HTML
        // img.alt = 'Link Icon'; // alt attribute for accessibility
        img.src = svgIconLinkInternal;
        img.alt = 'Internal Link';

    }

    link.appendChild(img);
});
