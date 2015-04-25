from flask.ext.assets import Bundle

less = Bundle(
  'bootstrap-less/bootstrap.less',
  'less/style.less',
  depends='bootstrap-less/*',
  filters='less',
  output='dist/style.css'
)

css = Bundle(
  less,
  filters='cssmin',
  output='dist/style.min.css'
)

js = Bundle(
  'js/jquery-2.1.3.min.js',
  'js/bootstrap.min.js',
  'js/script.js',
  filters='jsmin',
  output='dist/script.min.js'
)
