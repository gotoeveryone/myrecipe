// declare var require: any

// import Vue from 'vue/dist/vue.js';
const Vue = require('vue/dist/vue');

new Vue({
    el: '.container',
    methods: {
        toTop: function() {
            location.href = '/';
        },
        toMenu: function() {
            location.href = '/recipe/menu/';
        },
        toSearch: function(obj) {
            location.href = '/recipe/' + obj + '/search/';
        },
        block: function() {
            console.log(this);
            $(this.$el).block();
        }
    }
});
