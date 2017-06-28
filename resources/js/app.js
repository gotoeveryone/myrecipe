import './bootstrap';

import Dialog from './components/Dialog.vue';
import Search from './components/cuisine/Search.vue';
import Detail from './components/cuisine/Detail.vue';

new Vue({
    delimiters: ['${', '}'],
    el: '.content',
    data: {
        title: '',
        message: '',
    },
    components: {
        notice: Dialog,
        searchCuisine: Search,
        detailCuisine: Detail,
    },
    methods: {
        toTop() {
            location.href = '/';
        },
        toMenu() {
            location.href = '/recipe/menu/';
        },
    },
});
