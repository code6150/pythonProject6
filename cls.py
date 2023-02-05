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
