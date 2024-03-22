 exec { 'killmenow':
    command => 'pkill killmenow',
    path        => ['/bin', '/usr/bin'], # Specify PATH environment variable
  }
