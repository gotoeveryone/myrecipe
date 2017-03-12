const path = require('path');
const webpack = require('webpack-stream');

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
            {
                test: /\.vue$/,
                loader: 'vue'
            }
        ]
    },
    plugins: [
        new webpack.webpack.optimize.UglifyJsPlugin({ minimize: true })
    ],
    vue: {
        esModule: true
    }
};
