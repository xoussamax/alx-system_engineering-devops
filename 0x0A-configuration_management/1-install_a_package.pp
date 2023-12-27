# Using Puppet, install flask from pip3.
class { 'python':
  pip_provider => 'pip3',
}

python::pip { 'Flask':
  ensure => '2.1.0',
}
