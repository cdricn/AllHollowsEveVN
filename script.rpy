﻿# Mainchars
default An = Character("Ana", voice_tag="ana")
default Tr = Character("Trina", voice_tag="trina")
default So = Character("Sofia", voice_tag="female")
default Ax = Character("Alexei", voice_tag="male")
default SoAx = Character("Sofia & Alexei", voice_tag="")

# Sidechars
default Vl1 = Character("Villager 1", voice_tag="male")
default Vl2 = Character("Villager 2", voice_tag="female")
default Rv1 = Character("Revolutionary 1", voice_tag="enemy")
default Rv2 = Character("Revolutionary 2", voice_tag="enemy")
default Ex = Character("???", voice_tag="enemy")

default q = float(.2) #quick pause
default s = float(.5) #short pause

image forest1_night = im.Scale("ForestNight1.png", 1920, 1080)
image house_night = im.Scale("HouseNight1.png", 1920, 1080)
image village_night = im.Scale("VillageNight1.png", 1920, 1080)

#screen voice_toggle:
#    vbox:
#        textbutton "Mute Ana" action ToggleVoiceMute("ana")
#        textbutton "Mute Trina" action ToggleVoiceMute("trina")
#        textbutton "Mute Female" action ToggleVoiceMute("female")
#        textbutton "Mute Male" action ToggleVoiceMute("male")
#        textbutton "Mute Enemy" action ToggleVoiceMute("enemy")


label start:
    jump prologue
