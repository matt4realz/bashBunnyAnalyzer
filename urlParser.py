from urllib.parse import urlparse

analysisTxt = open("C:\Users\Matt\Desktop\2202\test.txt", 'r')

for line in analysisTxt:
    obj = urlparse(analysisTxt)
    print (obj.netloc)
    print (obj.path)