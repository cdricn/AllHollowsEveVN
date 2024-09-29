
label chapter_one:
    $ renpy.choice_for_skipping()
    show house_night
    show ana at center
    play sound "Hit.ogg"
    with vpunch


    An "ALEXEI!"

    show trina at left
    with moveinleft
    show ana at right
    with moveinleft

    Tr "Gah!"

    An "...Huh?{w=[s]} Where…{w=[s]} Where am I?"

    "My eyes gradually came into focus as I looked around.{w=[q]}
    Beside me a candle light dimly glows.{w=[q]}
    It illuminated the single room house.{w=[q]}
    Wooden walls, a low hanging ceiling,{w=[q]} in the distance,
    opposite the soft bed I laid upon, was a dining table."

    "And beside me, a bit shocked, but not as fearful as I was, a girl.{w=[q]}
    She was pretty, and far too…{w=[q]} common.{w=[q]}
    Like a deer on the far outskirts of a forest during a snowy day."

    Tr "Ah, goodness.{w=[q]} You’re awake."

    Tr "You haven’t been asleep for long, it was a miracle I found you just on the outskirts."

    Tr "In any case, sorry for talking too much, you might be overwhelmed.{w=[q]}
    But rest assured, you’re safe, Duchess."

    An "Duchess?{w=[q]} You know me?"

    Tr "Of course.{w=[q]} No one in the village doesn’t know you, you’re our duchess!{w=[q]} Revered and noble."

    An "Then you have heard of what occurred earlier today?"

    Tr "We have, unfortunately.{w=[s]} However, the village will do what it can to protect you."

    Tr "They owe you and your family a lot for our continued existence."

    An "Do they...?"

    "I had no idea what this place was.{w=[q]}
    Neither father nor mother mentioned it once in my education.{w=[q]}
    Surely such a loyal village would be mentioned in the event of a catastrophe,
    or at the very least in the ideas of politics."

    "But who am I kidding?{w=[q]} Such ideas were probably passed over to Alexei instead of me."

    "I was not destined for anything in that court, after all."

    "Like all women there, we were just going to be sold off to the highest bidder.{w=[q]}
    The greatest political ally possible.{w=[q]} The only one that had a future there was Alexei."

    Tr "They do!{w=[q]} Don’t worry, do you want to meet them?"

    Tr "When we found you in the outskirts we were worried that you had passed on already."

    Tr "They said the rites would’ve been a lot more complicated had that been the case."

    Tr "But since you’re well, they’re excited to see you!{w=[q]} Hup!"

    show trina at hide_L
    with moveinright
    play sound "Walk.ogg"

    An "Huh?{w=[q]} Hey, wait!"

    "She quickly bolted out of the house."
    play sound "Hit.ogg"

    An "Wait!"

    show ana at hide_L
    with moveinright

    $ renpy.choice_for_skipping()
    scene village_night
    with fade

    ""
    show ana at right
    with moveinright

    An "Hey!{w=[q]} At least tell me what that rite is.{w=[q]} Am I going to die here too?"

    show trina at left
    with moveinleft

    Tr "Huh?{w=[s]} Oh, no, please.{w=[q]}
    I didn’t mean it like that.{w=[q]} The rite is…{w=[q]} well.{w=[q]} The rite!"

    An "And what is the rite?"

    Tr "The rite of welcoming the saints!"

    Tr "Every few hundred years, someone from the royal family
    does the rites in the cave on the outskirts of the village."

    Tr "And this year is that year."

    An "Oh… I’m sorry,{w=[q]} this rites stuff wasn’t taught to me by my parents.{w=[q]}
    I don’t really know what to do."

    Tr "Don’t worry about it!"

    Tr "You’re the duchess!{w=[q]} Even if you mess up,
    people will think it’s part of the rite."

    An "I see..."

    An "Actually, what happens there?"

    Tr "Uhm..."

    Tr "I don’t know actually…{w=[q]} haha…"

    An "Eh...?"

    Tr "Well, the last time it happened was three hundred years ago."

    Tr "Anyone who witnessed it firsthand is already gone."

    Tr "All we have left are incomplete fragments from the past."

    Tr "I do want to witness it though, for what it’s worth.{w=[q]}
    They say it’s a great light show to seal the night!"

    An "Light shows huh?{w=[q]} Plenty of great light shows back in the capital!"

    Tr "Really? I haven’t really seen them.{w=[q]} Only ever glimpses beyond the trees."

    An "Oh, yes.{w=[q]} They’re wonderful."

    An "Maybe I should show them to you someday."

    An "If I ever could…{w=[q]} haaah…"

    #--- Monologue 1

    "Saying those things brought me back to the real gravity of the situation;{w=[q]}
    as if in that brief moment I had forgotten why I was here in the first place."
    
    "It was comforting that even though she knew who I was,
    she still spoke to me so casually."

    "Everyone in the court always tensed up when speaking to me."

    "The women stayed away from me."

    "All the men wanted was to court me."

    "Everyone else dared not to even meet my gaze."

    "The only people I could find comfort in were those closest to me.{w=[s]}
    Only ever to Alexei and Mother."

    "If this whole ordeal didn’t happen,
    would I have had a good relationship with my sisters too?{w=[q]} Maybe even father?"

    "Maybe that could’ve quelled the loneliness I felt in that court."

    "I feel ridiculous again.{w=[q]} They’re dead now, nothing I could say or do could change that."

    "I only think about myself.{w=[q]} Even now all I think about is how those people would perceive me."

    "I have to keep reminding myself that they’re dead.{w=[q]} I have to ensure that their memories will live on with me."

    "That’s the only way to do it, right?{w=[q]} That’s grieving?"

    "But why do I not really…{w=[s]} feel anything?"

    show trina at hide_L
    with moveinright
    show vil_f at hide_L
    show vil_m at left
    with moveinleft

    Vl1 "Oh! Is that the duchess!?"

    Vl1 "The duchess! She’s awake!"

    show vil_f at left_second
    with moveinleft
    Vl2 "Oh! Duchess. It is an honor."

    Vl1 "It is an honor."

    An "H-hello!{w=[q]} Hey wait.{w=[q]} Why are you all kneeling?"

    An "You too, Trina?"

    show vil_f at hide_L
    with moveinright
    show vil_m at hide_L
    with moveinright

    #--- Monologue 2

    "All kneeling, lined up all the way to the center of the village.{w=[q]}
    This was a familiar sight, one that I saw everytime I came with my
    family to certain villages and cities for whatever business."

    "There, in the center, was a stage made of wood."

    "It looked like the gallows."

    "I could hear them breathe with each step.{w=[q]}
    A minor gasp, then a vocal recognition.{w=[s]} An excitement that dwells upon them."
    
    "The wooden steps felt like they would give way with each step, so did the stage itself."

    "It could be that the beating of my heart added weight to me."

    "They all stood up in front of the stage and stared, expectant of my words."

    show ana at center
    with moveinright

    An "U-uhm.{w=[q]} Good evening, everyone! As you may know, I am your Duchess Anastasia Konstantin."

    An "As you all may know by now, my family was slaughtered by the revolutionaries that occupied this empire."

    An "In their final musings, my father wished for the wellness of all people."

    An "For all of us to remain safe and healthy.{w=[q]} Even those that dared to draw their blade at him."

    An "This shows his resilience and integrity as a servant of the people."

    An "As well as his mercy for those that dared wrong him."

    An "Remember his words, that they may ring true to the depths of your soul!"

    An "My mother wished for all of us to be better people."

    An "One capable of forgiveness and advancement."

    An "Such that we end the cycle of violence that plagues our nation, and the world itself."

    An "My sisters…"

    An "They were grateful for their life and wished for the people to have enjoyed all that they have enjoyed."

    An "And my brother, Alexei, wishes to have served all of you."

    An "As the only remaining member of the royal family,
    it is my solemn duty to serve all of you, as my father once had."

    An "I will assist in the Rite of Welcoming the Saints.{w=[q]}
    However, I must ask for assistance from you as well."

    An "The empire is no longer safe for me.{w=[q]}
    Even now I fear for my safety here, as well as everyone else’s."

    An "If you will, please assist me in taking the first train
    to the neighboring country by tomorrow morning."

    An "Make no mistake, I am not giving away the empire."

    An "By my name, it shall stand."

    An "But I must do it with the assistance of others, as my father had taught me."

    An "Please, understand."

    #--- Monologue 3

    "Every word I let out was a lie.{w=[q]} It should be obvious.{w=[q]}
    I only ever saw them get executed.{w=[q]} But it should be enough to rile up the hearts of people.{w=[q]}
    Especially those who found their continued existence thanks to us."

    "But still, it felt wrong to have lied to these people to garner sympathy."

    "Even if that was what my mother taught me to do."

    "Lies, lies.{w=[s]} Tiny little lies, expressed enough would be true.{w=[q]}
    As truth itself is nothing more than confirmation bias,
    whatever one believes is true, is true.{w=[q]}
    Of course, such a thing doesn’t apply to things we have no control over."

    "Like nature itself, or how we ought to be perceived."

    "It had been 2 seconds since I finished my speech."

    "Two-hundred and eighty-two eyes stared at me."

    "Right into my soul."

    "A pit has opened inside my stomach.{w=[q]}
    It wanted to rip me apart for saying the things that I said.{w=[q]}
    In the same vein, they would want to rip me apart for lying to them."

    "But I just stood here.{w=[q]} Frozen."

    "Waiting to be devoured."

    "Then, bullets whizzed by."
    
    play sound "Gunshot3.ogg"
    with vpunch
    ""

    An "Eek!"

    play music "Sample2.ogg" loop
    show ana at right
    with moveinleft
    show rev_L at left
    with moveinleft

    Rv1 "THERE SHE IS! GET HER!"
    play sound "Gunshot2.ogg"
    with vpunch

    show rev_L at hide_L
    with moveinright
    show vil_m at left
    with moveinleft

    Vl1 "Duchess! Come down here now!"

    An "Hey, what are you doing? Why are you pulling me down?!"

    Vl1 "We’re going to keep you safe."

    show vil_f at left_second
    with moveinleft

    Vl2 "Please! Go to the cave! The saints will keep you safe."

    An "But what about you?"
    
    Vl2 "So long as you’re safe, we will be too."

    Vl2 "Please.{w=[q]} Run."

    show ana at hide_R
    with moveinleft
    show vil_m at hide_L
    with moveinright
    show vil_f at hide_L
    with moveinright
    show rev_L at left
    with moveinright

    Rv1 "The villagers are fighting back!"

    show rev_R at right_flip
    with moveinright

    Rv2 "Fools!"

    Rv2 "Hopeless fools…"

    Rv1 "What do we do, sir?"

    Rv2 "It doesn’t matter what we do.
    Find the Duchess and gun down anyone that tries to pull you away."

    Rv2 "We mustn't let her get to the cave."

    show rev_L at hide_L
    with moveinright
    show rev_R at hide_R
    with moveinleft

    stop music
    jump chapter_two