label chapter_five:
    $ renpy.choice_for_skipping()
    play music "Sample2.ogg" loop
    hide palace_artroom
    hide palace_painting
    hide trina_w
    hide ana
    hide ana_w
    show palace_baseopened
    show trina_w at left
    show ana_w at right
    with fade

    An "T-thank you, Trina.{w=[q]} I’m sorry."

    Tr "Are you alright?"

    Tr "You stopped there so badly, I was worried."

    Tr "What did you even see?"

    An "What?{w=[q]} You didn’t see anything?"

    Tr "No.{w=[q]} That entire room was dark, that’s why I was so worried."

    Tr "Did you see anything?"

    An "Yes…{w=[q]} I think I saw something I shouldn’t have."

    Tr "..."

    $ renpy.choice_for_skipping()
    menu:
        Tr "Will you be alright if you tell me about it? Or do you want a time off?"

        "Tell her":
            $ good_ed += 1
            jump chapter_five_tell

        "It's better if she doesn't know":
            jump chapter_five_quiet

label chapter_five_tell:
    An "It’s…{w=[q]} there were paintings there. Portraits!"

    An "They were family portraits."

    An "Of the previous and current royal families."

    An "I was there, but…"

    An "The other portraits…{w=[q]} their youngest daughters."

    An "They were gone…"

    An "What does it mean, Trina?{w=[q]} I don’t…{w=[q]} I don’t understand."

    Tr "Calm down, calm down."

    Tr "I don’t know either…"

    Tr "I don’t know the answer to everything."

    Tr "But whatever it is, we’ll get through it."

    Tr "We promised, right?{w=[q]} So please calm down."

    "Despite the kindness of her words, the idea overwhelmed me."

    show ana_s at right
    hide ana_w

    An "Was I…{w=[q]} to be sacrificed?{w=[q]} Was that the point of me being here?{w=[q]}
    Was that the point of my existence?"

    Tr "Even if it was, I won’t let them do that."

    Tr "Even if I were to jump in front of a hail of bullets."

    Tr "Or be stabbed to let you escape."

    Tr "I promised to protect you, duchess.{w=[q]} That will be upheld."
    
    show ana_w at right
    hide ana_s

    An "But why?"

    An "We just met.{w=[q]} What’s the point?{w=[q]} Couldn’t you run away instead?"

    show trina at left
    hide trina_w

    Tr "I could.{w=[q]} But if I ran away, where would I go?{w=[q]}
    I take one step out of the cave, and I’ll get shot."

    Tr "I could try to find another way out of the cave, and if I’m not able to, I’ll starve to death."

    Tr "Even if I do get out, I probably won’t last long in the wilderness."

    Tr "It’s not like I have the privilege of escaping the empire via train."

    Tr "Protecting you is the most privileged I’ll ever be,
    it’s the last thing that will give my life purpose."

    Tr "If you were to die during it, I would never forgive myself.{w=[q]} Then, I’ll die."

    Tr "If I were to die during it, you may forget about me, but you might be fine."

    Tr "I may not be able to see the western lands."

    Tr "But…{w=[q]} that’s good enough for me."

    An "..."

    An "You’re right…{w=[q]} I’m sorry for losing myself like that."

    An "It wasn’t elegant of me."

    An "But I don’t want anyone else dying for me.{w=[q]} So please, try not to sacrifice yourself."

    An "Please…"

    Tr "I can’t promise that.{w=[q]} But let’s try to live as much as possible ‘til the end."

    An "That’s good enough…"

    jump chapter_five_part2

label chapter_five_quiet:
    An "I'll be fine"

    An "There were just things there that you would rather not know."

    An "Maybe once we get out of here, I’ll tell you."

    An "I’m sorry."
    
    show trina at left
    hide trina_w

    Tr "It’s alright."

    Tr "Whatever it is, I’ll wait until you’re well enough to tell me."

    Tr "Let’s try to get through this place first."

    jump chapter_five_part2

