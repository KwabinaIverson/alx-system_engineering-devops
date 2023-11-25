# init.pp

node '9665f0a47391' {
  package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }
}
