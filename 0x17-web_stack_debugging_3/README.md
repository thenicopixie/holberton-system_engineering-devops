# 0x17. Web stack debugging #3
![debugging](https://www.fivesquid.com/pics/t2/1482092358-63262-1-1_236px.jpg)
#### Requirements:
- All files are interpreted on Ubuntu 14.04 LTS
- All files end with a new line
- Puppet manifests pass `puppet-lint` without any errors (`version 2.1.1`)
- Puppet manifests run without error
- Puppet manifests first line is a comment explaining the Puppet manifest
- Puppet manifests files end with the extension `.pp`
- Files are checked with `Puppet v3.4`

---

#### Install `puppet-lint`
`gem install puppet-lint -v 2.1.1`

---
File | Description
0-strace\_is\_your\_friend.pp | Using `strace`, find out why Apache is returning a 500 error. Next, find and fix the issue, then automate it using Puppet.

---

#### Author
Nicole Swanson - [@Nicolette_Swan](https://twitter.com/Nicolette_Swan)
