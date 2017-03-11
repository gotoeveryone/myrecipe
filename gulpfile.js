const gulp = require('gulp');
const sass = require('gulp-sass');
const webpack = require('gulp-webpack');
const webpackConfig = require('./webpack.config.js');

gulp.task('sass', function() {
    gulp.src('./resource/sass/*.scss')
            .pipe(sass())
            .pipe(gulp.dest('./public/css'));
});

gulp.task('webpack', () => {
    gulp.src('./resource/js/*.js')
            .pipe(webpack(webpackConfig))
            .pipe(gulp.dest('./public/js'));
});

gulp.task('watch', function() {
    gulp.watch('./resource/js/*.js', ['webpack']);
    gulp.watch('./resource/sass/*.scss', ['sass']);
});
