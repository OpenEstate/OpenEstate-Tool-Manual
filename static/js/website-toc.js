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

$(document).ready(function () {

    var currentLevel = null;
    var rootLevel = null;
    var nav = '';

    $('#content h2, #content h3, #content h4, #content h5').each(function (index) {
        var element = $(this);
        var level = parseInt(element.prop('tagName').substring(1));
        //console.info('element at ' + index + ' (' + element.prop('tagName').substring(1) + ')');
        //console.info(element);

        if (currentLevel === null) {
            rootLevel = level;
            currentLevel = level;
        }

        var href = '#' + element.attr('id');
        var diff = level - rootLevel;
        var indent = (diff<1) ? 'initial;': 'padding-left:' + (1.25 + (diff*1)) + 'rem;';

        //nav += '<a class="nav-link" href="' + href + '" style="margin-left:' + diff + 'em;">' + element.text() + '</a>';
        nav += '<a class="list-group-item list-group-item-action" href="' + href + '" style="' + indent + '">' + element.text() + '</a>';
    });

    //$('#toc-nav').html('<nav class="nav nav-pills flex-column">' + nav + '</nav>');
    $('#toc-nav').html(nav);

});
