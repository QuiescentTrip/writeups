nmap
```
PORT      STATE SERVICE      VERSION  
135/tcp   open  msrpc        Microsoft Windows RPC  
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn  
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (work  
group: WORKGROUP)  
49152/tcp open  msrpc        Microsoft Windows RPC  
49153/tcp open  msrpc        Microsoft Windows RPC  
49154/tcp open  msrpc        Microsoft Windows RPC  
49155/tcp open  msrpc        Microsoft Windows RPC  
49156/tcp open  msrpc        Microsoft Windows RPC  
49157/tcp open  msrpc        Microsoft Windows RPC  
Service Info: Host: HARIS-PC; OS: Windows; CPE: cpe:/o:microsoft:windows  
  
Host script results:  
|_clock-skew: mean: -19m56s, deviation: 34m35s, median: 1s  
| smb2-time:    
|   date: 2024-09-25T13:42:29  
|_  start_date: 2024-09-25T13:35:32  
| smb-security-mode:    
|   account_used: guest  
|   authentication_level: user  
|   challenge_response: supported  
|_  message_signing: disabled (dangerous, but default)  
| smb2-security-mode:    
|   2:1:0:    
|_    Message signing enabled but not required  
| smb-os-discovery:    
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)  
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional  
|   Computer name: haris-PC  
|   NetBIOS computer name: HARIS-PC\x00  
|   Workgroup: WORKGROUP\x00  
|_  System time: 2024-09-25T14:42:32+01:00  
```

EternalBlue:
used metasploit :3
