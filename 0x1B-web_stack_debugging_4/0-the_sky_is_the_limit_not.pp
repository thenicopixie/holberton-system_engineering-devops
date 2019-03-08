# puppet manifest to fix error Too Many Open Files by increasing the ulimit value
exec { '/etc/default/nginx':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx; sudo service nginx restart"
}
