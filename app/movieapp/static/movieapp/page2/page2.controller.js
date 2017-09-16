
(function () {
    'use strict';

    angular.module('movieapp')
        .controller('Page2Controller', Page2Controller);

    Page2Controller.$inject = [];
    function Page2Controller() {
        var vm = this;

        vm.title = 'page2';
    }
}());