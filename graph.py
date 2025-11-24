# dict1 = {
#     'A':['B','D'],
#     'B':['A','C'],
#     'C':['B','D'],
#     'D':['A','C']
# }
class facebook:
    def __init__(self):
        self.friend = {}
    def add_user(self,user):
        if user not in self.friend:
            self.friend[user] = []
    def add_friend(self,user1,user2):
        self.add_user(user1)
        self.add_user(user2)
        # self.friend[user1].append(user2)
        # self.friend[user2].append(user1)

        if user2 not in self.friend[user1]:
            self.friend[user1].append(user2)
        if user1 not in user2:
            self.friend[user2].append(user1)
        return self.friend
    def friend_suggestion(self,user):
        if user not in self.friend:
            return "No suggestion will have"
        sug=set()
        for i in self.friend.get(user,[]):
            if i in self.friend:
                for j in self.friend.get(i,[]):
                    if i != j:
                        sug.add(j)
        return sug
    def mutual_friend(self,user1,user2):
        mutual = set()
        for i in self.friend.get(user1,[]):
            if i not in self.friend[user2]:
                mutual.add(user1)
        return mutual


obj = facebook()
print(obj.add_friend('A','B'))
print(obj.add_friend('B','C'))
print(obj.add_friend('C','D'))
print(obj.add_friend('D','A'))

print(obj.friend_suggestion('B'))

print(obj.mutual_friend('E','B'))