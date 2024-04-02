# Automate the creation of custom http header
exec {'insert the header':
  command => 'apt-get -y update;
  apt-get -y install nginx;
  sed -i "/^\s\+try_files/a \ \t\tadd_header  X-Served-By  \"$HOSTNAME\" always;" /etc/nginx/sites-available/default;
  service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
