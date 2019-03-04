# Postmortem
### [500 Internal Server Error](https://github.com/thenicopixie/holberton-system_engineering-devops/tree/master/0x17-web_stack_debugging_3)
![this_is_fine](https://www.dailydot.com/wp-content/uploads/6f2/bb/20130109-1022x512.png)

### Date
03-04-2019

### Author
- Nicole Swanson

### Status:
[Bug fixed](https://github.com/thenicopixie/holberton-system_engineering-devops/tree/master/0x17-web_stack_debugging_3). Server returns a status code of `200 OK`

### Summary
Monday, March 4th at 2pm access to the server went down and was not able to be access via website or curling the IP address. The server was returning a `500 Internal Server Error`.

![500_error_cat](https://i.chzbgr.com/full/1999218944/h369E3AB7/)

### Timeline
---
Time | Description
-----|-------------
2:00 PM | Access to server went down. Received `500 Internal Server Error` when requesting url site.
2:03 PM | Curled IP address in another terminal window. Again, got 500 internal error
2:07 PM | Ran ps -aux to see what ports were listening. Noted `www-data` listening on port
2:15 PM | Used `strace -p <pid> -o filename` to trace the `www-data` port and saved the result in a file
2:19 PM | In another terminal widow, curled the ip address again
2:24 PM | In the `strace` error log noted a typo. Site was trying to be configured with a filename extention `phpp` instead of `php`
2:29 PM | Searched in the `wp-config.php` file and found the the file `wp-setting.php` listed. Went to that file and found the typo there.
2:33 PM | Fixed the typo in the `wp-settings.php` file and curled `127.0.0.1` which returned status code `200 OK`


### Root Causes
---
The server was trying to configure using a file that did not exist. Instead of using `class-wp-locale.php`, it was trying to use `class-wp-locale.phpp`. This resulted in the server being unable to connect and returning the `500 Internal Server Error`.

### Lessons Learned
---
- For future risk prevention, local testing should be done on servers before deployment.
- Error logs should be kept to make any future debugging quicker and more efficient.
- Code review should be done to prevent typos and mistakes from going into production.
![lazy_code_review](https://image.slidesharecdn.com/webexpo-160923210924/95/how-to-successfully-grow-a-code-review-culture-61-638.jpg?cb=1476167539)
