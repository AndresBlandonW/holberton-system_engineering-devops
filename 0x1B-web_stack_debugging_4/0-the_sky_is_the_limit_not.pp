#!/usr/bin/env bash
# Fix 943 requests failed and our stack so that we get to 0
exec { 'fix--for-nginx':
  command => "sed -i '5c ULIMIT=\"-n 4096\"' /etc/default/nginx && sudo service nginx restart",
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}