# 1-install_a_package.pp

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin'],
  refreshonly => true,
  require     => Package['python3-pip'],
}

exec { 'check_flask_version':
  command => '/usr/bin/flask --version',
  path    => ['/usr/bin'],
  logoutput => true,
  unless  => '/usr/bin/flask --version | grep "Flask 2.1.0"',
  require => Exec['install_flask'],
}
