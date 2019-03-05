# 0x14. Mysql
![mysql](https://images.all-free-download.com/images/graphiclarge/mysql_68829.jpg)

#### What I should learn:
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- Why database backups need to be stored in different physical locations

### Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 14.04 LTS
- Bash scripts are executable
- Bash scripts pass `Shellcheck` (version `0.3.3-1~ubuntu14.04.1` via `apt-get`)
- First line of Bash scripts is `#!/usr/bin/env bash`
- Second line of Bash scripts is a comment

---
File | Description
-----|------------
0-mysql\_configuration\_primary, 0-mysql\_configuration\_replica | Installs and configures MyMSQL on `web-01` and `web-02` to form a primary/replica cluster.
1-mysql\_backup | Bash script that generates a MySQL dump and creates a compressed archive out of it.

#### Author
Nicole Swanson - [@Nicolette_Swan](https://twitter.com/Nicolette_Swan)
