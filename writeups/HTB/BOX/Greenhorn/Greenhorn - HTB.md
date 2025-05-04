Nmap
```
PORT     STATE SERVICE   REASON  VERSION  
22/tcp   open  ssh       syn-ack OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)  

PORT   STATE SERVICE VERSION  
80/tcp open  http    nginx 1.18.0 (Ubuntu)  
|_http-trane-info: Problem with XML parsing of /evox/about  
| http-title: Welcome to GreenHorn ! - GreenHorn  
|_Requested resource was http://greenhorn.htb/?file=welcome-to-greenhorn  
| http-robots.txt: 2 disallowed entries    
|_/data/ /docs/  
|_http-server-header: nginx/1.18.0 (Ubuntu)  
|_http-generator: pluck 4.7.18  
| http-cookie-flags:    
|   /:    
|     PHPSESSID:    
|_      httponly flag not set  
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

3000/tcp open  http      syn-ack Golang net/http server  
| http-methods:    
|_  Supported Methods: HEAD GET  
|_http-title: GreenHorn  
|_http-favicon: Unknown favicon MD5: F6E1A9128148EEAD9EFF823C540EF471  
| fingerprint-strings:    
|   GenericLines, Help, RTSPRequest:    
|     HTTP/1.1 400 Bad Request  
|     Content-Type: text/plain; charset=utf-8  
|     Connection: close  
|     Request  
|   GetRequest:    
|     HTTP/1.0 200 OK  
|     Cache-Control: max-age=0, private, must-revalidate, no-transform  
|     Content-Type: text/html; charset=utf-8  
|     Set-Cookie: i_like_gitea=9dde25bb34774b6e; Path=/; HttpOnly; SameSite=Lax  
|     Set-Cookie: _csrf=L1FMXiQMBOazVBXAI0MQ_jt91JY6MTcyNzI2NjcyNzcyOTgyODMwNA; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax  
|     X-Frame-Options: SAMEORIGIN  
|     Date: Wed, 25 Sep 2024 12:18:47 GMT  
|     <!DOCTYPE html>  
|     <html lang="en-US" class="theme-auto">  
|     <head>  
|     <meta name="viewport" content="width=device-width, initial-scale=1">  
|     <title>GreenHorn</title>  
|     <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiR3JlZW5Ib3JuIiwic2hvcnRfbmFtZSI6IkdyZWVuSG9ybiIsInN0YXJ0X3VybCI6Imh0dHA6Ly9ncmVlbmhvcm4uaHRiOjMwMDAvIiwiaWNv  
bnMiOlt7InNyYyI6Imh0dHA6Ly9ncmVlbmhvcm4uaHRiOjMwMDAvYXNzZXRzL2ltZy9sb2dvLnBuZyIsInR5cGUiOiJpbWFnZS9wbmciLCJzaXplcyI6IjUxMng1MTIifSx7InNyYyI6Imh0dHA6Ly9ncmVlbmhvcm4uaHRiOjMwMDAvYX  
|   HTTPOptions:    
|     HTTP/1.0 405 Method Not Allowed  
|     Allow: HEAD  
|     Allow: GET  
|     Cache-Control: max-age=0, private, must-revalidate, no-transform  
|     Set-Cookie: i_like_gitea=5a3169f8726bd7f7; Path=/; HttpOnly; SameSite=Lax  
|     Set-Cookie: _csrf=IPBxo2WJPuZlkEaLIfsjqxCh3jg6MTcyNzI2NjcyNzkxNDI0Mzk4Nw; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax  
|     X-Frame-Options: SAMEORIGIN  
|     Date: Wed, 25 Sep 2024 12:18:47 GMT  
|_    Content-Length: 0  
8000/tcp open  http-alt? syn-ack
```

Robots.txt:
```
User-agent: *
Disallow: /data/
Disallow: /docs/
```


Vulnurable RCE payload for module upload
```
https://sploitus.com/exploit?id=PACKETSTORM:173640
```