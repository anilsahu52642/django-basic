// $('#slider1, #slider2, #slider3').owlCarousel({
//     loop: true,
//     margin: 20,
//     responsiveClass: true,
//     responsive: {
//         0: {
//             items: 1,
//             nav: false,
//             autoplay: true,
//         },
//         600: {
//             items: 3,
//             nav: true,
//             autoplay: true,
//         },
//         1000: {
//             items: 5,
//             nav: true,
//             loop: true,
//             autoplay: true,
//         }
//     }
// })



$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true,
            autoplay:true,
        },
        600:{
            items:3,
            // nav:false,

            nav: true,
            autoplay: true,
        },
        1000:{
            items:5,
            nav:true,
            // loop:false,
            loop:true,
            autoplay:true,
        }
    }
})
