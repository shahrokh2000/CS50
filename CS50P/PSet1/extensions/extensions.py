L = {
    'gif' : "image/gif",
    'jpg' : "image/jpeg",
    'jpeg' : "image/jpeg",
    'png' : "image/png",
    'pdf' : "application/pdf",
    'txt' : "text/plain",
    'zip' : "application/zip"
}

a = input('File name: ').strip().lower()

if a.rfind('.') != -1:
    index = int(a.rindex('.')) + 1
    b = a[index:]

    if b in L:
        print(L[b])
    else:
        print('application/octet-stream')

else:
    print('application/octet-stream')
