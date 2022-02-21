$(document).ready(function () {
            $('.nav_menu > li > h2 > a').on({
                mouseenter: function (e) {
                    var target = e.target;
                    $(target).parents('.nav_menu').find('.nav_overMenu').slideDown(function () {
                        $('.nav').addClass('active');
                    });
                },
                click: function (e) {
                    var target = e.target;
                    if (!$('.nav').hasClass('active')) {
                        $(this).trigger('mouseenter');
                    } else {
                        $('.nav').trigger('mouseleave');
                    }
                }
            });

            /********************************************************
            //서브메뉴 구글 GA Analytics 로그 처리 - 2022.01.12 myilsan
            ********************************************************/
            //cgv화이트 메뉴클릭
            $('.nav > .contents > h1 > a').on({
                 click: function (e) {
                     gaEventLog('PC_GNB', '홈', '');
                }
            });

            //주메뉴 클릭
            $('.nav_menu > li > h2 > a').on({
                click: function (e) {
                    gaEventLog('PC_GNB', '주메뉴_' + this.text, '');
                }
            });

            //주메뉴 하위메뉴 클릭
            $('.nav_overMenu > dd > h3 > a').on({
                click: function (e) {
                    var target = e.target;
                    var parText = $(target).parents('.nav_overMenu').find('dt')[0].innerText;
                    gaEventLog('PC_GNB', parText + '_' + this.text, '');
                }
            });

            //하위메뉴 최상위 클릭
            $(".nav_overMenu > dt > h2 > a").on({
                click: function (e) {
                    gaEventLog('PC_GNB',this.text + '_' + this.text, '');
                }
            });

            //------------------end----------------------- [@,.o]>

            $('.nav').on({
                mouseleave: function (e) {
                    $(this).find('.nav_overMenu').slideUp(200, function () {
                        $('.nav').removeClass('active');
                    });
                }
            });

            $('.totalSearch_wrap input[type=text]').on({
                focusin: function () {
                    $('.totalSearch_wrap').addClass("active");
                }
            });

            $('.btn_totalSearchAutocomplete_close').on({
                click: function () {
                    $('.totalSearch_wrap').removeClass("active");
                },
                focusout: function (e) {
                    //     $('.totalSearch_wrap').removeClass("active");

                }
            });

            $(this).on({
                scroll: function (e) {
                    /* S GNB fixed */
                    var headerOffsetT = $('.header').offset().top;
                    var headerOuterH = $('.header').outerHeight(true);
                    var fixedHeaderPosY = headerOffsetT + headerOuterH;
                    var scrollT = $(this).scrollTop();
                    var scrollL = $(this).scrollLeft();

                    if (scrollT >= fixedHeaderPosY) {
                        $('.nav').addClass('fixed');
                        $('.fixedBtn_wrap').addClass('topBtn');
                    } else {
                        $('.nav').removeClass('fixed');
                        $('.fixedBtn_wrap').removeClass('topBtn');
                    }

                    /* S > GNB fixed 좌우 스크롤
                    Description
                    - GNB가 fixed 되었을때 좌우 스크롤 되게 처리
                    */
                    if ($('.nav').hasClass('fixed')) {
                        $('.nav').css({ 'left': -1 * scrollL })
                    } else {
                        $('.nav').css({ 'left': 0 })
                    }
                    /* E > GNB fixed 좌우 스크롤 */
                    /* S GNB fixed */
                }
            });

            $('.btn_gotoTop').on({
                click: function () {
                    $('html, body').stop().animate({
                        scrollTop: '0'
                    }, 400);
                }
            });

        });