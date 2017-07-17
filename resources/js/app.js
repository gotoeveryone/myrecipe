import './bootstrap';

import Dialog from './components/Dialog.vue';
import Search from './components/cuisine/Search.vue';
import Detail from './components/cuisine/Detail.vue';

new Vue({
    delimiters: ['${', '}'],
    el: '.content',
    data: {
        notices: {
            error: false,
            title: '',
            message: '',
        },
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
        setDialog(_obj) {
            this.notices = {
                error: ('error' in _obj && _obj.error),
                title: _obj.title,
                message: _obj.message,
            };
        },
        closeDialog() {
            this.notices = {
                error: false,
                title: '',
                message: '',
            };
        },
    },
});
