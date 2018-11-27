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

function installSearch(index) {
    var query = $.trim(url('?q'));
    //console.log( 'SEARCH FOR "' + query + '"' );
    if (query === undefined || query === null || query === '') {
        $('#search-empty').fadeIn();
        return;
    }

    $('.search-term').text(query);
    $('#search-query').val(query);

    $('#search-error').hide();
    $('#search-progress').show();

    $.ajax({
        method: 'GET',
        url: index,
        dataType: 'json'
    })
        .fail(function () {
            $('#search-progress').hide();
            $('#search-empty').hide();
            $('#search-error').fadeIn();
        })
        .done(function (data) {
            search(query, data);
        });
}

function search(query, data) {
    //console.log( 'data reveived', data )
    $('#search-result').hide();
    $('#search-result-container').hide();

    var idx = lunr(function () {
        this.field('title', {boost: 10});
        this.field('description', {boost: 5});
        this.field('content');
        this.ref('uri');

        data.forEach(function (page) {
            this.add(page)
        }, this);
    });

    var result = idx.search(query);
    //console.log( 'result', result )

    var totalHits = result.length;
    $('#search-result-count').text(' ' + totalHits + ' ');

    if (totalHits > 0) {
        result.slice(0, 25).forEach(function (row) {
            //console.log( 'FOUND ROW', row.ref );

            var page = data.filter(function (p) {
                return p.uri == row.ref;
            })[0];
            //console.log( page );

            var item = $('<li>');
            var href = page.uri;
            //var href = '../' + page.uri;
            //if (href.endsWith('/')) href += 'index.html';
            item.append($('<a>', {href: href, text: page.title}));
            item.append($('<br/>'));
            item.append($('<span>').text(page.description));

            $('#search-result-container').append(item);
        });
        $('#search-result-container').show();
    }

    $('#search-progress').hide();
    $('#search-result').fadeIn();
}
