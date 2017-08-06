const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = [
    {
        entry: {
            app: './resources/ts/app',
        },
        output: {
            path: path.join(__dirname, 'public/js'),
            filename: '[name].js',
        },
        resolve: {
            extensions: ['.ts', '.tsx', '.js'],
        },
        module: {
            loaders: [
                {
                    test: /\.tsx?$/,
                    loader: 'ts-loader',
                },
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    loader: 'buble-loader',
                },
            ],
        },
        plugins: [
            new webpack.DefinePlugin({
                'PRODUCTION': (process.env.NODE_ENV === 'production'),
            }),
        ],
    },
    // {
    //     entry: {
    //         app: './resources/js/app.js',
    //     },
    //     output: {
    //         path: path.join(__dirname, 'public/js'),
    //         filename: '[name].js'
    //     },
    //     resolve: {
    //         extensions: ['.vue', '.js']
    //     },
    //     module: {
    //         loaders: [
    //             {
    //                 test: /\.vue$/,
    //                 loader: 'vue-loader',
    //                 options: {
    //                     loaders: {
    //                         js: 'buble-loader'
    //                     }
    //                 },
    //             },
    //             {
    //                 test: /\.js$/,
    //                 exclude: /node_modules/,
    //                 loader: 'buble-loader',
    //             },
    //         ]
    //     },
    //     plugins: [
    //     ],
    // },
    {
        entry: './resources/sass/app.scss',
        output: {
            path: path.join(__dirname, 'public/css'),
            filename: 'app.css',
        },
        resolve: {
            extensions: ['.scss', 'css'],
        },
        plugins: [
            new ExtractTextPlugin({
                filename: 'app.css',
                disable: false,
                allChunks: true,
            }),
        ],
        module: {
            loaders: [
                {
                    test: /\.scss$/,
                    exclude: /node_modules/,
                    use: ExtractTextPlugin.extract({
                        fallback: 'style-loader',
                        use: 'css-loader!sass-loader',
                    }),
                },
            ],
        },
    },
];