label chapter_five_part2:

    "We went around the room, and noticed that the door to the basement was now opened."

    show trina_w at left
    hide trina

    "A terrible darkness seeped out of it."

    "But there was something there that was urging us to go in."

    "A waltz.{w=[q]} The sound of feet clashing against the floor.{w=[q]} Ballroom music."

    An "Should we go in?"

    Tr "I’m not sure…{w=[q]} but it’s better than nothing."

    An "At least we won’t be trapped in an endless hallway, right?"

    Tr "Yeah…{w=[q]} haha."

    "We approached the basement door, and entered it."

    play sound "Walk.ogg"
    hide trina_w
    hide ana_w
    show palace_ballroom
    show trina_w at left
    show ana_w at right
    with fade

    "Inside, a space that was impossible to exist.{w=[q]} But from all that we’ve seen, it hardly even matters."

    "The dancing came from the nobles, lit up by large chandeliers, yet some hidden behind the shadows.
    They were engrossed in their own selfishness."

    "Like all nobles were."

    "At the end of the hall, there it was."

    "The Saint’s Altar."

    "The blood of sacrificed animals swelled from it.
    All the more obvious as we approached it, little by little."

    "Then we stood before the pool of blood, our selves reflected back at us from its crimson hue."

    Ax "Do you understand?"

    show trina_w at right_flip2
    with moveinleft

    An "Alexei…"

    show alx2 at half
    play sound "Breath.ogg" volume 3.0
    with fade

    Tr "Who...?"

    Tr "Oh…{w=[q]} it’s something I can’t see, huh?"

    An "Tell me what you see, Trina."

    Tr "The room is clearly lit up.{w=[q]} This pool in front of us, is this blood?"

    An "Yes.{w=[q]} Is that all?"

    Tr "Yes."

    An "I see…{w=[q]} Yes, Alexei, I understand."

    An "You wanted to show me all of this."

    An "As the face of nobility, of royalty itself.{w=[q]} You wanted to show me why I exist."

    An "To be the sacrificial lamb."

    "Alexei looked at me with pity behind that unreadable face.{w=[q]} But I could hear it in the silence he let out."

    Ax "No…{w=[q]} she is."

    show ana_s at right
    hide ana_w

    Ax "She was always supposed to be the sacrificial lamb."

    An "Then why aren’t they there?{w=[q]} Where did those youngest daughters go?{w=[q]} Where will I go?"

    Ax "They sacrificed themselves…{w=[q]} for their peasant."

    Ax "They all believed they could change the fate of peasant
    society if they were to sacrifice themselves instead."

    Ax "But they weren’t.{w=[q]} They were continuing a cycle of idiocy, do you not understand?!"

    An "No!{w=[q]} I do!"

    An "I know why…{w=[q]} they would do that."

    Tr "Ana…?"

    An "I don’t want any more people dying for me, Alexei."

    Ax "And then what, sister?"

    Ax "A noble blood being sacrificed…{w=[q]} a new dynasty will be put up."

    Ax "In a few hundred years they will be replaced."

    Ax "Over, and over again."

    Ax "Sacrifice the peasant!{w=[q]} Our lineage will carry on forever!"

    Ax "We will live again."

    Ax "And everything will be alright."

    Ax "Do you remember what our mother asked you?"

    Ax "What I asked you?"

    An "If…{w=[q]} given the choice--"
    
    An "No, if I can.{w=[q]} Will I change the plight of the commoners?"

    Ax "One for the many, or all of us for one?"

    An "When you both asked me that, I didn’t understand what kind of power I held."

    An "Nor whether or not I had a decision in the first place."

    An "I was confused, scared even.{w=[q]} Scared that I had a responsibility that was beyond me."

    $ renpy.choice_for_skipping()

    default good_ed_option = False

    if good_ed == 3:
        $ good_ed_option = True

    menu:
        An "But I understand it now, what I must do."

        "For Trina":
            jump chapter_five_tr

        "For everyone":
            jump chapter_five_ana

        "For me" if good_ed_option:
            jump chapter_five_good

