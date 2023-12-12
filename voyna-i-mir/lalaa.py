import time
import random
from PIL import ImageGrab, ImageOps
import pyautogui
import numpy


class BirdBot:
    def __init__(self, replay_btn, bird):
        self.replay_btn = replay_btn
        self.bird = bird

    def restart_game(self):
        pyautogui.click(self.replay_btn)

    def jump(self):
        pyautogui.keyDown("space")
        time.sleep(0.255)
        pyautogui.keyUp("space")

    def grabimage(self):
        box = (
            self.bird[0] + 60,  # x1
            self.bird[1],  # y1
            self.bird[0] + 60,  # x2
            self.bird[1] + 35,  # y2
        )
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)
        a = numpy.array(grayImage.getcolors())
        return a.sum()


def main():
    replay_coord = (315, 505)
    bird = (322, 509)
    bot = BirdBot(replay_coord, bird)
    bot.restart_game()
    time.sleep(1)
    bot.jump()
    while True:
        if not 22000 <= bot.grabimage() <= 25000:
            bot.jump()
        else:
            for i in range(2):
                bot.jump()


main()
