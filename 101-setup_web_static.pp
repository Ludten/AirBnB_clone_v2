# configure an nginx web server
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file { [  '/data/',
          '/data/web_static/',
          '/data/web_static/releases/',
          '/data/web_static/shared/',
          '/data/web_static/releases/test/', ] :
  ensure  =>  directory,
  recurse =>  true,
  owner   =>  'ubuntu',
  group   =>  'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
',
  require => Package['nginx'],
}

file { '/data/web_static/current':
  ensure =>  link,
  target =>  '/data/web_static/releases/test/',
}

file_line { 'index':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => ' location /hbnb_static/ {
                alias /data/web_static/current/;
        }
        ',
  require => Package['nginx'],
}


service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
