def on_on_overlap(sprite, otherSprite):
    global count, level
    count += 1
    info.change_score_by(1)
    otherSprite.destroy()
    otherSprite.start_effect(effects.smiles, 200)
    if count > 10 + level:
        level += 1
        music.jump_up.play()
        startLevel()
    else:
        music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def startLevel():
    global count, food
    scene.set_background_color(randint(3, 7))
    count = 0
    index = 0
    while index <= 10 + level:
        food = sprites.create(sprites.food.small_cherries, SpriteKind.food)
        food.set_position(randint(20, 140), randint(20, 100))
        index += 1
    player2.say("Level " + str(level), 1000)
    info.start_countdown(10)
food: Sprite = None
count = 0
player2: Sprite = None
level = 0
game.splash("Hurry!", "Eat the cherries!")
level = 1
player2 = sprites.create(sprites.castle.princess_front0, SpriteKind.player)
controller.move_sprite(player2, 70, 70)
startLevel()