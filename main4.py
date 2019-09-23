#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.blue_4)

        self.animal_list = arcade.SpriteList()


    def setup(self):
        animals = ['bear','buffalo','chick','chicken','cow','crocodile','dog','duck','elephant','frog','giraffe','goat','gorilla','hippo','horse','monkey','moose','narwhal','owl','panda','parrot','penguin','pig','rabbit','rhino','sloth','snake','walrus','whale','zebra']
        trees = ['foliagePack_005', 'foliagePack_006', 'foliagePack_007', 'foliagePack_008', 'foliagePack_009', 'foliagePack_010','foliagePack_011']
        flowers = ['foliagePack_001','foliagePack_002','foliagePack_003','foliagePack_062']

        animal = 'panda'


        
        x = 16

        for i in range(30):
            self.animal_sprite = arcade.Sprite("assets/BG/Leaves/foliagepack_leaves_018.png".format(animal=animal), 0.5)
            self.animal_sprite.center_x = x
            self.animal_sprite.center_y = 16
            self.animal_list.append(self.animal_sprite)
            x += 32       
        
        x = 16
        
        for i in range(30):
            self.animal_sprite = arcade.Sprite("assets/BG/Leaves/foliagepack_leaves_026.png".format(animal=animal), 0.5)
            self.animal_sprite.center_x = x
            self.animal_sprite.center_y = 48
            self.animal_list.append(self.animal_sprite)
            x += 32

        x = 16

        for i in range(30):
            self.animal_sprite = arcade.Sprite("assets/BG/Leaves/foliagepack_leaves_002.png".format(animal=animal), 0.5)
            self.animal_sprite.center_x = x
            self.animal_sprite.center_y = 80
            self.animal_list.append(self.animal_sprite)
            x += 32

        x = 40

        for i in range(10):
            tree = random.choice(trees)

            y = random.randint(181, 187)
            self.animal_sprite = arcade.Sprite("assets/BG/{tree}.png".format(tree=tree), 1)
            self.animal_sprite.center_x = x
            self.animal_sprite.center_y = y
            self.animal_list.append(self.animal_sprite)
            x += random.randint(75,100)

        x = 50

        for i in range(6):
            animal = random.choice(animals)

            self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
            self.animal_sprite.center_x = x
            self.animal_sprite.center_y = 70
            self.animal_list.append(self.animal_sprite)
            x += random.randint(75,175)

        x = 20

        for i in range(10):
            flower = random.choice(flowers)

            y = random.randint(32, 40)
            self.animal_sprite = arcade.Sprite("assets/BG/{flower}.png".format(flower=flower), 1)
            self.animal_sprite.center_x = x
            self.animal_sprite.center_y = y
            self.animal_list.append(self.animal_sprite)
            x += random.randint(75,100)



    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()


    def update(self, delta_time):
        pass


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()