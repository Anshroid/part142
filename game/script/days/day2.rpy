label day2:
    call screen calendar(2) with fade

label day2morning:
    play music main

    show screen top_right_ui(2, "Morning")
    scene entrance day
    with fade

    Y "{i}It's a new day, I hope to breeze through lectures and make it to lunch!{/i}"

    show naoto happy glee with dissolve
    N "Oh good morning! Didn't expect to see you so early!"
    show naoto neutral none
    N "I don't actually have any lectures or classes now. I'm just here early to be on patrol."
    
    menu: 
        "patrol?":
            pass
        "What exactly are you \"patrolling\" for?":
            pass

    show naoto disgust sigh
    N "Looking out for weapons, drugs, fire extinguishers, anything that can be harmful that I have to flag up to councillors in our school for the students safety."
    N "I heard we have to do this because well incidents happened at another school, an academy if I recall."
    
    show naoto -sigh

    menu:
        "I don't think that's ever happened before.":
            show naoto neutral
            N "You're right, but it could."
            show naoto happy
            N "If not here then in another universe. hehe-"
        "I think I heard about that. Something about an obsessive high love?":
            show naoto fear
            N "Yes, that story."
            show naoto fear
            N "I wonder if that guy is still out there. I don't think his crush ever even found out about him, allegedly."
            N "Or maybe he's too traumatised to talk about it."
            N "Or maybe it didn't happen at all and it's some weird paradox..."
    
    show naoto neutral
    N "Oh my apologies. I should be more focused on this patrol of course."

    "{i}…! (foot step noises){/i}"
    Y "{i}I see miku rushing past-{/i}"

    show miku fear at right with dissolve
    show naoto fear exclamation
    N "Miku? A-are you okay?"

    show miku serious
    M "I'm fine!"
    show naoto neutral none
    N "You look a bit panicked."
    show miku neutral
    M "I'm fine. Really, I am."
    show naoto neutral
    N "Miku, you can speak to me."

    M "I will, naoto, I will speak to you both at lunch."

    show naoto fear question
    N "Is it something serious?"

    M "Anything serious has been settled now."
    show naoto -question

    N "A-are you sure?"
    
    show miku embarrassed
    M "You worry for me too much, naoto."
    show naoto embarrassed
    N "Sorry I didn't mean it like-"
    show miku neutral
    M "No, it's fine! I guess your worry for me has grounded me a bit hehe-"
    show naoto neutral
    M "Anyways, I have duties to fulfil. I will be seeing you both later in the club room."

    hide miku with dissolve
    "{i}Miku runs off...{/i}"
    
    N "…"
    
    menu:
        "That was a lot of emotions all at once-":
            show naoto neutral
            N "Miku is like that sometimes. When she's stressed she always expresses it, but she thinks she doesn't. I've seen it many times being in the school council and all."
        "Is she okay?":
            show naoto disgust
            N "She is. Maybe? Truthfully I don't think so but she thinks she's got it together."

    show naoto neutral
    N "regardless, we will find the cause of her problems later."
    N "I'd love to talk still but again, I'm on patrol."

    show naoto sparkles
    N "I'll be seeing you!"
    
    hide naoto with dissolve
    "{i}Naoto walks off...{/i}"
    Y "{i}I should get heading to my first class now.{/i}"

