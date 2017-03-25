// declare var require: any

// import Vue from 'vue/dist/vue.js';
const Vue = require('vue/dist/vue');

// 作り方
Vue.component('cooking-row', {
    template: '\
        <li>\
            <input type="text" value="" class="">\
            <input type="text" value="" class="">\
        </li>'
});

// 調理手順
Vue.component('quantity-row', {
    template: '\
        <li>\
            <input type="text" value="" class="">\
            <input type="text" value="" class="">\
        </li>'
});

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
        },
        addCookingRow: () => {

        },
        deleteCookingRow: () => {

        },
        addQuantityRow: () => {

        },
        deleteQuantityRow: () => {

        }
    }
});
