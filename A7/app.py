"""
Primary module for Alien Invaders

This module contains the main controller class for the Alien Invaders app.
There is no need for any additional classes in this module.  If you need
more classes, 99% of the time they belong in either the wave module or the
models module. If you are unsure about where a new class should go, post a
question on Piazza.

# River Strumwasser (rns88) and Katherine Son (ks2395)
# 12/10/2023
"""
from consts import *
from game2d import *
from wave import *


# PRIMARY RULE: Invaders can only access attributes in wave.py via getters/setters
# Invaders is NOT allowed to access anything in models.py

class Invaders(GameApp):
    """
    The primary controller class for the Alien Invaders application

    This class extends GameApp and implements the various methods necessary
    for processing the player inputs and starting/running a game.

        Method start begins the application.

        Method update either changes the state or updates the Play object

        Method draw displays the Play object and any other elements on screen

    Because of some of the weird ways that Kivy works, you SHOULD NOT create
    an initializer __init__ for this class.  Any initialization should be done
    in the start method instead.  This is only for this class.  All other
    classes behave normally.

    Most of the work handling the game is actually provided in the class Wave.
    Wave should be modeled after subcontrollers.py from lecture, and will
    have its own update and draw method.

    The primary purpose of this class is to manage the game state: which is
    when the game started, paused, completed, etc. It keeps track of that in
    an internal (hidden) attribute.

    For a complete description of how the states work, see the specification
    for the method update.

    Attribute view: the game view, used in drawing
    Invariant: view is an instance of GView (inherited from GameApp)

    Attribute input: user input, used to control the ship or resume the game
    Invariant: input is an instance of GInput (inherited from GameApp)
    """
    # HIDDEN ATTRIBUTES:
    # Attribute _state: the current state of the game represented as an int
    # Invariant: _state is one of STATE_INACTIVE, STATE_NEWWAVE, STATE_ACTIVE,
    # STATE_PAUSED, STATE_CONTINUE, or STATE_COMPLETE
    #
    # Attribute _wave: the subcontroller for a single wave, managing aliens
    # Invariant: _wave is a Wave object, or None if there is no wave currently
    # active. It is only None if _state is STATE_INACTIVE.
    #
    # Attribute _text: the currently active message
    # Invariant: _text is a GLabel object, or None if there is no message to
    # display. It is onl None if _state is STATE_ACTIVE.
    #
    # You may have new attributes if you wish (you might want an attribute to
    # store any score across multiple waves). But you must document them.
    #
    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY:
    # Attribute _background: the background for the game
    # Invariant: _background is a GRectangle object

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    def getState(self):
        """
        Returns the State of the game
        """
        return self._state


    def getWave(self):
        """
        Returns the active Wave of the game
        """
        return self._wave


    def getText(self):
        """
        Returns the active player message on the screen
        """
        return self._text


    def setState(self, newstate):
        """
        Sets the state of the game.

        Parameter newstate: The new state of the game.
        Precondition: newstate is STATE_INACTIVE, STATE_NEWWAVE,
        STATE_ACTIVE, STATE_PAUSED, STATE_CONTINUE, or STATE_COMPLETE
        """
        assert (newstate == STATE_INACTIVE
        or newstate == STATE_NEWWAVE
        or newstate == STATE_ACTIVE
        or newstate == STATE_PAUSED
        or newstate == STATE_CONTINUE
        or newstate == STATE_COMPLETE)
        self._state = newstate


    def setWave(self, newwave):
        """
        Sets the active wave of the game.

        Parameter newwave: The new wave for the game.
        Precondition: newwave is None or a newwave is a Wave object
        """
        assert isinstance(newwave, Wave) or newwave is None
        self._wave = newwave


    def setText(self, newtext):
        """
        Sets the active player message of the game

        Parameter newtext: The new message for the game.
        Precondition: newtext is None or newtext is a GLabel object
        """
        assert isinstance(newtext, GLabel) or newtext is None
        self._text = newtext


    # DO NOT MAKE A NEW INITIALIZER!

    # THREE MAIN GAMEAPP METHODS

    def start(self):
        """
        Initializes the application.

        This method is distinct from the built-in initializer __init__ (which
        you should not override or change). This method is called once the
        game is running. You should use it to initialize any game specific
        attributes.

        This method should make sure that all of the attributes satisfy the
        given invariants. When done, it sets the _state to STATE_INACTIVE and
        create a message (in attribute _text) saying that the user should press
        to play a game.
        """
        # IMPLEMENT ME
        self._background = GRectangle(x=GAME_WIDTH//2, y=GAME_HEIGHT//2,
        width=GAME_WIDTH, height=GAME_HEIGHT, fillcolor='black')

        self.setState(STATE_INACTIVE)

        if self.getState() == STATE_INACTIVE:
            self.setText(GLabel(x=GAME_WIDTH//2, y=GAME_HEIGHT//2,
            text="Press 'S' to Play", font_name="Arcade.ttf", font_size=64,
            fillcolor='black',linecolor='white'))


    def update(self,dt):
        """
        Animates a single frame in the game.

        It is the method that does most of the work. It is NOT in charge of
        playing the game.  That is the purpose of the class Wave. The primary
        purpose of this game is to determine the current state, and -- if the
        game is active -- pass the input to the Wave object _wave to play the
        game.

        As part of the assignment, you are allowed to add your own states.
        However, at a minimum you must support the following states:
        STATE_INACTIVE, STATE_NEWWAVE, STATE_ACTIVE, STATE_PAUSED,
        STATE_CONTINUE, and STATE_COMPLETE.  Each one of these does its own
        thing and might even needs its own helper.  We describe these below.

        STATE_INACTIVE: This is the state when the application first opens.
        It is a paused state, waiting for the player to start the game.  It
        displays a simple message on the screen. The application remains in
        this state so long as the player never presses a key.  In addition,
        this is the state the application returns to when the game is over
        (all lives are lost or all aliens are dead).

        STATE_NEWWAVE: This is the state creates a new wave and shows it on
        the screen. The application switches to this state if the state was
        STATE_INACTIVE in the previous frame, and the player pressed a key.
        This state only lasts one animation frame before switching to
        STATE_ACTIVE.

        STATE_ACTIVE: This is a session of normal gameplay.  The player can
        move the ship and fire laser bolts.  All of this should be handled
        inside of class Wave (NOT in this class).  Hence the Wave class
        should have an update() method, just like the subcontroller example
        in lecture.

        STATE_PAUSED: Like STATE_INACTIVE, this is a paused state. However,
        the game is still visible on the screen.

        STATE_CONTINUE: This state restores the ship after it was destroyed.
        The application switches to this state if the state was STATE_PAUSED
        in the previous frame, and the player pressed a key. This state only
        lasts one animation frame before switching to STATE_ACTIVE.

        STATE_COMPLETE: The wave is over, and is either won or lost.

        You are allowed to add more states if you wish. Should you do so, you should
        describe them here.

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        # IMPLEMENT ME
        assert isinstance(dt, int) or isinstance(dt, float)

        self.waveSetup()

        if self.getState() == STATE_ACTIVE:

            #MOVE SHIP
            if GInput.is_key_down(self.input, 'left') == True:
                self.getWave().moveShipLeft()
            elif GInput.is_key_down(self.input, 'right') == True:
                self.getWave().moveShipRight()

            self.getWave().update(dt)

            #SHOOT BOLTS
            if (GInput.is_key_pressed(self.input, 'spacebar') == True
                and self.getWave().getShip() is not None):
                self.getWave().shootBolt()

            self.checkOver()

        #COME BACK WHEN SHIP DESTRYOED
        self.comeBack()

        #UPDATE LABELS
        if self.getState() != STATE_INACTIVE:
            self.getWave().updateLabels()


    def draw(self):
        """
        Draws the game objects to the view.

        Every single thing you want to draw in this game is a GObject.  To
        draw a GObject g, simply use the method g.draw(self.view).  It is
        that easy!

        Many of the GObjects (such as the ships, aliens, and bolts) are
        attributes in Wave. In order to draw them, you either need to add
        getters for these attributes or you need to add a draw method to
        class Wave.  We suggest the latter.  See the example subcontroller.py
        from class.
        """
        # IMPLEMENT ME
        self._background.draw(self.view)

        if self.getState() is not STATE_INACTIVE:
            self.getWave().draw(self.view)

        if self.getText() is not None:
            self.getText().draw(self.view)


    # HELPER METHODS FOR THE STATES GO HERE

    def waveSetup(self):
        """
        Generates a new wave upon the game being opened.
        """
        if (self.getState() == STATE_INACTIVE and
            GInput.is_key_pressed(self.input, 's') == True):
            self.setState(STATE_NEWWAVE)
            self.setText(None)
            self.setWave(None)

        if self.getState() == STATE_NEWWAVE:
            wavey = Wave()
            self.setWave(wavey)
            self.setState(STATE_ACTIVE)


    def checkOver(self):
        """
        Checks if the game is over

        - If no lives are left and the game's state is STATE_PAUSED
        - If all of the aliens have been killed
        - If the aliens pass the defense line

        And displays an error message in response. Does nothing otherwise.
        """
        if self.getWave().getShip() == None:
            self.setState(STATE_PAUSED)
            if self.getWave().getLives() == 0:
                self.setState(STATE_COMPLETE)
                self.setText(GLabel(x=GAME_WIDTH//2, y=GAME_HEIGHT//2,
                text="You Lose!", font_name="Arcade.ttf", font_size=64,
                fillcolor='black',linecolor='white'))
            else:
                self.setText(GLabel(x=GAME_WIDTH//2, y=GAME_HEIGHT//2,
                text="Press 'S' to Continue", font_name="Arcade.ttf",
                font_size=64, fillcolor='black',linecolor='white'))

        if self.getWave().isOver():
            self.setState(STATE_COMPLETE)
            self.setText(GLabel(x=GAME_WIDTH//2, y=GAME_HEIGHT//2,
            text="You Win!", font_name="Arcade.ttf", font_size=64,
            fillcolor='black',linecolor='white'))

        if self.getWave().alienPassedLine():
            self.setState(STATE_COMPLETE)
            self.setText(GLabel(x=GAME_WIDTH//2, y=GAME_HEIGHT//2,
            text="You Lose!", font_name="Arcade.ttf", font_size=64,
            fillcolor='black',linecolor='white'))


    def comeBack(self):
        """
        If the ship is killed (and game not over), creates new ship
        when 's' key is pressed, and resumes game.
        """
        if self.getState() == STATE_PAUSED:
            if GInput.is_key_pressed(self.input, 's') == True:
                self.setState(STATE_CONTINUE)

        if self.getState() == STATE_CONTINUE:
                self.getWave().setShip(Ship(x=GAME_WIDTH/2,
                y=(SHIP_BOTTOM + SHIP_HEIGHT/2),
                width=SHIP_WIDTH, height=SHIP_HEIGHT, source='ship.png'))
                self.setText(None)
                self.setState(STATE_ACTIVE)
