---
type: box
finished: "false"
writeup: "false"
---
# Notes:
### IP: 
10.10.11.219
### Difficulty:
Easy

# nmap
with nmap `nmap -p- -sV -sC 10.10.11.219` we got this result:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 20be60d295f628c1b7e9e81706f168f3 (RSA)
|   256 0eb6a6a8c99b4173746e70180d5fe0af (ECDSA)
|_  256 d14e293c708669b4d72cc80b486e9804 (ED25519)
80/tcp open  http    nginx 1.18.0
|_http-title: Did not follow redirect to http://pilgrimage.htb/
|_http-server-header: nginx/1.18.0
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

So we know there's a SSH server, and a http server running nginx 1.18

//what to check

- Google common file upload vulns
- Maybe upload file and make it connect back to you on SSRF
- hmmm do not know

