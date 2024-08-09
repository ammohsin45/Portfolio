// Get the modal elements
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const closeBtn = document.getElementsByClassName('close')[0];

// Function to open the lightbox with the clicked image
document.querySelectorAll('.gallery-item img').forEach(img => {
    img.addEventListener('click', function() {
        lightbox.style.display = 'block';
        lightboxImg.src = this.src;
    });
});

// Function to close the lightbox
closeBtn.addEventListener('click', function() {
    lightbox.style.display = 'none';
});

// Close the lightbox when clicking outside the image
lightbox.addEventListener('click', function(event) {
    if (event.target === lightbox) {
        lightbox.style.display = 'none';
    }
});
