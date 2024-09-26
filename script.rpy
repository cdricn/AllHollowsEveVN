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
image forest_night1 = im.Scale("ForestNight1.png", 1920, 1080)
image forest_night2 = im.Scale("ForestNight2.png", 1920, 1080)
image house_night = im.Scale("HouseNight1.png", 1920, 1080)
image village_night = im.Scale("VillageNight1.png", 1920, 1080)
image cave_entrance = im.Scale("ForestCave.png", 1920, 1080)
image cave_hallway1 = im.Scale("CaveInside.png", 1920, 1080)
image cave_hallway2 = im.Scale("CaveHallway.png", 1920, 1080)
image palace_outside = im.Scale("CavePalace.png", 1920, 1080)
image palace_hallway = im.Scale("PalaceHallway1.png", 1920, 1080)
image palace_artroom = im.Scale("PalaceArtroom.png", 1920, 1080)
image palace_painting = im.Scale("PalacePainting.png", 1920, 1080)
image palace_baseclosed = im.Scale("PalaceBasement_Closed.png", 1920, 1080)
image palace_baseopened = im.Scale("PalaceBasement_Open.png", 1920, 1080)
image palace_ballroom = im.Scale("PalaceBallroom2.png", 1920, 1080)
image palace_ballroom_blood = im.Scale("PalaceBallroom_Blood2.png", 1920, 1080)
image palace_ballroom_trina = im.Scale("PalaceBallroom_Trina2.png", 1920, 1080)
image palace_ballroom_ana = im.Scale("PalaceBallroom_Ana2.png", 1920, 1080)

# Characters
image ana = "char_ana.png" #always right
image ana_dirty = "char_ana_dirty.png" #always right
image trina = "char_trina.png"
image alx = "char_alexei.png"
image alx2 = "char_alexei_black.png"
image mom = "char_queen.png"
image tsar = "char_tsar.png"
image sis = "char_sister.png"

image vil_m = "char_villager_male"
image vil_f = "char_villager_female"

image rev_R = "char_enemy1.png" #for right
image rev_L = "char_enemy2.png" #for left

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
