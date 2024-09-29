
label chapter_four:
    $ renpy.choice_for_skipping()
    play music "Sample2.ogg" loop
    play sound "Hit.ogg"
    hide alx
    hide ana
    show palace_hallway
    show ana at right
    show trina at left
    with vpunch
    
    An "!"

    Tr "Ana? Thank goodness, you’re awake."

    Tr "Are you feeling well? Can you stand?"

    An "Y-yes."

    An "Yes, I’m fine.{w=[q]} Where are we?{w=[q]} Are we in…"

    Tr "I don’t know, but it looks lavish, no?"

    Tr "I was thinking you’d immediately know wh--"

    An "Urk!"

    "We were in the royal palace.{w=[q]} I could tell from the splendor that surrounded us."

    "It was sickening, full of red and gold.{w=[q]}
    They were enough to hide the blood spilled by the nobles, but you could still smell the iron."

    "Why..."

    An "Why are we here?{w=[q]} Were we captured?"

    An "Are they going to kill us?"

    An "A--"

    Tr "Ana, calm down."

    Tr "I don’t know what happened either, but the moment we entered the Cathedral we just woke up here."

    An "Eugh.{w=[q]} I didn’t think I would be back in this place so soon."

    Tr "If anything, we’re still under the cave.{w=[q]} So maybe this is what’s inside of the Cathedral."

    An "Is that so..."

    "This can’t be right.{w=[q]} I know I went and snuck through the cathedral dozens of times,
    and none of it looks even remotely similar to anything in the palace."

    "I slapped my hands, pinched my cheeks and tried to recalibrate myself to the world around me."

    "It was real.{w=[q]} The underground Cathedral’s interiors were similar to the Palace of the royal family, my home."

    Tr "Also, something was chasing us"

    An "HUH?!"

    Tr "Yeah. When I woke up there was a creeping darkness.
    It snuffed out the lights, and was cold to the touch."

    Tr "You weren’t awake still, so I had no choice but to carry you all the way here."

    Tr "So we’re safe, for now."

    An "Thank you, Trina."

    An "But we can’t stay here.{w=[q]} This hallway can’t be where we’ll “Do” the “Rite” after all."

    Tr "?{w=[q]} How did you do that with you--"

    Tr "Nevermind.{w=[q]} Yes, let’s go."

    Tr "And hopefully not that way because that’s where I just ran away from that weird darkness."

    play sound "Walk.ogg"
    with fade

    An "Hm, that’s weird."

    Tr "Yeah?"

    An "Haven’t you noticed?"

    Tr "I have, I was just seeing how long it’d take for you to notice.{w=[q]}
    I don’t really know the place after all."

    An "Uh-huh.{w=[q]} We seem to be going down similar paths."

    An "Or perhaps we’re going in circles?"

    Tr "We took three rights and one left, then another right, then another left.{w=[q]}
    By that path we shouldn’t have gone in circles.
    Not to mention we’ve gone down the stairs numerous times already."

    An "Even still, the palace wasn’t that huge."

    An "At least, not huge enough to warrant such sprawling hallways."

    Tr "That’s fair.{w=[q]} If that was the case then the palace would be a lot bigger than my village."

    Tr "Why not open that door then?"

    "Beside me was a door we had not yet opened.{w=[q]} There was also another on the far end of the hallway,
    but seeing as this was closest, I went ahead and opened it."
    
    play sound "Walk.ogg"
    hide ana
    hide trina
    show palace_baseclosed
    show ana at right
    show trina at left
    with fade

    An "Oh."

    Tr "Do you know that place?"

    An "That’s… that’s the basement."

    "Stairs went down towards a closed door.{w=[q]}
    The faint sound of ballroom music could be heard from the inside.{w=[q]} Muffled, and terrible."

    An "The basement was…"

    An "That’s where they were executed."

    "I should know.{w=[q]} I saw it with my own eyes.{w=[q]} I was down there with them,
    but I hid somewhere.{w=[q]} Somewhere where only Alexei could see me."

    "Our eyes locked in that moment, even as he was shot.{w=[q]} Even as he fell down the floor.{w=[q]}
    Neither of us left each other’s gaze."

    An "But… that’s not possible.{w=[q]} Even if I knew intuitively that that’s the basement."

    An "This layout doesn’t make sense."

    An "It should make sense.{w=[q]} There’s a reason for the madness around."

    $ renpy.choice_for_skipping()
    menu:
        "But I can’t quite grasp it."

        "Make a guess":
            jump guess

        "Try to remember":
            $ good_ed += 1
            jump remember

