

#while True:
#    print('=' * 32)
#    print('1. 할 일 추가')
#    print('2. 할 일 확인')
#    print('=' * 32)
#    select = int(input('선택 ㄱㄱ >>> '))
#    if select == 1:
#        schedule.add_schedule(input('뭐 할껀데 >>> '))
#    elif select == 2:
#        schedule.read_schedule()

class student:
    # 클래스의 생성자 -> 클래스가 생성될때 자동으로 실행되는 메소드
    #               -> 클래스의 생성 조건을 만들어 줄 수 있다.
    def __init__(self, num, name, address, phone, grade):
        #self -> 객체 자기 자신을 가르키는 변수
        #     -> 객체 안에서 만드는 모든 매서드에 self는 첫번째 매개변수로 등장
        self.num = num
        self.name = name
        self.address = address
        self.phone = phone
        self.grade = grade

    # 메소드는 동사로 시작
    def print_info(self):
        print(f'[{self.name}]')
        print(f'학번 : {self.num}')
        print(f'주소 : {self.address}')
        print(f'번호 : {self.phone}')
        print(f'학점 : {self.grade}')

li = []

with open('info.csv', 'r') as f:
    f.readline()
    for i in f.readlines():
        sub = i.rstrip('\n').split(',')
        st = student(int(sub[0]), sub[1], sub[2], sub[3], float(sub[4]))
        li.append(st)

li[0].print_info()
