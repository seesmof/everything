"""
На стенді стоїть деяка кількість об’єктів. Деякі з них рухаються. Користувач кидає в них набір предметів. Кожен з них має свої фізичні характеристики (прискорення, точність потрапляння). Кожен предмет можна кинути тільки один раз. Кожен об’єкт на стенді у разі потрапляння в нього приносить певну кількість очок. Падаючи, предмети можуть збивати інші предмети, приносячи додаткову кількість очок. Необхідно набрати максимальну кількість очок. Результати користувача зберігаються.
  - each projectile is being thrown
  - objects on stand fall and can do collateral damage to other objects
  - projectiles can have different speed, accuracy
  - if projectile hits, the object has a chance to be hit
"""

"""
task description:
There are a number of objects on the stand. Some of them are moving. The user throws a set of objects at them. Each of them has its own physical characteristics (acceleration, accuracy). Each object can be thrown only once. Each object on the stand, if hit, brings a certain number of points. Falling objects can knock down other objects, bringing additional points. The goal is to score the maximum number of points. The user's results are saved.

stand on right side of screen
multiple objects on the stand, just grey circles, some of them move up and down
score displayed at the bottom of the screen
if object hits another object on its way, more points
play until all points are collected

for projectiles:
green - high speed, low accuracy
yellow - medium speed, medium accuracy
red - low speed, high accuracy

each projectile is to be aimed using mouse and thrown at the direction the mouse is facing once LMB is pressed
if projectile hits an object on stand, it gets knocked off and gets a little bit of kickback applied to it when knocked off
stand object under kickback can also do collateral damage to other objects
"""

import pygame
import random
from sys import exit
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Thrower Game")
clock = pygame.time.Clock()


class Object:
    def __init__(self, x, y, radius: int = 20, color: str = "cadetblue1"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.moving = random.randint(0, 1)
        self.knockback = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Projectile:
    def __init__(
        self,
        x: float = 20,
        y: float = 200,
        speed: float = 0.5,
        accuracy: float = 0.5,
        color: str = "darkgoldenrod1",
    ):
        self.x = x
        self.y = y
        self.speed = speed
        self.accuracy = accuracy
        self.color = color
        self.direction = (0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 7)


projectileProps = {
    "green": {"speed": 1, "accuracy": 0.35, "color": "chartreuse3"},
    "yellow": {"speed": 0.5, "accuracy": 0.5, "color": "darkgoldenrod1"},
    "red": {"speed": 0.35, "accuracy": 1, "color": "crimson"},
}

objects = [Object(700, 200)]
projectiles = [
    Projectile(
        speed=projectileProps["red"]["speed"],
        accuracy=projectileProps["red"]["accuracy"],
        color=projectileProps["red"]["color"],
    ),
]

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            for projectile in projectiles:
                projectile.direction = (
                    mousePos[0] - projectile.x,
                    mousePos[1] - projectile.y,
                )
                projectile.direction = (
                    projectile.direction[0] / 10,
                    projectile.direction[1] / 10,
                )

    for object in objects:
        # if object.moving:
        #     object.y += random.randint(-10, 10)
        object.draw(screen)
    for projectile in projectiles:
        projectile.x += projectile.direction[0] * projectile.speed
        projectile.y += projectile.direction[1] * projectile.speed

    for projectile in projectiles:
        for object in objects:
            distance = (
                (projectile.x - object.x) ** 2 + (projectile.y - object.y) ** 2
            ) ** 0.5
            if distance < projectile.speed * 2:
                object.knockback = 10

    screen.fill("white")
    for object in objects:
        object.draw(screen)
    for projectile in projectiles:
        projectile.draw(screen)
    pygame.display.update()
    clock.tick(60)
