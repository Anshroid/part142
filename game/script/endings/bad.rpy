label badending:
    queue music sentimental
    
    show cyno fear
    C "?!…"
    show miku serious question
    M "…you,, you really think so?"
    show miku sad none
    M "everything we did… what was it all for then?"
    show scara happy glee
    S "see? Now have you finally got it in that head of yours?"
    show miku angry vein
    M "JUST SHUT UP SCARA!"
    M "THIS ISNT ABOUT ME OR YOU RIGHT NOW."
    show scara disgust none
    S "…tch."
    show cyno sad
    C "this is… quite a harsh reality to come to terms with. I have very few words."
    show naoto neutral
    N "if that is what you really believe, then I have no choice but to accept it as fact."
    show naoto sad
    N "though I must say, I'm a little disheartened by your conclusion."
    show lyney sad
    L "you guys… this isn't fair-"
    show lyney sad
    L "…actually, maybe it is."
    show lyney sad exclamation
    L "but even so, if this is really the case, I don't want to have to pretend as if nothing special happened between us."
    show lyney sad question
    L "miku… you said you'll forever treasure the club… the connections we made… right?"
    show miku serious sigh
    M "…"
    show lyney fear none
    L "m-miku?"
    show miku sad none
    M "…please stop, lyney."
    show lyney fear exclamation
    L "!!"
    
    Y "…"
    
    show cyno neutral
    C "this is… strange. after all the time we've spent the past week, it only took this choice to break each of our convictions."
    show lyney sad none
    L "c'mon… you know that's not true…"
    show naoto neutral sigh
    N "I appreciate you for trying, but we don't need your false optimism right now."
    show lyney fear
    L "that's not… w-what?!"
    show naoto neutral none
    N "we find ourselves in a situation where we have turned our backs away from the truth, albeit potentially flawed."
    show naoto sad
    N "the only solace I'm able to welcome in this moment is,, some time to reflect… on my own."
    show miku fear
    M "wait… you're leaving?"
    show naoto neutral question
    N "yes, is there a problem?"
    show miku sad
    M "no… it's just, we have a mandatory student council meeting after school."
    show naoto disgust none
    N "then authorise my absence, would you?"
    show miku serious sigh
    M "hm,, alright."
    show cyno sad
    C "so… this is it then?"
    show miku serious
    M "what do you mean?"
    show cyno angry
    C "what do you mean what do I mean, don't try and dodge the bullet. It's over now, isn't it?"
    show miku fear
    M "cyno… I-"
    show lyney disgust
    L "guys, save this for after our exchange student's gone. after all, we still have yet to say goodbye to him."
    show miku serious question
    M "ah, I almost forgot! you'll be taking the train, right?"
    show miku neutral none
    M "then I guess we'll see you at the station before you leave."
    
    "{i}one by one, everyone exits the rooftop and heads back inside the building.{/i}"

    if chosen.name == "miku":
        show miku serious
        M "hey…"
        show miku serious question
        M "remember that time underneath the cherry tree? I told you a lot of things I wouldn't usually tell anyone."
        show miku serious none
        M "in that moment, I thought that I could finally have someone to depend on unconditionally."
        show miku disgust
        M "but right now, it feels like something I can only dream of again. Maybe its for the best… I don't know, its just hard to tell at this point in time."
        show miku sad sigh
        M "I hope that somebody you'll reflect on our times together and realise that it wasn't all meaningless. Not to me at least."
    
    hide miku with dissolve

    if chosen.name == "lyney":
        show lyney sad
        L "well, it appears that the show took an impromptu end."
        show lyney sad
        L "the magic behind it all feels dim, as if you successfully pulled the curtains off and revealed everything… for nothing."
        show lyney disgust
        L "I must say, I wouldn't have expected you to go out without a curtain call, or even an encore."
        show lyney neutral
        L "no hard feelings, but next time I might not let my naivety get the better of me."
    
    hide lyney with dissolve

    if chosen.name == "naoto":
        show naoto neutral question
        N "may I have a word before I take my leave?"
        show naoto neutral none
        N "back when we were investigating the insane asylum, I thought I could sense a lot of determination within you."
        show naoto embarrassed
        N "I suppose that I was wrong. Maybe it was too much for me to think you'd bring this case to justice."
        show naoto disgust sigh
        N "instead, you've chosen the exact opposite."
        show naoto angry none
        N "and like you, I'll try to do the same. But I can't say I'll forgive you it."
    
    hide naoto with dissolve

    if chosen.name == "cyno":
        show cyno sad
        C "partner…"
        show cyno neutral question
        C "you know I don't open up easily, that's why we had to play that card game, remember?"
        show cyno neutral none
        C "although when I did, I had this expectation that I'd feel seen… somehow."
        show cyno sad
        C "I was pretty stupid for thinking that mattered, huh…"
        show cyno neutral
        C "try not to worry, I'll get over it, and you should to."

    hide cyno with dissolve

    Y "before I head off, I notice scara remain in his place, looking at me. He has not moved."

    show scara neutral
    S "look, I'll be the one to say it, you did what you had to."
    show scara happy glee
    S "that kind of realistic outlook commands my respect."
    show scara neutral none
    S "I'm not gonna congratulate you, just be relieved that things didn't end up worse than they already are."
    S "just remember, you did the right thing… "
    show scara neutral
    S "…probably."
    
    Y "…"
    
    show scara neutral
    S "well then. I suppose we're done here."
    
    "{i}Scara turns and walks away without looking back.{/i}"

    scene black with fade
    
    Y "{i}my time as a exchange student is now over.{/i}"
    Y "{i}it's now evening, I prepare to head for the station.{/i}"

    queue music train_ambience

    scene station
    show naoto at r51
    show miku at r52
    show cyno at r53
    show scara at r54
    show lyney at r55
    with fade
    
    Y "{i}everyone's standing by the platform, waiting for me to leave.{/i}"

    show miku serious
    M "there you are…"
    show miku neutral
    M "I wish you didn't have to leave so soon, if only that-"
    show naoto neutral
    N "miku, remember what we talked about."
    show miku sad sigh
    M "hm. Well, all I can say is that it was over too quick."
    show miku serious none
    M "I only wish I had more time to get to know you."
    show scara disgust
    S "normally the exchange students we get are real stuck ups."
    show scara happy
    S "but I'll admit, you were a nice change."
    show lyney neutral question
    L "hey, you will visit, won't you?"
    show lyney embarrassed none
    L "…please?"
    show lyney sad
    L "if only, its going to get quite boring without you."
    show naoto neutral
    N "be sure to take good care of yourself when you get back."
    show cyno neutral
    C "…"
    show cyno neutral
    C "you helped us out a lot, so thanks."
    show cyno sad
    C "I'm not very good at farewells, so, uh… ahem. Bye."
    
    Y "{i}I nod at them before heading inside the train.{/i}"
    
    "{i}not long after, the train departs, the others quickly turn and exit the station.{/i}"

    stop music fadeout 1.0

    scene black with fade

    Y "{i}…{/i}"
    Y "{i}just like that, I left the university and travelled back to the place where I had come from.{/i}"
    Y "{i}the supernatural investigation club disbanded with immediate effect…{/i}"
    Y "{i}and the members never got into contact with each other as they once did…{/i}"
    Y "{i}nor did they once attempt to speak to one another about what they had experienced that week.{/i}"
    Y "{i}those so-called “weird occurrences” still continued, though this time everyone turned a blind eye to it.{/i}"
    Y "{i}despite this, life on campus quickly returned to its natural ebb and flow, like nothing strange had ever happened…{/i}"
    Y "{i}Miku buried herself in piles of documentation, lyney's charm became just another performance for strangers…{/i}"
    Y "{i}naoto's resolve crumbled and was soon kicked out of the council, and Cyno lost who he thought were his friends, later becoming an inpatient for life.{/i}"
    Y "{i}looking back, I'm not so sure if the “closure” that followed from my absence was an act of safety, or proof of my dismissal.{/i}"
    Y "{i}…{/i}"
    Y "{i}I'm sorry.{/i}"
    
    ">> {i}you have reached the bad ending.{/i}"

    $ renpy.set_return_stack([])
    return


# scara cyno naoto lyney miku sparrow