label chapter_five_tr:

    show ana_w at right
    hide ana_s 

    An "Trina.{w=[q]} Push me down."

    Ax "You never changed.{w=[q]} No, this empire will never change."

    Ax "Selfishness will always rule our heart."

    hide alx2
    with fade
    show trina_w at left_flip
    with moveinright

    Tr "Ana, what are you talking about?{w=[q]} No way I’m pushing you down there."

    An "Trina, please."

    An "This is my destiny.{w=[q]} This is what I’m born to do."

    An "You understand, right?{w=[q]} We’re trapped as what we are?"

    An "You will always be a peasant, and I will always…"

    An "I will always try so hard."

    An "To not be me.{w=[q]} But to no avail."

    An "The both of us will struggle, but it’s futile."

    An "We’ll always just be who we are."

    Tr "I refuse to believe that."

    Tr "Why would you think I would believe such things coming from you?"

    show trina_s at left
    hide trina_w

    Tr "You’re not like the others, right?{w=[q]} You were…"

    show ana at right
    hide ana_w

    An "Trina.{w=[q]} This is an order from your duchess."

    show ana_h at right
    hide ana

    An "This is for you."

    An "I’m sorry I said that you will never escape being a peasant.{w=[q]} That was wrong of me.{w=[q]}
    Rather, the fact that you came from so low means you can only go up."

    An "Right? I’m stuck up here.{w=[q]} With a role determined by the cosmos."

    Tr "For me…?"

    Tr "This isn’t for me."

    Tr "Losing you isn’t for me."

    Tr "Where would I be once you’re gone?"

    An "I don’t know, but probably better than where you are now."

    "I hold her wrist and put it on my shoulders.{w=[q]} She hesitated, her hands trembling.{w=[q]}
    And the more I urged her, the more she refused to do so."

    Tr "Don’t…{w=[q]} stop this.{w=[q]} We can get out of here, we can find another way."

    show ana at right
    hide ana_h

    An "There is no other way."

    An "Trina, this is my order to you.{w=[q]} As your duchess, as the one whom you serve directly under."

    An "Push me down."

    Tr "Please!"

    show palace_ballroom_trina
    with fade

    "Her push was light, the lightest it ever felt, and yet it was enough to send me down the pool of blood."

    "It hurts."

    "It hurts. It hurts. It hurts. It hurts. It hurts. It hurts. It hurts. It hurts. It hurts. It hurts.
    It hurts. It hurts. It hurts. It hurts. It hurts. It hurts. It hurts.It hurts. It hurts. It hurts."

    "And yet..."

    Tr "Ana… I’m sorry.{w=[q]} I’m sorry.{w=[q]} I should’ve, I should’ve pulled you away.{w=[q]}
    We could find another way."

    "She was trying to pull me up.{w=[q]} Yet the blood had grasped me fully.{w=[q]}
    I was never going to leave this pool alive."

    "She leaned over the pool, her hands reaching for my face,
    the only thing not yet submerged beyond the crimson darkness."

    "It felt warm."

    Tr "I’m sorry."

    An "Trina…{w=[q]} it’s okay."

    An "Let me feel warm, one last time."

    "The last vestige of her warmth came from her palms.{w=[q]} They held onto my cheeks, they wanted me to live."

    "I wanted to say something, but the pain, and the blood had engulfed me to my mouth."

    "I’m sorry, Trina."

    "I should’ve been a better duchess."

    "A better person for you."

    #lightshow bg

    stop music
    scene palace_hallway
    show trina at right_flip
    with fade
    #palace bg but more ppl

    $ renpy.choice_for_skipping()
    "My name is Trina Yagnenok.{w=[q]} Three days ago,
    I woke up in this palace without any idea of what happened the night before
    Yet it felt as though I had lived here my whole life."

    "Everything was familiar.{w=[q]} The names of the people, the places within and without."

    "But I dare not question it."

    "I may just be losing my mind."

    Nb1 "You there!"

    show mom at left
    with moveinleft

    Tr "Y-yes, m'lady!"

    Nb1 "Go to the third floor.{w=[q]} We need you to clean the portrait room."

    Nb1 "It would be bad if Tsar Raskolnikov would see such a horrendous sight."

    Nb1 "Haah…{w=[q]} coronations are always stressful times."

    Tr "Understood!{w=[q]} I will go right away."

    play sound "Walk.ogg"
    hide trina
    hide mom
    show palace_artroom
    show trina at left
    with fade

    "I hurriedly went upstairs towards the portrait room.{w=[q]}
    Inside this place was the family portraits of the previous dynasties.{w=[q]}
    The tsars that had lived, and their family."

    show trina_w at left
    hide trina

    "Weirdly, despite having never gone here before, it felt too familiar."

    "No, it felt like it was wrong to be here."

    "I quietly cleaned the room, making sure to dust away any particular elements.{w=[q]}
    One thing that always caught my attention in these family portraits were the empty chairs.{w=[q]}
    I always wondered what it meant."

    "Especially in the family portrait of the previous dynasty, the Konstantin."

    "It was large, and at the far end of the room."

    "The empty seat was visible from anywhere, so vivid.{w=[q]} So obvious."

    show trina_s at left
    hide trina_w

    "I feel my heart ache everytime I see it."

    "As if there was someone once there, someone dear."

    "..."

    "But not a single face could pop up in my head."

    "Thus, I continued to clean."

    hide trina_s
    scene black
    with fade
    stop music
    $ renpy.choice_for_skipping()
    centered "End."
    return

