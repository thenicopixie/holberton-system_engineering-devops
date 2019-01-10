# Create a manifest that kills a process named killmenow
exec { 'sleep':
  command => "pkill 'sleep'",
  path    => '/usr/bin'
}
