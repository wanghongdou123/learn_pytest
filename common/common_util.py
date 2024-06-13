

class CommonUtil:
    def setup_class(self):
        print('每个类之前执行一次')

    def teardown_class(self):
        print('每个类之后执行一次')

    def setup(self):
        print('每个用例前执行一次')

    def teardown(self):
        print('每个用例后执行一次')