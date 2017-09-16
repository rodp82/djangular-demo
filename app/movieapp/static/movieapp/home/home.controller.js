
(function () {
    'use strict';

    angular.module('movieapp')
        .controller('HomeController', HomeController);

    HomeController.$inject = ['$scope'];
    function HomeController($scope) {
        $scope.person = {
            name: 'joe',
            age: 30
        }
    }
}());