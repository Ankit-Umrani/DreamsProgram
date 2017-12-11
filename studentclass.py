__author__ = 'ankit'


# class Best_Club():
# website = "https://www.fcbarcelona.com/"

# def __init__(self,name,founded,arena):
#   self.name = name
#  self.founded = founded
# self.arena = arena

# club = Best_Club("FC Barcelona","1899","Camp Nou")

# print(club.name)
# print(Best_Club.website)

class Fighter():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10
        self.recovery = 10

    def attack(self, enemy):
        enemy.health -= self.damage
        print("{} is puching you!".format(self.name))


    def powermove(self, enemy):
        enemy.health = enemy.health - 20
        print("{} made a powermove on you".format(self.name))

    def defense(self,enemy):
        self.health = self.health
        print("{} defended attack from {}".format(self.name,enemy.name))

    def restore_health(self):
        self.health += self.recovery
        print("{} recovered health by 10 percent, 12 coins debited".format(self.name))

    def __str__(self):
        return ("{}:{}%".format(self.name, self.health))


player1 = Fighter("Ankit")
player2 = Fighter("Dmon")



print(player1)
print(player2)

#Ankit is Attacking Dmon
player1.attack(player2)
print(player2)

#Dmon defending Ankit's attack, restores health by 5 percent
player2.defense(player1)
print(player1)
print(player2)

#player2 attacks player 1
player2.attack(player1)
print(player1)

#player2 powermoves player1
player2.powermove(player1)
print(player1)

#restoring health
player1.defense(player2)
player1.defense(player2)
print(player1)

player1.powermove(player2)
print(player2)

player2.restore_health()
print(player2)

player1.defense(player2)
print(player1)
print(player2)


