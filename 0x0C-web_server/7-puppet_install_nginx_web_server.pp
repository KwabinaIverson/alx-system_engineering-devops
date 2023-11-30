# puppet/nginx_setup.pp

# Update package lists
exec { 'apt-update':
  command => 'apt-get update',
}

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create a simple HTML page with "Hello World!"
file { '/usr/share/nginx/html/index.html':
  content => 'Hello World!',
}

# Create a custom HTML page for the redirection
file { '/usr/share/nginx/html/redirect.html':
  content => '<html>
               <head>
                   <title>301 Moved Permanently</title>
               </head>
               <body>
                   <h1>301 Moved Permanently</h1>
                   <p>The document has moved <a href="https://www.youtube.com/watch?v=QH2-TGUlwu4">here</a>.</p>
               </body>
             </html>',
}

# Configure Nginx with a 301 redirect
file { '/etc/nginx/sites-available/default':
  content => "server {
                 listen 80 default_server;
                 listen [::]:80 default_server;

                 root /usr/share/nginx/html;
                 index index.html;

                 server_name _;

                 location / {
                     try_files \$uri \$uri/ =404;
                 }

                 location /redirect_me {
                     return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
                 }

                 error_page 404 /404.html;
                 location = /404.html {
                     internal;
                 }

                 error_page 500 502 503 504 /50x.html;
                 location = /50x.html {
                     internal;
                 }
             }",
}

# Restart Nginx after configuration changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
