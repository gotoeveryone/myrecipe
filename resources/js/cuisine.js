require('./bootstrap');

import Dialog from './components/Dialog.vue';
import Instruction from './components/Instruction.vue';
import Quantity from './components/Quantity.vue';

new Vue({
    delimiters: ['${', '}'],
    el: '[cuisine]',
    data: {
        id: '',
        cuisine: {},
        title: '',
        message: '',
    },
    components: {
        notice: Dialog,
        instructions: Instruction,
        quantities: Quantity,
    },
    methods: {
        toTop() {
            location.href = '/';
        },
        toMenu() {
            location.href = '/recipe/menu/';
        },
        save() {
            this.$http.put('/recipe/api/cuisine/1/', JSON.stringify(this.cuisine)).then((data) => {
                this.title = 'メッセージ';
                this.message = 'レシピを更新しました。';
                this.cuisine = data.body;
            }).catch((s, a, v) => {
                console.log(s, a, v);
            });
        }
    },
    mounted() {
        this.$http.get('/recipe/api/cuisine/1/').then((data) => {
            this.cuisine = data.body;
        });
    },
});
