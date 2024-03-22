file { '/home/ubuntu/.ssh/config':
    ensure  => file,
    content => "\
	Host *
    		HostName 52.87.233.136
    		User ubuntu
    		IdentityFile ~/.ssh/school
    		PreferredAuthentications publickey
    		PasswordAuthentication no
	",
  }
