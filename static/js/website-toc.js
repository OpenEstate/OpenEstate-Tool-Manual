/*
 * Copyright 2009-2019 OpenEstate.org.
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

$(document).ready(function () {

    var currentLevel = null;
    var rootLevel = null;
    var multipleRootLevels = false;
    var headlines = [];
    $('#content h2, #content h3, #content h4, #content h5').each(function (index) {
        var element = $(this);
        var level = parseInt(element.prop('tagName').substring(1));
        //console.info('element at ' + index + ' (' + element.prop('tagName').substring(1) + ')');
        //console.info(element);

        if (currentLevel === null) {
            rootLevel = level;
            currentLevel = level;
        }
        else if (level === rootLevel) {
            multipleRootLevels = true;
        }
        headlines.push(element);
    });

    var tocLinks = '';
    var tocLinkEnter = function (element, position) {
        //console.info('ENTER');
        //console.info(element);
        $('#toc-nav a')
            .removeClass('list-group-item-primary');
        $('#toc-nav a[href="#' + element.id + '"]')
            .addClass('list-group-item-primary');
    };
    var tocLinkLeave = function (element, position) {
        //console.info('LEAVE');
        //console.info(element);
    };
    for (var i = 0; i < headlines.length; i++) {
        var element = headlines[i];
        var level = parseInt(element.prop('tagName').substring(1));

        if (multipleRootLevels !== true && level === rootLevel)
            continue;

        var position = element.position();
        //console.info(position);
        //console.info('min: ' + position.top + ' / max: ' + window.parseInt(position.top + element.height(), 10));
        var scrollStart = position.top + 80;
        //var scrollEnd = scrollStart + element.height();
        var scrollEnd = ((i + 1) < headlines.length) ?
            headlines[i + 1].position().top + 70 :
            scrollStart + element.height();

        element.scrollspy({
            min: scrollStart,
            max: scrollEnd,
            buffer: 0,
            onEnter: tocLinkEnter,
            onLeave: tocLinkLeave
        });

        var href = '#' + element.attr('id');
        var diff = level - rootLevel;
        if (multipleRootLevels !== true) diff--;
        var indent = (diff < 1) ? 'initial;' : 'padding-left:' + (1.25 + diff) + 'rem;';

        tocLinks += '<a class="list-group-item list-group-item-action" href="' + href + '" style="' + indent + '">' + element.text() + '</a>';
    }

    $('#toc-nav').html(tocLinks);
    $('#toc-nav a').click(function (event) {
        event.preventDefault();
        scrollToElement($($(this).attr('href')));
    });

    $('#toc-card').scrollToFixed({
        minWidth: 980,
        marginTop: function () {
            var marginTop = $(window).height() - $('#toc-card').outerHeight(true);
            if (marginTop >= 80) {
                //console.info('scrollToFixed / 80');
                return 80;
            }
            //console.info('scrollToFixed / ' + marginTop);
            return marginTop;
        }
    });
});