label chapter_five_ana:
    stop music
    An "Trina..."

    An "I’m sorry."

    play sound "Hit.ogg"
    hide trina_w
    with vpunch

    "It was a swift motion, yet one of the most difficult that I’ve ever done."

    "Despite all the aching feet, all the swollen muscles, all the chronic pain around my body."

    play music "Sample4.ogg" volume 0.7 fadein 2.0
    "The chill of the palace."

    "To push her down the pool felt painful."

    "It didn’t help that…"

    hide ana
    hide alx2
    show palace_ballroom_ana
    show alx2 at half
    with fade

    Tr "Why?"

    Tr "It hurts."

    Tr "It hurts everywhere."

    "I couldn’t even look at her.{w=[q]} Nor listen to her scream out in pain, nor…{w=[q]} anything.{w=[q]}
    I couldn’t do anything."

    Ax "Thank you, dear sister."

    Ax "You’ve broken the cycle of careless affectation towards those that don’t matter."

    Ax "Lambs should not be given the time of day."

    Ax "Only ever slaughtered."

    Ax "For the greater good."

    Tr "ANAAAAA!!!"

    Tr "WHYYY!!!??"

    "Her screams were getting louder.{w=[q]} I could hear it through my covered ears.{w=[q]}
    She hated me.{w=[q]} The only person that ever saw me past the appearance of a duchess."

    "The only other person that cared."

    "Finally, I glanced at her one last time."

    "Her face melted off of her bones, her body merged with the blood, became part of it, consumed by it.{w=[q]}
    Yet I could still see it, the anger in her eyes."

    "There was a rage in her heart.{w=[q]} Over being betrayed, over being wronged."

    "That rage seeped into the pool like boiling oil.{w=[q]}
    Bubbling and cascading against the altar.{w=[q]} Against everything."

    "And it overflowed."

    "Little by little, more and more.{w=[q]} The once delicate pool of blood had grown with her rage.{w=[q]}
    She yells for which I could do nothing but listen."

    "I yelled in my mind to apologize but I couldn't, it was too late.{w=[q]} I had killed her."

    #[lightshow bg, where it quickly disappears]

    #ballroom bg again, this time show the overflowing blood slowly covering the entire room.
    #Maybe after every other click
    #do it next time, show blood overflowing place bg instead

    Ax "No! What’s going on! This is--"

    hide black
    show black
    stop music
    play sound "Crash.ogg"
    with vpunch

    ""

    "I fell down to my knees and felt the hot oily blood boil through my clothes, through my skin."

    "I wept."

    "I wept and I wept."

    "As her rage consumed everything, and everyone."

    "Until all…{w=[q]} there was nothing left."

    "I’m sorry, Trina."

    "I should’ve been a better duchess."

    "A better person for you."

    $ renpy.choice_for_skipping()
    centered "The end."

    return

