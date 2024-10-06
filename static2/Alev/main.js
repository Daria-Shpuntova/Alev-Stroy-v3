$('.carusel').slick({
    centerMode: true,
    centerPadding: '10px',
    slidesToShow: 3,
    responsive: [
      {
        breakpoint: 991,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 1
        }
      }
    ]
});


