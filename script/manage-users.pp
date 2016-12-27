# assume directory modules/new_users_home_files/files/profiles contain a list of files like .bashrc, .profile, etc
# and we want supply them on destination hosts which starts with dev prefix.

node /dev.*/ {
    user { 'new_user':
        ensure           => present,
        groups           => 'developers',
        comment          => 'New User',
        password         => '$1$kGu3KjX5$AM3iZGvwkmIpszKhJvUQb1',
        password_max_age => '365',
        password_min_age => '0',
        home             => '/home/new_user',
        managehome       => true,
        shell            => '/bin/bash',
    }
    file { '/home/new_user':
        ensure  => 'directory',
        source  => 'puppet:///modules/new_users_home_files/profiles',
        recurse => true,
        owner   => 'new_user',
        group   => 'new_user',
        mode    => '640',
    }
}

# password can be generated by command openssl passwd -1 