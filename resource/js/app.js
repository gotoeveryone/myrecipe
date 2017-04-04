// declare var require: any

// import Vue from 'vue/dist/vue.js';
const $ = require('jquery');
const Vue = require('vue/dist/vue');
const VueResource = require('vue-resource');
Vue.use(VueResource);

// 作り方
Vue.component('cooking-row', {
    template: `
        <li>
            <input type="text" value="" class="">
            <input type="text" value="" class="">
        </li>`
});

// 調理手順
Vue.component('quantity-row', {
    template: `
        <li>
            <input type="text" value="" class="">
            <input type="text" value="" class="">
        </li>`
});

new Vue({
    delimiters: ['${', '}'],
    el: '.container',
    data: {
        cookings: $('.cookings').length,
        quantities: $('.quantities').length
    },
    methods: {
        toTop: function() {
            location.href = '/';
        },
        toMenu: function() {
            location.href = '/recipe/menu/';
        },
        block: () => {
            $(this.$el).block();
        },
        loadCuisine: function(id) {
            // console.log(this.$http);
            this.$http.get(`https://local.kazukisv.com/recipe/api/cuisine/${id}/`).then((response) => {
                this.cuisine = response.body;
                alert(JSON.stringify(response.body));
            }, () => {alert('error');});
        },
        addRow: (parentSelector) => {
            const len = $(`${parentSelector} li`).length;
            switch (parentSelector) {
                case '.cookings':
                    $(parentSelector).append(`<li>
                        <span class="cooking-order">${len + 1}：</span>
                        <input type="text" name="instructions.description" value="" class="cooking-description">
                    </li>`);
                    break;
                case '.quantities':
                    $(parentSelector).append(`<li>
                        <input type="text" name="quantities.foodstuff.name" value="" class="">
                        <input type="text" name="quantities.detail" value="" class="">
                    </li>`);
                    break;
                default:
                    break;
            }
        },
        deleteRow: (parentSelector) => {
            $(`${parentSelector} li:last-child`).remove();
        }
    }
});
