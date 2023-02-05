import time

file_name = time.strftime('%y%m%d') + '.txt'

def add_schedule(schedule):
    if not schedule:
        print('뭐지tv?')
        return
    with open(file_name, 'a', encoding='UTF-8') as f:
        f.write(schedule + "\n")
    print('할 일이 추가 되었습니다.')

def read_schedule():
    with open(file_name, 'r', encoding='UTF-8') as f:
        # readlines() 파일안의 내용을 전부 list로 들고옴.

        #for 변수명 in 반복가능객체:
        for s in f.readlines():
            print(s.rstrip('\n'))

        # readline()
        while True:
            line = f.readline()
            if not line:
                break
            print(line.rstrip('\n'))
