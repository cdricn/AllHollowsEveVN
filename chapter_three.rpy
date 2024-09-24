
label chapter_three:
    $ renpy.choice_for_skipping()
    show palace_outside
    with fade

    An "No..."

    An "This isn't..."

    "The cathedral that stood before me was an impostor.{w=[q]} Or perhaps it was the real one.{w=[q]}
    Much taller, much more ancient than the one in the outside world."

    "Yet despite the obvious aging in between the cracks of its walls, it stood firm."

    "It was not always that you would see something so utterly alien,
    yet still benign that you cannot grasp within your mind where it’s supposed to go."

    "It was insanity to even proclaim that such a building could exist in this depth.{w=[q]}
    And yet there it stood.{w=[q]} A cathedral whose towers seemingly held up the cave that surrounds it."

    "Where the shining beacon of God’s cross reflects the pale moonlight which seeps through the cracks in the ceiling."

    "And the saints, they watched."

    "Their eyes followed us as we made our way towards the Cathedral."

    "Piercing gaze, straight to my soul.{w=[q]} Yet whenever I looked back at them,
    their eyes remained still towards a horizon I could not see."

    Tr "This is… the Cathedral in the Royal Capital."

    An "It’s where they hold the yearly procession to welcome the saints."

    An "Is it… is it like that?{w=[q]} Is the rite like that?"

    An "If it is, then I don’t want to be here."

    "I stopped in front of the Cathedral’s door, reluctant to enter."

    "If I was going to be a sacrificial lamb for the powers at be,
    then I’d rather let my soul be damned to eternity."

    "Although I say that, I wasn’t the only one here."

    "I looked at the girl beside me, her features fierce yet all too familiar now.
    What was she thinking behind those glossy eyes?"

    "Was she thinking of home? Of the family she left behind to tag along with me?"

    "Why did she even do all of that?"

    "Then again, they were being killed there.{w=[q]} Perhaps this was just a play for her to find some safety."

    "God willing, she might sacrifice me too."

    "I could ask her, but I don’t know if now’s the right time."

    "Will there even be a right time?"

    "Either way, I think I’m starting to piece together the makings of this rite."

    Tr "I see… you don’t want to go in?"

    An "No, we should."

    An "It’s what we ought to do."

    Tr "Why is that?"

    An "Huh?"

    Tr "Why must we do it?"

    Tr "Even though I wished to see it, a part of me is asking if we should continue the rite."

    An "I don’t know either."

    An "But us nobles have been all about continuing traditions."

    An "And though unnatural, I feel like this place is part of that tradition."

    An "And it’s my duty to uphold it."

    Tr "I see."

    Tr "You’re stuck here too, huh?"

    An "What do you mean?"

    Tr "I mean that you don’t have anywhere else to go.{w=[q]} For whatever reason, you’re stuck here."

    Tr "Following the same traditions.{w=[q]} Following what the past circumstance has given your birth."

    Tr "Like me!"

    Tr "Except unlike you, I was born in poverty."

    Tr "And you were born in lavish excess."

    "She was right.{w=[q]} As much as I didn’t want to admit it myself."

    "Even if we were born in vastly different circumstances,
    we were still both trapped in the circumstances of our existence."

    "She will never be able to explore the world she read in her books,
    only ever imagining them in her wildest dreams."

    "I have never, and most likely will never escape the traditions of nobility."

    "We will be hanged, castrated, burned in hell forever.
    We will both suffer the worst of humanity at the hands of those that put us here in the first place."

    "And if I was right about what’s actually going to happen to us inside this cathedral,
    we will suffer a much worse hell."

    "It’s funny, thinking about it now."

    "I really should’ve died with them."

    "And maybe she’s thinking the same.{w=[q]} That she should’ve died with the other villagers."

    "I don’t want to ask her.{w=[q]} It’s far too sensitive of a question to ask.{w=[q]}
    Although, I could tell it in her eyes."

    "A sort of uncertainty in the decision we’re making."

    "We both wanted to run away from this place."

    "But we both know that if we did, we’ll still be killed.{w=[q]} That was a guarantee, the rite wasn’t."

    "Who knows, right? It might just be a train directly away from here.{w=[q]} At least that would be nice."

    "That’s too hopeful."

    $ renpy.choice_for_skipping()
    menu:
        "But at least, in this short moment in between the hells we’ve lived in and will live through…"

        "I have her":
            jump chapter_three_minus

        "We have each other":
            $ good_ed += 1
            jump chapter_three_plus

label chapter_three_minus:
    An "Even if that’s the case, I have you now."

    An "And you’ll protect me, right?"

    An "And once we’re out of this mess, we can leave the country together."

    An "I can tell them you’re my personal retainer."

    An "And we can both live comfortably in ways we couldn’t imagine."

    Tr "My, duchess. You’re quite hopeful."

    Tr "I guess that’s why people admire you a lot!"

    Tr "If your plan is to escape the terrible traditions and circumstances of your birth."

    Tr "Then I’ll be with you for as long as I can."

    Tr "I do want to see the Western lands with my own eyes after all."

    An "Then it’s a promise."

    "I smile at her, eager for the future.{w=[q]} Then,--"

    jump chapter_three_part2

