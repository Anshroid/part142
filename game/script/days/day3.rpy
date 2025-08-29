label day3:
    call screen calendar(3) with fade

image library:
    "bg/library.png"
    zoom 0.5

label day3morning:
    play music main

    show screen top_right_ui(3, "Morning")
    scene entrance day
    with fade

    Y "{i}After yesterday, I should prepare to conduct research with the club today.{/i}"
    
    show scara disgust with dissolve
    S "Are you stalking me?"
    
    menu:
        "What? I just got to school.":
            show scara disgust
            S "Thats what a stalker would say, creep." 
            show scara neutral
            S "I'm kidding. I hope you got the joke or else I'd be concerned."
        
        "Yes, scara, I love you.":
            show scara disgust
            S "Well, I was joking but now I'm weirded out-"

    show lyney fear at left with dissolve
    L "Scara, surely you aren't harassing our newest exchange student!"
    show scara disgust
    S "They were being weird!"
    show lyney neutral
    L "Yea.. I don't believe you."
    show lyney happy glee
    L "Wow, this is the second time already I've had to save you from an awkward conversation!"
    
    show lyney neutral -glee
    L "You need to avoid people like this.."
    show lyney embarrassed
    L "Or else I might have to step in again!"
    show scara angry
    S "yea, Jack, I'd take his advice."
    show lyney neutral question
    L "Really, you think that? Or do you just miss being a loner already."

    show lyney -question
    show scara angry vein
    S "augh, shut up."

    menu:
        "You should really stop avoiding people so much, Scara.":
            show scara neutral none
            S "Hey, thats not true."
            show scara neutral glee
            S "Didn't I start the conversation this morning?"
            show lyney disgust
            L "By accusing him of being a stalker?"
        
        "Let him be, Lyney.":
            show scara angry none
            S "You heard him."
            show lyney neutral
            L "I'll consider it…"
            show lyney happy
            L "But I think it's funnier this way."

    show scara embarrassed
    S "Whatever, I don't want to see you freaks outside of the club."
    show lyney happy glee
    L "Oh right, the club! You must be so excited for it today scara!"

    show lyney -glee
    show scara neutral
    S "I am curious to see if our 'research' will lead us anywhere."
    show scara embarrassed
    S "I guess you could say I am a bit invested in this plot-"
    show scara happy
    S "But only because you all are a bit delusional, it's like watching a train-wreck!"

    menu:
        "Do you not have some belief in it?":
            show scara happy
            S "I like what naoto said. I don't believe it right now but if you show me good evidence, then hey, maybe I'll believe it."
            show lyney disgust
            L "How original."
        "Why do you attend the club then?":
            show scara fear question
            S "You don't know…"
            show scara fear -question
            S "When you signed up.. You were actually selling your soul to miku!"
            show scara happy
            S "How's that for supernatural?"
            show lyney disgust
            L "Oh come on.. I've seen you read teen wolf fanfiction scara."

    show scara angry
    S "yea, I'm going."
    show lyney neutral
    L "I'll come with you!"
    show scara angry sigh
    S "augh…"

    hide scara with dissolve
    show lyney sparkles
    L "As for you dear, I'll see you around!"

    hide lyney with dissolve
    
    Y "{i}What a weird morning. I should head to class now.{/i}"

