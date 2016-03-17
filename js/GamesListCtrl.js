(function() {
    'use strict';

    angular
        .module('app')
        .controller('GamesListCtrl', GamesListCtrl);

    GamesListCtrl.$inject = ['$log', '$http', '_'];
    function GamesListCtrl($log, $http, _) {
        var vm = this;

        activate();

        ////////////////

        function activate() {
            listAllGames();
            listMyGames();
        }

        function listAllGames() {
            $http.get("/js/games.json", { cache: true }).then(function(response) {
                vm.list = response.data;
            });
        }
        function listMyGames() {
            $http.get("/js/my_games.json", { cache: true }).then(function(response) {
                vm.myList = response.data;
                vm.listWithMine = _.map(vm.list, function(element) {
                    _.extend(element, { "have": false })
                    _.each(vm.myList, function(regex) {
                        var r = new RegExp(regex, "i");
                        if (r.test(element.title)) {
                            element.have = true;
                        }
                    });
                    return element;
                });
            });

        }
    }
})();