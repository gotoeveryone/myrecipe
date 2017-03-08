const path = require('path');

module.exports = {
    entry: './resource/ts/app.ts',
    output: {
        path: path.join(__dirname, 'public/js'),
        filename: 'app.js'
    },
    resolve: {
        // alias: {
        //     'vue$': 'vue/dist/vue.common.js'
        // },
        extensions:['', '.ts', '.js']
    },
    module: {
        loaders: [
            { test: /\.vue$/, loader: 'vue' },
            { test: /\.ts$/, loader: 'vue-ts' }
        ]
    },
    vue: {
        loaders: { js: 'vue-ts-loader' },
        esModule: true
    }
};
