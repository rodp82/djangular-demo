
(function () {
    'use strict';

    angular.module('movieapp.demo', [])
        .controller('HomeController', HomeController);

    HomeController.$inject = ['$scope'];
    function HomeController($scope) {
        $scope.person = {
            name: 'joe',
            age: 30
        }
    }
}());