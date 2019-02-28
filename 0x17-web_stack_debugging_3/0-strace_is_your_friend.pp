# puppet manifest to fix typo in file
exec { '/var/www/html/wp-settings.php':
  path    => '/bin',
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php'
}
