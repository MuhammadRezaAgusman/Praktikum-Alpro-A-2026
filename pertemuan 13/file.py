#import time
f = open("contoh.txt", "rt")
print(f.read())

f.close()

#time.sleep(5)
with open("contoh.txt", "w") as f:
    f.write("\nSelamat kena hacknjhbecnjkfhjwf")

import os
if os.path.exists("File Baru.txt"):
    os.remove("File Baru.txt")
else:
    print("File Telah Dihapus")

