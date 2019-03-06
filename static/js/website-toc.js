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

    var TocNode = function (element, parentNode, level) {
        this.id = element.attr('id');
        this.level = level;
        this.element = element;
        this.parentNode = parentNode;
        this.childNodes = [];
    };

    TocNode.prototype.html = function (prefix, depth = 0) {
        //var indent = 'padding-left:' + (1.25 + depth) + 'rem;';
        var indent = '';
        var display = (depth > 1) ? 'd-none' : '';
        var links = '<a class="list-group-item list-group-item-action ' + display + '" ' +
            'href="#' + this.id + '" ' +
            'style="' + indent + '">' + prefix + ' ' + this.element.text() + '</a>';
        for (var i = 0; i < this.childNodes.length; i++) {
            //var childPrefix = prefix + (i + 1) + '.';
            var childPrefix = prefix + '&raquo;';
            links += this.childNodes[i].html(childPrefix, depth + 1);
        }
        return links;
    };

    TocNode.prototype.show = function () {
        this.showParents();
        this.showInToc();
        if (this.parentNode !== null) this.parentNode.showChildren();
        this.showChildren();
    };

    TocNode.prototype.showChildren = function () {
        for (var i = 0; i < this.childNodes.length; i++) {
            this.childNodes[i].showInToc();
        }
    };

    TocNode.prototype.showParents = function () {
        if (this.parentNode != null) {
            this.parentNode.showInToc();
            this.parentNode.showParents();
        }
    };

    TocNode.prototype.showInToc = function () {
        $('#toc-nav a[href="#' + this.id + '"]')
            .removeClass('d-none');
    };

    TocNode.prototype.hideInToc = function () {
        $('#toc-nav a[href="#' + this.id + '"]')
            .addClass('d-none');
    };

    var rootNodes = [];
    var allNodes = [];
    var headlines = [];
    $('#content h2, #content h3, #content h4, #content h5').not('.notoc').each(function (index) {
        var element = $(this);
        var level = parseInt(element.prop('tagName').substring(1));

        var node = new TocNode(element, null, level);

        if (level === 2) {
            rootNodes.push(node);
        }

        var lastNode = (allNodes.length > 0) ? allNodes[allNodes.length - 1] : null;

        if (lastNode !== null) {

            // current node is on the same level then the last node
            if (level === lastNode.level) {
                node.parentNode = lastNode.parentNode;
                if (lastNode.parentNode != null) {
                    lastNode.parentNode.childNodes.push(node);
                }
            }

            // current node is on a higher level then the last node
            else if (level > lastNode.level) {
                node.parentNode = lastNode;
                lastNode.childNodes.push(node);
            }

            // current node is on a lower level then the last node
            else if (level < lastNode.level) {
                var parent = lastNode.parentNode;
                for (var i = level; i < lastNode.level; i++) {
                    parent = parent.parentNode;
                }
                node.parentNode = parent;
                if (parent != null) {
                    parent.childNodes.push(node);
                }
            }
        }

        allNodes.push(node);
        headlines.push(element);
    });

    var tocLinkEnter = function (element, position) {
        //console.info('ENTER');
        //console.info(element);
        $('#toc-nav a')
            .removeClass('list-group-item-primary');
        $('#toc-nav a[href="#' + element.id + '"]')
            .addClass('list-group-item-primary');

        //$('#toc-nav a')
        //    .removeClass('d-none');

        var currentNode = null;
        for (var i = 0; i < allNodes.length; i++) {
            if (allNodes[i].id === element.id) {
                currentNode = allNodes[i];
            }
            if (allNodes[i].level > 3) {
                allNodes[i].hideInToc();
            }
        }

        if (currentNode !== null) {
            currentNode.show();
        }
    };
    var tocLinkLeave = function (element, position) {
        //console.info('LEAVE');
        //console.info(element);
    };
    for (var i = 0; i < headlines.length; i++) {
        var element = headlines[i];
        var position = element.position();
        //console.info(position);
        //console.info('min: ' + position.top + ' / max: ' + window.parseInt(position.top + element.height(), 10));
        var scrollStart = (i > 0) ? position.top + 60 : 0;
        //var scrollEnd = scrollStart + element.height();
        var scrollEnd = ((i + 1) < headlines.length) ?
            headlines[i + 1].position().top + 50 :
            scrollStart + element.height();

        element.scrollspy({
            min: scrollStart,
            max: scrollEnd,
            buffer: 0,
            onEnter: tocLinkEnter,
            onLeave: tocLinkLeave
        });
    }

    var tocLinks = '';
    for (var i = 0; i < rootNodes.length; i++) {
        //var prefix = (i + 1) + '.';
        var prefix = '';
        tocLinks += rootNodes[i].html(prefix);
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

    var top = $(window).scrollTop();
    $(window).scrollTop(top + 1);
    $(window).scrollTop(top - 1);
});
