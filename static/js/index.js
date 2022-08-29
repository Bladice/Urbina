let carousel = document.getElementById('carousel-inner');
let carouselContent = [
    // {class: 'd-block w-100', src: 'https://cdn.pixabay.com/photo/2018/11/03/22/24/fire-3792951_1280.jpg', alt: 'Image 1'},
    {class: 'd-block w-100 h-90', src: 'static/image/downhill.jpg', alt: 'dawnhill 1'},
    {class: 'd-block w-100 h-90', src: 'static/image/urbina_cfi_200.jpg', alt: 'Image 2'},
    {class: 'd-block w-100 h-90', src: 'static/image/mtb_200.jpg', alt: 'Image 3'},
    {class: 'd-block w-100 h-90', src: 'static/image/urbina_cpi_200.jpg', alt: 'Image 4'},
    {class: 'd-block w-100 h-90', src: 'static/image/urbina_gae_200.jpg', alt: 'Image 5'},
    {class: 'd-block w-100 h-90', src: 'static/image/urbina_cd_200.jpg', alt: 'Image 6'}
/*    {class: 'd-block w-100 h-90', src: 'https://cdn.pixabay.com/photo/2018/10/22/11/58/grass-3765172_1280.jpg', alt: 'Image 2'},
    {class: 'd-block w-100 h-90', src: 'https://cdn.pixabay.com/photo/2018/10/07/11/49/fallow-deer-3729821_1280.jpg', alt: 'Image 3'},
    {class: 'd-block w-100 h-90', src: 'https://cdn.pixabay.com/photo/2018/10/07/19/25/walk-3731094_1280.jpg', alt: 'Image 4'},
    {class: 'd-block w-100', src: 'https://cdn.pixabay.com/photo/2018/10/21/19/23/lily-3763573_1280.jpg', alt: 'Image 5'},
    {class: 'd-block w-100', src: 'https://cdn.pixabay.com/photo/2018/09/30/19/03/metro-3714290_1280.jpg', alt: 'Image 6'},
    {class: 'd-block w-100', src: 'https://cdn.pixabay.com/photo/2018/10/21/21/28/autumn-3763897_1280.jpg', alt: 'Image 7'}*/
];

for (let slide of carouselContent) {
    let carouselItem = document.createElement('div');
    carouselItem.classList.add('carousel-item');
    let image = document.createElement('img');
    image.className = slide.class;
    image.src = slide.src;
    image.alt = slide.alt;
    carouselItem.appendChild(image);
    carousel.appendChild(carouselItem);
}

let firstImage = document.getElementsByClassName('carousel-item')[0];
firstImage.classList.add('active');