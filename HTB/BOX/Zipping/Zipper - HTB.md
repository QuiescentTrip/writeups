---
type: box
finished: "false"
writeup: "false"
---
# Info
IP:
10.10.11.229

# Enum




### notes:

might be LFI
http://10.10.11.229/shop/index.php?page=a

might upload a file:
http://10.10.11.229/upload.php

code:

```html
<form id="zip-form" enctype="multipart/form-data" method="post" action="[upload.php](view-source:http://10.10.11.229/upload.php)">
              <div class="mb-3">
                <input type="file" class="form-control" name="zipFile" accept=".zip">
              </div>
              <button type="submit" class="btn btn-primary" name="submit">Upload</button>
            </form><!-- End submit file -->
```
