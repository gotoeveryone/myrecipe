window.Vue = require('vue/dist/vue.min');
require('vue-resource');

// ウィンドウがロードできればフェードを解除
window.addEventListener('load', () => {
    document.querySelector('.content').classList.remove('fade');
}, false);

window.Vue.http.interceptors.push((req, next) => {
    document.querySelector('.block-ui').classList.add('blocked');
    next((res) => {
        document.querySelector('.block-ui').classList.remove('blocked');
    });
});
