
#___________________________________________________________________________________________________ 상속
class Unit:
    def __init__(self, name, hp): 
        self.name =name
        self.hp = hp 
        
class Attackunit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
    def attack(self, location):
        print("{} | {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다. ".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))
firebat1 = Attackunit("파이어뱃", 50 ,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)