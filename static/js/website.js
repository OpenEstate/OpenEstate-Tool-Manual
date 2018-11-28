/*
 * Copyright 2009-2018 OpenEstate.org.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

function updateScrollButton() {
    //var documentHeight = $(document).height();
    //var windowHeight = $(window).height();
    var scrollTop = $(window).scrollTop();
    //var diff = documentHeight - windowHeight;

    //console.info( 'document height : ' + documentHeight );
    //console.info( 'window height   : ' + windowHeight );
    //console.info( 'scroll position : ' + scrollTop );

    if (scrollTop > 50) {
        if (!$('#scroll-up').is(':visible')) {
            //console.info( 'SHOW SCROLLER' );
            $('#scroll-up').fadeIn();
        }
    }
    else {
        if ($('#scroll-up').is(':visible')) {
            //console.info( 'HIDE SCROLLER' );
            $('#scroll-up').hide();
        }
    }
}

function scrollToElement(element) {
    //console.info('SCROLL TO');
    //console.info(element);
    var top = element.offset().top - 75;
    scrollToPosition(top);
}

function scrollToPosition(top) {
    $('html, body').animate({scrollTop: top}, 600);
}

$(document).ready(function () {

    // hide empty table headers
    $('#content table thead').each(function (index) {
        var thead = $(this);

        var empty = true;
        thead.find('th').each(function (index) {
            var th = $(this);
            if (th.text() != '') {
                empty = false;
            }
        });

        if (empty === true) {
            thead.addClass('d-none');
        }
    });

    // add css classes for tables
    $('#content table')
        .addClass('table table-striped table-bordered table-hover')
        .wrap('<div class="table-responsive"></div>');

    // add css classes for figures
    $('#content figure')
        .wrap('<div class="figure-container text-center"></div>');
    $('#content figure > img')
        .addClass('img-fluid');

    // don't hide search popup as long as the search field is focused
    $('#nav-search').on('beforehide.smapi', function(e, menu)
    {
        if ($('#nav-search .form-control').is(':focus')) {
            //console.info( 'keep search open' );
            return false;
        }
        else {
            //console.info( 'close search' );
            return true;
        }
    });

    // hide search popup if the search field looses its focus
    $('#nav-search .form-control').blur(function() {
        //console.info( 'lost focus' );
        $('#nav-search .dropdown-menu').fadeOut();
    });

    // show / hide the scroll button
    updateScrollButton();
    $(window).resize(function () {
        updateScrollButton();
    });
    $(window).scroll(function () {
        updateScrollButton();
    });

    // process clicks on the scroll button
    $('#scroll-up').click(function () {
        scrollToPosition(0);
        $('#scroll-up').blur();
        return false;
    });

    $('#content a[href^="#"]').click(function (event) {
        event.preventDefault();
        scrollToElement($($(this).attr('href')));
    });
});
