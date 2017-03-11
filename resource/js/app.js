// declare var require: any

// import Vue from 'vue/dist/vue.js';
const Vue = require('vue/dist/Vue');

const app = new Vue({
    el: '.container',
    methods: {
        toTop: () => {
            location.href = '/';
        },
        toMenu: () => {
            location.href = '/recipe/menu/';
        },
        toSearch: (obj) => {
            location.href = '/recipe/' + obj + '/search/';
        },
        block: () => {
            console.log(this);
            $(this.$el).block();
        }
    }
});
