# Install Flask 2.1.0
package { 'Flask':
  ensure          => '2.1.0',
  provider        => 'pip3',
  install_options => ['--upgrade'],
}
