

class Participant:
    def __init__(self, name):
        self.name = name
        self.__points__ = 0
        self.choice = ""

    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name=self.name))
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))

    def toNumber(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissors": 2
        }
        return switcher[self.choice]

    def incrementPoint(self):
        self.__points__ += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("Round resulted in a " + self.getResultString(result) )
        if result > 0:
            p1.incrementPoint
        elif result < 0:
            p2.incrementPoint
        else:
            pass

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumber()][p2.toNumber()]

    def getResultString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

    def awardPoints(self):
        print("implement")




class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)

    def checkEndCondition(self):
        print("implement")

    def determineWinner(self):
        print("implement")


game = Game()
game.start()