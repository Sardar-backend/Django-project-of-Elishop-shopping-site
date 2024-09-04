$(document).ready(function () {
    // add swiper main slider to home page
    let swiper = new Swiper('.main-slider__inner', {
        spaceBetween: 30,
        effect: 'fade',
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
});


$(document).ready(function () {
    // add swiper main slider to home page
    let discountSlider = new Swiper('.discounts-slider__inner', {
        spaceBetween: 30,
        effect: 'fade',
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
    // add swiper products slider
    let productsSlider = new Swiper('.products-slider__inner', {
        slidesPerView: 6,
        slidesPerGroup: 5,
        lazy: {
            enabled: true
        },
        navigation: {
            nextEl: '.next-slide-button',
            prevEl: '.prev-slide-button',
        },
        keyboard: {
            enabled: true,
            onlyInViewport: true
        },
        breakpoints: {
            1367: {
                slidesPerView: 4,
                slidesPerGroup: 3,
                spaceBetweenSlides: 1
            },
            1679: {
                slidesPerView: 5,
                slidesPerGroup: 4,
                spaceBetweenSlides: 1
            }
        }
    });
    // add brands swiper slider
    let brandsSlider = new Swiper('.brands-slider__inner', {
        slidesPerView: 6,
        slidesPerGroup: 6,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        navigation: {
            nextEl: '.next-slide-button',
            prevEl: '.prev-slide-button',
        },
        breakpoints: {
            1679: {
                slidesPerView: 5,
                spaceBetweenSlides: 1
            }
        }
    });
    // add trigger if slide changed arrow pointer change same one
    discountSlider.on('slideChange', function () {

        let activeIndex = discountSlider.activeIndex;
        let discountListTitle = jQuery(".main .main__inner .home .home__inner .right .discounts .discounts-title-list .discounts-title-list__inner .items");
        $(discountListTitle).find(".item").each(function () {
            let _this = jQuery(this);
            _this.removeClass("active");
        });
        $(discountListTitle).find(`[data-discount-id = ${activeIndex} ]`).addClass("active");
    });
    let discountItem = jQuery(".main .main__inner .home .home__inner .right .discounts .discount-item").each(function () {
        let _this = jQuery(this);
        let self = _this.find(".discount-time-to-left .discount-time-to-left__inner");
        let selfTimeLeft = _this.find(".discount-time-to-left .discount-time-to-left__inner").attr("data-time-left");
        timeLeftCounter(selfTimeLeft, self, "<span class='finish-time-left--text'>تمام شد</span>", true);
    });

    //change active tabs in single product information
    let tabs = $(".single-product-page .single-product-page__inner .product-full-information .product-full-information__inner .tabs .tab");
    $(tabs).click(function () {
        let tabId = $(this).attr('data-tab-id');
        $(tabs).each(function () {
            $(this).removeClass("active");
        });
        $(this).addClass("active");
        let productFulInformationInner = $(this).parent().parent();
        let content = productFulInformationInner.find(".contents .content-item");
        content.each(function () {
            $(this).removeClass("show");
        });
        $(productFulInformationInner).find(`[data-self-tab-id=${tabId}]`).addClass('show');
    })

    // config bar-rating-js
    $('#pd-rating').barrating('show', {
        theme: 'pd-rating',
        hoverState: true
    });
    $('#pd-rating').barrating('set', 'Mediocre');

    //config fancybox
    $('[data-fancybox="pd-gallery"]').fancybox({
        buttons: ["close", "thumbs", "share", "zoom"],
    });

    //show/hide social share
    let socialButton = $(".single-product-page .single-product-page__inner .share__like .mdi-share-variant");
    $(socialButton).click(function () {
        $(".single-product-page .single-product-page__inner .share__like .items").toggleClass("visible");
    });

    jQuery(".home .discounts .discounts-title-list__inner .items .item").click(function () {
        let sliderItemId = jQuery(this).attr("data-discount-id");
        console.log(sliderItemId);
        discountSlider.slideTo(sliderItemId);
    });

    //
    jQuery(".profile-page .menus .menu .menu__inner").click(function () {
        let thiz = jQuery(this).parent();
        if(thiz.find(".sub-menu").length > 0){
            thiz.find(".sub-menu").toggleClass("p-menu-hidden", 800, 'easeOutQuint');
            thiz.find(".mdi-chevron-down").toggleClass("rotate180");
        }
    });
});

// calculating time counter
function timeLeftCounter(date, element, text, hasHour) {

    let countDownDate = new Date(date).getTime();
    let x = setInterval(function () {

        let now = new Date().getTime();

        // Find the distance between now and the count down date
        let distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        let days = Math.floor(distance / (1000 * 60 * 60 * 24));
        let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor((distance % (1000 * 60)) / 1000);
        hours = hours > 9 ? "" + hours : "0" + hours;
        minutes = minutes > 9 ? "" + minutes : "0" + minutes;
        seconds = seconds > 9 ? "" + seconds : "0" + seconds;

        // Output the result in an element with id="demo"
        if(hasHour) {
            jQuery(element).text(hours + ":" + minutes + ":" + seconds).persiaNumber();
        }else{
            jQuery(element).text(minutes + ":" + seconds).persiaNumber();
        }
        // If the count down is over, write some text
        if (distance < 0) {
            clearInterval(x);
            jQuery(element).html(text);
        }
    }, 1000);


}

// config the sticky sidebar for single-post
jQuery(document).ready(function () {
    jQuery('.search-side-bar, .search-main-bar').theiaStickySidebar({
        // Settings
        additionalMarginTop: 30
    });
});


jQuery(window).on('load', function () {

    //config zoom image product in single product page
    jQuery("#zoom_01").ezPlus({
        zoomWindowPosition: 10,
        zoomWindowHeight: 450,
        zoomWindowWidth: 550,
        lensFadeIn: 200,
        lensFadeOut: 200,
        lensBorderSize: 2.5,
        lensBorderColour: '#ee4000',
        lensColour: 'transparent',
        borderColour: '#ddd',
        zoomTintFadeIn: 200,
        zoomTintFadeOut: 200,
        scrollZoom: false,
        scrollZoomIncrement: 0.3,
        easing: true,
        cursor: "crosshair",
        tint: false,
        tintColour: '#fff',
        tintOpacity: 0,
        borderSize: 1,
        delay: 300,
        easingDuration: 150
    });
});

// price-slider-range config in search page
var slider = document.querySelector('#pd-price-range');
let $raneSliderFrom = jQuery('.price-slider-box .from-price .price').attr('data-value');
let $raneSliderTo = jQuery('.price-slider-box .to-price .price').attr('data-value');
let min = parseInt($raneSliderFrom);
let max = parseInt($raneSliderTo);
if (slider) {
    noUiSlider.create(slider, {
        start: [min, max],
        connect: true,
        format: wNumb({
            decimals: 0
        }),
        range: {
            'min': min,
            'max': max
        },
        direction: 'rtl'
    });
    slider.noUiSlider.on('update', function (values, handle) {
        jQuery('.price-slider-box .from-price .price').text(tomansCurrency(values[0])).persiaNumber();
        jQuery('.price-slider-box .to-price .price').text(tomansCurrency(values[1])).persiaNumber();
    });
}

// filter brands side-bar form in search page

let brandsSearchInput = jQuery(".brands-box .search-in-brands--input");
brandsSearchInput.on("input", function () {
    let searchedTxt = jQuery(this).val();
    let $brandsItem = jQuery(".brands .brand-item");
    $($brandsItem).each(function () {
        jQuery(this).removeClass("hidden");
    });
    $($brandsItem).each(function () {
        let brandItemTxt = jQuery(this).find(".brand-item__inner label").text();
        if (!brandItemTxt.includes(searchedTxt)) {
            jQuery(this).addClass("hidden");
        }
    })
});

// toggle class has-drop-down boxes hide/show

jQuery(document).ready(function () {
    let dropDownBox = jQuery(".boxes .box .has-drop-down");
    jQuery(dropDownBox).find(".box-title .icon").click(function () {
        jQuery(this).toggleClass("mdi-window-minimize").toggleClass("mdi-open-in-new");
        let parentBox = parentByClass(jQuery(this), "box");
        parentBox.find(".box-content").toggleClass("no-active");
    });
});

// active filter item in search page
let filtersItem = jQuery(".search-main-bar .filters .filter");
jQuery(filtersItem).click(function () {
    jQuery(filtersItem).each(function () {
        jQuery(this).removeClass("active");
    });
    jQuery(this).addClass("active");
    let sortType = jQuery(this).attr("data-sort");
    $.ajax({
        type: 'GET',
        data: {
            filter_type: sortType
        },

    })
});

// find parent's parent by class given
function parentByClass(_element, _class) {
    while (_element.tagName !== 'body') {
        if (_element.hasClass(_class)) {
            return _element;
        } else {
            _element = _element.parent();
        }
    }
}
// check if brands filter checked true in search page
function ifbrandsChekedTrue() {
    let brandsId = [];

    jQuery(".search-page .search-side-bar .brands-box .brand-item").each(function () {
        if (jQuery(this).find(".md-checkbox input").prop("checked")) {
            brandsId.push(`${jQuery(this).find(".md-checkbox input").attr("data-brand-id")}`);
        }
    });
    console.log(brandsId);
    return brandsId;
}

// check all active search-main-bar sorts
function activeSort() {
    let sortId = null;
    jQuery(".search-page .search-main-bar .filters .filter").each(function () {
        if (jQuery(this).hasClass("active")) {
            sortId = jQuery(this).attr("data-sort-id");
        }
    });
    return sortId;
}


// check all filters element for if user use filter
function searchPageAjaxFilter() {
    let params = {};
    let priceMinSet = parseInt(slider.noUiSlider.get()[0]);
    let priceMaxSet = parseInt(slider.noUiSlider.get()[1]);
    let searchInResultInput = jQuery(".search-page .search-side-bar .search-in-result .search-in-result--input");
    let searchExistProduct = jQuery(".search-page .search-side-bar .existing-pd-box .switch-input");
    let searchReadyProduct = jQuery(".search-page .search-side-bar .ready-pd-box .switch-input");
    if (priceMinSet != min) {
        params.price_min = slider.noUiSlider.get()[0];
    }
    if (priceMaxSet != max) {
        params.price_max = slider.noUiSlider.get()[1];
    }
    if ((ifbrandsChekedTrue().length > 0)) {

        params.brands = ifbrandsChekedTrue();
    }
    if (activeSort()) {
        params.sort_type= activeSort();
    }
    if (jQuery(searchInResultInput).val() !== "") {
        params.search_result = jQuery(searchInResultInput).val();
    }
    if (searchExistProduct.prop("checked")) {
        params.only_selling=true;
    }
    if (searchReadyProduct.prop("checked")) {
        params.only_ready=true;
    }
    let categorySlug = jQuery(".main").attr('data-category-name');
    let token = jQuery("meta[name='csrf-token']").attr("content");
    params.category_name = categorySlug;
    jQuery.ajax({
        url: '/Product/filter',
        method: "POST",
        dataType: 'html',
        data: params,
        beforeSend: function (request) {
            jQuery(".loading-svg").toggleClass("hidden");
            request.setRequestHeader('X-CSRF-TOKEN', token)
        },
        success: function (response) {
            jQuery(".search-page .products .products__inner .product").remove();
            jQuery(".search-page .products .products__inner").append(response);
            jQuery(".loading-svg").toggleClass("hidden");
        },
        error : function () {
            jQuery(".loading-svg").toggleClass("hidden");
        }
    });
}
jQuery(document).ready(function () {

    // add all events filters and sorts in search page
    let sorts = jQuery(".search-page .search-main-bar .filters .filter");
    let searchExistProduct = jQuery(".search-page .search-side-bar .existing-pd-box .switch-input");
    let priceLimiter = jQuery(".search-page .search-side-bar .price-slider-box .button-filter .button-filter__inner")
    let searchReadyProduct = jQuery(".search-page .search-side-bar .ready-pd-box .switch-input");
    let brandsFilter = jQuery(".search-page .search-side-bar .brands-box .brands .brand-item");
    let searchInResultBtn = jQuery(".search-page .search-side-bar .search-box .search-in-result .search-in-result--btn");

    jQuery.merge(sorts, priceLimiter, searchInResultBtn).click(function () {
        searchPageAjaxFilter();
    });
    jQuery.merge(searchExistProduct, searchReadyProduct).change(function () {
        searchPageAjaxFilter();
    });
    jQuery(brandsFilter).change(function () {
       searchPageAjaxFilter();
    });
    jQuery(searchInResultBtn).click(function () {
        searchPageAjaxFilter();
    });

    // add quantity product in cart page
    let cartItem = jQuery(".cart-page .cart-main-bar .cart-main-bar__inner .cart-item .cart-item__inner");
    let addCartItem = jQuery(cartItem).find(".mdi-plus");
    let removeCartItem = jQuery(cartItem).find(".mdi-minus");
    jQuery(addCartItem).click(function () {
        let pNumberReg = /[\u06F0-\u06F90-9]+/;
        let quantityCartItemString = jQuery(this).parent().parent().find(".value").text();
        //console.log(quantityCartItemString);
        let pdId = parentByClass(jQuery(this), "cart-item").attr("data-pd-id");
        let quantity = parseInt(persianParseInt(pNumberReg.exec(quantityCartItemString)[0]));
        if(quantity + 1 > 5){
            showSnackbar("امکان سفارش بیشتر از ۵ عدد برای هر محصول وجود ندارد!");
            return;
        }
        $.ajax({
            type: 'POST',
            url: 'check-cart.php',
            data: {
                pd_id : pdId,
                pd_quantity: quantity
            },
            beforeSend: function(){
                jQuery(".loading-svg").toggleClass("hidden");
            },
            success: function () {
                jQuery(".loading-svg").toggleClass("hidden");
            },
            error: function () {
                jQuery(".loading-svg").toggleClass("hidden");
            }
        });
        quantity = quantity + 1;
        jQuery(this).parent().parent().find(".value").html(`${quantity.toLocaleString('fa')} عدد `);
    });
    // remove quantity product in cart page
    jQuery(removeCartItem).click(function () {

        let pNumberReg = /[\u06F0-\u06F90-9]+/;
        let quantityCartItemString = jQuery(this).parent().parent().find(".value").text();
        let pdId = parentByClass(jQuery(this), "cart-item").attr("data-pd-id");
        //console.log(quantityCartItemString);
        let quantity = parseInt(persianParseInt(pNumberReg.exec(quantityCartItemString)[0]));
        if(quantity - 1  < 1){
            showSnackbar("تعداد محصول سفارش شما صفر نمیتواند باشد!");
            return
        }
        $.ajax({
            type: 'POST',
            url: 'check-cart.php',
            data: {
                pd_id : pdId,
                pd_quantity: quantity
            },
            beforeSend: function(){
                jQuery(".loading-svg").toggleClass("hidden");
            },
            success: function () {
                jQuery(".loading-svg").toggleClass("hidden");
            },
            error: function () {
                jQuery(".loading-svg").toggleClass("hidden");
            }
        });
        quantity = quantity - 1;
        jQuery(this).parent().parent().find(".value").html(`${quantity.toLocaleString('fa')} عدد `);
    });

    // remove product with close icon in cart page
    jQuery(".cart-page .cart-items .cart-item .cart-item__inner .close").click(function () {
        let thiz = jQuery(this);
        let pdId = parentByClass(jQuery(this), "cart-item").attr("data-pd-id");
        jQuery.ajax({
            url: 'check-cart.php',
            type: 'POST',
            data: {
                pd_id : pdId ,
            },
            success: function () {
                jQuery(".loading-svg").toggleClass("hidden");
                parentByClass(thiz, "cart-item").remove();
            },
            error: function () {
                jQuery(".loading-svg").toggleClass("hidden");
                parentByClass(thiz, "cart-item").remove();
            },
            beforeSend: function () {
                jQuery(".loading-svg").toggleClass("hidden");
            }
            
        })
    })

    // open dialog registration / login
    jQuery(".header .reg-log .reg-log--text").click(function () {
        if(jQuery("#reg-log__dialog .login__form").length){
            jQuery(".reg-log__dialog .reg-log__dialog__inner").css("display", "flex");
            return;
        }
        if(jQuery("#reg-log__dialog .register__form").length){
            jQuery("#reg-log__dialog .register__form").remove();
            jQuery("#reg-log__dialog .log__ref").remove();
        }
        else if(jQuery("#reg-log__dialog .forget-password").length){
            jQuery("#reg-log__dialog .forget-password__form").remove();
            jQuery("#reg-log__dialog .log__ref").remove();
        }
        jQuery("#reg-log__dialog .dialog__content .row").append(`<div class="login__form col-md-8"><script>var account_image =  "./asset/images/account.png";jQuery("#account--image").attr("src", account_image);</script><div class="login__form__inner"> <h4 class="title">ورود به حساب کاربری</h4> <div class="username"> <span class="mdi mdi-account"></span> <input placeholder="نام کاربری" type="text" class="username--inp"> </div><div class="password"> <span class="mdi mdi-lock"></span> <input placeholder="رمز عبور" type="password" class="password--inp"> </div><span class="forget--password">فراموشی رمزعبور</span> <div class="submit-login"> <button class="submit-login--btn">ورود به حساب کاربری</button> </div></div></div><div class="reg__ref col-md-4"> <div class="reg__ref__inner"> <div class="reg--image"><img id="account--image" src="" alt=""></div><div class="reg--text">برای خریدکردن و آگاهی از اطلاعات کاربری خود در باستینک ثبت نام کنید.</div><div class="reg-btn"><a id="reg-btn__inner" href="#">ثبت نام</a></div></div></div>`);
        jQuery(".reg-log__dialog .reg-log__dialog__inner").css("display", "flex");
    });

    // open dialog for registration
    var reg_open_dialog = jQuery("#reg-btn__inner");
    var body = jQuery("body");
    body.on("click", "#reg-btn__inner", function () {
        jQuery("#reg-log__dialog .login__form").remove();
        jQuery("#reg-log__dialog .reg__ref").remove();
        jQuery("#reg-log__dialog .dialog__content .row").append(`<div class="register__form col-md-8"> <script>var account_image="./asset/images/account.png"; jQuery("#account--image").attr("src", account_image); </script> <div class="register__form__inner"><h4 class="title">ثبت‌نام در باستینک</h4><span class="show-status"></span> <div class="mobile"><span class="mdi mdi-phone"></span> <input maxlength="11" minlength="11" id="reg-username" placeholder="شماره موبایل" type="text" name="reg-mobile--inp" class="mobile--inp"></div><div class="email"><span class="mdi mdi-email"></span> <input id="reg-email" placeholder="پست الکترونیکی" type="email" name="reg-email--inp" class="email--inp"></div><div class="password"><span class="mdi mdi-lock"></span> <input id="reg-password" placeholder="رمز عبور" type="password" name="reg-password--inp" class="password--inp"></div><div class="privacy-policy-check"><span class="arrow mdi mdi-arrow-left-bold"></span><label class="privacy-policy-check__inner" for="privacy-policy-check"> <span class="md-checkbox"> <input class="privacy-policy-check--inp" name="reg-privacy-policy-check--inp" id="privacy-policy-check" type="checkbox"> <label for="privacy-policy-check">سیاست حریم خصوصی<a href="http://bastink.com/privacy-policy">باستینک</a>را خواندم و آن را قبول دارم</label> </span> </label></div><div class="submit-register"> <button class="submit-register--btn"><span class="text">ثبت‌نام در باستینک</span> <span class="mdi mdi-loading"></span></button> </div></div></div><div class="log__ref col-md-4"> <div class="log__ref__inner"> <div class="log--image"><img id="account--image" src="" alt=""></div><div class="log--text">قبلا ثبت‌نام کرده‌اید؟</div><div class="log-btn"><a id="log-btn__inner" href="#">ورود به باستینک</a></div></div></div>`);
    });

    // open dialog for login
    body.on("click", "#log-btn__inner", function () {
        jQuery("#reg-log__dialog .register__form").remove();
        jQuery("#reg-log__dialog .log__ref").remove();
        jQuery("#reg-log__dialog .forget-password__form").remove();
        jQuery("#reg-log__dialog .dialog__content .row").append(`<div class="login__form col-md-8"> <script>var account_image="./asset/images/account.png"; jQuery("#account--image").attr("src", account_image);</script> <div class="login__form__inner"><h4 class="title">ورود به حساب کاربری</h4><span class="show-status"></span> <div class="username"><span class="mdi mdi-phone"></span> <input placeholder="شماره موبایل" type="text" name="log-username--inp" class="username--inp"></div><div class="password"><span class="mdi mdi-lock"></span> <input placeholder="رمز عبور" type="password" name="log-password--inp" class="password--inp"></div><span class="forget--password">فراموشی رمزعبور</span> <div class="submit-login"> <button class="submit-login--btn"><span class="text">ورود به حساب کاربری</span> <span class="mdi mdi-loading"></span></button> </div></div></div><div class="reg__ref col-md-4"> <div class="reg__ref__inner"> <div class="reg--image"><img id="account--image" src="" alt=""></div><div class="reg--text">برای خریدکردن و آگاهی از اطلاعات کاربری خود در ایراماشین ثبت نام کنید.</div><div class="reg-btn"><a id="reg-btn__inner" href="#">ثبت نام</a></div></div></div>`);
    });

    //open forget-password form
    body.on("click", "#reg-log__dialog .forget--password", function () {
        console.log("awasa");
        jQuery("#reg-log__dialog .login__form").remove();
        jQuery("#reg-log__dialog .reg__ref").remove();
        jQuery("#reg-log__dialog .dialog__content .row").append(`<div class="forget-password__form col-md-8"> <div class="forget-password__form__inner"><h4 class="title">بازیابی رمز عبور</h4><span class="show-status"></span> <div class="forget-password"><span class="mdi mdi-account"></span> <input id="reg-username" name="forget-password--inp" placeholder="شماره موبایل شما" type="text" class="forget-password--inp"></div><div class="submit-forget-password"> <button class="submit-forget-password--btn"><span class="text">بازیابی رمز عبور</span> <span class="mdi mdi-loading hidden"></span></button> </div></div></div><div class="log__ref col-md-4"> <div class="log__ref__inner"> <div class="log--image"><img id="account--image" src="./asset/images/account.png" alt=""></div><div class="log--text">قبلا ثبت&zwnj;نام کرده&zwnj;اید؟</div><div class="log-btn"><a id="log-btn__inner" href="#">ورود به باستینک</a></div></div></div>`);
    });
});


// config snackbar
jQuery(".snackbar .figure-out").click(function () {
   jQuery(".snackbar").css("transform", "translateY(-60px)");
});
function showSnackbar(message) {
    let snackbar = jQuery(".snackbar");
    jQuery(snackbar).find(".title").html(message);
    setTimeout(function () {
        jQuery(snackbar).css("transform", "translateY(-60px)");
    }, 4000);
    jQuery(snackbar).css("transform", "translateY(0px)");
}

var menus = jQuery('.header .header__inner .main__menu .main__menu__inner .items .item');

menus.hover(
    function () {
        // console.log(111);
        menus.each(function () {
            jQuery(this).find(".underLine").removeClass("unline--active");
            jQuery(this).removeClass("menu-item--active");
        });
        jQuery(".sub__menu").each(function () {
            jQuery(this).hide();
        });
        jQuery(this).addClass("menu-item--active");
        jQuery(this).find(".underLine").addClass("unline--active");
        var menuItemLink = jQuery(this).find("a");
        var elm = this.getAttribute('data-id');
        jQuery("#sub__menu-" + elm).show();
        jQuery(".menu__overlay--bg").addClass("mbg-is-active");

    }, function () {
        if (jQuery(".main__menu").find(".sub__menu:hover").length > 0) {
            //console.log("are");
        } else {
            menus.removeClass("menu-item--active");
            var menuItemLinkActive = menus.find(".menu-item-link--active");
            menuItemLinkActive.removeClass("menu-item-link--active");
            jQuery(".menu__overlay--bg").removeClass("mbg-is-active");
            menus.each(function () {
                jQuery(this).find(".underLine").removeClass("unline--active");
            });
            jQuery(".sub__menu").hide();
        }

});

jQuery(".sub__menu").hover(function () {
    },
    function () {
        //console.log("aaaa");
        menus.removeClass("menu-item--active");
        var menuItemLinkActive = menus.find(".menu-item-link--active");
        menuItemLinkActive.removeClass("menu-item-link--active");
        jQuery(".menu__overlay--bg").removeClass("mbg-is-active");
        menus.each(function () {
            jQuery(this).find(".underLine").removeClass("unline--active");
        });
        jQuery(".sub__menu").hide();
});



// convert persian number to latin number
let PERSIAN_NUMERALS = '۰'.charCodeAt(0);
function numeralParseInt(zero, str) {
    let digits = new Array(str.length);
    for (let i = 0; i < str.length; i++) {
        digits[i] = str.charCodeAt(i);
        if (zero <= digits[i] && digits[i] < zero + 10) {
            digits[i] -= zero - 48;     // '0' = ASCII 48
        }
    }
    return String.fromCharCode.apply(null, digits);
}

function persianParseInt(str) {
    return numeralParseInt(PERSIAN_NUMERALS, str);
}


// function convert tomans currency
function tomansCurrency(num){
    num = num.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
    return num;
}

jQuery(document).ready(function(){
    // convert all en number to persian number
    jQuery("body").persiaNumber();

    // close modal login / register on click close btn
    jQuery("#reg-log__dialog  .dialog__content .header .close-dialog").click(function () {
        jQuery(".reg-log__dialog .reg-log__dialog__inner").css("display", "none");
    });
    var body = jQuery("body");
    // login ajax POST method
    body.on("click", ".login__form .submit-login--btn", function () {
       let mobile = jQuery(".login__form .username--inp");
       let password = jQuery(".login__form .password--inp");
       let rememberMe = false;
       let status = false;
       jQuery(".login__form .remember-me .remember-me--inp").prop("checked") ?  rememberMe =  true :  rememberMe = false;
       if(!(checkErrorInput(mobile, "mobile"))){
            let right = getRightPos(mobile, "mobile");
            mobile.parent().append(`<span class="check-inp--status" style="right: ${ right + "px" }">شماره موبایل را به درستی وارد کنید!</span>`);
            status = false;
       }
        if(!(checkErrorInput(password, "password"))){
            let right = getRightPos(password, "password");
            password.parent().append(`<span class="check-inp--status" style="right: ${ right + "px" }">رمز عبور باید  ترکیبی از حروف و اعداد بین ۸ تا ۱۵ کاراکتر باشد.</span>`);
            status = false;
        }
        if(status === false){
            return
        }
       jQuery.ajax({
           type: "POST",
           url: "check-account.php",
           data : {
               username : username.val(),
               password : password.val(),
               remember_me : rememberMe
           },
           success: function (response) {
               jQuery(".reg-log__dialog__inner .show-status").html(`${response.user_display_name} عزیز خوش آمدید. لطفا چند لحظه صبر کنید `).addClass("success");
               jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
           },
           error: function () {
               jQuery(".reg-log__dialog__inner .show-status").html("خطایی در ارتباط با سرور رخ داده است!").addClass("danger");
               jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
           },
           beforeSend: function () {
               jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("hidden").addClass("mdi-spin-faster");
           }
       })
    });
     // registration ajax POST method
    body.on("click", ".register__form .submit-register--btn", function () {
        let status = true;
        if(!(jQuery(".register__form .privacy-policy-check--inp").prop("checked"))){
            jQuery(".reg-log__dialog__inner .show-status").html(`موافقت با سیاست حریم خصوصی وب سایت الزایمی میباشد.`).addClass("danger");
            jQuery(".register__form .privacy-policy-check .arrow").css("animation", "privacy-policy-opacity 1s 3 ease");
            setTimeout(function () {
                jQuery(".register__form .privacy-policy-check .arrow").css("animation", "unset");
            }, 3000);
            status = false;
        }
        let mobile = jQuery(".register__form .mobile--inp");
        let email = jQuery(".register__form .email--inp");
        let password = jQuery(".register__form .password--inp");
        if(mobile.parent().find(".check-inp--status").length){
            mobile.parent().find(".check-inp--status").remove();
        }
        if(!(checkErrorInput(mobile, "mobile"))){
            let right = getRightPos(mobile, "mobile");
            mobile.parent().append(`<span class="check-inp--status" style="right: ${ right + "px" }">شماره موبایل را به درستی وارد کنید!</span>`);
            status = false;
        }
        if(email.parent().find(".check-inp--status").length){
            email.parent().find(".check-inp--status").remove();
        }
        if(!(checkErrorInput(email, "email"))){
            let right = getRightPos(email, "email");
            email.parent().append(`<span class="check-inp--status" style="right: ${ right + "px" }">آدرس ایمیل را به درستی وارد کنید!</span>`);
            status = false;
        }
        if(!(checkErrorInput(password, "password"))){
            let right = getRightPos(password, "password");
            password.parent().append(`<span class="check-inp--status" style="right: ${ right + "px" }">رمز عبور باید  ترکیبی از حروف و اعداد بین ۸ تا ۱۵ کاراکتر باشد.</span>`);
            status = false;
        }
        if(status === false){
            return
        }
        let data = {};
        data.email = email.val();
        data.passwordd = password.val();
        data.mobile = mobile.val();
        jQuery.ajax({
            type: "POST",
            url: "check-account.php",
            data : {
                mobile : data.mobile,
                email : data.email
            },
            success: function (response) {
                /*jQuery(".reg-log__dialog__inner .show-status").html(`${response.user_display_name} عزیز خوش آمدید. لطفا چند لحظه صبر کنید `).addClass("success");*/
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
                let registerForm = jQuery(".reg-log__dialog__inner .register__form");
                let showElement = jQuery(registerForm).find(".show-status");
                registerForm.find(".mobile").addClass("hidden");
                registerForm.find(".email").addClass("hidden");
                registerForm.find(".password").addClass("hidden");
                registerForm.find(".privacy-policy-check").addClass("hidden");
                registerForm.find(".submit-register").addClass("hidden");
                registerForm.find(".register__form__inner").append(`<div class="verification"><input maxlength="5" type="text" autofocus class="verification--inp" placeholder="_ _ _ _ _"></div><div class="resend-code"><span class="text hidden">ارسال دوباره کد</span><span class="time-left"><span class="time-left--text">ارسال مجدد کد تایید</span><span class="time-left--counter"></span></span></div><div class="submit-verification"><button class="submit-verification--btn"><span class="text">تایید کد</span><span class="mdi mdi-loading hidden"></span></button></div>`);
                sendVerificationCode(data, registerForm, showElement);
            },
            error: function (response) {
                jQuery(".reg-log__dialog__inner .show-status").html("این شماره قبلا ثبت شده است!").addClass("danger");
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
            },
            beforeSend: function () {
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("hidden").addClass("mdi-spin-faster");
            }
        })
    });


    // resend verification code
    body.on("click", ".reg-log__dialog__inner .register__form .resend-code .text" , function () {
        let mobile = jQuery(".register__form .mobile--inp").val();
        let email = jQuery(".register__form .email--inp").val();
        let data = {};
        data.email = email;
        data.mobile = mobile;
        let registerForm = jQuery(".reg-log__dialog__inner .register__form");
        let showElement = jQuery(registerForm).find(".show-status");
        sendVerificationCode(data, registerForm, showElement);
    });

    // final registration state with send verification code to server by user
    body.on("click", ".reg-log__dialog__inner .register__form .submit-verification--btn" , function () {
        let mobile = jQuery(".register__form .mobile--inp");
        let email = jQuery(".register__form .email--inp");
        let password = jQuery(".register__form .password--inp");
        let verificationCode = jQuery(".register__form .verification--inp");
        jQuery.ajax({
            type: "POST",
            url: "check-account.php",
            data : {
                mobile : mobile.val(),
                email : email.val(),
                password : password.val(),
                verification_code : verificationCode.val()
            },
            success: function (response) {
                jQuery(".reg-log__dialog__inner .show-status").html(` کاربر خوش آمدید. لطفا چند لحظه صبر کنید `).addClass("success");
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");

            },
            error: function (response) {
                jQuery(".reg-log__dialog__inner .show-status").html("کد تایید شما اشتباه است. دوباره سعی کنید!").addClass("danger");
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
            },
            beforeSend: function () {
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("hidden").addClass("mdi-spin-faster");
            }
        })
    });

    // forget-password request ajax post
    body.on("click", ".forget-password__form .forget-password__form__inner .submit-forget-password--btn", function () {
       let status = true;
       let mobile = jQuery(".forget-password__form .forget-password__form__inner .forget-password--inp");
       if(!(checkErrorInput(mobile, "mobile"))){
           let right = getRightPos(mobile, "mobile");
           mobile.parent().append(`<span class="check-inp--status" style="right: ${ right + "px" }">شماره موبایل معتبر نیست!</span>`);
           status = false;
       }
       if(status === false){
           return
       }
       jQuery.ajax({
           type: "POST",
           url: 'forget-password.php',
           data: {
               mobile: mobile.val()
           },
           success: function () {
               jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
               mobile.parent().addClass("hidden");
               let forgetPasswordForm = jQuery(".forget-password__form");
               forgetPasswordForm.find(".submit-forget-password").addClass("hidden");
               forgetPasswordForm.find(".forget-password__form__inner").append(`<div class="verification"><input maxlength="5" type="text" autofocus class="verification--inp" placeholder="_ _ _ _ _"></div><div class="resend-code"><span class="text hidden">ارسال دوباره کد</span><span class="time-left"><span class="time-left--text">ارسال مجدد کد تایید</span><span class="time-left--counter"></span></span></div><div class="submit-verification"><button class="submit-verification--btn"><span class="text">تایید کد</span><span class="mdi mdi-loading hidden"></span></button></div>`);
               let data = {};
               data.mobile = mobile.val();
               let showElement = jQuery(forgetPasswordForm).find(".show-status");
               sendVerificationCode(data, forgetPasswordForm, showElement);
           },
           error: function () {
               jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
           },
           beforeSend: function () {
               jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("hidden").addClass("mdi-spin-faster");
           }
       })
    });

    // resend verification code for forget-password request
    body.on("click", ".reg-log__dialog__inner .forget-password__form .resend-code .text" , function () {
        let mobile = jQuery(".forget-password__form .forget-password--inp").val();
        let data = {};
        data.mobile = mobile;
        let forgetPasswordForm = jQuery(".reg-log__dialog__inner .forget-password__form");
        let showElement = jQuery(forgetPasswordForm).find(".show-status");
        sendVerificationCode(data, forgetPasswordForm, showElement);
    });

    body.on("click", ".reg-log__dialog__inner .forget-password__form .submit-verification .submit-verification--btn" , function () {
        let verification_code = jQuery(".forget-password__form .verification--inp").val();
        let mobile = jQuery(".forget-password__form .forget-password--inp").val();
        let forgetPasswordForm = jQuery(".reg-log__dialog__inner .forget-password__form");
        jQuery.ajax({
            type: "POST",
            url: "check-forget-verification",
            data: {
                verification_code: verification_code,
                mobile: mobile
            },
            dataType: "json",
            success: function () {
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
                forgetPasswordForm.find(".verification").addClass("hidden");
                forgetPasswordForm.find(".submit-verification").addClass("hidden");
                forgetPasswordForm.find(".resend-code").addClass("hidden");
                forgetPasswordForm.find(".forget-password__form__inner").append(`<div class="password-one"><span class="mdi mdi-lock"></span><input  type="text"  class="password-one--inp" placeholder="رمز عبور جدید"></div><div class="password-two"><span class="mdi mdi-lock"></span><input  type="password"  class="password-two--inp" placeholder="تکرار رمز عبور جدید"></div><div class="submit-change-password"><button class="submit-change-password--btn"><span class="text">ثبت رمز عبور</span><span class="mdi mdi-loading hidden"></span></button></div>`);
            },
            error: function () {
                forgetPasswordForm.find(".verification").addClass("hidden");
                forgetPasswordForm.find(".submit-verification").addClass("hidden");
                forgetPasswordForm.find(".resend-code").addClass("hidden");
                forgetPasswordForm.find(".forget-password__form__inner").append(`<div class="password-one"><span class="mdi mdi-lock"></span><input  type="text"  class="password-one--inp" placeholder="رمز عبور جدید"></div><div class="password-two"><span class="mdi mdi-lock"></span><input  type="password"  class="password-two--inp" placeholder="تکرار رمز عبور جدید"></div><div class="submit-change-password"><button class="submit-change-password--btn"><span class="text">ثبت رمز عبور</span><span class="mdi mdi-loading hidden"></span></button></div>`);
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
            },
            beforeSend: function () {
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("hidden").addClass("mdi-spin-faster");
            }
        })
    });

    // btn send two password input forget-password
    body.on("click", ".reg-log__dialog__inner .forget-password__form .submit-change-password .submit-change-password--btn" , function () {
        let passwordOne = jQuery(".reg-log__dialog__inner .forget-password__form .password-one .password-one--inp");
        let passwordTwo = jQuery(".reg-log__dialog__inner .forget-password__form .password-two .password-two--inp");
        let status = true;
        if(passwordTwo.val() !== passwordOne.val()){
            jQuery(".reg-log__dialog__inner .show-status").html("رمز شما یکسان نیست دوباره سعی کنید.").addClass("danger");
            status = false;
        }
        if(!(checkErrorInput(passwordOne, "password"))){
            let right = getRightPos(passwordOne, "password");
            passwordOne.parent().append(`<span class="check-inp--status" style="right: ${ right + "px" }">رمز عبور باید  ترکیبی از حروف و اعداد بین ۸ تا ۱۵ کاراکتر باشد.</span>`);
            status = false;
        }
        if(!(checkErrorInput(passwordTwo, "password"))){
            let right = getRightPos(passwordTwo, "password");
            passwordTwo.parent().append(`<span class="check-inp--status" style="right: ${ right + "px" }">رمز عبور باید  ترکیبی از حروف و اعداد بین ۸ تا ۱۵ کاراکتر باشد.</span>`);
            status = false;
        }
        if(status === false){
            return
        }
        jQuery.ajax({
            url: 'change-password',
            type: 'POST',
            data: {
                password_one : passwordOne.val(),
                password_two : passwordTwo.val()
            },
            success: function () {
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
                jQuery(".reg-log__dialog__inner .show-status").html("رمز شمت با موفقیت تغییر کرد چند لحظه صبر کنید...").addClass("success");
                setTimeout(function () {
                    window.location.reload();
                },2000);
            },
            error: function(){
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("mdi-spin-faster").addClass("hidden");
            },
            beforeSend: function () {
                jQuery(".reg-log__dialog__inner .mdi-loading").removeClass("hidden").addClass("mdi-spin-faster");
            }

        })
    });

    // config select2
    $('.input-select').select2({ width: '100%', dir: "rtl",  containerCssClass : "input-select"});

    // set sticky pos to compare page
    if(jQuery(".compare-page .compare-page__inner").length > 0){
        let productHeightPointer = jQuery(".compare-page .compare-page__inner .products-height-pointer");
        let products = jQuery(".compare-page .compare-page__inner .products");
        arrivedElement(productHeightPointer, products, "sticky-compare-products");
    }
    // close normal-modal
    jQuery(".normal-modal .close").click(function () {
       jQuery(".overlay--bg").css("opacity", "0");
       jQuery(this).parent().parent().addClass("hidden");
    });

    // open normal-modal
    jQuery(".compare-page .products .add").click(function () {
       jQuery(".overlay--bg").css("opacity", "1");
       jQuery(".compare-page .normal-modal").removeClass("hidden");
    });

    jQuery(".compare-page .normal-modal .p-compare-list .p-compare-list__inner .item").click(function () {
        let pId = jQuery(this).attr("data-id");
        let ids = [];
        jQuery(".compare-page .products .product").each(function () {
            if(jQuery(this).hasClass("add")){

            }else {
                ids.push(jQuery(this).attr("data-id"));
            }
        });
        ids.push(pId);
        let url = "";
        for(let id in ids){
            url += ids[id] + '/';
        }
        window.location.href = "/compare/" + url;
    });

    // open lists-address  for adding new address
    body.on("click" ,".shipping-page .shipping-page__inner .address-area .change-address", function () {
        jQuery(".shipping-page .address-lists").removeClass("hidden");
        jQuery(".shipping-page .shipping-page__inner .address-area").addClass("hidden");
    });

    // open add address dialog
    body.on("click", ".shipping-page .shipping-page__inner .address-area .add-address", function () {
        jQuery(".overlay--bg").css("opacity", "1");
       jQuery(".normal-modal").removeClass("hidden");
    });

    // change selected address with ajax and given html
    body.on("click", ".shipping-page .shipping-page__inner .address-lists .address", function () {
        let addressId = jQuery(this).attr("data-id");
        let token = jQuery("meta[name='csrf-token']").attr("content");
        jQuery.ajax({
            url: 'add-address.php',
            dataType: 'html',
            data: {
                address_id : addressId,
                token: token
            },
            success: function (response) {
                jQuery(".shipping-page .shipping-page__inner .address-area .address-area__inner").each(function () {
                   jQuery(this).empty();
                });
                /// ***pay attention you must return all elements that are in .address-area__inner
                jQuery(".shipping-page .shipping-page__inner .address-area .address-area__inner").append(response);
                jQuery(".shipping-page .address-lists").addClass("hidden");
                jQuery(".shipping-page .shipping-page__inner .address-area").removeClass("hidden");
                jQuery(".loading-svg").toggleClass("hidden");
            },
            error : function () {
                jQuery(".loading-svg").toggleClass("hidden");
            },
            beforeSend: function (request) {
                jQuery(".loading-svg").toggleClass("hidden");
                request.setRequestHeader('X-CSRF-TOKEN', token)
            },

        })

    });

    // close lists-address on close btn
    jQuery(".shipping-page .shipping-page__inner .address-lists .close").click(function () {
       let addressLists = parentByClass(jQuery(this), "address-lists");
       addressLists.addClass("hidden");
        jQuery(".shipping-page .shipping-page__inner .address-area").removeClass("hidden");
    });

    body.on("click", ".shipping-page .shipping-page__inner .address-add-form .submit-add-address input", function () {
        let thiz = jQuery(".shipping-page .shipping-page__inner .address-add-form");
        let getterName = thiz.find(".getter-name--inp");
        let getterMobile = thiz.find(".getter-mobile--inp");
        let getterPostalCode = thiz.find(".getter-postal-code--inp");
        let getterState = thiz.find(".getter-state").find(".input-select");
        let getterCity = thiz.find(".getter-city").find(".input-select");
        let getterAddress = thiz.find(".getter-address--inp");
        let token = jQuery("meta[name='csrf-token']").attr("content");
        jQuery.ajax({
            url: 'add-address-ajax',
            data: {
                token: token,
                name: getterName.val(),
                mobile: getterMobile.val(),
                postal_code : getterPostalCode.val(),
                state: getterState.val(),
                city: getterCity.val(),
                address: getterAddress.val()
            },
            success: function () {
                jQuery(".shipping-page .shipping-page__inner .address-area .address-area__inner").append(response);
                jQuery(".loading-svg").toggleClass("hidden");
            },
            beforeSend(){
                jQuery(".loading-svg").toggleClass("hidden");
                request.setRequestHeader('X-CSRF-TOKEN', token);
            }
        });
    });

    // open small user dialog in header user-account
    jQuery(".header .reg-log .user-display-name").click(function () {
        jQuery(".header .reg-log .reg-log__logged-in__box").toggleClass("hidden");
    });

});
// send verification code
function sendVerificationCode(data, formEle, showEle) {
    jQuery(formEle).find(showEle).html(` کد تایید به شماره ${data.mobile} ارسال شد.`).addClass("success");

    if(!(formEle.find(".resend-code .text").hasClass("hidden"))){
        formEle.find(".resend-code .text").addClass("hidden");
    }
    if((formEle.find(".resend-code .time-left--text").hasClass("hidden"))){
        formEle.find(".resend-code .time-left--text").removeClass("hidden")
    }
    let timeLeftVerification = formEle.find(".time-left--counter");
    let todayDate = new Date();
    todayDate = todayDate.getFullYear()+'-'+(todayDate.getMonth()+1)+'-'+todayDate.getDate();
    let todayTime = new Date();
    todayTime = todayTime.getHours() + ":" + (todayTime.getMinutes()+1) + ":" + todayTime.getSeconds();
    console.log(todayTime, todayDate);
    let oneMinuteNext = todayDate +' '+ todayTime;
    timeLeftCounter(oneMinuteNext, timeLeftVerification,"", false);
    setTimeout(function () {
        jQuery(formEle).find(".time-left--text").addClass("hidden");
        jQuery(formEle).find(".resend-code .text").removeClass("hidden");
    }, 17000);

    jQuery.ajax({
        url: '/user/active-user',
        type: 'POST',
        data : {
            mobile : data.mobile,
            email : data.email
        },
    })
}


function getRightPos(element) {
    let parent = element.parent();
    let parentWidth = element.parent().width();
    let parentLeft = parent.offset().left;
    let elementLeft = element.offset().left;
    let elementWidth = element.outerWidth();
    let elementLeftFromParent = elementLeft - parentLeft;
    return parentWidth - elementWidth - elementLeftFromParent;
}

function checkErrorInput(element, type) {
    let status = true;
    let textVal = element.val();
    if(type === "email"){
        let pattern = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        status = pattern.test(textVal);
    }
    else if(type === "mobile"){
        let pattern = new RegExp('^(?:(?:(?:\\+?|00)(98))|(0))?((?:90|91|92|93|99)[0-9]{8})$', 'i');
        status = pattern.test(textVal);
    }
    else if(type === "password"){
        let pattern = /^[a-zA-Z0-9_-]{8,15}$/;
        status = pattern.test(textVal);
    }
    return status;
}



//
function arrivedElement(referenceElement, element , _class) {
    jQuery(window).scroll(function () {
        let hT = jQuery(referenceElement).offset().top,
            hH = jQuery(referenceElement).outerHeight(),
            wH = jQuery(window).height(),
            wS = jQuery(this).scrollTop();
        if (wS > 250) {
            jQuery(element).addClass(_class);
        }else{
            jQuery(element).removeClass(_class);
        }
    });
}


