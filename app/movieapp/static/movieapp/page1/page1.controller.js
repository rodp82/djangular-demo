
(function () {
    'use strict';

    angular.module('movieapp')
        .controller('Page1Controller', Page1Controller);

    Page1Controller.$inject = [];
    function Page1Controller() {
        var vm = this;

        vm.title = 'page1';
    }
}());