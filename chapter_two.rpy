
label chapter_two:
    $ renpy.choice_for_skipping()
    show forest_night2
    with fade

    An "Haah..."

    "I could hear it all still."

    "Despite having run for ten minutes, and ten minutes more."

    "The desperate screams of those murdered.{w=[q]}
    The gunshots, the ravaging flames of conquest and revolution."

    "Much the same sounds I heard in the palace."

    "I know, I know a terrible fate will befall me soon.{w=[q]} I just know it.{w=[q]}
    Too many people have given their lives for my sake already…"
    
    with vpunch
    Ex "HEY! WAIT!"

    An "Eek!"

    Ex "Duchess! Wait!{w=[q]} It’s me!"

    An "That voice..."

    An "Trina?"

    Tr "Haah… I’m glad to see you’re safe.{w=[q]} But you do run fast."

    An "I’m sorry, I didn’t realize it was you."

    An "But why did you follow me? It’s not safe, you know."

    An "But then again, it’s no less safer here than back there."

    Tr "Haha. That’s exactly why!{w=[q]}
    I thought during that entire chaos that if I were to die,
    I’d rather be by your side actually trying to protect you."

    Tr "And also, you’d need a guide down that cave, no?"

    An "I suppose.{w=[q]} They told me it would be safe there,
    but I don’t know what to expect at all."

    Tr "Expect nothing at all, in all honesty!
    I’ve been down that cave dozens of times and everytime it was still just a cave."

    Tr "Frankly it was too shallow.
    I expected a cave of huge significance to be… deeper.{w=[q]} But it wasn’t."

    Tr "I’ve seen animal burrows deeper than that cave!"

    An "Is that so?"

    An "I wonder now if that cave will actually keep me safe."

    An "At least safe enough to last the day."

    Tr "It doesn’t matter, duchess.{w=[q]} I’ll protect you!"

    An "Heh… thanks, Trina."

    #--mono

    "The moon rose high into the sky by the time we saw even a glimpse of the cave."

    "Before then all that was set in front of us was thick foliage and
    the overwhelming fear of being caught in the sights of a revolutionary."

    "My feet felt sore. It was rough running through these woods in heels.
    And in all honesty I wanted to nab a shoe off of a fallen villager earlier."

    "If I had not panicked I would’ve done it."

    "Maybe I could just ask Trina for her own shoes.
    But then that would make me feel more terrible than I already do."

    "After all, I’ve been blaming myself for my family’s demise.{w=[q]}
    Rather, the fact that I survived when I was not supposed to."

    "It should’ve been Alexei.{w=[q]} Despite how young he was,
    he would’ve been a lot more respected as the true heir of Father."

    "Though, before all those musings took hold of my psyche even further the cave presented itself to us."

    show cave_entrance
    with fade

    "Between the trees, like a gaping maw by the mountainside.{w=[q]} There it was, a river flowed out of it,
    pristine delicate water clashed upon rocks eroded for thousands of years."

    "The Rite will take place here."

    "Pale moonlight shone from above and seemed to highlight the entrance.{w=[q]}
    As if the world, nay, the universe itself, showed us the way."

    "And yet there’s a growing pit of anxiety welling within me."

    "{i}This isn’t the way.{/i}"

    "Two different gravitational pulls, each pulling me towards separate places.{w=[q]}
    One telling me to go into the cave"

    "And the other, urging me to run."

    "Run far away from there.{w=[q]} As far away as possible."

    "Away from the revolutionaries, away from the cave."

    "Anywhere but here."

    $ renpy.choice_for_skipping()
    menu:
        "But do I have a choice?"

        "Enter the cave":
            jump continue_cave_entrance

        "Run away, far away from here":
            jump fail_cave_entrance

