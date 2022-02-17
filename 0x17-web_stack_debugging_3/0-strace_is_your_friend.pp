# Using Strace to fix a problem
exec { 'fix-wordpress':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell,
}