label chapter_five_good:

    show ana_w at right
    hide ana_s

    An "I’m breaking this cycle."

    Ax "What!?" with vpunch

    Ax "Do you not understand?!"

    Ax "Do I have to spell it out for you?"

    show ana at right
    hide ana_w

    An "No, Alexei.{w=[q]} I get it."

    An "But I’m sorry."

    An "I think I’m starting to understand things far more than anyone in my place before ever had."

    An "They suffer because of our existence.{w=[q]}
    And in turn, one of us has to suffer far more than anyone ever could."

    An "“Damnatio Memoriae”, to be forgotten in history, as if you never existed in the first place."

    An "I am too selfish to want that for myself."

    An "And at the same time…"

    "My hand held Trina’s, and my eyes fell towards hers.{w=[q]}
    She looked confused, still.{w=[q]} After all, she can’t hear Alexei."

    "For all she knows I’m mindlessly monologuing."

    Tr "What’s…{w=[q]} what’s going on?"

    Tr "Why did you…"

    An "Don’t worry about it."

    An "I’m not going to accept a world where you’re forgotten as well."

    Tr "Thank you…{w=[q]} but…"

    An "Listen to me, Trina."

    An "The nobility sometimes…{w=[q]} no.{w=[q]} They always want to kill you."

    "Trina scoffed."

    Tr "I knew that much."

    An "No, this is worse.{w=[q]} They think they don’t.{w=[q]}
    They think what they’re doing is for the greater good,
    that them partying in their lofty mansions. In their fancy suites…"

    An "All of that is for the good of everyone."

    An "Their delusions have rooted themselves so deep that they believe it to be the truth."

    An "And this altar, this rite, this is the source of their truth."

    An "You said we’re trapped by the circumstances of our birth, right?"

    An "You will always be an impoverished peasant, I will always be a terrible noble."

    Tr "You didn’t have to say it like that."

    Tr "But I suppose.{w=[q]} Where are you going with this?"

    An "We don’t have to exist for them, we can exist for us.{w=[q]} Not for others, not for anyone."

    An "It might not be the best solution but…"

    An "I think that’s the best we’ll ever have."

    Tr "Is that so…"

    Tr "Are you sure you’re alright with that decision?"

    Tr "I still don’t know what’s going on but I can understand glimpses of it."

    Tr "Ana, you don’t have to choose for me."

    An "I’m choosing for myself."

    An "Do you not wish for it too?{w=[q]} To live as yourself?{w=[q]} To not be forgotten?"

    Tr "I wish for it, but will I gain such a wish?"

    Tr "Who am I to receive such a wish?"

    An "You are Trina Yagnenok.{w=[q]} But that is not your full name, is it?"

    Tr "It’s…{w=[q]} Katherine Elizabeth Yagnenok.{w=[q]} My mother picked it for me, 
    she loved how it sounded, and if I’m being honest, so do I."

    Tr "But it’s been long since she died."

    Tr "All she ever gave me was my ability to read, and this name."

    An "Then…{w=[q]} that name will be remembered.{w=[q]} And so will your mother, and so will everyone."

    show ana_h at right
    hide ana

    An "We’ll be okay."

    Ax "This is your decision, then.{w=[q]} For no one to be forgotten?"

    Ax "To let time pass on the eternal empire?"

    Ax "To let it crumble like everything else?"

    An "We’ve been dancing for far too long.{w=[q]} Our legs have gone numb, it’s time for us to take a break, right?"

    An "Let’s go, Alexei."

    Ax "..."

    Ax "My dear sister."

    Ax "I will never understand you."

    An "I will never understand you, and mother, and father, and my sisters."

    An "I shouldn’t have been born here."

    Ax "At least you made me feel like a child."

    Ax "Thank you.{w=[q]} And goodbye.{w=[q]} Don’t forget about me."

    An "I won’t."

    stop music
    hide alx2
    show palace_ballroom_gd
    play sound "Crash.ogg"
    with fade

    "Alexei’s essence slowly faded out of existence.{w=[q]}
    He took with him the splendor that pervaded the ballroom, as the lights slowly went out,
    and the dancers stopped in their tracks."

    "It was dark now, and so unbelievably cold."

    Tr "So what’s your plan, duchess?"

    "The golden pool’s liquid seemed less like blood and more like water.{w=[q]} Purified, clear."

    An "Shall we take a dive?"

    Tr "Heh.{w=[q]} Even after saying all of that, at the end of it, we’re just going to die still, huh?"

    An "At the very least, it’s on our own terms."

    An "That’s more than anyone else could have."

    Tr "I suppose so.{w=[q]} Shall we?"

    An "We shall."

    hide black
    show black
    with fade

    "In the coldness, we embraced."

    "And fell to the waters below."

    "It was warm, and the liquid that flowed into our lungs did not burn."

    "Was it because we breathed into each other, ‘til our consciousness faded?"

    "The light of the moon pierced through the surface."

    "It lit up the abyss below us, as we faded into the darkness."

    stop music
    centered "End."

    return