label chapter_three_plus:
    An "Even if that’s the case, we have each other now."

    An "Even if, right now, it’s just a matter of circumstance, I think we can work decently well together."

    An "We’ll work against what life puts us through, and the deterministic nature of our existence."

    Tr "Is that so, Duchess?{w=[q]} Do you sincerely hope that?"

    An "As much as I enjoyed the comforts of home."

    An "Being desperately put down like this feels terrible to the soul."

    "I did see my parents be killed in cold blood after all. And maybe she did as well."

    An "So what do you say?{w=[q]} Do you wanna stick together, even after this?"

    Tr "Why not?"

    Tr "If I’m a part of your plans, then who am I to refuse the wishes of a duchess."

    Tr "And especially if that plan will let me see the western lands."

    Tr "So, I suppose, I’ll stay with you for as long as you need me."

    An "Thank you, Trina."

    An "It’s a promise.{w=[q]} We’ll get through this together."

    "I smiled at her, though uncertain about what would happen in the future,
    I knew it would be alright so long as we have each other to run back to."

    "And with that,--"

    jump chapter_three_part2

label chapter_three_part2:
    "--I pushed open the door, and entered the Cathedral."
    #procession bg, black if no time
    scene black
    with fade
    
    "I remembered the first time I witnessed the Procession."

    "We were required to attend it, as is the procedure of the royal family.{w=[q]}
    Sunlight pierced through the stained glass windows;
    it bathed the entire cathedral in a myriad of colors."

    "We were seated on a terrace, high above the commoners below.{w=[q]}
    Yet from here, we could see just how much they changed the cathedral to prepare for the Procession."

    "The aisle, which normally was the width of one man, was stretched out to fit four.{w=[q]}
    All walking side by side."

    "The commoners were all on the far side, terribly cramped, and crushing each other with every breath."
    
    "Mother asked me, “If you think you can, will you willingly change their plight?”"

    "I was twelve then, I didn’t really understand what she was talking about.{w=[q]}
    But even now, I still don’t understand her.{w=[q]}
    So still, like back then, my answer is, “I don’t know.”"

    "I wouldn’t say she was disappointed.{w=[q]} When I looked over to her,
    she seemed to look a little content.{w=[q]} As if the answer I posed was the one that she expected."

    "Then, the church bells rang, and like clockwork, white petals fell from numerous places above us.
    They rained on the coming procession, and reflected the beauty of the colorful lights."

    "It was solemn.{w=[q]} A terrible silence that predicated terrible things.{w=[q]}
    First came the Patriarch, dressed in a purple so Tyrian not even father could wear such garb."

    "He carried the staff of the holy Sun with him.{w=[q]} Gold, tall, and full of splendor."

    "Then, behind him came the eight lesser priests.{w=[q]}
    Those that were responsible for the regional lessons on scripture."

    "They weren’t around much, but they were like Patriarchs of their own.
    They held similar staves as the Patriarch, yet named after the planets."

    "And further behind them, carried by the common folk that they selected by random, was the altar.{w=[q]}
    A golden pool, yet unfilled. Upon its sides, the saints were engraved.{w=[q]}"

    "Their figures, their faces, their achievements.{w=[q]}
    As if it wasn’t enough that they were statues that looked down upon everyone from above."

    "Furthermore, a cross was erected upon one end of it.
    They wanted to suggest something with its design, that God is watching.{w=[q]}
    Not only that,{w=[q]} he approved of this procession."

    #black bg, don't add scene is already black

    Ax "Of course, sister.{w=[q]} Why wouldn’t God approve?"

    An "Because if He saw what we did with our freedom, then He wouldn’t approve."

    Ax "Which part would He not approve of, dear sister?"

    An "That we’re using Him as a scapegoat for our own misdeeds?"

    An "Is this part of his plan when He got Himself killed for us?"

    An "When He allowed us to have the freedom of existence?"

    Ax "Sister, we still have the freedom of existence.{w=[q]}
    He must’ve understood that such freedom also means we bear the responsibility of it."

    Ax "This is freedom.{w=[q]} This is what we choose to do with it.{w=[q]}
    We choose to ask for help from the saints, we choose to remain peaceful in our own lives."

    Ax "Even if it meant trampling those who cannot afford such luxuries."

    Ax "Do you not understand that?{w=[q]} Due to the circumstances of our birth,
    we are far more free than any of these commoners could ever be."

    Ax "We can leave anytime we want.{w=[q]} We can simply abandon our duties
    and run away with so much money that we could live comfortably anywhere until we die."

    Ax "But what did you choose to do with your own sense of free will?"

    An "I..."

    Ax "Threw it away reading books and looking at flowers.{w=[q]}
    You enjoyed the comfort of your existence and now that it came to bite you, you’re regretting it?"

    Ax "You wish to run away now?"

    Ax "Is that what you were thinking when you looked me in the eyes as I was about to be shot?"

    Ax "That you should run away?"

    Ax "You should’ve been there with us."

    Ax "No, you should’ve been there instead of me.{w=[q]} You should’ve been the only one there."

    Ax "You were the most useless in the family after all."

    Ax "Tell me, sister.{w=[q]} After the few short hours you’ve spent with that commoner,
    will you now decide to change their plight?"

    Ax "You’re the only one who can now, after all."

    An "..."

    An "I… I still don’t know."

    Ax "Then, the cycle will continue."

    jump chapter_four