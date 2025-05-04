```
USER nathan
PASS Buck3tH4TF0RM3!
```

Priv esq:

Python has the capability of using setuid as the owner of the group (root), so if you run python as Nathan (non-root) you can import os and run os.setuid(0) to get the uid of root. Then you can run bash as root with os.system("/bin/bash").