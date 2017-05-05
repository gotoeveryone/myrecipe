window.Vue = require('vue/dist/vue.min');
require('vue-resource');

// ウィンドウがロードできればフェードを解除
window.addEventListener('load', () => {
    document.querySelector('.content').classList.remove('fade');
}, false);
