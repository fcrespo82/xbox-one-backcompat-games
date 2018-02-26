(function() {
    'use strict';

    angular
        .module('app')
        .controller('GamesListCtrl', GamesListCtrl);

    GamesListCtrl.$inject = ['$log', '$http', '_'];
    function GamesListCtrl($log, $http, _) {
        var self = this;

        function activate() {
            listAllGames().then(function(response) {
                self.list = response.data;
                listMyGames();
            })
            
        }

        function listAllGames(callback) {
            return $http.get("/js/games.json");
        }

        function listMyGames() {
            $http.get("/js/my_games.json").then(function(response) {
                self.myList = response.data;
                self.listWithMine = _.map(self.list, function(element) {
                    _.each(self.myList, function(regex) {
                        var r = new RegExp(regex, "i");
                        if (r.test(element.title)) {
                            _.extend(element, { "have": true })
                        }
                    });
                    return element;
                });
            });

        }

        self.$postLink = activate;
    }
})();