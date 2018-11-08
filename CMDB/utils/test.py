class BaseForm(object):
    res = {}
    def __init__(self, data, num):
        self.data = data
        self.num = num
        self.error_mes = {}

    def clean_num(self):
        if len(self.data.key()) != self.num:
            self.error_mes["mes"]["num"] = "参数个数不够"
            return self.error_mes #{'mes':{'num': '参数个数不够'}}
        else:
            return True

    def clean(self):
        self.res = self.clean_num()
        return self.res

    def get_A_X_methods(self):
        a = dir(self)
        #a = filter(lambda x: x.startswith('clean') and callable(getattr(self, x)), dir(self))
        return a
a = BaseForm({"name":1}, 1)
print(a.get_A_X_methods())



