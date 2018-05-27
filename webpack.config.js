const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');

module.exports = {
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
        loaders: [{
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
        ],
    },
    plugins: [
        new webpack.ContextReplacementPlugin(
            /(.+)?angular(\\|\/)core(.+)?/,
            path.join(__dirname, 'resources'), {}
        ),
        new webpack.DefinePlugin({
            'PRODUCTION': (process.env.NODE_ENV === 'production'),
        }),
        new ExtractTextPlugin({
            filename: '[name]',
            disable: false,
            allChunks: true,
        }),
        new FriendlyErrorsWebpackPlugin(),
    ],
};
