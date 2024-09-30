# Mainchars
default An = Character("Ana")
default Tr = Character("Trina")
default So = Character("Sofia")
default Ax = Character("Alexei")
default SoAx = Character("Sofia & Alexei")

# Sidechars
default Vl1 = Character("Villager 1")
default Vl2 = Character("Villager 2")
default Rv1 = Character("Revolutionary 1")
default Rv2 = Character("Revolutionary 2")
default Ex = Character("???")
default Nb1 = Character("Noble")

# Pauses
default q = float(.2) #quick pause
default s = float(.5) #short pause

# Backgrounds
# Update: Upload 512 base images instead, then scale to nearest neighbor using renpy.
# Scaling from 512 is not in near neighbor, maybe additional argument? Search more why
image forest_night1 = im.Scale("bgs/ForestNight1.png", 1920, 1080)
image forest_night2 = im.Scale("bgs/ForestNight2.png", 1920, 1080)
image house_night = im.Scale("bgs/HouseNight1.png", 1920, 1080)
image village_night = im.Scale("bgs/VillageNight1.png", 1920, 1080)
image cave_entrance = im.Scale("bgs/ForestCave.png", 1920, 1080)
image cave_hallway1 = im.Scale("bgs/CaveInside.png", 1920, 1080)
image cave_hallway2 = im.Scale("bgs/CaveHallway.png", 1920, 1080)
image palace_outside = im.Scale("bgs/CavePalace.png", 1920, 1080)
image palace_hallway = im.Scale("bgs/PalaceHallway1.png", 1920, 1080)
image palace_artroom = im.Scale("bgs/PalaceArtroom.png", 1920, 1080)
image palace_painting = im.Scale("bgs/PalacePainting.png", 1920, 1080)
image palace_baseclosed = im.Scale("bgs/PalaceBasement_Closed.png", 1920, 1080)
image palace_baseopened = im.Scale("bgs/PalaceBasement_Open.png", 1920, 1080)
image palace_ballroom = im.Scale("bgs/PalaceBallroom2.png", 1920, 1080)
image palace_ballroom_blood = im.Scale("bgs/PalaceBallroom_Blood2.png", 1920, 1080)
image palace_ballroom_trina = im.Scale("bgs/PalaceBallroom_Trina2.png", 1920, 1080)
image palace_ballroom_ana = im.Scale("bgs/PalaceBallroom_Ana2.png", 1920, 1080)
image palace_ballroom_gd = "bgs/PalaceBallroom_Tr.png"
image palace_ballroom_quiet = "bgs/PalaceBallroom_Quiet.png"

# Characters
image ana = "sprites/char_ana.png" #always right
image ana_h = "sprites/char_ana_happy.png"
image ana_s = "sprites/char_ana_scared.png"
image ana_w = "sprites/char_ana_worried.png"
image ana_dirty = "sprites/char_ana_dirty.png" #always right
image trina = "sprites/char_trina.png"
image trina_s = "sprites/char_trina_sad.png"
image trina_w = "sprites/char_trina_worried.png"
image alx = "sprites/char_alexei.png"
image alx2 = "sprites/char_alexei_black.png"
image mom = "sprites/char_queen.png"
image tsar = "sprites/char_tsar.png"
image sis = "sprites/char_sister.png"

image vil_m = "sprites/char_villager_male.png"
image vil_f = "sprites/char_villager_female.png"

image rev_R = "sprites/char_enemy1.png" #for right
image rev_L = "sprites/char_enemy2.png" #for left

# Transforms
transform right:
    xalign 1.0 yalign 0.5
transform right_flip:
    xalign 1.0 yalign 0.5
    xzoom -1.0
transform right_flip2:
    xalign 0.9 yalign 0.5
    xzoom -1.0
transform left:
    xalign 0.0 yalign 0.5
transform left_flip:
    xalign 0.0 yalign 0.5
    xzoom 1.0
transform left_second:
    xalign 0.2 yalign 0.5
transform center:
    xalign 0.5 yalign 0.5
transform half:
    xalign 0.1 yalign 0.5

transform hide_L:
    xalign -0.5 yalign 0.5
transform hide_R:
    xalign 1.5 yalign 0.5
transform hide_Bottom:
    xalign 1.5 yalign 1.3


init python:
    renpy.music.register_channel('normal', "music")

label start:
    $ good_ed = 0

    jump prologue
