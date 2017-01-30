'use strict'

var gulp = require('gulp');
var sass = require('gulp-sass');
var util = require('gulp-util');

var sassOutput;
var env = process.env.NODE_ENV || 'development'
env == 'development' ? "extended" : "compressed"


gulp.task("sass", function(){
    gulp.src('blog/static/blog/*.sass')
    .pipe(sass({outputStyle: sassOutput}).on('error', sass.logError))
    .pipe(gulp.dest('./blog/static/blog/'));
});



gulp.task("watch", function(){
    gulp.watch("blog/static/blog/*.sass", ['sass']);
});

gulp.task("default", ['watch', 'sass'])
