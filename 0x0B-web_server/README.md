# 0x0B. Web server
![web_server_illustration](https://cdn.dribbble.com/users/949592/screenshots/4211815/worry-free-2.jpg)
#### What I should learn:
- What DNS stands for
- What is DNS main role
- What are DNS record types for:
	- A
	- CNAME
	-TXT
	- MX
- What is the main role of a web server
- What is a child process
- Why web server usually have a parent process and child process
- What are the main HTTP requests

#### Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted on Ubuntu 14.04 LTS
- All Bash scripts are executable
- Bash scrips pass `Shellcheck` (version `0.3.3-1~ubuntu14.04.1` via `apt-get`)
- The first line of Bash scripts is `!3/usr/bin/env bash`
- The second line of Bash scrips is a comment explaining what the script is doing

---
File | Descirption
-----|------------
0-transfer\_file | Bash script that transers a file from a client to a server
1-install\_nginx\_web\_server | Install nginx web server
2-setup\_a\_domain\_name | Setup a domain name using Gandi.
3-redirection | Configure the Ngink server so that `/redirect_me` is redirecting to another page
4-not\_found\_page\_404 | Configure the Ngink server to have a custom 404 page that contains the string `Ceci n'est pas une page`

#### Author
Nicole Swanson - [@Nicolette_Swan](https://twitter.com/Nicolette_Swan)
