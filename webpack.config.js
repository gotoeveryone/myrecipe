const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = [
    {
        entry: {
            app: './resources/ts/app.module',
        },
        output: {
            path: path.join(__dirname, 'static/js'),
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
                    test: /\.(html|css)$/,
                    loader: 'raw-loader',
                },
            ],
        },
        plugins: [
            new webpack.DefinePlugin({
                'PRODUCTION': (process.env.NODE_ENV === 'production'),
            }),
        ],
    },
    {
        entry: './resources/sass/app.scss',
        output: {
            path: path.join(__dirname, 'static/css'),
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
