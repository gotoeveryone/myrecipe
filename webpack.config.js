const path = require('path');

module.exports = {
    entry: './resources/js/app.js',
    output: {
        path: path.join(__dirname, 'public/js'),
        filename: 'app.js'
    },
    resolve: {
        extensions:['.vue', '.js']
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
    ],
};
