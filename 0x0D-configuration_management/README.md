# Configuration management
#### Requirements
- All files interpreted on Ubuntu 14.04 LTS
- Puppet manifests pass `puppet-lint` without errors
- Puppet manifests run without error
- Puppet manifests first line is a comment
- Puppet manifests files end with the extention `.pp`
- File checked with Puppet v3.4

--
File | Description
0-create\_a\_file.pp | Using Puppet, create a file in `/tmp`. File path is `/tmp`holberton`. File permission is `0744`. File owner is `www-data`. File groupd is `www-data`. File containts `I love Puppet`
1-install_a_package.pp | Using Puppet, install `puppet-lint`
2-execute_a_command.pp | Using Puppet, create a manifest that kills a process named `killmenow`. Must be the `exec` Puppet resource. Must use `pkill`

#### Author
Nicole Swanson = [@Nicolette_Swan](https://twitter.com/Nicolette_Swan)
