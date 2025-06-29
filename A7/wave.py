"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in
the Alien Invaders game.  Instances of Wave represent a single wave. Whenever
you move to a new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on
screen. These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or
models.py. Whether a helper method belongs in this module or models.py is
often a complicated issue.  If you do not know, ask on Piazza and we will
answer.

# River Strumwasser (rns88) and Katherine Son (ks2395)
# 12/10/2023
"""
from game2d import *
from consts import *
from models import *
import random

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.

    This subcontroller has a reference to the ship, aliens, and any laser bolts
    on screen. It animates the laser bolts, removing any aliens as necessary.
    It also marches the aliens back and forth across the screen until they are
    all destroyed or they reach the defense line (at which point the player
    loses). When the wave is complete, you  should create a NEW instance of
    Wave (in Invaders) if you want to make a new wave of aliens.

    If you want to pause the game, tell this controller to draw, but do not
    update.  See subcontrollers.py from Lecture 24 for an example.  This
    class will be similar to than one in how it interacts with the main class
    Invaders.

    All of the attributes of this class ar to be hidden. You may find that
    you want to access an attribute in class Invaders. It is okay if you do,
    but you MAY NOT ACCESS THE ATTRIBUTES DIRECTLY. You must use a getter
    and/or setter for any attribute that you need to access in Invaders.
    Only add the getters and setters that you need for Invaders. You can keep
    everything else hidden.

    """
    # HIDDEN ATTRIBUTES:
    # Attribute _ship: the player ship to control
    # Invariant: _ship is a Ship object or None
    #
    # Attribute _aliens: the 2d list of aliens in the wave
    # Invariant: _aliens is a rectangular 2d list containing Alien objects or None
    #
    # Attribute _bolts: the laser bolts currently on screen
    # Invariant: _bolts is a list of Bolt objects, possibly empty
    #
    # Attribute _dLine: the defensive line being protected
    # Invariant : _dLine is a GPath object
    #
    # Attribute _lives: the number of lives left
    # Invariant: _lives is an int >= 0
    #
    # Attribute _time: the amount of time since the last Alien "step"
    # Invariant: _time is a float >= 0s
    #
    # You may change any attribute above, as long as you update the invariant
    # You may also add any new attributes as long as you document them.

    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY

    # Attribute _direct: the direction the aliens are walking in
    # Invariant: _direct is a string == 'L', 'R', 'LD', or 'RD'

    # Attribute _stepsTilShoot: the number of steps until next alien bolt
    # Invariant: _stepsTilShoot is an int 0 <= _stepsTilShoot <= BOLT_RATE

    # Attribute _score
    # Invariant: _score is an int >= 0

    # Attrbute _livesLabel1
    # Invariant: _livesLabel1 is a GLabel object

    # Attribute _livesLabel2
    # Invariant: _livesLabel1  is a GLabel object

    # Attribute _scoreLabel1
    # Invariant: _scoreLabel1  is a GLabel object

    # Attribute _scoreLabel2
    # Invariant: _scoreLabel2  is a GLabel object

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    def getShip(self):
        """
        Returns the current ship
        """
        return self._ship

    def getAlien(self, r, c):
        """
        Returns the alien at (r,c) in _aliens

        Parameter r: the new row for the alien
        Precondition r is an int such that -ALIEN_ROWS <= r < ALIEN_ROWS

        Parameter c: the new column for the alien
        Precondition: c is an int such that -ALIENS_IN_ROW <= r < ALIENS_IN_ROW
        """
        assert -ALIEN_ROWS <= r and r < ALIEN_ROWS
        assert isinstance(r, int)
        assert -ALIENS_IN_ROW <= c and c < ALIENS_IN_ROW
        assert isinstance(c,int)

        return self._aliens[r][c]

    def getAliens(self):
        """
        Returns the list of aliens
        """
        return self._aliens

    def getBolts(self):
        """
        Returns the list of bolts currently active
        """
        return self._bolts

    def getLives(self):
        """
        Returns the number of player lives
        """
        return self._lives

    def getTime(self):
        """
        Returns the current time since an alien movement for the wave
        """
        return self._time

    def getDirect(self):
        """
        Returns the direction the aliens are walking in
        """
        return self._direct

    def getStepTilShoot(self):
        """
        Returns the number of alien walk steps until an alien shoots a bolt
        """
        return self._stepsTilShoot

    def getScore(self):
        """
        Returns the current score of the game
        """
        return self._score

    def getLivesLabel2(self):
        """
        Returns the 2nd lives label
        """
        return self._livesLabel2

    def getScoreLabel2(self):
        """
        Returns the 2nd score label
        """
        return self._scoreLabel2

    def setShip(self, newship):
        """
        Sets the new ship for the wave

        Parameter newship: The new ship for the wave
        Precondition: newship is None or a Ship object
        """
        assert isinstance(newship, Ship) or newship is None

        self._ship = newship

    def setAlien(self, r, c, newalien):
        """
        Sets the new alien at (r,c) in _aliens.

        Parameter r: the new row for the alien
        Precondition r is an int such that -ALIEN_ROWS <= r < ALIEN_ROWS

        Parameter c: the new column for the alien
        Precondition: c is an int such that -ALIENS_IN_ROW <= r < ALIENS_IN_ROW

        Parameter newalien: The new alien object
        Precondition: newalien is None or an Alien object
        """
        assert -ALIEN_ROWS <= r and r < ALIEN_ROWS
        assert isinstance(r, int)
        assert -ALIENS_IN_ROW <= c and c < ALIENS_IN_ROW
        assert isinstance(c,int)
        assert isinstance(newalien, Alien) or newalien is None

        self._aliens[r][c] = newalien

    def setAliens(self, alienlist):
        """
        Sets the new list of aliens

        Parameter alienlist: The new list of aliens.
        Precondition: alienlist is a list of list[s] of alien[s]
        """
        assert isinstance(alienlist, list)
        for eachrowwe in alienlist:
            assert isinstance(eachrowwe, list)
            for eachalienne in eachrowwe:
                assert isinstance(eachalienne, Alien) or eachalienne is None

        self._aliens = alienlist

    def setLives(self, newlives):
        """
        Sets the new number of lives of the ship

        Parameter newlives: The new number of lives of the ship
        Precondition: newlives is an int >= 0
        """
        assert isinstance(newlives, int) and newlives >= 0

        self._lives = newlives

    def setTime(self, newtime):
        """
        Sets the time since an alien movement of the wave.

        Parameter newtime: The new time of the wave
        Precondition: newtime is a float >= 0
        """
        assert isinstance(newtime, float) and newtime >= 0
        self._time = newtime

    def setDirect(self, newdirect):
        """
        Sets the walking direction of the aliens

        Parameter newdirect: The new direction of the aliens.
        Precondition: newdirect is string 'R', 'RD', 'L', or 'LD'
        """
        assert (newdirect == 'R'
        or newdirect =='RD'
        or newdirect == 'L'
        or newdirect == 'LD')

        self._direct = newdirect

    def setStepTilShoot(self, newstepsse):
        """
        Sets the wave's number of alien walk steps until they fire a shot.

        Parameter newstepsse: The new number of steps
        Precondition: newstepsse is an int so that 0 <= newsteppse <= BOLT_RATE
        """
        assert 0 <= newstepsse and newstepsse <= BOLT_RATE
        assert isinstance(newstepsse, int)

        self._stepsTilShoot = newstepsse

    def setScore(self, newscore):
        """
        Sets the wave's score.

        Parameter newscore: The new score for the wave
        Precondition: newscore is an int and >= 0
        """
        assert isinstance(newscore, int) and newscore >= 0

        self._score = newscore

    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self):
        """
        Initalizes the wave.
        """
        self.setShip(Ship(x=GAME_WIDTH/2, y=(SHIP_BOTTOM + SHIP_HEIGHT/2),
        width=SHIP_WIDTH, height=SHIP_HEIGHT, source='ship.png'))

        self.initializeAliens()

        self._bolts = []

        self._dLine = GPath(points=[0,DEFENSE_LINE,GAME_WIDTH,DEFENSE_LINE],
        linewidth=2, linecolor='gray')
        self.setLives(3)
        self.setTime(0.0)
        self.setDirect('R')
        self.setStepTilShoot(random.randint(1, BOLT_RATE))
        self.setScore(0)
        self.initializeLabels()

    def initializeAliens(self):
        """
        Initalizes the list of aliens for the wave.
        """
        alien_list = []

        for yvr in range(ALIEN_ROWS):
            alien_single_row = []
            for xvr in range(ALIENS_IN_ROW):
                if yvr % 6 == 0 or yvr % 6 == 1:
                    alien_single_row.append(Alien(x=(ALIEN_H_SEP+ALIEN_WIDTH//2+
                    ((ALIEN_H_SEP+ALIEN_WIDTH)*xvr)),
                    y=(GAME_HEIGHT-ALIEN_CEILING-ALIEN_HEIGHT//2-
                    (ALIEN_V_SEP+ALIEN_HEIGHT)*(ALIEN_ROWS-yvr-1)),
                    width=ALIEN_WIDTH, height=ALIEN_HEIGHT, source='alien1.png'))
                elif yvr % 6 == 2 or yvr % 6 == 3:
                    alien_single_row.append(Alien(x=(ALIEN_H_SEP+ALIEN_WIDTH//2+
                    ((ALIEN_H_SEP+ALIEN_WIDTH)*xvr)),
                    y=(GAME_HEIGHT-ALIEN_CEILING-ALIEN_HEIGHT//2-
                    (ALIEN_V_SEP+ALIEN_HEIGHT)*(ALIEN_ROWS-yvr-1)),
                    width=ALIEN_WIDTH, height=ALIEN_HEIGHT, source='alien2.png'))
                elif yvr % 6 == 4 or yvr % 6 == 5:
                    alien_single_row.append(Alien(x=(ALIEN_H_SEP+ALIEN_WIDTH//2+
                    ((ALIEN_H_SEP+ALIEN_WIDTH)*xvr)),
                    y=(GAME_HEIGHT-ALIEN_CEILING-ALIEN_HEIGHT//2-
                    (ALIEN_V_SEP+ALIEN_HEIGHT)*(ALIEN_ROWS-yvr-1)),
                    width=ALIEN_WIDTH, height=ALIEN_HEIGHT, source='alien3.png'))
            alien_list.append(alien_single_row)

        self.setAliens(alien_list)

    def initializeLabels(self):
        """
        Initalizes the lives and score labels.
        """
        self._livesLabel1 = GLabel(x=GAME_WIDTH-130, y=GAME_HEIGHT-50,
        text="Lives:", font_name="Arcade.ttf", font_size=50,
        fillcolor='black',linecolor='yellow')

        self._livesLabel2 = GLabel(x=GAME_WIDTH-40, y=GAME_HEIGHT-50,
        text=str(self.getLives()), font_name="Arcade.ttf", font_size=50,
        fillcolor='black',linecolor='white')

        self._scoreLabel1 = GLabel(x=100, y=GAME_HEIGHT-50,
        text="Score:", font_name="Arcade.ttf", font_size=50,
        fillcolor='black',linecolor='yellow')

        self._scoreLabel2 = GLabel(x=195, y=GAME_HEIGHT-50,
        text=str(self.getScore()), font_name="Arcade.ttf", font_size=50,
        fillcolor='black',linecolor='white')

    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    # Ship movement in app.py, not here

    def update(self, dt):
        """
        Updates the frame for the wave.

        Moves the ship, aliens, and laser bolts. Generates alien bolts,
        as well as checks for collisions between players, aliens, and bolts.

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        assert isinstance(dt, int) or isinstance(dt, float)

        self.setTime(self.getTime()+dt)

        alien_speed_dynam = ALIEN_SPEED * .99 ** self.numberOfAliensKilled()

        if self.getTime() >= alien_speed_dynam:
            self.walk()
            self.setStepTilShoot(self.getStepTilShoot() - 1)
            self.setTime(0.0)

        self.boltMove()
        self.clearBolts()

        if self.getStepTilShoot() == 0:
            randombottomalien = self.randombottomalien()
            self.getBolts().append(Bolt(-BOLT_SPEED, x=randombottomalien.getx(),
            y=randombottomalien.gety(), width=4, height=16, fillcolor='white'))
            self.setStepTilShoot(random.randint(1, BOLT_RATE))

        self.checkCollisions()

    def updateLabels(self):
        """
        Updates the lives and score labels of the wave.
        """
        self._livesLabel2.text = str(self.getLives())
        self._scoreLabel2.text = str(self.getScore())
        self._scoreLabel2.x = 195-12*int(1-len(str(self.getScore())))

    def moveShipLeft(self):
        """
        Decreases the ship's x coordinate by SHIP_MOVEMENT
        """
        if self.getShip().getx() > SHIP_WIDTH//2:
            self.getShip().setx(self.getShip().getx() - SHIP_MOVEMENT)

    def moveShipRight(self):
        """
        Increases the ship's x coordinate by SHIP_MOVEMENT
        """
        if self.getShip().getx() < GAME_WIDTH-SHIP_WIDTH//2:
            self.getShip().setx(self.getShip().getx() + SHIP_MOVEMENT)

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS

    def draw(self, viewey):
        """
        Draws the objects in view for the game.

        Parameter viewey: the game view, used in drawing
        Precondition: viewey is an instance of GView (inherited from GameApp)
        """
        assert isinstance(viewey, GView)

        self._dLine.draw(viewey)

        for row in self.getAliens():
            for alien in row:
                if alien is not None:
                    alien.draw(viewey)

        if self.getShip() is not None:
            self.getShip().draw(viewey)

        for eachbolt in self.getBolts():
            eachbolt.draw(viewey)

        self._livesLabel1.draw(viewey)
        self._livesLabel2.draw(viewey)
        self._scoreLabel1.draw(viewey)
        self._scoreLabel2.draw(viewey)

    # HELPER METHODS FOR COLLISION DETECTION

    def checkCollisions(self):
        """
        Checks if any player bolts hit aliens, or if any alien bolts
        hit player bolts. If so, both objects are removed.
        """
        for arow in range(len(self.getAliens())):
            for acol in range(len(self.getAliens()[0])):
                bolti = 0
                while bolti < len(self.getBolts()):
                    if self.getAlien(arow, acol) is not None:
                        if (self.getAlien(arow,acol).
                            collides(self.getBolts()[bolti])):
                            del self.getBolts()[bolti]
                            self.addScore(self.getAlien(arow, acol))
                            self.setAlien(arow, acol, None)
                        else:
                            bolti = bolti + 1
                    else:
                        bolti = bolti + 1

        bolti = 0
        while bolti < len(self.getBolts()):
            if self.getShip() is not None:
                if self.getShip().collides(self.getBolts()[bolti]):
                    del self.getBolts()[bolti]
                    self.setShip(None)
                    self.setLives(self.getLives() - 1)
                else:
                    bolti = bolti + 1
            else:
                bolti = bolti + 1

    # ADDITIONAL HELPER METHODS

    def walk(self):
        """
        Moves the aliens.

        Direction:
        L is for aliens moving to the left
        R is for moving to the right
        RD is for moving down after moving right (left next)
        LD is for moving down after moving left (right next)
        R --> RD --> L --> LD --> R...
        """
        self.walkh()
        self.walkv()

    def walkh(self):
        """
        Moves the alien across the screen.

        Generally, walk horizontally. If the aliens hit the bounds of
        their movement, they move down and switch directions.
        """
        if self.getDirect() == 'R':
            if (self.rightMostAlien().getx() + ALIEN_H_WALK
                < GAME_WIDTH - ALIEN_WIDTH//2 - ALIEN_H_SEP):
                for row in self.getAliens():
                    for alien in row:
                        if alien is not None:
                            alien.setx(alien.getx() + ALIEN_H_WALK)
            else:
                self.setDirect('RD')

        if self.getDirect() == 'L':
            if (self.leftMostAlien().getx() - ALIEN_H_WALK
                > ALIEN_WIDTH//2 + ALIEN_H_SEP):
                for row in self.getAliens():
                    for alien in row:
                        if alien is not None:
                            alien.setx(alien.getx() - ALIEN_H_WALK)
            else:
                self.setDirect('LD')

    def walkv(self):
        """
        Moves the alien down, and sets the course of the aliens to the
        appropriate horizontal direction.
        """
        if self.getDirect() == 'RD':
            for row in self.getAliens():
                for alien in row:
                    if alien is not None:
                        alien.sety(alien.gety() - ALIEN_V_WALK)
            self.setDirect('L')

        if self.getDirect() == 'LD':
            for row in self.getAliens():
                for alien in row:
                    if alien is not None:
                        alien.sety(alien.gety() - ALIEN_V_WALK)
            self.setDirect('R')

    def boltMove(self):
        """
        Moves each bolt, by adding the bolt's velocity to its y position
        """
        for eachbolty in self.getBolts():
            eachbolty.sety(eachbolty.gety() + eachbolty.getVelocity())

    def clearBolts(self):
        """
        Removes bolts out of the bounds of the game.
        """
        acc = 0
        while acc < len(self.getBolts()):
            if (self.getBolts()[acc].gety()+self.getBolts()[acc].getHeight()/2 < 0
                or (self.getBolts()[acc].gety()
                -self.getBolts()[acc].getHeight()/2 > GAME_HEIGHT)):
                del self.getBolts()[acc]
            else:
                acc = acc + 1

    def noOtherBolts(self):
        """
        Returns True if no player bolts are currently active.
        """
        for eachboltie in self.getBolts():
            if eachboltie.getVelocity() == BOLT_SPEED:
                return False
        return True

    def leftMostAlien(self):
        """
        Returns an alien from the leftmost column where at least one
        position of the list of aliens is not None
        """
        for aliencolumn in range(len(self.getAliens()[0])):
            for alienrow in range(len(self.getAliens())):
                if self.getAlien(alienrow,aliencolumn) is not None:
                    return self.getAlien(alienrow,aliencolumn)

    def rightMostAlien(self):
        """
        Returns an alien from the rightmost column where at least one
        position of the list of aliens is not None
        """
        for aliencolumn in range(len(self.getAliens()[0])):
            for alienrow in range(len(self.getAliens())):
                if self.getAlien(-(1+alienrow),-(1+aliencolumn)) is not None:
                    return self.getAlien(-(1+alienrow),-(1+aliencolumn))

    def randombottomalien(self):
        """
        Returns a random alien out of the current active aliens in the lowest
        position with an alien in their row.
        """
        listofbottomaliens = []

        for eachcol in range(len(self.getAliens()[0])):
            bottomalien = None
            for eachrow in range(len(self.getAliens())):
                if (self.getAlien(eachrow,eachcol) is not None
                    and bottomalien is None):
                    bottomalien = self.getAlien(eachrow,eachcol)

            if bottomalien is not None:
                listofbottomaliens.append(bottomalien)

        randalienindex = random.randint(0,len(listofbottomaliens)-1)

        return listofbottomaliens[randalienindex]

    def isOver(self):
        """
        Returns True if the Wave's alien list is empty (every position is None)
        """
        for row in self.getAliens():
            for alien in row:
                if alien is not None:
                    return False
        return True

    def alienPassedLine(self):
        """
        Returns True if any Alien has passed the defense line.
        """
        for row in self.getAliens():
            for alien in row:
                if alien is not None:
                    if alien.gety()-ALIEN_HEIGHT//2 < DEFENSE_LINE:
                        return True
        return False

    def addScore(self, alienne):
        """
        Adds the proper score for shooting an alien:
        10 points for alien with source alien1.png
        20 points for alien with source alien2.png
        40 points for alien with source alien3.png

        Parameter alienne: The alien being shot down
        Precondition: alienne is an Alien object
        """
        assert isinstance(alienne, Alien)

        if alienne.getSource() == 'alien1.png':
            self.setScore(self.getScore() + 10)
        elif alienne.getSource() == 'alien2.png':
            self.setScore(self.getScore() + 20)
        elif alienne.getSource() == 'alien3.png':
            self.setScore(self.getScore() + 40)

    def shootBolt(self):
        """
        Shoots a bolt from te player ship's position, if no other Bolt objects
        shot by the player are currently existing.
        """
        if self.noOtherBolts() == True:
            self.getBolts().append(Bolt(BOLT_SPEED, x=self.getShip().getx(),
            y=self.getShip().gety(), width=4, height=16, fillcolor='white'))

    def numberOfAliensKilled(self):
        """
        Returns the number of aliens that are None in _aliens
        """
        nummy = 0
        for row in self.getAliens():
            for alien in row:
                if alien is None:
                    nummy = nummy + 1
        return nummy
