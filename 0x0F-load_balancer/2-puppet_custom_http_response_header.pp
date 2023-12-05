# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a custom fact to retrieve the hostname
facts:
  'custom_hostname' => '/bin/hostname -f'

# Configure Nginx with custom header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('path/to/nginx_config.erb'), # Path to your custom Nginx configuration template
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
