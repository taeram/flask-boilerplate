/** @jsx React.DOM */

require.config({
    baseUrl: '/static/',
    urlArgs: "d=" + parseInt(Config.cache_buster, 10),
    paths: {
        // Dependencies
        "bootstrap": "components/bootstrap/dist/js/bootstrap.min",
        "jquery": "components/jquery/dist/jquery.min",

        // Helpers
        "modal": "js/helpers/Modal",
    },
    shim: {
        'bootstrap': {
            deps: ['jquery']
        },
        'underscore': {
            exports: '_'
        }
    }
});

// Configure the application
Config.App = {
    // The DOM id of the app container
    elementId: 'app',

    // The DOM id of the Modal container
    modalElementId: 'app-modal'
};

require(['react', 'bootstrap'], function (React, Bootstrap) {
    // Setup React
    React.initializeTouchEvents(true);
});
