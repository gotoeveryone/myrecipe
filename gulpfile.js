const gulp = require('gulp');
const sass = require('gulp-sass');
const webpack = require('webpack-stream');
const webpackConfig = require('./webpack.config.js');

gulp.task('sass', () => {
    gulp.src('./resource/sass/*.scss')
            .pipe(sass())
            .pipe(gulp.dest('./public/css'));
});

gulp.task('webpack', () => {
    gulp.src('./resource/js/*.js')
            .pipe(webpack(webpackConfig))
            .pipe(gulp.dest('./public/js'));
});

gulp.task('watch', () => {
    gulp.watch('./resource/js/*.js', ['webpack']);
    gulp.watch('./resource/sass/*.scss', ['sass']);
});

gulp.task('production', ['sass', 'webpack'], () => {
});
