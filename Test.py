import traceback


class TestRunner(object):
    def __init__(self, name):
        self.name = name
        self.testNo = 1

    def expectTrue(self, cond):
        try:
            if cond():
                self._pass()
            else:
                self._fail()
        except Exception as e:
            self._fail(e)

    def expectFalse(self, cond):
        self.expectTrue(lambda: not cond())

    def expectException(self, block):
        try:
            block()
            self._fail()
        except:
            self._pass()

    def _fail(self, e=None):
        print(f'FAILED: Test  # {self.testNo} of {self.name}')
        self.testNo += 1
        if e is not None:
            traceback.print_tb(e.__traceback__)

    def _pass(self):
        print(f'PASSED: Test  # {self.testNo} of {self.name}')
        self.testNo += 1


def match(string, pattern):
# ------------------------------------------------------------------------------------------------
# Решение задачи 1
# ------------------------------------------------------------------------------------------------
    if len(string) != len(pattern):
        return False
    i = 0 
    for i in range(len(string)):
        if pattern[i] =='a':
            if string[i].isalpha() == False:
                return False
        else: 
            if pattern[i] =='d':
                if string[i].isdigit() == False:
                    return False
            else:
                if pattern[i] =='*':
                    if string[i].isdigit() == False and string[i].isalpha() == False:
                         return False
                else:
                    if pattern[i] ==' ':
                        if string[i] != ' ': 
                            return False
                    else:
                        raise ValueError("Ошибка шаблона")
        i +=1
        return True
    
      


def testMatch():
    runner = TestRunner('match')

    runner.expectFalse(lambda: match('xy', 'a')) #1
    runner.expectFalse(lambda: match('x', 'd')) #2
    runner.expectFalse(lambda: match('0', 'a')) #3
    runner.expectFalse(lambda: match('*', ' ')) #4
    runner.expectFalse(lambda: match(' ',  'a')) #5

    runner.expectTrue(lambda:  match('01 xy', 'dd aa')) #6
    runner.expectTrue(lambda: match('1x', '**')) #7

    runner.expectException(lambda:  match('x', 'w')) #8

testMatch()
