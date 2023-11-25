# init.pp

package { 'flask':
  ensure => '2.1.0',
  porvider => 'pip3',
}
