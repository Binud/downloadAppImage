import requests
print('Starting to download')
url = 'https://github.com/martpie/museeks/releases/download/0.9.3/museeks-x86_64.AppImage'
r = requests.get(url)
filename = url.split('/')[-1]
with open(filename, 'wb') as out_file:
    
    out_file.write(r.content)
print("Downloaded")