label day2lunch:
    scene classroom day with fade
    show screen top_right_ui(2, "Lunch") with Dissolve(2)

    scene roof day
    show scara neutral at r51
    show miku happy at r52
    show naoto neutral at r54
    show lyney neutral at r55
    with fade

    M "Thank you, everyone, for gathering!"

    "{i}There's a slight bit of tension in the air.{/i}"

    S "Psstt-"

    Y "?"

    S "Jack, where's Cyno?"

    "{i}We both look around for him.{/i}"

    play sound running
    $ renpy.pause(4)

    show cyno neutral at r53 with dissolve
    C "Relax, I'm here."
    show miku fear
    M "Cyno! Is everything okay? Did the hospital say anything about it?"
    show cyno embarrassed
    C "Yea, yea Ms Student Council president. I'm fine."
    show lyney fear exclamation
    L "Cyno, what happened to your face?"
    show naoto fear exclamation
    N "Yea, and did miku say you were in the hospital??"
    show cyno happy sparkles
    show naoto -exclamation
    show lyney -exclamation
    C "I'm loving the attention today!"
    show scara disgust
    S "Okay, don't get too cocky."
    show miku neutral
    M "It is what I wanted to talk about though."
    M "But first me and Cyno would need to catch you up on the events that happened last night."
    show cyno disgust sigh
    C "Am I supposed to say this?"

    stop music fadeout 1.0
    
    scene black
    hide screen top_right_ui
    with fade

    C "well…"

    scene room cyno night
    show screen top_right_ui(1, "Night")
    with fade

    ">> Cyno's apartment: last night"

    show cyno fear exclamation with dissolve
    C "!"

    queue music tense

    show cyno neutral none
    C "why does it suddenly feel so light..."
    show cyno sad
    C "My head.."
    C "…"

    play sound "<from 0 to 4.6>sfx/phone.mp3"

    $ renpy.pause(4.5)

    M "Cyno?"
    C "Miku…"
    M "Cyno? What's wrong, why do you sound like that?"
    show cyno fear
    C "I feel like … I can't feel…"
    C "anything…"
    M "What? Are you in bed, is this some sort of sleep paralysis?"
    show cyno disgust
    C "No its just.."
    C "I'm moving, I just-"
    show cyno fear
    C "Just don't feel anything."
    C "It's like my body is moving by itself!"
    M "Did you do something that could have damaged a nerve or something?"
    C "It was so sudden, I just-"
    
    show cyno exclamation
    C "!"

    hide cyno
    play sound falling

    M "Cyno?"
    M "Cyno?!"
    M "ARE YOU OKAY? ARE YOU STILL THERE?"
    M "It can't be… what's going on with him?"
    M "CYNO I'M CALLING AN AMBULANCE!"

    stop music fadeout 1.0
    queue music main

    scene roof day
    show screen top_right_ui(2, "Lunch")
    show scara neutral at r51
    show miku neutral at r52
    show cyno neutral at r53
    show naoto neutral at r54
    show lyney neutral at r55
    with fade

    show cyno neutral
    C "So yea, the end."

    show lyney fear exclamation
    L "What? Are you okay?"
    
    show miku serious
    M "I called him an ambulance but he was conscious by the time they arrived."
    show miku angry vein
    M "I still had to persuade him to go to the hospital to at least get checked, even if it was pointless."
    
    show lyney neutral -exclamation
    show cyno neutral sigh
    C "Well, I'm fine now… mostly."

    show cyno -sigh
    show scara neutral
    S "Okay I get that, but why are we gathered here then?"

    show miku serious none
    M "Because, this isn't a one off case."
    M "Not just with Cyno, but with others as well."
    M "And every time Cyno visits the hospital, the same results arrive."
    M "Physically in perfect condition."

    show cyno embarrassed sparkles
    C "I mean, I don't mean to boast with those results-"

    show scara disgust vein
    S "Right.."

    show scara neutral none
    show cyno neutral none
    
    show naoto neutral question
    N "So you are saying Cyno and others have all experienced episodes like these without any medical explanation?"
    
    show miku neutral
    M "Exactly."

    show naoto neutral -question
    show miku serious
    M "And there's more to it as well."

    show cyno neutral
    C "Each week, each day, more and more stories are being reported."
    C "Strange phenomena have been occurring all around us."
    C "And it's not just the children's story book stuff."
    C "there have been many other reports of people experiencing full mental shutdowns, and this seems to be happening anytime and anywhere, but only so many are affected, like me."

    show miku neutral
    M "hm, and yesterday, I managed to catch a rumour from the faculty that our principal sheldon lee cooper didn't leave campus until 3am."
    M "The staff noticed he printed out tons of 'exam papers' with literal gibberish on them, we don't even have exams until next semester!"

    show cyno neutral
    C "and don't forget eepy, the founder of the university. He's been missing for a few days now, the police don't have any clues either."
    show cyno fear
    C "other sources even state the dancing plague of 1518 is back!"

    show scara angry
    S "…"

    show miku disgust sigh
    M "That last part wasn't true.."

    show cyno happy
    show scara disgust
    S "would make your story sound more credible!"
    show miku angry
    show cyno neutral
    M "Well we aren't joking!"

    show scara neutral    
    show miku serious none
    M "This issue has been slowly unravelling itself and integrating into peoples lives."
    show miku fear
    M "but it goes beyond that."
    show miku serious
    M "its easy for us to call these things supernatural, but maybe don't look at it literally like that."
    M "memory, cognition, etc, they're fragile and largely unknown. Even science is still trying to define how important they are."

    show miku fear
    M "so what if these events aren't just mere coincidences or 'anomalies'?"
    show naoto fear
    N "Miku, what are you trying to say?"

    show miku serious
    M "think about it, it's kind of like cracks in one large system that we're all a part of and as we all know, we are all in this together."
    M "Not to mention we are also members of one body AND we are responsible for eachother. and I could be exaggerating BUT I think we are breaking free." 
    M "Persona! Wake up get up get out there, even."
    M "Or whatever they say, I don't dance."

    show naoto fear
    N "Are you okay."
    M "I mean, I don't know but at this point it's way beyond a coincidence!"

    show lyney neutral sigh
    L "Well.. I get what you're saying but I'm struggling to link everything together."

    M "With the sheer amount of these occurrences, I can't help believe that all of this is connected."

    show naoto neutral
    N "sometimes, our brain links things that aren't related, I wouldn't put that thought past us."
    
    show miku disgust sigh
    M "hmm yess well.."

    show cyno neutral sparkles
    C "don't worry miku."
    show miku neutral -sigh

    C "what links all of them is that they contradict basic logic."
    C "Take for instance, me. Last night, I could tell I was losing control of myself, and at the same time I was also gaining these weird memories that are difficult to make out, but I know at the time they felt so real."
    C "what should be a straightforward record of events has become quite the opposite. The contradictory nature of it all is the only thing that is consistent."
    C "One could obviously continue dismissing things like this as psychological breaks or urban myths. however in this case, I'm not so sure."

    show cyno -sparkles
    show naoto neutral
    N "So what do you think actually links this all?"
    show scara neutral
    S "It seems this conversation is too complex for anyone to comprehend."
    show miku angry
    M "I mean we are getting somewhere.."

    show miku neutral
    show lyney neutral question
    L "Do you not believe in the supernatural, scara?"
    show scara neutral
    S "I mean I do to some extent..."
    show scara disgust
    S "but certainly not in this context-"
    show lyney happy sparkles
    L "Well, sometimes you just have to believe, yknow? And just like that, the theories will all start to make sense!"
    show scara angry
    S "what? I'm not turning into some conspiracist if that's what youre suggesting."
    
    show lyney neutral none
    show naoto neutral
    show scara neutral
    N "well, I don't necessarily believe in the 'supernatural' existing."
    show naoto neutral
    N "But I can admit I don't know enough about the universe to doubt any possibility."
    show lyney neutral
    L "then perhaps we could come to a more decisive conclusion if we understood how this condition that people are experiencing works a little better."
    show scara neutral
    S "I don't hate that approach."
    show miku neutral sparkles
    M "that's it! we will set out and look for evidence!"
    show scara angry
    S "Don't get over your head miku, we don't even know where to start!"
    show miku  neutral
    M "But we have a plan of action now!"
    show miku neutral glee
    M "We can investigate this issue, find some convincing evidence to provide our argument, test our theories, before finally coming to a conclusion!"
    show miku happy
    M "a conclusion that will reveal the truth behind what's exactly happening to us."
    show naoto neutral
    N "the truth…"
    show miku neutral
    M "mhm! Even though we might just be some undergrads in university, that doesn't mean anything to me."
    show miku neutral
    M "these leaders… these scientists, they're failing us right now, so I say we need to step up while no one else will."
    show miku neutral
    M "And with a set motif for what we do, you want to know what that makes us?"
    show cyno question
    C "Uhmmm.."

    show cyno -question
    show miku neutral
    M "A club!! We will be the… uhh… "
    show miku happy glee
    M "The supernatural investigation club!"
    
    show miku -glee
    show lyney happy
    L "Well that sounds fun! Count me in!"


    show scara disgust
    S "…"
    show scara angry
    S "augh fine. Only since I have nothing better to suggest!"
    show miku neutral question
    M "and what about you, new guy?"
    
    menu:
        "I will be a seeker of truth!":
            show miku happy glee
            M "that's what I like to hear!!"
        "is this voluntary or paid?":
            show miku neutral none
            M "I'll slip you 10 quid at the end of the week."
            show naoto disgust
            N "as long as ur not embezzling council funds…"

    show miku none    
    show naoto happy
    N "well, I'm just glad we've come to an agreement, not just for cyno but for everyone who's under the influence."
    S "I think that's not the right use of that phrase.."
    show naoto neutral
    N "though what scara said earlier was right, we do need a good starting point."
    show lyney neutral
    L "We can start by compiling everything we know at the very least."
    show miku neutral
    M "and then from there we have a good starting point. We can then set out tomorrow to research and find a lead on what connects this all."
    show miku neutral sparkles
    M "Sounds like a plan, right guys?"
    menu:
        "no":
            show miku neutral
            M "well shut up you don't get a say anymore-"
        "before we get too deep into anything, cyno just to be clear you don't have a last name? ":
            show cyno angry vein
            C "Bro."
        "ok":
            show cyno embarrassed
            C "Yuh."

    show miku none
    show cyno neutral
    C "I presume this also counts as medical research?"
    show lyney disgust
    L "Not directly, but I guess we are researching… you?"
    show cyno angry
    C "Don't put it like that."
    show lyney fear
    L "What?! But you were the one who said so!"

    "{i}Scara turns to me.{/i}"

    show scara disgust
    S "Tch.."
    show scara embarrassed
    S "You all are so weird."
    
    "{i}we spend the rest of lunch compiling information as the newly formed supernatural investigation club.{/i}"


label day2afternoon:
    scene entrance evening
    show screen top_right_ui(2, "After School")
    with fade

    call hangout from _call_hangout

    call dayend from _call_dayend_1

