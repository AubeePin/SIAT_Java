fp = open("io_test.txt","r",encoding="utf-8")
while True:
    data=fp.readline()#파일을 한줄씩 읽엇다.
    data=data[0:len(data)-1]
    if not data:
        break
    print(data)
fp.close()