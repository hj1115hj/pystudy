# 피클 사용을 위해  pickle을 임포트 
import pickle

def pwrite01():
    f = open("./sample/players.bin","wb")
    data = {"baseball": 9}
    pickle.dump(data,f)

    f.close()

pwrite01()


def pread01():
    f = open("./sample/players.bin","rb")  # b 모드
    data = pickle.load(f)
    f.close()
    print(data,type(data))


#pread01()


def pwrite02():
    # 복수의 객체 저장 
    with open("./sample/players.bin","wb") as f:
        pickle.dump({"baseball" : 9},f,1)  # protocol 1
        pickle.dump({"baseball" : 5},f,2) # protocol2
        pickle.dump({"soccer" : 5},f,pickle.HIGHEST_PROTOCOL) # protocol2


pwrite02()

def pread02():
    # 복수의 객체 읽기 
    with open("./sample/players.bin","rb") as f:      
        print(pickle.load(f))  # 프로토콜 버전이 저장되어있어서 로드할때 명시하지 않아도 된다
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f)) #Eof Error  Ran out of input  에러


#pread02()

def pread03():
    #복수의 객체 읽기 
    with open("./sample/players.bin","rb") as f:
        data_list =[]
        while True :
            try:
                data= pickle.load(f)
            except EOFError:
                break

            data_list.append(data)

        print(data_list)


pread03()



