document.addEventListener('DOMContentLoaded', () => {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const close = document.querySelector('.close');

    galleryItems.forEach(item => {
        item.addEventListener('click', () => {
            lightbox.style.display = 'block';
            lightboxImg.src = item.src;
        });
    });

    close.addEventListener('click', () => {
        lightbox.style.display = 'none';
    });

    lightbox.addEventListener('click', (e) => {
        if (e.target !== lightboxImg) {
            lightbox.style.display = 'none';
        }
    });
});
