from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map 

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            # be sure to print out the last scene
            current_scene.enter

class Home(Scene):

    scenarios = [
           "Starting out, leaving front door with fishing pole",
            "Starting out, forget to bring fishing pole...",
            "Stay home, don't go fishing."
    ]

    def enter(self):
        print(Home.scenarios[randint(0, len(self.scenarios)-1)])
        exit(1)

class Forest(Scene):

    def enter(self):
        print(dedent("""
             You're walking through the forest. 
             You're carrying your fishing pole. 
             It's a beautiful day.
             """))
        
        action = input("> ")

        if action == "turn around and go back home":
            print(dedent("""
                you get lazy. you turn around and go back home
                """))
            return 'home'

        elif action == "keep walking":
            print(dedent("""
                you keep walking towards the river. You're almost there. 
                """))
            return 'forest'

        elif action == "take a break":
            print(dedent("""
                it's hot outside. you stop at a tree stump and take a break.
                """))
            return 'forest'

        else:
            print("You make it to the river")
            return 'river'

class River(Scene):

    def enter(self):
        print(dedent("""
            you make it to the river. it's beautiful. the sound of the water
            rushing past the rocks. You start catching fish
            """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("Buzzz")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                you guessed the correct code to unlock the fishery
                """))
            return 'forest'
        else: 
            print(dedent("""
                you didn't guess the code and fall asleep
                """))
            return 'river'

class Map(object):

    scenes = {
        'home': Home(),
        'forest': Forest(),
        'river': River(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('home')
a_game = Engine(a_map)
a_game.play()


