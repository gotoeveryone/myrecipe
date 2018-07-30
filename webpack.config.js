const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');

module.exports = {
    devtool: process.env.NODE_ENV !== 'production' ? false : 'source-map',
    entry: {
        'js/app.js': './resources/ts/main.ts',
        'css/app.css': './resources/sass/app.scss',
    },
    output: {
        path: path.join(__dirname, 'templates', 'assets'),
        filename: '[name]',
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js', '.scss', 'css'],
    },
    stats: 'minimal',
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                loader: 'ts-loader',
            },
            {
                test: /\.(html|css)$/,
                loader: 'raw-loader',
            },
            {
                test: /\.scss$/,
                exclude: /node_modules/,
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    use: 'css-loader!sass-loader',
                }),
            },
            // Ignore warnings about System.import in Angular
            {
                test: /[\/\\]@angular[\/\\].+\.js$/,
                parser: {
                    system: true,
                },
            },
        ],
    },
    plugins: [
        // Ignore warnings about Critical dependency in Angular
        new webpack.ContextReplacementPlugin(
            /(.+)?angular(\\|\/)core(.+)?/,
            path.join(__dirname, 'resources'), {}
        ),
        new ExtractTextPlugin({
            filename: '[name]',
            disable: false,
            allChunks: true,
        }),
        new FriendlyErrorsWebpackPlugin(),
    ],
    performance: {
        hints: false,
    },
};
