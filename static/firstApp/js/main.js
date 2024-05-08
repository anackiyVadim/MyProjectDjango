$(function () {
    document.querySelectorAll('.sells__cart-grade').forEach(item =>
            item.addEventListener('click', () => 
                item.parentNode.dataset.totalValue = item.dataset.itemValue
            )
        );

        // not is discount
    const firstB = $(".sells__cart-sale");
        var firstC = $.makeArray(firstB)

        for (let i = 0; i < firstC.length; i++) {
            const element = firstC[i];
            if(element.textContent == ""){
                element.parentNode.style.display = "none"
            }else{
                element.parentNode.style.display = "flex"
            }
        }


    // main logic
    $('.first-box__slider-wrapp').slick({
        dots: true,
        arrows: false,
        fade: false,
        autoplay: true,
        slidesToScroll: 1,
        slidesToShow: 1,
    });
    $('.product-cart__slider').slick({
        dots: false,
        arrows: false,
        fade: true,
        autoplay: false,
        slidesToScroll: 1,
        asNavFor: '.product-cart__slider-nav',
        slidesToShow: 1,
        responsive: [
            {
            breakpoint: 1024,
            settings: {
                slidesToScroll: 1,

            }
        },
        {
            breakpoint: 600,
            settings: {
               slidesToScroll: 1,
               dots: true,
               autoplay: true
            }
        },
        {
            breakpoint: 480,
            settings: {
               slidesToScroll: 1,
               dots: true,
               autoplay: true
                
            }
        }
    ],
    });
    $('.product-cart__slider-nav').slick({
        dots: false,
        vertical: true,
        verticalSwiping: true,
        slidesToShow: 10,
        arrows: false,
        asNavFor: '.product-cart__slider',
        autoplay: false,
        focusOnSelect: true,
        slidesToScroll: 1,
        
    });
    // history test slider

    // $('.account__history-wrapp').slick({
    //     dots: true,
    //     arrows: false,
    //     fade: false,
    //     slidesToShow: 6,
    // });

    // -------------------------------------------------------
    $('.nav-media__inner-catalog').on('click', function (){
        $('.catalog-media').addClass('catalog-media__open')
    })
    $('.catalog-media__close').on('click', function (){
        $('.catalog-media').removeClass('catalog-media__open')
    })
    $('.product-cart__head-reviews').on('click', function (){
        $('.product-cart__reviews-box-wrapp').addClass('product-cart__display-block')
    })
    $('.product-cart__head-reviews').on('click', function (){
        $('.product-cart__reviews-box-wrapp').addClass('product-cart__display-block')
    })
    // account logic
    $('.account__btn-general').on('click', function (){
        // btn 
        $('.account__btn-general').addClass('account__btn-active')

        $('.account__btn-personal').removeClass('account__btn-active')
        $('.account__btn-history').removeClass('account__btn-active')
        $('.account__btn-order').removeClass('account__btn-active')
        $('.account__btn-password').removeClass('account__btn-active')
        
        // box
        $('.account__general').addClass('account__active-wrapp')

        $('.account__personal').removeClass('account__active-wrapp')
        $('.account__history').removeClass('account__active-wrapp')
        $('.account__order').removeClass('account__active-wrapp')
        $('.account__password').removeClass('account__active-wrapp')
    })
    $('.account__btn-personal').on('click', function (){
        $('.account__btn-personal').addClass('account__btn-active')

        $('.account__btn-general').removeClass('account__btn-active')
        $('.account__btn-history').removeClass('account__btn-active')
        $('.account__btn-order').removeClass('account__btn-active')
        $('.account__btn-password').removeClass('account__btn-active')
        
        // box
        $('.account__personal').addClass('account__active-wrapp')

        $('.account__general').removeClass('account__active-wrapp')
        $('.account__history').removeClass('account__active-wrapp')
        $('.account__order').removeClass('account__active-wrapp')
        $('.account__password').removeClass('account__active-wrapp')
    })
    $('.account__btn-history').on('click', function (){
        $('.account__btn-history').addClass('account__btn-active')

        $('.account__btn-general').removeClass('account__btn-active')
        $('.account__btn-personal').removeClass('account__btn-active')
        $('.account__btn-order').removeClass('account__btn-active')
        $('.account__btn-password').removeClass('account__btn-active')

        // box
        $('.account__history').addClass('account__active-wrapp')

        $('.account__general').removeClass('account__active-wrapp')
        $('.account__personal').removeClass('account__active-wrapp')
        $('.account__order').removeClass('account__active-wrapp')
        $('.account__password').removeClass('account__active-wrapp')

    })
    $('.account__btn-order').on('click', function (){
        $('.account__btn-order').addClass('account__btn-active')

        $('.account__btn-general').removeClass('account__btn-active')
        $('.account__btn-personal').removeClass('account__btn-active')
        $('.account__btn-history').removeClass('account__btn-active')
        $('.account__btn-password').removeClass('account__btn-active')
    
        // box
        $('.account__order').addClass('account__active-wrapp')

        $('.account__general').removeClass('account__active-wrapp')
        $('.account__personal').removeClass('account__active-wrapp')
        $('.account__history').removeClass('account__active-wrapp')
        $('.account__password').removeClass('account__active-wrapp')

    })
    $('.account__btn-password').on('click', function (){
        $('.account__btn-password').addClass('account__btn-active')

        $('.account__btn-general').removeClass('account__btn-active')
        $('.account__btn-personal').removeClass('account__btn-active')
        $('.account__btn-history').removeClass('account__btn-active')
        $('.account__btn-order').removeClass('account__btn-active')
    
        // box
        $('.account__password').addClass('account__active-wrapp')

        $('.account__general').removeClass('account__active-wrapp')
        $('.account__personal').removeClass('account__active-wrapp')
        $('.account__history').removeClass('account__active-wrapp')
        $('.account__order').removeClass('account__active-wrapp')

    })
})