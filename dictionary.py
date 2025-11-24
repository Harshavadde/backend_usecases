from itertools import permutations


class Dictionary:
    def __init__(self):
        self.db = {
    "apple": [],"banana": [],"orange": [],"grape": [],"mango": [],"table": [],"chair": [],
    "window": [],"bottle": [],"laptop": [],
    "keyboard": [],"mouse": [],"screen": [],"mobile": [],
    "charger": [],"camera": [],"flower": [],"garden": [],"river": [],
    "mountain": [],"rain": [],"cloud": [],"storm": [],"forest": [],"planet": [],
    "animal": [],"bird": [],"fish": [],"ocean": [],"school": [],"college": [],
    }
        for i in self.db:
            perms = permutations(i)
            for j in perms:
                self.db[i].append("".join(j))
        # print(self.db["apple"])
    def suggestion(self,n):
        for i,j in self.db.items():
            if n in j:
                return i
    def display(self):
        return self.db
obj = Dictionary()
print(obj.suggestion("ytrunoc"))
