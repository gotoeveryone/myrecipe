const path = require('path');

module.exports = {
    entry: './resource/js/app.js',
    output: {
        path: path.join(__dirname, 'public/js'),
        filename: 'app.js'
    },
    resolve: {
        extensions:['', '.vue', '.js']
    },
    module: {
        loaders: [
            { test: /\.vue$/, loader: 'vue' }
        ]
    },
    vue: {
        // loaders: { js: 'vue-ts-loader' },
        esModule: true
    }
};
