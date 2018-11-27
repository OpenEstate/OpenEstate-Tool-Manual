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

$( document ).ready(function() {

    // leere Tabellen-Kopfzeilen ausblenden
    $( '#content table thead' ).each(function( index ) {
        var thead = $( this );

        var empty = true;
        thead.find( 'th' ).each(function( index ) {
            var th = $( this );
            if (th.text()!='') {
                empty = false;
            }
        });

        if (empty===true) {
            thead.addClass( 'd-none' );
        }
    });

    // CSS-Klassen für Tabellen setzen
    $('#content table')
        .addClass( 'table table-striped table-bordered table-hover' )
        .wrap( '<div class="table-responsive"></div>' );

    // CSS-Klassen für Figure setzen
    $('#content figure')
        .wrap( '<div class="figure-container text-center"></div>' );
    $('#content figure > img')
        .addClass('img-fluid');
});
