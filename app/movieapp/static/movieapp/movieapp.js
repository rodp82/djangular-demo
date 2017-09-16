(function () {
    'use strict';

    angular.module('movieapp', ['ui.router'])
        .config(routeConfig);


    routeConfig.$inject = ['$stateProvider', '$urlServiceProvider','$locationProvider'];
    function routeConfig($stateProvider, $urlServiceProvider,$locationProvider) {

        $urlServiceProvider.rules.otherwise({ state: 'home' });

        $locationProvider.html5Mode({
            enabled     : true,
            requireBase : false
        }).hashPrefix('!');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/static/movieapp/home/home.view.html',
                controller: 'HomeController',
                controllerAs: 'vm'
            })
            .state('page1', {
                url: '/page1',
                templateUrl: '/static/movieapp/page1/page1.view.html',
                controller: 'Page1Controller',
                controllerAs: 'vm'
            })
            .state('page2', {
                url: '/page2',
                templateUrl: '/static/movieapp/page2/page2.view.html',
                controller: 'Page2Controller',
                controllerAs: 'vm'
            })
    }

}());