label guess:
    Tr "Could it be because they were stuck here for quite a while
    building the place that they still had old blueprints?"

    Tr "That happens sometimes in the mines.{w=[q]}
    People tend to be down there for so long that they miss out on developments in the village."

    Tr "As a result, they get lost."

    An "Oh, goodness.{w=[q]} How long do they stay down in the mines anyway?"

    Tr "Two hours."

    Tr "But because of the time dilation there they actually stay for about two years."

    An "Oh, I see."

    An "…That seems wildly inefficient though?"

    An "Is that why there’s so many all over the empire?"

    Tr "Is it?"

    Tr "I don’t know."

    An "Oh… right.{w=[q]} Sorry."

    An "Actually…"

    An "Do you think this cave has that too?"

    An "The time dilations, I mean."

    Tr "It could be that.{w=[q]} It might be that."

    jump chapter_four_part2

label remember:
    An "Wait a minute…"

    "The design on the walls. The feel of the carpet beneath our feet.{w=[q]}
    And how could I have been so blind to the pillars that held up the ceiling!"

    "I saw all of these in my mother’s lessons!"
    
    An "We’re in the royal palace, yes.{w=[q]} But this was back when it was used by the Cronian Dynasty."

    Tr "Am I… supposed to know them?"

    An "I suppose you said you knew how to read, no?"

    Tr "Yes, but they were more on children’s stories if anything."

    Tr "Nothing fancy like biology textbooks or some philosophy."

    An "I suppose.{w=[q]} But anyway, the Cronian Dynasty existed 3000 years ago."

    An "For reasons unknown to us, with methods lost to time,
    they started the Cronian crisis which is still ongoing."

    An "Do you know at least that?"

    Tr "Cronian crisis… Oh!{w=[q]} I heard about that!{w=[q]}
    That’s the reason why all of the mines are time dilated, right?"

    Tr "Some of our miners stay down there for two hours but actually come out two years later in the worst parts."

    An "That’s terrible.{w=[q]} Two hours to two years?
    I heard the worst was only two minutes of separation."

    An "I guess some of those textbooks were wrong or outdated."

    Tr "Who knows?{w=[q]} Then, if this is the royal palace of the Cronian Dynasty,
    then wouldn’t it make sense if we were stuck in a time dilation as well?"

    An "That’s very much possible.{w=[q]} But who knows how long we’ve been out now…"

    jump chapter_four_part2

label chapter_four_part2:
    $ renpy.choice_for_skipping()
    An "In any case, we can’t go down there right now.{w=[q]} So might as well go somewhere else instead."

    An "Like that door at the end."

    An "It might be unlocked."

    Tr "You sure you don’t wanna head down the basement instead?"

    Tr "It is quite noisy, maybe there’s people there?"

    An "Even if there are, do you think we should trust them?"
    
    Tr "You said they might be nobility, right?{w=[q]} What if you’re right?"

    An "If I'm right and they’re nobility that just makes things worse."

    An "For me, specifically."

    An "And for you as well, they might sacrifice you for all we know."

    Tr "Does the nobility do that?"

    An "They go to war."

    $ renpy.choice_for_skipping()
    menu:
        Tr "I suppose. Still, you choose."

        "Enter the other room":
            jump chapter_four_pass

        "Try to enter the basement":
            jump chapter_four_fail

label chapter_four_fail:
    hide black
    "As reluctant as I was to enter, seeing another person would at least ease up the tension in the place."

    "Trina and I carefully approached the door at the end of the stairs.{w=[q]}
    An odd darkness had engulfed it almost entirely."

    "It looked as though the light of the torches stopped at a certain point.{w=[q]}
    As if the shadow actively ate away at the light."

    "I reached for the golden handle, and tried to push it open."

    "But it wouldn’t budge."

    "I tried again, and again, and again.{w=[q]} Yet it still wouldn’t budge."

    "Worse still, the music inside grew fainter."

    "Something was dying in there."

    An "L-let’s go."

    "I tried to move away, but a terrible, cold darkness seeped from beneath the door and clutched my legs.{w=[q]}
    I couldn’t move it.{w=[q]} Furthermore, it felt like death."

    "A total loss of sensation, to the point that I don’t feel it existing anymore,
    yet still, I couldn’t move from it."

    play sound "Hit.ogg"
    show black
    with vpunch

    An "Trina, help!"

    "She reached out for my hand and tried to pull me away to no avail."

    "The darkness was overwhelming.{w=[q]} It sought to engulf me whole."

    play sound "Breathing.ogg"

    "It went up from my legs,{w=[q]} to my thighs,{w=[q]} to everywhere.{w=[q]} Until it reached my neck."

    An "Help..."

    "Trina held on for as long as she could.{w=[q]} She tried to scream for help, I think.{w=[q]}
    I think she yelled my name aloud too."

    "But I couldn’t hear her.{w=[q]} Not with the darkness coming up to my ears."

    "As my eyes slowly but surely darken,
    the last thing I saw were her desperate pleas to get me out of the eternal dark."

    "Her hands slipping from mine, as I fell into the depths below."

    centered "You have been swallowed by the darkness."

    $ renpy.choice_for_skipping()
    menu:
        "Continue from last checkpoint?"

        "Yes":
            hide black
            jump chapter_four_part2

        "No":
            return

