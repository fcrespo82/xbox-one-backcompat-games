(function() {
    'use strict';

    var app = angular.module('app', ['ngAnimate']);

    app.factory('_', function() {
        return window._; // assumes underscore has already been loaded on the page
    });

    app.filter('onlyBooleanValueFilter', [function() {
        return function(input, column, TrueOrFalse) {
            var ret = [];
            if (!angular.isDefined(TrueOrFalse)) TrueOrFalse = true;
            angular.forEach(input, function(v) {
                if (angular.isDefined(v[column]) && v[column] === TrueOrFalse) {
                    ret.push(v);

                }
            });
            return ret;
        };
    }])
})();