class stack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
        return self.stack
    def pop(self):
        return self.stack.pop()
    def show_his(self):
        print(self.stack)
class browser_stack(stack):
    def __init__(self):
        super().__init__()
    def push_url(self,url):
        return super().push(url)
    def pop_url(self):
        return super().pop()
    def show_history(self):
        super().show_his()

obj = browser_stack()
obj.push_url("www.google.com")