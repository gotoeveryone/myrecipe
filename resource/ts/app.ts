// declare var require: any

import Vue = require('vue/dist/vue.js')

// export default {
//     methods: {
//         toTop(): void {
//             location.href = '/';
//         }
//     }
// }

const app = new Vue({
    methods: {
        toTop(): void {
            location.href = '/';
        }
    }
}).$mount('.loginForm');