label day3lunch:
    stop music fadeout 1.0

    scene classroom day with fade
    show screen top_right_ui(3, "Lunch") with Dissolve(2)

    Y "{i}I'm here at the club early, hopefully people will show up soon{/i}"

    play sound scary
    Y "{i}…?{/i}"

    menu .investigate:
        "{i}Should I go investigate the sound?{/i}"
        
        "yes":
            Y "{i}The sound appears to be coming from the back of the classroom.{/i}"
            Y "{i}I may as well check there.{/i}"
        "remain put":
            play audio scary
            Y "{i}maybe I should reconsider...{/i}"
            jump .investigate

    show cyno at r55 with dissolve

    Y "!"

    queue music tense

    Y "{i}Is that cyno?{/i}"

    C "Huh?"
    
    menu:
        "are you okay?":
            pass
        "what are you doing on the floor?":
            pass

    C "…"

    menu:
        "{i}What should I do?{/i}"

        "Help Cyno up.":
            Y "{i}I can try to pick him up. {/i}"
            
            show cyno neutral with hpunch
            play sound falling

            Y "{i}His body seems lifeless, I can't even feel a pulse from him but he seems to be breathing fine.{/i}"

        "Check to see if he's injured.":
            Y "{i}I can try checking around for injuries.{/i}"
            
            show cyno neutral with hpunch
            show cyno neutral with vpunch

            Y "{i}He appears to have a bruise, most likely from falling.{/i}"

    Y "{i}Weird, he's so unresponsive that it's concerning!{/i}"
    Y "{i}I don't know how much else I can do…{/i}"
    Y "{i}I leave cyno to rest on a table.{/i}"

    show naoto neutral at r51 with dissolve

    show naoto neutral
    N "Oh, you're here early!"
    show naoto disgust
    N "What are you doing in the corner?"

    menu:
        "Come over here and see-":
            show naoto fear
            N "Mysterious.."
        "It's cyno, he needs help.":
            show naoto neutral question
            N "huh? What is he doing over there?"

    show naoto fear exclamation
    N "oh my god, is he okay?"

    show naoto -exclamation

    menu:
        "No, he's extremely unresponsive.":
            show naoto fear
            N "Cyno? Is everything alright?"
            C "{i}stares blankly at her{/i}"
            show naoto angry glee
            N "Cyno? Cynooo?  Cyyyyyyynoooo? CYYNOO?"
            show naoto neutral -glee
            N "I can conclude he is unresponsive."

        "He's breathing fine but he seems lifeless.":
            show naoto neutral
            N "Its good to know he's at least breathing."
            show naoto disgust
            N "What do you mean by 'lifeless'?"

        "He has some bruises on him.":
            show naoto neutral
            N "Bruises? My best guess is he sustained them from falling."

        "Nah we just playing, he's fine.":
            show naoto angry
            N "That's not funny."

    show naoto neutral
    N "If you move aside, maybe I can examine him." 
    show naoto neutral at r54 with move
    N "Oh my, there are so many bruises!"
    show naoto fear
    N "This state is worrying..."

    show lyney neutral glee at r51 with dissolve
    
    L "Hey guys!"
    
    show naoto neutral
    N "Lyney, we need to catch you up on this situation."
    show lyney disgust -glee
    L "Huh? Naoto why are you on Cyno?"
    show naoto embarrassed
    N "Do not phrase it like that!!"
    show naoto neutral
    N "I was simply examining him."
    show naoto neutral
    N "I entered this room and these two were in the corner."
    show naoto neutral
    N "Cyno is in concerning conditions."
    N "He has sustained several bruises, despite breathing, his pulse cannot be detected and he is completely unresponsive. "
    show lyney neutral
    L "Unresponsive? Lets see.."

    show naoto at r53
    show lyney neutral sparkles at r54
    with move
    L "CYNOOOO!"

    show lyney -sparkles

    show naoto embarrassed
    N "I have.. already attempted that."

    show naoto neutral
    show lyney sad
    L "So then what, say we bring him to the nurses room."

    show scara at r51 with dissolve
    S "it's best not to do that."
    
    show lyney happy glee
    L "Look what the cat dragged in!"

    show lyney -glee
    show naoto neutral question
    N "Scara, what are you saying?"

    show scara neutral
    S "It's probably one of his episodes."
    S "You know, the thing miku was explaining!"

    show scara neutral glee
    S "I'm sure he's fine."

    show naoto -question
    show scara -glee
    show lyney sad
    L "Well, it's a risk. And I don't know how I feel leaving him here."

    show naoto sad
    N "Maybe we're wrong, we don't even know what's causing it. I think it's not worth the risk."
    show scara neutral
    S "Hey you admitted to not knowing everything. We don't know everything about this."
    show scara disgust
    S "besides, I thought you guys made this weird investigation thingy because you wanted to link this whole illness thing to the weird occurrences and blah blah blah..."
    show lyney angry
    L "Ignoring the passive aggression.."
    show lyney neutral
    L "What are you suggesting?"
    show scara neutral
    S "I don't know, do your own research and figure something out."
    show naoto neutral sigh
    N "That is a lot easier said than done."

    show naoto -sigh
    show lyney happy sparkles
    L "Well, Scara, as you've so generously offered to take the lead on this, the stage is yours!"
    
    show lyney -sparkles
    show scara angry
    S "Hey, what?"
    S "Ugh fine, I guess I'll look at him."

    show scara neutral at r54
    show lyney neutral at r52
    with move

    S "hmmm..."
    show scara happy
    S "So I think he probably had an episode, fainted or fell or something because he couldn't move and now he's like this."
    show naoto neutral question
    N "Yes, however, what do you think caused it?"

    show naoto -question
    show scara neutral
    S "early stage alzheimer's!"
    show lyney disgust sigh
    L "right.."

    show lyney -sigh
    show naoto neutral
    N "Since Cyno is seemingly unconscious as of now, we are missing an aspect of the story."

    show miku fear at r51 with dissolve
    show miku with vpunch

    show miku fear
    M "AH, SORRY I'M LATE EVERYONE!"
    show naoto neutral exclamation
    N "Miku!"

    show lyney neutral
    L "A lot has occurred whilst you were gone."
    L "We came in and found cyno on the floor."
    show lyney fear
    L "We did a check up on him, examined him and it didn't look promising."
    show lyney neutral
    L "Initially we were going to take him to the nurse."
    show naoto neutral none
    N "But scara implied this is likely what you were explaining to us yesterday."

    show lyney happy
    L "and he so kindly offered to investigate the cause of this, just look over there."

    show scara happy
    S "See, when I lift up his arm, the bruises are on this one but not on this one."
    show miku disgust
    M "I see…"

    show cyno angry
    C "Get this twink off me!"
    show miku fear exclamation
    M "Cyno?!"
    show naoto neutral
    N "Be careful, he might still be in a vulnerable state!"
    show cyno neutral
    C "No, I'm fine."

    stop music fadeout 1.0
    queue music main

    show cyno disgust
    C "Why is this one touching me?"
    show scara angry
    S "I have a name!"
    show scara happy glee
    S "Also, I saved your life."

    show scara -glee
    show naoto neutral
    N "He did not."
    show miku neutral
    M "Cyno what happened?"
    show cyno neutral
    C "Same thing as the night I called you."
    show scara neutral
    S "Well I was right.."
    show miku neutral
    M "Should we maybe halt our research for today?"
    show cyno neutral
    C "No, I've already kept you back long enough."
    show cyno sad
    C "And I want to get my mind off this traumatic event."
    show naoto sad
    N "I'm so sorry that this keeps happening to you, you don't deserve to go through this.."
    show cyno disgust
    C "oh, I'm referring to being touched by scara."
    show scara angry
    S "That's enough. Lets go!"
    show miku neutral glee
    M "Alright guys, follow me."

    hide miku
    hide cyno
    hide lyney
    hide scara
    with dissolve

    "{i}Everyone follows miku, besides naoto who stays back to chat with me.{/i}"
    
    show naoto sad
    N "I'm a bit concerned."
    show naoto sad
    N "I know cyno is acting as if this is nothing, but I think we are moving on from this too quickly."
    N "We haven't been informed of anything new either."
    
    menu:
        "Well, we are starting our research today, we can look into it now.":
            show naoto neutral
            N "I suppose.."
            show naoto sad
            N "But also I fear this may not be an issue that has been documented before."
        
        "Leave it for now, lets bring it up later.":
            show naoto neutral
            N "That is a sensible approach."
            N "However I fear it might remain on my mind."

    show naoto neutral
    N "Regardless, I think this should be a matter of discussion for tomorrow."
    N "Maybe we could figure out something new today and pair it with what we already know to get towards a conclusion."
    show naoto embarrassed
    N "anyway, lets get heading."

    scene library 
    show miku neutral at r53
    show lyney neutral at r51
    show naoto neutral at r55
    show cyno neutral at r52
    show scara neutral at r54
    with fade

    M "Welcome to the library!"
    show lyney happy
    L "Woo!"
    show cyno neutral
    C "Don't get too excited, we've got important business to do."
    show scara disgust question
    S "So, we came here to research but how do we know where to start?"
    
    show scara neutral -question
    show miku neutral
    M "Well we documented everything we know about this weird medical condition that Cyno and others have been experiencing."
    show cyno neutral
    C "I mean, its a broad field but now that we have this, we can use it as a starting point. We can start to theorise some leads or research any well-documented historical occurrences of this."
    show scara disgust
    S "Do we have a name for this, or are we just going to keep referring to it as a vague medical condition?"
    show lyney neutral
    L "I think it should be called 'the condition', it's like a movie title, you know?"
    show cyno neutral
    C "Sure…"
    show naoto happy
    N "Well, with that I guess we should head off and start researching."

    hide cyno with dissolve
    hide lyney
    hide scara
    with dissolve
    hide naoto with dissolve
    hide miku with dissolve

    Y "{i}Everyone else heads off to different sections of the library. I wonder what section I should check out first?{/i}"

    default library_searched = set()

    menu .library_search:
        set library_searched
        "Where should I look?"

        "Biology section":
            show miku neutral with dissolve

            Y "{i}I head into the biology section. Miku is also here.{/i}"
            show miku happy
            M "Oh hey! I was actually gonna ask for someone to help me out here."
            
            menu:
                "sure, I got a GCSE in biology.":
                    show miku angry
                    M "duh, no shit. You probably wouldn't have ended up here if you didn't pass science."
                    show miku embarrassed
                    M "but you sound confident so-"
                "actually I don't know anything about biology.":
                    show miku disgust
                    M "yea me neither but that's because I'm a voice bank materialised as a humanoid robot and not because I'm actually dumb."

            show miku serious
            M "this university leans more toward social science than traditional medical science for the sake of the plot, so the resources we have are quite skewed."
            show miku serious sigh
            M "I'm being serious, the only book in the biology section is jekyll and hyde."
            show miku disgust -sigh
            M "I've read it like 3 times because it's all I can research."
            show miku angry
            M "I'm pretty sure this isn't even medical, like at all, but I have to gaslight myself into thinking it is because its the propaganda the university wants us to fall for."
            show miku serious
            M "that being said, whoever left it here might have done it for a reason."
            show miku neutral
            M "you see, mr. hyde is the embodiment of the evil side of dr. jekyll and the premise of the whole plot highlights the fragility of human nature as well as the duality of man and one could also argue the repression homosexuality and its impact psychologically \(\#gayrights) BUT I DIGRESS!" 
            show miku serious
            M "more importantly, mr. hyde represents this kind of regression to a more primitive state of mankind, and this is where the hear me out part comes in…"
            show miku neutral
            M "WHAT IF, cyno is experiencing reverse evolution, cause he's not exactly evolving per se… so?"
            
            menu:
                "but what about the fainting the loss of control and not to mention the influx of random memories?":
                    show miku neutral
                    M "well thats true, but if I was actually passionate about jekyll and hyde I could easily argue that these are just his innate and primal instincts!"
                    Y "…"
                    show miku sad sigh
                    M "okay fine, you make a good point."
                "anything else?":
                    show miku sad
                    M "I take it you didn't like my idea then."
                    show miku serious sigh
                    M "in that case, then no I don't, unfortunately…"
            
            show miku angry -sigh
            M "c'mon, this is where you're meant to help now, what do you think?"
            
            menu:
                "some sort of infection?":
                    show miku serious
                    M "the doctors would've spotted the signs if cyno really was infected with something."
                "cellular decay?":
                    show miku serious question
                    M "don't human cells replace those that die all the time though?"
                "he inherited two recessive genes?":
                    show miku serious exclamation
                    M "its highly likely he would've been screened for those kind of disorders in the first place!"
           
            show miku angry
            M "ugh, this isn't getting us anywhere."
            show miku serious
            M "but I'm not that surprised, dead ends were always going to be a potential outcome when researching various different fields."
            show miku neutral
            M "if you haven't looked already, you'll probably have better findings in almost any other section in this library."
            show miku neutral
            M "in the meantime, I'll see if there's anything better online…"

            hide miku with dissolve
            jump .library_search

        "History section":
            Y "{i}I head into the history section and browse some books.{/i}"
            Y "{i}not long after, I am soon approached by cyno.{/i}"

            show cyno with dissolve
            C "Yo, what's up?"
            C "I've actually been here for ages I just hadn't bothered to speak to you."
            
            menu:
                "wow rude..":
                    show cyno angry
                    C "I think I was very respectful and obliging to the unspoken silent reading time rules."
                    show cyno happy
                    C "I don't know if you missed it but I actually included a secondary joke within that joke."
                    show cyno embarrassed
                    C "See, I referred to the rules as 'unspoken' in reference to 'silent' reading time because if you're silent, you can't speak. Get it?"
                
                "honestly I don't care.":
                    show cyno angry
                    C "Okay whatever then bye."
                    show cyno happy
                    C "I'm kidding-"
                    show cyno sad
                    C "As were you? I hope.."

            menu:
                "why are you talking to me?":
                    show cyno embarrassed
                    C "Not sure."
                    show cyno neutral
                    C "I guess maybe I was bored or maybe I wanted to share my work."
                "Are you actually looking into anything?":
                    show cyno disgust
                    C "Yea, I was getting onto that."
            
            show cyno neutral
            C "Speaking of, this section might have some serendipitous discoveries."
            C "Well, not entirely, considering for a long portion of western history most abnormal cases could be explained away by religion or hysteria."
            C "But when mental illness began to be considered more thoroughly, cases of hysteria could be seen more clearly and were later categorized into some early form of mental conditions that we know of."
            C "Like for shell shock, many would regard it now as to be a branch of ptsd which is a mental condition."
            C "But at the time the whole concept of shell shock was not viewed through this lens of it being a mental thing."
            C "You see at the time, doctors who treated patients involved in trench warfare who likely suffered shell shock would only have the knowledge of physical conditions and the cause of these conditions to also be physical."
            C "But the human body is a miracle in some kind of way because through this acknowledgement of this system, the body could display muteness, paralysis and a range of physical symptoms."
            C "The better understanding of physical symptoms worked as a method of communication to express the pains felt psychologically."
            C "What I'm trying to say is probably throughout history and even now our understanding of physical illness being stronger means tensions felt medically can manifest into physical conditions to indicate a deeper, mental pain."

            show cyno disgust
            C "..."
            C "This feels useful until I remember it's applied to myself-"
            show cyno neutral
            C "Overall this whole 'research' thing actually being about me is.."
            show cyno disgust
            C "Weird…"
            show cyno neutral
            C "Not even sure if I know myself that well in that regard."
            show cyno sad
            C "Am I trying to express some form of emotionally repressed pain?"
            show cyno happy
            C "Or maybe I am suffering due to the age old hysteria.."
            show cyno neutral
            C "Although that mainly applied to women."
            show cyno sad
            C "It pretty much only applied to women in ancient Greece."
            show cyno neutral question
            C "There must be a male version, or is that still yet to release?"
            
            menu:
                "The greeks thought sperm had healing properties.":
                    show cyno disgust -question
                    C "Wow, the glaze for men is infinite.. Smh"
                "it might be because they apparently don't have last names.":
                    show cyno angry -question
                    C "fuck you."

            show cyno neutral
            C "Eh whatever I've gone on too much of a tangent."
            show cyno neutral
            C "I'll see you."

            hide cyno with dissolve
            jump .library_search

        "Psychology section":
            show naoto with dissolve

            Y "I head into the psychology section. Naoto seems to have taken a pile of books from the shelf."
            
            show naoto happy
            N "ah, its you."
            show naoto neutral glee
            N "I believe this section should have much of what we're trying to look for."
            show naoto -glee
            N "if we're lucky, maybe we can understand more about cyno's condition."
            
            menu:
                "so you think its something psychological?":
                    show naoto neutral
                    N "I believe so. After all, we've seen his most recent episode with our very own eyes, and it's not too far from the mental shutdown cases we discussed before."
                "do you think it might be medical related instead?":
                    show naoto neutral
                    N "that's a fair point, but miku's already at the biology section, so it only makes sense to spread our findings a bit."
            
            show naoto neutral thought
            N "to start off, let's focus on his symptoms. If you can remember, he said it was like his body was moving on its own, though he couldn't feel anything."
            show naoto neutral
            N "it's almost as if he's dissociating from reality."
            show naoto neutral thought
            N "So if that's the case, I don't think its entirely a neurological condition."

            menu:
                "is it psychological trauma?":
                    pass
                "some kind of delirium?":
                    pass
            
            show naoto fear
            N "that's quite possible indeed."
            
            show naoto neutral
            N "in rare cases, this kind of dissociation can lead to a loss of agency to the point where the mind detaches itself from the body."
            show naoto disgust
            N "there are some pseudoscientific theories inside this journal too, but as you might expect, their validity is questionable at best."
            show naoto neutral
            N "still though, it is argued that the unconscious, that which sits below our conscious mind containing innate biological drives and instincts, can resurface into real life under certain conditions."
            show naoto neutral
            N "these unconscious patterns are able to manifest physically and emotionally when they can no longer be contained."
            show naoto neutral glee
            N "and these memories, which are meant to be repressed, may be able to cause someone to lose control."
            
            menu:
                "so cyno's losing his own conscience?":
                    show naoto neutral thought
                    N "sounds like it, but I don't want to jump to any conclusions just yet."
                "I don't trust freudian contemporaries.":
                    show naoto disgust -glee
                    N "I wouldn't either, but in this case it's difficult to rule out."
            
            show naoto neutral
            N "moving towards something a little more scientific, there's also this concept in behavioural psych called learned helplessness."
            show naoto neutral
            N "if someone is exposed to a repetitive and inescapable situation, they can become passive and stop trying to act."
            show naoto disgust
            N "So much so that their free will becomes… performative."
            show naoto neutral
            N "and such is the debate between free will and determinism."
            show naoto disgust thought
            N "Are we truly making our own choices? Or are we really subject to external forces beyond our control - biology, the environment? Maybe something even deeper?"
            show naoto neutral -thought
            N "unfortunately that's something we cannot answer neither here or now."
            show naoto sad
            N "but the way cyno's episodes have acted out, its disturbingly close to these concepts."

            hide naoto with dissolve
            jump .library_search

        "Religion section":
            show lyney neutral glee with dissolve

            L "Hey!"
            show lyney happy
            L "I'm so glad you're here."
            show lyney neutral -glee
            L "In all honesty I got bored and wandered here."
            show lyney embarrassed
            L "Research… it sounds fun but it isn't really my thing.."
            show lyney neutral
            L "I make illusions happen not figure out why they happen."
            
            menu:
                "Have you actually read anything here?":
                    show lyney happy
                    L "Would you be surprised if I told you I have?"
                "Do you find this similar to magic?":
                    show lyney neutral
                    L "Magic and the supernatural are fundamentally very different."
                    L "However, one aspect that matters to both is perspective."
                    show lyney sparkles
                    L "If you believe in magic, it can make the illusion seem all the more real."
                    show lyney -sparkles
                    L "Likewise, if you believe in religion or spirituality or anything supernatural it makes instances like these seem as proof."
                    Y "So you have actually found stuff here?"
            
            show lyney neutral
            L "I was getting to that anyways."
            show lyney fear
            L "A lot of what cyno and others are experiencing reads similar to beliefs around evil spirits."
            show lyney sad
            L "In many religions and cultures globally possession or the presence of an evil spirit has been an answer to misfortune, illness or strange behaviour."
            
            menu:
                "Why do you think that is?":
                    show lyney neutral
                    L "To connote to something bad as a doing of 'evil' can make it palatable to some people I guess."
                    L "It's hard to accept that bad things can happen to anyone regardless of morality, so some people view it as an act of evil that actively has something to gain from causing tragedy."
                    show lyney sad
                    L "In cyno's cause, it's such a strange and abnormal occurrence it would be easy to explain it with the belief of spirits interfering."
                    show lyney fear
                    L "It does seem very similar when you look into the symptoms and compare it to what cyno and others are experiencing it does seem very similar.."

                "Do you think cyno is possessed?":
                    show lyney neutral exclamation
                    L "Well, I was researching the whole 'possession' thing and came across an account by an Anglican priest."
                    show lyney neutral -exclamation
                    L "he depicts it to be that 'the person's will is taken over by an intruding alien entity' which can lead to delusion, changes in personality and mental absence."
            
            show lyney fear exclamation
            L "But what I find more interesting was account of people actively trying to fight demonic spirits possessing them!"
            show lyney neutral -exclamation
            L "It's depicted  as the person under the influence of evil spirits will appear physically and mentally numb as it is a battle that takes place entirely subconsciously."
            show lyney fear
            L "The victim's body in this process may exert irrational behaviour that may even be self destructive."
            show lyney neutral
            L "And, the person under possession usually cannot recall any significant happenings afterwards."
            show lyney embarrassed
            L "I can't say definitely, but it kinda does sound like cyno in that case."
            show lyney happy glee
            L "However when I think more critically I begin to wonder 'who on earth would want to possess cyno'"
            L "I mean, I've known the guy my entire life."
            show lyney neutral -glee
            L "I don't know any specific reasons for why a “demon” would want to possess him."
            show lyney embarrassed
            L "In the end I don't know how useful this truly is."
            show lyney neutral
            L "It's not like I'm researching something deeply scientific that has solid reasons for every explanation."
            
            menu:
                "It is useful as you can see how people who dealt with this before answered their questions.":
                    show lyney neutral
                    L "Well yea, the whole evil spirits thing may nor be familiar to us because we have a better understanding of psychology and other sciencey stuff."
                    show lyney neutral sparkles
                    L "but to people who wholeheartedly believe in this, this probably helps explain some things."
                "It's useful because it explores the possibilities that science would be too critical of to explore.":
                    show lyney happy
                    L "I agree with you, it may not be as plausible factually but there's still a chance!"
                "It's not useful.":
                    show lyney embarrassed sigh
                    L "I guess it's not the most useful…"
                    show lyney happy sparkles
                    L "at face value!"
                    show lyney neutral -sparkles
                    L "it's an unconventional approach but maybe it can help reveal aspects of this that science can't explain."
            
            show lyney neutral none
            L "and besides, this whole condition is weird, so its quite unlikely to be something deeply rooted in science, can't put this supernatural stuff off the table!"
            L "Ah, well. I'm gonna take a break now."

            show lyney neutral glee
            L "I'll see ya I guess since you should probably get back to work." 

            hide lyney with dissolve
            jump .library_search

        "Fiction section":
            show scara happy glee
            S "See, I'm in the fiction section because it's made up!"
            show scara disgust -glee
            S "That wasn't a very impactful joke."

            menu:
                "Are you using this as an excuse to not research?":
                    show scara neutral
                    S "Hmmm yea pretty much."
                "why the fiction section?":
                    show scara embarrassed
                    S "But also not really."
            
            show scara neutral
            S "it's kind of dumb thinking a newly discovered condition or whatever will be found in the stem stuff."
            show scara happy sparkles
            S "But someone has probably imagined something like that before."
            show scara neutral -sparkles
            S "Did you come here for the same reason?"
            
            menu:
                "No I'm just lost.":
                    show scara angry
                    S "Geez, did nobody show you around before you came?"
                    show scara neutral
                    S "Well just read the signs and just know the left hand side of the library is all fiction and the right is all non-fiction."
                "100\% yea totally.":
                    show scara disgust
                    S "Yea, you sound unsure, are you sure you didn't pick the wrong dialogue option?"
            
            show scara neutral
            S "I suggest you just go to the right hand side because the actual useful stuff will be there."
            show scara neutral
            S "and I'm DEEP in research so can't talk."
            S "Cya."

            hide scara with dissolve
            jump .library_search

    Y "{i}Afterwards, we met up again and concluded our investigation for the day.{/i}"
    Y "{i}Tomorrow we will go through all our findings and draw out possible conclusions.{/i}"