label chapter_four_pass:
    An "I really don’t trust whatever’s going on in that basement."

    An "As I’ve said, even if the nobility was there.{w=[q]} They’d probably harm you for being a commoner."

    An "It’s better we look around first."

    Tr "Sure…"

    "I pushed open the door."

    jump chapter_four_part3

label chapter_four_part3:
    $ renpy.choice_for_skipping()
    play sound "Walk.ogg"
    hide trina
    hide ana
    show palace_artroom
    show ana at right
    show trina at left
    with fade

    "Inside was a long hallway, dimly lit save for a few torches and
    the window at the far end where an unknown light seemed to emerge from beyond.{w=[q]}
    It imitated the moon, yet was significantly dimmer."

    "At the far end of the hallway was a portrait.{w=[q]} A family portrait."

    "I approached it, careful with each step.{w=[q]} I could hear Trina trailing behind me."
    
    "Her breath was sharp.{w=[q]} Like daggers that gasped and clutched my back."

    "There was something about this room that made her so terrified that she would
    rather grab hold onto my sleeves rather than simply follow idly behind."

    "As if she saw something that I couldn’t."

    "Then there it was, at the end of the hallway.{w=[q]} I saw the family portrait so vividly,
    despite the minimal amount of light around it."

    show palace_painting
    with fade

    "It was our family portrait."

    An "No..."

    "Trina held tightly now.{w=[q]} As if she was pulling me back."

    An "Trina, what are you doing?"

    Tr "Ana, let’s get out of here."

    An "No, don’t you see?!{w=[q]} Why is my family painting here?"

    An "That’s me, right there!"

    An "How did it get down here after so long?"

    An "Tell me!"

    "I turned around and let my voice echo through the walls.{w=[q]}
    There, numerous torches light up across the hallway, bathing the entire room in a warm orange glow."

    "I could see it all now, all hung up on the wall."

    "Family portraits."

    "The Cronian Dynasty, the Echidnon Dynasty, the Lagrange…{w=[q]} they’re all here."

    "I stepped towards each and every portrait, analyzing any inconsistencies.{w=[q]}
    But there were none, save for one thing."

    "I would say it’s an inconsistency but it’s always a constant.{w=[q]} A consistent inconsistency."

    An "No..."

    "And it was a terrible one."

    An "What…{w=[q]} what the…"

    "Every portrait, save for the Konstantin Dynasty’s"

    An "Where are the youngest daughters?"

    Tr "Huh?"

    An "There!"

    "I point at the empty seats in every other portrait."

    An "The youngest daughter is supposed to be seated there!{w=[q]} But why!?{w=[q]} Where are they?!"

    "Nothing,{w=[q]} nothing,{w=[q]} nothing."

    "All that’s left in those portraits were an empty seat and the implication that someone once seated there."

    An "I don’t understand…{w=[q]} Why?!"

    Tr "Ana, please.{w=[q]} Calm down.{w=[q]} We should leave this room."

    An "No!{w=[q]} I…"

    Tr "No!{w=[q]} Let’s go! Now!"

    "I looked back at my family portrait and saw it getting engulfed in darkness.{w=[q]}
    The false light of the moon had disappeared."

    "It was approaching."

    "And yet I couldn’t move.{w=[q]} As if my legs locked in place, or rather frozen in place.{w=[q]}
    It was cold, after all."

    "I could feel Trina tugging on my sleeve, trying to pull me out but to no avail."

    An "T-trina.{w=[q]} Please."

    Tr " I got you!"

    "She held on to my waists and pulled me away.{w=[q]} Nothing restricted my legs,
    so it seemed she just carried me away."

    "All the way out of the hallway."
    
    "I watched the paintings slowly become consumed by the darkness, until they were all no more."

    stop music
    jump chapter_five