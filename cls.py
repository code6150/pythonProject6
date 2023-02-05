class Calculator:

    def __init__(self):
        self.expr = None

    def input_expr(self):
        self.expr = input('수식을 입력하세요 >>> ')

    def calculate(self):
        if not self.expr:
            print('input_expr 메소드를 먼저 실행하세요.')
            return
        return eval(self.expr)

c = Calculator()
c.input_expr()
print(c.calculate())

#다음 지시사항을 읽고 책의 제목과 저자 정보를 저장할 수 있는 Book 클래스를 생성하세요
# 1. 책 제목과 책 저자 정보를 출력하는 print_info() 메소드를 구현하세요.
# 2. 다음과 같은 방법으로 book1 과 book2 인스턴스(생성된 객체) 를 생성하세요.

#book1 = Book()
#book2 = Book()
#book1.set_info('파이썬', '민경태')
#book2.set_info('어린왕자', '생텍쥐페리')
# 3. 생성된 인스턴스 book1과 book2를 리스트 book_list 에 저장하세요.

#출력
#책 제목: 파이썬
#책 저자: 민경태
#책 제목: 어린왕자
#책 저자: 생텍쥐페리

class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author
    def print_info(self):
        print(f'책 제목 : {self.title}')
        print(f'책 저자 : {self.author}')

book1 = Book()
book2 = Book()
book1.set_info('파이썬', '민경태')
book2.set_info('어린왕자', '생텍쥐페리')

book_list = [book1, book2]

for book in book_list:
    book.print_info()