label day3afternoon:
    scene entrance evening
    show screen top_right_ui(3, "After School")
    with fade

    call hangout from _call_hangout_1

    call dayend from _call_dayend_2

label day3night:
    queue music ambience

    scene room naoto
    show naoto neutral at left
    show screen top_right_ui(3, "Night")
    with fade
    
    "{i}Naoto appears to be writing in their diary.{/i}"

    show naoto sad
    N "After I was visited in the psychology section, it was as if something had shook me."
    N "A vision, so vivid it appear to be like a memory of my own."
    
    show naoto neutral
    N "And at such a perplexing time, nothing significant had occurred prior."
    N "But when {i}he{/i} left our conversation.."
    N "Hm.."
    N "It's just not something I can fully articulate or translate into written words."
    N "I wonder if this counts as a strange occurrence?"
    
    show naoto thought
    N "..."

    show naoto -thought

    play sound "<from 0 to 4.6>audio/sfx/phone.mp3"

    $ renpy.pause(4.5)
    
    scene room naoto cyno 
    show naoto neutral at left
    show cyno fear exclamation at right
    with dissolve

    C "Naoto?"

    show cyno -exclamation
    show naoto neutral
    N "Yes, hello cyno, sorry for calling at this hour."
    show cyno neutral
    C "I didn't even know you had my number to begin with."
    show cyno embarrassed
    C "Would have never expected a call from you."
    show naoto disgust
    N "I would at least keep your number-"
    show naoto neutral
    N "I know we aren't awfully close, but we are acquaintances.."
    show cyno sad
    C "Wow, you called to acquaintance-zone me."
    show naoto angry
    N "Cyno!"
    show cyno neutral glee
    C "My bad!"
    show cyno happy -glee
    C "Anyways, what's up?"
    
    show naoto embarrassed
    N "I'm not sure how to word this."
    show naoto neutral sweat
    N "In the library today, something strange occurred."
    show naoto neutral -sweat
    N "I was approached by him, and we had a conversation."
    show naoto embarrassed
    N "It was casual, just about our research and all."
    show naoto neutral
    N "But once he left, I saw.."

    show naoto fear
    N "This vision."
    N "It just flashed before my eyes! It was so detailed and vivid, like deja vu."
    
    show cyno neutral question
    C "What was the vision of?"
    
    show naoto neutral
    N "Him and I were in a desert and the emotions in the moment were tense."

    show naoto sad
    N "He was gripping onto me and shouting, I suppose we were in an argument and I must have upset him someway."
    N "It was honestly quite upsetting, I didn't know the context or anything but then for a second he spoke, to me, in that moment"
    N "'Do you want to continue like this? watching our friends die, watching the world crumble, all us just succumbing to our fate of destruction painfully slowly?'"

    show naoto neutral
    N "..that's what he said at least."
    show naoto fear
    N "And then the next second, I was back to reality, I saw him walking away and everything from there just felt off."
    show naoto embarrassed
    N "Ah, sorry for the tangent."
    show naoto neutral
    N "If you are still there, what I was meant to call you to ask was just: have you experienced this before?"
    
    show cyno happy sparkles
    C "Don't apologise, I am here for you."
    
    show naoto embarrassed
    N "This is very awkward..."
    show cyno angry -sparkles
    C "Well my bad-"
    C "Anyways, in terms of what you saw, yes, I have experienced that."
    show naoto fear exclamation
    N "you have?!"
    show cyno disgust
    C "Yes.."
    
    show cyno neutral
    C "They come to me quite often, these depictions of events."
    C "I've had so many in fact they all seem to be fragments of a linear story."

    show cyno disgust thought
    C "Not enough that I could put it together"
    show naoto neutral exclamation
    N "What are they like?"
    show cyno neutral -thought
    C "They appear to me like memories. Strangely enough I remember these visions more clearly than my actual memories."
    show naoto fear -exclamation
    N "Did you experience one today, when you were unconscious?"
    
    C "I wasn't unconscious,no it was much more than that, It was like I was in a different reality entirely and I was experiencing a vision then."
    show naoto angry
    N "Well, sorry you decided to move on from that really quickly-"
    show cyno neutral sparkles
    C "Didn't want to steal the show."
    show naoto disgust sigh
    N "..."
    
    show naoto -sigh
    show cyno neutral none
    C "Naoto, hello?"
    show cyno disgust
    C "Well anyways when I was in that state was me being in a room, it was dark and empty. I was paralysed and on the floor. It felt like there was constant whispers in the background."
    show cyno neutral
    C "There was an open door in front of me and standing there was some kid."
    show cyno neutral
    C "He look like he was in year 9 not gonna lie"
    show naoto neutral question
    N "Did you know him?"
    show cyno happy
    C "Yes, he's my cousin."
    
    show naoto fear -question
    N "eh?"
    show cyno neutral
    C "Just kidding, he was white anyways."
    show cyno angry
    C "and I am NOT white #proudEgyptian #DontFallForGenshinRacePropaganda"

    show cyno fear
    C "But more relevant, behind that kid, you and him were there."
    show naoto fear
    N "?!"
    show naoto sad
    N "Were we arguing?"
    show cyno angry
    C "Don't ruin my story I'm getting there!"
    show naoto angry
    N "Not sure if we have time for this…"
    show cyno neutral
    C "It's our story, any spirits or demons or interdimensional entities viewing this via a visual novel can wait."
    
    show cyno neutral
    C "What I was not telling you was in the library, he also came to me and after we chatted, I had another vision"
    show cyno sad
    C "I was in a desert, I was bloody and on the ground as if I was in a fight."
    show cyno sad
    C "I felt like I was dying."
    show cyno neutral
    C "But far away, I saw you and him, It seemed like you were walking away from me."
    show cyno neutral
    C "And then I saw you guys starting to argue."
    
    show naoto fear exclamation
    N "you were there then!?"
    show cyno neutral thought
    C "I suppose."
    show naoto fear -exclamation
    N "Is this like you said, these visions are fragment of a story!"
    show cyno fear -thought
    C "And you think we possess the same memory of this event?"
    show naoto neutral
    N "Well, they almost line up."
    show cyno neutral
    C "We know someone else who was there as well."
    show cyno neutral question
    C "Do you think maybe he experienced it too?"
    show naoto neutral
    N "Maybe it was not just him."
    show naoto neutral thought
    N "maybe it was all of us that will experience these visions."
    
    show cyno happy -question
    C "Then from there, maybe we can piece this together and find what it means!"
    show naoto happy -thought
    N "Exactly!"
    show cyno sad
    C "Do you think it's related to my condition at all?"
    show naoto neutral
    N "Well you saw this whole memory that state."
    show cyno neutral
    C "I didn't just see it, I was there!"
    show naoto neutral
    N "Then it probably is, and it means we could probably delve deeper."
    show cyno neutral
    C "Well tomorrow we should report this to the others and try get to the bottom of this."
    
    show naoto happy
    N "Yes, I agree."
    show naoto happy glee
    N "and, thank you cyno. This was actually really beneficial to me."
    show cyno happy
    C "My pleasure."
    show naoto happy -glee
    N "So then, I'll see you tomorrow I suppose."
    show cyno happy
    C "Yup. Good night."

    stop music fadeout 1.0

    scene black
    hide screen top_right_ui
    with fade