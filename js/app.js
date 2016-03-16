(function() {
    'use strict';

    var app = angular.module('app', []);

    app.factory('_', function() {
        return window._; // assumes underscore has already been loaded on the page
    });

})();