label continue_cave_entrance:
    #--mono
    "Even if I did have a choice, it won’t matter."

    "That cave called to me. Its gaping maw spoke to my soul."

    "It beckoned me to approach it, to enter."

    "It wasn’t a choice of whether or not I should run away."

    "There wasn’t any in the first place."

    "Every step of the way felt heavier, and yet that calling grew louder, and louder."

    "Until the deep dark maw swallowed us whole."

    "Of all the lessons my mother taught me, only one of them ever struck me as odd."

    "It was a lesson on handling cavernous creatures."

    "She said they were capable of human speech.{w=[q]}
    And that they were always going to lead you astray,
    perhaps deeper into a part of the cave that’s unsurveyed, or has just spontaneously opened up."

    "It could even be that they made that part of the cave themselves,
    whose sole purpose is to devour you in silence."

    "She told me two fundamental rules.{w=[q]}
    The first of which was to always follow the torchlight in the cave."

    "I recall that now for one reason."

    "And that is the fact that a part of this cave, or perhaps one of its path is artificial.{w=[q]}    
    A long, seemingly endless hallway lined with torches."

    show cave_hallway1
    with fade

    An "..."

    Tr "..."

    Tr "I could’ve sworn it wasn’t there before."

    "I approached the hallway and touched the stone that made up its walls.
    They weren’t carved or mined out of the cave at all."

    "The texture felt smooth to the touch and yet not a speck of dust was there to indicate any sort of age or exposure to the outside world."

    "It’s as though this was made just a few seconds ago."

    "Instantly."

    An "It might not have been here before, but I don’t know how to explain it."

    Tr "Do you trust it?"

    An "Do you?"

    Tr "If it’s something the nobles built, then it’s probably related to the rite."

    An "I suppose so. But how could the nobles build this in such a short amount of time?"

    Tr "Did they know perhaps that they’re going to be killed?
    Then maybe they made this and retreated here."

    An "!"

    An "It could be that."

    An "Still.{w=[q]} That could only mean they’re down here. And I don’t know how to feel about that."

    An "They’re not my family. They’re just nobles vaguely related to us by finance or merit."

    An "They don’t care about me for anything other than my name."

    Tr "Huh, I see."

    Tr "I can’t really understand the relationship between you and others."

    Tr "Do you not have friends back home?"

    show cave_hallway2
    with fade

    An "Friends..."

    An "Maybe Alexei, my brother.{w=[q]} Sometimes we laze around reading books in the library."

    An "I couldn’t really connect with anyone else."

    An "The women there were too caught up with the dances and parties.{w=[q]}
    Everything really.{w=[q]} They were vain."
    
    An "Much too vain.{w=[s]} My sisters were too."

    An "Make no mistake, I don’t hate them.{w=[q]} If I were, I'd be more scathing."

    An "We were just different in terms of how we saw the world."

    Tr "But how did you see the world, madam?"

    An "Madam? Well, anyway.{w=[q]} I tend to try and understand it more."

    An "So I was more engrossed in books, and heading outskirts to witness the world in its rawest form."

    An "It’s why I understand why the revolutionaries act the way they do."

    An "Though, it’s not like I can change that."

    An "I’m just a duchess, the youngest at that.
    My fate is to be… married off, to someone, and never return to my home."

    Tr "I see. I won’t pretend to understand your troubles so,
    perhaps I can ask more about the things you’ve read."

    Tr "You know, despite how it is, I actually know how to read! My mother taught me!"

    An "Oh! Well. It was mostly biological textbooks I found in our expansive library."

    An "Oftentimes they would contain illustrations for the specific plants and flowers."

    An "Then, I sneak outside to look at the wildflower patches near the outskirts."

    An "My brother loved it whenever I brought back some beautiful looking flowers."

    An "He knew about my sneaking-out adventures so sometimes he requests me to bring stuff too!"

    An "It was fun.{w=[q]} A fun I would never get from being around my sisters.{w=[s]} Or my father."

    An "But that’s in the past now."

    Tr "You’re really just saying that aren’t you?"

    An "That it’s in the past?"

    Tr "Yeah."
    
    An "Yeah.{w=[q]} I am.{w=[q]} Even then it’s a casual admittance right?{w=[q]}
    What can I do when everything has already happened?"

    Tr "When winter comes by and our crops start to wither, we start to look forward to the summer."

    An "..."

    An "I still long for spring."

    "Trina tried to speak but held her tongue.
    I couldn’t tell what she thought of my words, and honestly,
    I cared too much for it for some reason. I wanted to ask her, but we urged ourselves forward."

    "Because, for some reason, the hallway ended."

    "Not in a room, but towards another cave."

    show palace_outside
    with fade

    "test"
    return


label fail_cave_entrance:
    #--run fx
    show forest_night1
    with fade

    "Of course I have a choice.{w=[q]} I always, always have a choice."

    "I took Trina’s hand and ran away with her.{w=[q]} Even when my feet sores from each step of my heels."

    "It was better to receive that pain than to die in a random cave somewhere."

    "Whatever it was that I felt, it wasn’t good. This was the better choice."

    Tr "H-hey! Where are we going?!{w=[q]} The cave’s right there!"

    An "I don’t know.{w=[q]} But I don’t trust it one bit."

    An "I don’t want to enter that place.{w=[q]} You’d understand right?{w=[q]} You felt it too."

    Tr "Yes.{w=[q]} Yes I did, but…"

    Tr "Even if I did feel something sinister, I still felt compelled to enter."

    Tr "It felt like it was calling me too.{w=[q]} That it was safe there."

    Tr "Like my mother would call me back home after a long day of play."

    An "That’s madness.{w=[q]} And you know it.{w=[q]}
    Tell me, then, where’s the path to the station, we’ll be safer there."
    
    "Trina sighed. Then, she stopped in her tracks.{w=[q]}
    Her grip was tight and forced me down alongside her."

    An "Wha, huh? What’s wrong?"

    Tr "Duchess.{w=[q]} Be quiet."

    An "Why?"

    Tr "They’re here."

    "We were crouched down, hopeful that the thick foliage and
    the darkness of the night would mask us away from the eyes of the revolutionaries."

    "I held my breath.{w=[q]} Held my heart.{w=[q]} Held everything."

    "But it was too late."

    #--gunshot sfx
    with vpunch

    "A shot rang out.{w=[q]} It disturbed the calm silence of the forest."

    "And the girl beside me fell to the ground.{w=[q]} Consumed by it, face down.{w=[q]}
    I couldn’t even see her face anymore."

    An "Trina...?"

    "I poke her.{w=[s]} I touch her.{w=[s]} I push her to and fro to no avail."

    An "Trina?{w=[s]} Please…?"

    "I don’t even care if they heard me anymore."

    with vpunch
    An "TRINA!"

    "Trina doesn’t respond.{w=[s]} She will never respond."

    "I just wanted to keep her safe.{w=[s]} My gut feeling warned me about that cave."

    "I wanted to take her with me to that station, so we could flee together."

    "It should’ve been like that."

    "But not like this.{w=[q]} It shouldn’t be like this.{w=[q]}
    No matter how much I shake her she just doesn’t seem to budge."

    "Not like this."

    "Not the one person that made me feel familiar to this world."

    "Even if it was just for a brief exchange."

    "You still made me feel special."

    "More than any other noble."

    #run sfx

    "The heavy steps of revolutionaries come to approach me, their guns drawn."

    "In their eyes were a raging fire that never once quelled."

    "It felt like they were possessed by the spirit of revenge, born from spite towards the royal nobility."

    "I understand them."

    An "Please..."

    scene black
    #gunshot sfx
    with vpunch

    centered "You have been shot to death by the revolutionaries."

    menu:
        "Continue from last checkpoint?"

        "Yes":
            jump chapter_two

        "No":
            return