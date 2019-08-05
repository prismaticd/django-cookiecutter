'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

var root_input = './{{cookiecutter.project_slug}}/static_src/';
var root_output = './{{cookiecutter.project_slug}}/static/';

var sourcemaps = require('gulp-sourcemaps');
var refresh = require('gulp-refresh');

gulp.task('sass', function () {
  return gulp.src(root_input + "sass/base.scss")
      .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
      .pipe(sourcemaps.write("sourcemaps/"))
    .pipe(gulp.dest(root_output + "css"))
      .pipe(refresh());
});

const imagemin = require('gulp-imagemin');
gulp.task('images', function(cb) {
    return gulp.src(root_input + 'images/*')
        .pipe(imagemin())
        .pipe(gulp.dest(root_output + 'images'))
});

gulp.task('logo', function(cb) {
    return gulp.src(root_input + 'logo/*')
        .pipe(imagemin())
        .pipe(gulp.dest(root_output + 'logo'))
});

gulp.task('icons', function(cb) {
    return gulp.src(root_input + 'icons/*')
        .pipe(imagemin())
        .pipe(gulp.dest(root_output + 'icons'))
});


gulp.task('image_playground', function(cb) {
    return gulp.src(root_input + 'image_playground/input/*')
        .pipe(imagemin())
        .pipe(gulp.dest(root_input + 'image_playground/output'))
});

var uglify = require('gulp-uglify');

gulp.task('js', function() {
  return gulp.src(root_input + 'js/**/*.js')
      .pipe(sourcemaps.init())
    .pipe(uglify())
      .pipe(sourcemaps.write("sourcemaps/"))
    .pipe(gulp.dest(root_output + 'js'))
    .pipe(refresh())
});


gulp.task('watch', function () {
    refresh.listen();
  gulp.watch(root_input + "sass/**/*.scss", gulp.parallel('sass'));
  gulp.watch(root_input + "js/**/*.js", gulp.parallel('js'));
  gulp.watch(root_input + "../**/templates/**/*.html").on("change", refresh.reload);
});

gulp.task('default', gulp.parallel('sass', 'js', 'watch'));
gulp.task('img', gulp.parallel('images', 'logo', 'icons'));
