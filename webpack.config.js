/* eslint-disable @typescript-eslint/no-var-requires */
const path = require('path');
const webpack = require('webpack');
const FixStyleOnlyEntriesPlugin = require('webpack-fix-style-only-entries');
const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const StylelintBarePlugin = require('stylelint-bare-webpack-plugin');
/* eslint-enable @typescript-eslint/no-var-requires */

module.exports = (_, args) => {
  return {
    devtool: args.mode !== 'production' ? false : 'source-map',
    entry: {
      'js/app': './resources/scripts/main.ts',
      'css/app': './resources/styles/app.scss',
    },
    output: {
      path: path.join(__dirname, 'templates', 'assets'),
    },
    resolve: {
      extensions: ['.ts', '.tsx', '.js', '.scss', 'css'],
    },
    stats: 'minimal',
    module: {
      rules: [
        {
          enforce: 'pre',
          test: /\.tsx?$/,
          exclude: /node_modules/,
          use: [
            {
              loader: 'eslint-loader',
              options: {
                esModule: true,
              },
            },
          ],
        },
        {
          test: /\.tsx?$/,
          loader: 'ts-loader',
        },
        {
          test: /\.(html|css)$/,
          loader: 'raw-loader',
        },
        {
          test: /\.(sa|sc|c)ss$/,
          exclude: /node_modules/,
          use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
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
        path.join(__dirname, 'resources'),
        {},
      ),
      new FixStyleOnlyEntriesPlugin(),
      new FriendlyErrorsWebpackPlugin(),
      new MiniCssExtractPlugin({
        filename: '[name].css',
      }),
      new StylelintBarePlugin({
        files: ['resources/styles/**/*.scss'],
      }),
    ],
    performance: {
      hints: false,
    },
  };
};
