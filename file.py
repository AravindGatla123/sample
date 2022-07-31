f = open("sample.txt", 'r')

f1 = open("abc", 'a')
for data in f:
    f1.write(data)

f3 = open("/Users/bhargavreddymudireddy/Downloads/download.png", 'rb')

f4 = open("SMILE.JPG",'wb')
for i in f3:
    f4.write(i)
