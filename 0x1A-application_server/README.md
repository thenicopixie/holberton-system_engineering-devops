# README
## Application Server

![server](https://i.redd.it/xrbttena25301.gif)

## Requirements

#### General

- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments

#### Bash Scripts
- All files will are interpreted on Ubuntu 14.04 LTS
- All files end with a new line
- All Bash script files are executable
- Bash scripts pass `Shellcheck` (`version 0.3.3-1~ubuntu14.04.1` via `apt-get`)
- First line of Bash scripts is `#!/usr/bin/env bash`
- The second line of Bash scripts is a comment

![server_structure](https://datadog-prod.imgix.net/img/blog/nginx-502-bad-gateway-errors-gunicorn/gunicorn-health-focus-3.png?fit=max)

Update local packages and install packages:

```
sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx
```

Install `virtualenv`:

`sudo pip3 install virtualenv`

To create a virtual environment in a project, cd into the project, then do:
`virtualenv projectenv`

Activate the virtual environment:
`source projectenv/bin/activate`

Prompt now changes to:
`(projectenv) user@host:~/project$`

Creating an Upstart script:
- create a conf file for your project in the `/etc/init/` directory (`/etc/init/project.conf`)
- `0-welcome_gunicorn-upstart_config` is the conf file for this

Configuring Nginx to Proxy Requests:
- Go to `/etc/nginx/sites-available/defualt` and add a new route for the new location.
- `0-welcome_gunicorn-nginx_config` is the config file for this nginx
- Next, restart nginx -> `sudo service nginx restart`

#### Author
Nicole Swanson - [@Nicolette_Swan](https://twitter.com/Nicolette_Swan)
