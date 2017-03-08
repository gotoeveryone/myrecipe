const gulp = require('gulp');
const sass = require('gulp-sass');
const webpack = require('gulp-webpack');
const webpackConfig = require('./webpack.config.js');
// const typescript = require('gulp-typescript');

gulp.task('sass', function() {
    gulp.src('./resource/sass/*.scss')
            .pipe(sass())
            .pipe(gulp.dest('./public/css'));
});

gulp.task('webpack', () => {
    gulp.src('./resource/ts/*.ts')
            // .pipe(typescript({out: 'app.js'}))
            .pipe(webpack(webpackConfig))
            .pipe(gulp.dest('./public/js'));
});

gulp.task('watch', function() {
    gulp.watch('./resource/ts/*.ts', ['webpack']);
    gulp.watch('./resource/sass/*.scss', ['sass']);
});
