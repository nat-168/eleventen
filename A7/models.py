"""
Models module for Alien Invaders

This module contains the model classes for the Alien Invaders game. Anything
that you interact with on the screen is model: the ship, the laser bolts, and
the aliens.

Just because something is a model does not mean there has to be a special
class for it. Unless you need something special for your extra gameplay
features, Ship and Aliens could just be an instance of GImage that you move
across the screen. You only need a new class when you add extra features to
an object. So technically Bolt, which has a velocity, is really the only model
that needs to have its own class.

With that said, we have included the subclasses for Ship and Aliens. That is
because there are a lot of constants in consts.py for initializing the
objects, and you might want to add a custom initializer.  With that said,
feel free to keep the pass underneath the class definitions if you do not want
to do that.

You are free to add even more models to this module.  You may wish to do this
when you add new features to your game, such as power-ups.  If you are unsure
about whether to make a new class or not, please ask on Piazza.

# River Strumwasser (rns88) and Katherine Son (ks2395)
# 12/10/2023
"""
from consts import *
from game2d import *

# PRIMARY RULE: Models are not allowed to access anything in any module other
# than consts.py.  If you need extra information from Gameplay, then it should
# be a parameter in your method, and Wave should pass it as a argument when it
# calls the method.


class Ship(GImage):
    """
    A class to represent the game ship.

    At the very least, you want a __init__ method to initialize the ships
    dimensions. These dimensions are all specified in consts.py.

    You should probably add a method for moving the ship.  While moving a
    ship just means changing the x attribute (which you can do directly),
    you want to prevent the player from moving the ship offscreen.  This
    is an ideal thing to do in a method.

    You also MIGHT want to add code to detect a collision with a bolt. We
    do not require this.  You could put this method in Wave if you wanted to.
    But the advantage of putting it here is that Ships and Aliens collide
    with different bolts.  Ships collide with Alien bolts, not Ship bolts.
    And Aliens collide with Ship bolts, not Alien bolts. An easy way to
    keep this straight is for this class to have its own collision method.

    However, there is no need for any more attributes other than those
    inherited by GImage. You would only add attributes if you needed them
    for extra gameplay features (like animation).
    """
    #  IF YOU ADD ATTRIBUTES, LIST THEM BELOW

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    def getx(self):
        """
        Returns the x coordinate of the center of the Ship object.
        """
        return self.x

    def gety(self):
        """
        Returns the y coordinate of the center of the Ship object.
        """
        return self.y

    def getWidth(self):
        """
        Returns the width of the Ship object's image.
        """
        return self.width

    def getHeight(self):
        """
        Returns the height of the Ship object's image.
        """
        return self.height

    def getSource(self):
        """
        Returns the source of the image file for the Ship.
        """
        return self.source

    def setx(self, newx):
        """
        Sets the ship's x coordinate

        Parameter newx: The new x coordinate
        Precondition: x is an int or a float
        """
        assert isinstance(newx, float) or isinstance(newx, int)
        self.x = newx

    def sety(self, newy):
        """
        Sets the ship's y coordinate.

        Parameter newy: The new y coordinate
        Precondition: y is an int or a float
        """
        assert isinstance(newy, float) or isinstance(newy, int)
        self.y = newy

    # INITIALIZER TO CREATE A NEW SHIP

    def __init__(self, **keywords):
        """
        Initializes a new ship

        Inherits GImage's attributes.
        """
        super().__init__(**keywords)

        assert self.getx() is not None
        assert self.gety() is not None
        assert self.getWidth() is not None
        assert self.getHeight() is not None
        assert self.getSource() is not None

    # METHODS TO MOVE THE SHIP AND CHECK FOR COLLISIONS

    def collides(self,bolt):
        """
        Returns True if there is an alien-fired bolt
        within the bounds of the ship's image.
        """
        return (self.contains((bolt.getx(), bolt.gety()))
                and bolt.getVelocity() == -BOLT_SPEED)

    # COROUTINE METHOD TO ANIMATE THE SHIP

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Alien(GImage):
    """
    A class to represent a single alien.

    At the very least, you want a __init__ method to initialize the alien
    dimensions. These dimensions are all specified in consts.py.

    You also MIGHT want to add code to detect a collision with a bolt. We
    do not require this.  You could put this method in Wave if you wanted to.
    But the advantage of putting it here is that Ships and Aliens collide
    with different bolts.  Ships collide with Alien bolts, not Ship bolts.
    And Aliens collide with Ship bolts, not Alien bolts. An easy way to
    keep this straight is for this class to have its own collision method.

    However, there is no need for any more attributes other than those
    inherited by GImage. You would only add attributes if you needed them
    for extra gameplay features (like giving each alien a score value).
    """
    #  IF YOU ADD ATTRIBUTES, LIST THEM BELOW

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    def getx(self):
        """
        Returns the x coordinate of the center of the Alien object.
        """
        return self.x

    def gety(self):
        """
        Returns the y coordinate of the center of the Alien object.
        """
        return self.y

    def getWidth(self):
        """
        Returns the width of the Alien object's image.
        """
        return self.width

    def getHeight(self):
        """
        Returns the height of the Alien object's image.
        """
        return self.height

    def getSource(self):
        """
        Returns the source of the image file for the Alien.
        """
        return self.source

    def setx(self, newx):
        """
        Sets the alien's x coordinate

        Parameter newx: The new x coordinate
        Precondition: x is an int or a float
        """
        assert isinstance(newx, float) or isinstance(newx, int)
        self.x = newx

    def sety(self, newy):
        """
        Sets the alien's y coordinate.

        Parameter newx: The new y coordinate
        Precondition: y is an int or a float
        """
        assert isinstance(newy, float) or isinstance(newy, int)
        self.y = newy

    # INITIALIZER TO CREATE AN ALIEN

    def __init__(self, **keywords):
        """
        Initializes a new alien

        Inherits GImage's attributes.
        """
        super().__init__(**keywords)

        assert self.getx() is not None
        assert self.gety() is not None
        assert self.getWidth() is not None
        assert self.getHeight() is not None
        assert self.getSource() is not None

    # METHOD TO CHECK FOR COLLISION (IF DESIRED)

    def collides(self,bolt):
        """
        Returns True if there is a player-fired bolt
        within the bounds of the ship's image.
        """
        return (self.contains((bolt.getx(), bolt.gety()))
        and bolt.getVelocity() == BOLT_SPEED)

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Bolt(GRectangle):
    """
    A class representing a laser bolt.

    Laser bolts are often just thin, white rectangles. The size of the bolt
    is determined by constants in consts.py. We MUST subclass GRectangle,
    because we need to add an extra (hidden) attribute for the velocity of
    the bolt.

    The class Wave will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with
    no setters for the velocities.  That is because the velocity is fixed and
    cannot change once the bolt is fired.

    In addition to the getters, you need to write the __init__ method to set
    the starting velocity. This __init__ method will need to call the __init__
    from GRectangle as a  helper.

    You also MIGHT want to create a method to move the bolt.  You move the
    bolt by adding the velocity to the y-position.  However, the getter
    allows Wave to do this on its own, so this method is not required.
    """
    # INSTANCE ATTRIBUTES:
    # Attribute _velocity: the velocity in y direction
    # Invariant: _velocity is an int or float

    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getVelocity(self):
        """
        Returns the velocity of the Bolt object.
        """
        return self._velocity

    def getx(self):
        """
        Returns the x coordinate of the center of the Bolt object.
        """
        return self.x

    def gety(self):
        """
        Returns the y coordinate of the center of the Bolt object.
        """
        return self.y

    def getWidth(self):
        """
        Returns the width of the Bolt rectangle.
        """
        return self.width

    def getHeight(self):
        """
        Returns the height of the Bolt rectangle.
        """
        return self.height

    def setVelocity(self, newvelocity):
        """
        Sets the bolt's velocity

        Parameter newvelocity: The new velocity for the bolt
        Precondition: newvelocity is an int or a float
        """
        assert isinstance(newvelocity, float) or isinstance(newvelocity, int)
        self._velocity = newvelocity

    def sety(self, newy):
        """
        Sets the alien's y coordinate.

        Parameter newx: The new y coordinate
        Precondition: y is an int or a float
        """
        assert isinstance(newy, float) or isinstance(newy, int)
        self.y = newy

    # INITIALIZER TO SET THE VELOCITY

    def __init__(self, velocity, **keywords):
        """
        Initializes a new bolt.

        Inherits GRectangle's attributes.

        Parameter velocity: The bolt's velocity – BOLT_SPEED for Ships,
        -BOLT_SPEED for Aliens
        Precondition: velocity is an int or float
        """
        super().__init__(**keywords)

        assert self.getx() is not None
        assert self.gety() is not None
        assert self.getWidth() is not None
        assert self.getHeight() is not None

        self.setVelocity(velocity)


    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE
