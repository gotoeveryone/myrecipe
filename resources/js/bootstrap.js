window.Vue = require('vue/dist/vue.common');
require('vue-resource');

// ウィンドウがロードできればフェードを解除
window.addEventListener('load', () => {
    document.querySelector('.content').classList.remove('fade');
}, false);

// Vueのリクエスト時にはブロックUIを有効にする
window.Vue.http.interceptors.push((req, next) => {
    document.querySelector('.block-ui').classList.add('blocked');
    next((res) => {
        document.querySelector('.block-ui').classList.remove('blocked');
    });
});

// リンク押下時にはブロック有効
const links = document.querySelectorAll('a');
links.forEach((item, idx) => {
    item.addEventListener('click', function(event) {
        document.querySelector('.block-ui').classList.add('blocked');
    }, false);
});
