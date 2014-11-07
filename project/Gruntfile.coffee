module.exports = (grunt) ->
  require('time-grunt')(grunt)
  require('load-grunt-tasks')(grunt)

  appConfig = grunt.file.readJSON('package.json')

  pathsConfig = (appName)->
    @app = appName || appConfig.name

    return {
      app: @app
      # assets
      coffee: 'assets/coffee'
      less: 'assets/less'
      temlatesSrc: 'assets/tmpl'
      # static
      bower: 'static/components'
      js: 'static/js'
      img: 'static/img'
      fonts: 'static/fonts'
      css: 'static/css'
      temlatesDst: 'static/js/tmpl'
    }

  grunt.initConfig({
    paths: pathsConfig(),
    pkg: appConfig,
    watch:
        grunt:
          files: ['Gruntfile.coffee']
        coffee:
          files: ['<%= paths.coffee %>/**/*.coffee']
          tasks: ['coffee']
        #less:
        #  files: ['<%= paths.less %>/**/*.less']
        #  tasks: ['less']
        #  options:
        #    nospawn: true
        #copy:
        #  files: ['<%= paths.temlatesSrc %>/**']
        #  tasks: ['copy']
        #  options:
        #    nospawn: true
    bower:
      install:
        options:
          targetDir: '<%= paths.bower %>'
          layout: 'byComponent'
          #install: false
          verbose: false
          cleanTargetDir: true
          cleanBowerDir: false
          bowerOptions: {}
    less:
      development:
        options:
          paths: ['./assets/less'],
        files:
          {'<%= paths.css %>/app.css': '<%= paths.less %>/app.less'}
    copy:
      main:
        expand: true
        cwd: '<%= paths.temlatesSrc %>'
        src: ['**']
        dest: '<%= paths.temlatesDst %>'
    coffee: {
      frontend:
        options:
          bare: true
        expand: true
        flatten: false
        cwd: '<%= paths.coffee %>'
        src: ['**/*.coffee']
        dest: '<%= paths.js %>'
        ext: '.js'
    }
  })


  grunt.registerTask('build', ['bower', 'coffee', 'less', 'copy'])
  grunt.registerTask('default', ['build', 'watch'])
