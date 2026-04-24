class player:
    count = 0
    def __init__(self,name,level):
        self.name=name
        self.level=level
        player.count+=1
    @classmethod
    def player_count(cls):
        print(f"Total players = {cls.count}")

p1=player("Nishant",5)
p2=player("Rahul",2)
p3=player("Ral",4)
p4=player("hul",3)

player.player_count()