IP:
10.10.11.243
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-11-09 22:42 CET                                                                                                
Nmap scan report for 10.10.11.243                                                                                                                              
Host is up (0.062s latency).                                                                                                                                   
Not shown: 65523 closed tcp ports (conn-refused)                                                                                                               
PORT      STATE SERVICE    VERSION                                                                                                                             
22/tcp    open  ssh        OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.
80/tcp    open  http       nginx 1.18.0 (Ubuntu)                                       
1337/tcp  open  http       nginx 1.18.0 (Ubuntu)  
1338/tcp  open  http       nginx 1.18.0 (Ubuntu)                         
8161/tcp  open  http       Jetty 9.4.39.v20210325
9999/tcp  open  http       nginx 1.18.0 (Ubuntu)                                        
42041/tcp open  tcpwrapped
61613/tcp open  stomp      Apache ActiveMQ
61614/tcp open  http       Jetty 9.4.39.v20210325                               
|_  Potentially risky methods: TRACE

61616/tcp open  apachemq   ActiveMQ OpenWire transport                                                                                                                                                              
| fingerprint-strings:                                                                                                                                                                                              
|   NULL:                                                                                                                                                                                                           
|     ActiveMQ                                                                                                                                                                                                      
|     TcpNoDelayEnabled                                                                                                                                                                                             
|     SizePrefixDisabled                                                                                                                                                                                            
|     CacheSize                                                                                                                                                                                                     
|     ProviderName                                                                                                                                                                                                  
|     ActiveMQ                                                                                                                                                                                                      
|     StackTraceEnabled                                                                                                                                                                                             
|     PlatformDetails                                                                                                                                                                                               
|     Java                                                                                                                                                                                                          
|     CacheEnabled                                                                                                                                                                                                  
|     TightEncodingEnabled                                                                                                                                                                                          
|     MaxFrameSize                                                                                                                                                                                                  
|     MaxInactivityDuration                                                                                                                                                                                         
|     MaxInactivityDurationInitalDelay                                                                                                                                                                              
|     ProviderVersion                                                                                                                                                                                               
|_    5.15.15                                                                                                                                                                                                       
3 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :                                      
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============                                                                                                                                          
SF-Port5672-TCP:V=7.93%I=7%D=11/9%Time=654D5261%P=x86_64-pc-linux-gnu%r(Ge                                                                                                                                          
SF:tRequest,89,"AMQP\x03\x01\0\0AMQP\0\x01\0\0\0\0\0\x19\x02\0\0\0\0S\x10\                                                                                                                                          
SF:xc0\x0c\x04\xa1\0@p\0\x02\0\0`\x7f\xff\0\0\0`\x02\0\0\0\0S\x18\xc0S\x01                                                                                                                                          
SF:\0S\x1d\xc0M\x02\xa3\x11amqp:decode-error\xa17Connection\x20from\x20cli                                                                                                                                          
SF:ent\x20using\x20unsupported\x20AMQP\x20attempted")%r(HTTPOptions,89,"AM                                                                                                                                          
SF:QP\x03\x01\0\0AMQP\0\x01\0\0\0\0\0\x19\x02\0\0\0\0S\x10\xc0\x0c\x04\xa1                                                                                                                                          
SF:\0@p\0\x02\0\0`\x7f\xff\0\0\0`\x02\0\0\0\0S\x18\xc0S\x01\0S\x1d\xc0M\x0                                                                                                                                          
SF:2\xa3\x11amqp:decode-error\xa17Connection\x20from\x20client\x20using\x2                                                                                                                                          
SF:0unsupported\x20AMQP\x20attempted")%r(RTSPRequest,89,"AMQP\x03\x01\0\0A                                                                                                                                          
SF:MQP\0\x01\0\0\0\0\0\x19\x02\0\0\0\0S\x10\xc0\x0c\x04\xa1\0@p\0\x02\0\0`                                                                                                                                          
SF:\x7f\xff\0\0\0`\x02\0\0\0\0S\x18\xc0S\x01\0S\x1d\xc0M\x02\xa3\x11amqp:d                                                                                                                                          
SF:ecode-error\xa17Connection\x20from\x20client\x20using\x20unsupported\x2                                                                                                                                          
SF:0AMQP\x20attempted")%r(RPCCheck,89,"AMQP\x03\x01\0\0AMQP\0\x01\0\0\0\0\                                                                                                                                          
SF:0\x19\x02\0\0\0\0S\x10\xc0\x0c\x04\xa1\0@p\0\x02\0\0`\x7f\xff\0\0\0`\x0                                                                                                                                          
SF:2\0\0\0\0S\x18\xc0S\x01\0S\x1d\xc0M\x02\xa3\x11amqp:decode-error\xa17Co                                                                                                                                          
SF:nnection\x20from\x20client\x20using\x20unsupported\x20AMQP\x20attempted                                                                                                                                          
SF:")%r(DNSVersionBindReqTCP,89,"AMQP\x03\x01\0\0AMQP\0\x01\0\0\0\0\0\x19\                                                                                                                                          
SF:x02\0\0\0\0S\x10\xc0\x0c\x04\xa1\0@p\0\x02\0\0`\x7f\xff\0\0\0`\x02\0\0\                                                                                                                                          
SF:0\0S\x18\xc0S\x01\0S\x1d\xc0M\x02\xa3\x11amqp:decode-error\xa17Connecti                                                                                                                                          
SF:on\x20from\x20client\x20using\x20unsupported\x20AMQP\x20attempted")%r(D                                                                                                                                          
SF:NSStatusRequestTCP,89,"AMQP\x03\x01\0\0AMQP\0\x01\0\0\0\0\0\x19\x02\0\0                                                                                                                                          
SF:\0\0S\x10\xc0\x0c\x04\xa1\0@p\0\x02\0\0`\x7f\xff\0\0\0`\x02\0\0\0\0S\x1                                                                                                                                          
SF:8\xc0S\x01\0S\x1d\xc0M\x02\xa3\x11amqp:decode-error\xa17Connection\x20f                                                                                                                                          
SF:rom\x20client\x20using\x20unsupported\x20AMQP\x20attempted")%r(SSLSessi                                                                                                                                          
SF:onReq,89,"AMQP\x03\x01\0\0AMQP\0\x01\0\0\0\0\0\x19\x02\0\0\0\0S\x10\xc0                                                                                                                                          
SF:\x0c\x04\xa1\0@p\0\x02\0\0`\x7f\xff\0\0\0`\x02\0\0\0\0S\x18\xc0S\x01\0S                                                                                                                                          
SF:\x1d\xc0M\x02\xa3\x11amqp:decode-error\xa17Connection\x20from\x20client                                                                                                                                          
SF:\x20using\x20unsupported\x20AMQP\x20attempted")%r(TerminalServerCookie,                                                                                                                                          
SF:89,"AMQP\x03\x01\0\0AMQP\0\x01\0\0\0\0\0\x19\x02\0\0\0\0S\x10\xc0\x0c\x                                                                                                                                          
SF:04\xa1\0@p\0\x02\0\0`\x7f\xff\0\0\0`\x02\0\0\0\0S\x18\xc0S\x01\0S\x1d\x                                                                                                                                          
SF:c0M\x02\xa3\x11amqp:decode-error\xa17Connection\x20from\x20client\x20us                                                                                                                                          
SF:ing\x20unsupported\x20AMQP\x20attempted");                                                                                                                                                                       
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============                                                                                                                                          
SF-Port61613-TCP:V=7.93%I=7%D=11/9%Time=654D525C%P=x86_64-pc-linux-gnu%r(H                                                                                                                                          
SF:ELP4STOMP,27F,"ERROR\ncontent-type:text/plain\nmessage:Unknown\x20STOMP                                                                                                                                          
SF:\x20action:\x20HELP\n\norg\.apache\.activemq\.transport\.stomp\.Protoco                                                                                                                                          
SF:lException:\x20Unknown\x20STOMP\x20action:\x20HELP\n\tat\x20org\.apache                                                                                                                                          
SF:\.activemq\.transport\.stomp\.ProtocolConverter\.onStompCommand\(Protoc                                                                                                                                          
SF:olConverter\.java:258\)\n\tat\x20org\.apache\.activemq\.transport\.stom                                                                                                                                          
SF:p\.StompTransportFilter\.onCommand\(StompTransportFilter\.java:85\)\n\t                                                                                                                                          
SF:at\x20org\.apache\.activemq\.transport\.TransportSupport\.doConsume\(Tr                                                                                                                                          
SF:ansportSupport\.java:83\)\n\tat\x20org\.apache\.activemq\.transport\.tc                                                                                                                                          
SF:p\.TcpTransport\.doRun\(TcpTransport\.java:233\)\n\tat\x20org\.apache\.                                                                                                                                          
SF:activemq\.transport\.tcp\.TcpTransport\.run\(TcpTransport\.java:215\)\n                                                                                                                                          
SF:\tat\x20java\.lang\.Thread\.run\(Thread\.java:750\)\n\0\n");                                                                                                                                                     
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============                                                                                                                                          
SF-Port61616-TCP:V=7.93%I=7%D=11/9%Time=654D525C%P=x86_64-pc-linux-gnu%r(N                                                                                                                                          
SF:ULL,140,"\0\0\x01<\x01ActiveMQ\0\0\0\x0c\x01\0\0\x01\*\0\0\0\x0c\0\x11T                                                                                                                                          
SF:cpNoDelayEnabled\x01\x01\0\x12SizePrefixDisabled\x01\0\0\tCacheSize\x05                                                                                                                                          
SF:\0\0\x04\0\0\x0cProviderName\t\0\x08ActiveMQ\0\x11StackTraceEnabled\x01                                                                                                                                          
SF:\x01\0\x0fPlatformDetails\t\0\x04Java\0\x0cCacheEnabled\x01\x01\0\x14Ti                                                                                                                                          
SF:ghtEncodingEnabled\x01\x01\0\x0cMaxFrameSize\x06\0\0\0\0\x06@\0\0\0\x15                                                                                                                                          
SF:MaxInactivityDuration\x06\0\0\0\0\0\0u0\0\x20MaxInactivityDurationInita                                                                                                                                          
SF:lDelay\x06\0\0\0\0\0\0'\x10\0\x0fProviderVersion\t\0\x075\.15\.15");                                                                                                                                             
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel                                                                                                                                                             

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                                                                                      
Nmap done: 1 IP address (1 host up) scanned in 64.85 seconds                                                                                                                                                        
┌─[quiescent@parrot]─[~]                                           
```