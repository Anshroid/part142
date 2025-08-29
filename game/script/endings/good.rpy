label goodending:
    queue music sentimental

    show scara neutral
    show lyney neutral
    show naoto neutral
    show miku neutral
    show cyno neutral

    "All" "…"
    show naoto happy glee
    N "Well said."
    show miku neutral
    show naoto -glee
    M "yeah, I couldn't have put it any better myself."
    show miku happy
    M "we'll keep investigating, no matter how long it takes."
    show scara neutral
    S "hm…"
    show cyno happy heart
    C "thank you for choosing to continue believing in this investigation, for my sake."
    show cyno -heart
    show lyney happy
    L "so it appears the spectacle will continue at last!"
    show lyney happy glee
    L "though the truth still seems like a veil of endless mysteries, the curtain call will come in due time, and we will reveal what's behind the curtain for good!"
    show naoto -glee
    show miku embarrassed sigh
    show lyney -glee
    M "lyney… you could just say you're happy with his decision instead of hiding your words behind figurative language…"
    
    menu:
        "I'm not dumb. I understood what he meant.":
            show miku -sigh
            show lyney happy glee
            L "haha, I knew you would."

        "actually explain to me like I'm 5.":
            show miku -sigh
            show lyney embarrassed sigh
            L "tch, you guys are so dull…"

    show miku neutral
    M "anyway, even when the club has to 'shut down', I hope we can still be the supernatural investigation team within each of our hearts!"
    show lyney neutral question
    L "come now, you're just being a little too soppy. Hypocritical much?"
    show lyney -question
    show miku angry exclamation
    M "s-shut it! I'm just happy for us, that's all!"
    show miku neutral -exclamation

    show scara neutral
    S "Hmph." 
    show naoto neutral question
    N "What's up scara?"
    show lyney disgust
    show naoto -question
    L "You not happy now? Well, we have all decided on this."
    show scara neutral
    S "No not really."
    show cyno disgust
    C "That's surprising."
    show scara neutral
    S "Its something you all have personally come to terms."
    show scara neutral
    S "I wouldn't want to personally advocate for this idea because I mean, it is flawed."
    show scara happy
    S "But it does make you think."
    show miku sad
    M "So then, are you leaving?"
    show scara neutral
    S "Don't think I will."
    show naoto disgust
    N "You don't want to advocate for what we do, and yet you'll still be here?"
    show scara neutral
    S "Yea I mean, I guess you were all right in the end."
    show lyney fear
    L "huh?"
    show scara embarrassed
    S "I have no friends…"
    show cyno fear exclamation
    C "He said the thing!"
    show scara neutral
    show cyno -exclamation
    S "I'm joking obviously-"
    show scara happy
    S "But I have grown close to you all so it'd be a bit stupid leaving now!"
    show lyney happy heart
    L "Awww well we are lucky to have you!"
    show scara embarrassed
    S "Don't make it weird-"
    show lyney embarrassed -heart
    L "kind of hard not to.."
    show naoto happy
    N "Well, it is a good note to finally end this week on!"
    show naoto happy sparkles
    N "We are all together in the end, and the club with the original members will continue! Somehow."
    show naoto -sparkles
    show cyno happy
    C "Thanks for the synopsis."
    show miku happy glee
    M "It's only looking up from here."
    show cyno neutral question
    C "so we will end up becoming a group of vigilantes then?"
    show miku -glee
    show cyno -question
    show miku embarrassed
    M "huh? Where'd you get that idea from?"
    show cyno neutral
    C "well I just thought that since we're no longer under the jurisdiction of the school…"
    show miku angry
    M "hey! we're not becoming phantom thieves if that's what you're suggesting!"
    show cyno sad
    C "aww…"
    show naoto neutral
    N "ahem. Back to the matter at hand."
    show miku fear exclamation
    M "oh, right!"
    show miku neutral none
    M "listen, I know you'll be leaving later today, but I do hope you'll continue to work with us."
    show naoto neutral
    N "me as well. your help thus far has been nothing short of a miracle."
    show miku happy
    M "and I think I can speak on behalf of everyone when I say we trust you to help lead us forward."
    show miku embarrassed
    M "if travels not an issue… of course…"

    menu .istravelanissue:
        "I'll come visit soon.":
            show miku happy glee
            M "great! That means a lot."
        
        "I'm not too sure.":
            show miku neutral
            M "Aw really? Do reconsider?"
            jump .istravelanissue

    show miku fear exclamation
    M "…what's that? You don't have our contact info?!"
    show cyno disgust
    show miku -exclamation
    C "so that's why he never messaged on the group chat…"
    show scara neutral
    S "what group chat?!"
    show cyno happy sparkles
    C "I'm joking-"
    show cyno neutral none
    C "but we should probably make one."
    show naoto neutral
    N "that's a separate matter to attend to later though."
    show miku embarrassed
    M "yea, there's a mandatory student council meeting in 15 so…"
    show lyney disgust
    L "so now we have to conclude our infinitely-more-important meeting then?"
    show miku serious
    M "well we've established a plan of action for the upcoming week and, considering the situation we landed ourselves in yesterday, we recovered pretty quickly."
    show miku neutral question
    M "so I'd say we're all satisfied with the outcome, right?"
    show cyno neutral
    C "no, I want to kill myself."
    show miku embarrassed none
    M "uhm…"
    show miku neutral
    M "anyways, I don't wanna leave your last day as an exchange student on a serious note."
    show miku neutral question
    M "and I think we all deserve a little break from this research, don't you think?"
    show cyno neutral
    show miku -question
    C "no-"
    show scara angry vein
    S "if you finish that sentence I'll kill YOU myself /srs /platonic /real /sexual"
    show naoto neutral sigh
    N "I mean, I would love to do something on campus to conclude your stay here at this school but 15 minutes does not seem like a good amount of time for everyone's goodbyes."
    show scara neutral none
    S "Then how about the evening again? On the roof, like on that one day."
    show naoto -sigh
    show cyno neutral question
    C "Will the sky be as visible tonight?"
    show cyno -question
    show miku neutral
    M "no, but surely that's not what matters."
    show lyney happy glee
    L "I'm bringing alcohol!"
    show scara disgust
    S "this can only end badly."
    show lyney -glee
    show miku happy
    M "so uhh yeah see you in a few hours then?"
    show cyno angry
    C "I won't be coming because I hate you."
    show miku angry
    M "Shut up your jokes aren't funny-"

    Y "{i}For now, we all go our separate ways, hoping to end my last day here with some final memories to carry forward.{/i}"

    stop music fadeout 1.0
    queue music hangout

    scene roof stars
    show screen top_right_ui(7, "Evening")
    with fade

    Y "{i}evening quickly arrives, I soon head up to the rooftop to join the party.{/i}"

    show miku at r51
    show lyney at r54
    show cyno at r53
    show naoto at r52
    with dissolve

    show cyno happy
    C "Yo."
    Y "?!"
    show cyno embarrassed
    C "Did you know that every man has two fantasies? You know what they are?"
    
    menu:
        "Happiness and love?":
            show cyno angry
            C "Who gave you that idea?"
        "Mango shake and a second mango shake?":
            show cyno happy heart
            C "Attaboy!"

    show cyno neutral none
    show lyney happy
    L "*hic*. I'm glaaad weee… we c-could defeaaat the enemy… wiiiith the pow'r of frien'shippp!"
    show miku angry
    M "ugh, is lyney drunk already?"
    show naoto fear
    N "perhaps more importantly, what enemy!?!"
    show lyney fear
    L "If there wuzznt an enemy… w-who did I beat up, huhhh?"
    show lyney happy sparkles
    L "Check- *hic* checkmaaaate liberal!!"
    show lyney -sparkles
    show miku fear
    M "oh no lyney… did you really hurt someone?"
    show lyney neutral
    L "mmhh y-yeah…! It wazz some creep, wanted cyno sooo bad, like, REALLYYY bad. *hic*"
    show miku fear exclamation
    M "HUH?!"
    show cyno happy
    C "don't worry miku, if it's who I think it is, then lyney actually did us a favour."
    show miku embarrassed -exclamation
    M "uhm… if you say so?"
    
    show scara at r55 with dissolve

    show scara angry
    S "I smell alcohol already…"
    show miku happy
    M "scara! You showed up!"
    show scara happy
    S "Why wouldn't I?"
    
    show lyney happy
    L "*hic*. An' looksssh like the maaan of th' hourr's 'ere too!!"
    show scara disgust
    S "augh, this guy reeks!"
    show naoto fear
    N "lyney… please sit down for a moment, you're barely able to stand."
    show lyney happy
    L "i-im NOT stann-dinn… I'm ♫ SOOARINNNGGG, FLYYINN- ♫ *hic*!"
    show miku serious
    M "You know what, I'm going to take him inside."

    if chosen.name == "miku":
        show miku happy
        M "I don't know how long I'll be down there for but just a heads up, I want to speak to you later!"
        
        menu:
            "I'll be here waiting.":
                show miku happy glee
                M "Hehe, I won't keep you long now since I'll definitely be taking up a lot of your time later!"
            "am I in trouble?":
                show miku embarrassed
                M "Don't be like that! Especially when we are dating now.."
       
        show miku none
        show lyney fear
        L "Huh? Watcha two love birdzzzz saying?"
        show lyney disgust
        L "Waaaaaittt you twoo… are likeeee, together now?"
        show miku embarrassed
        M "I guess we didn't really tell the others."
        show miku neutral
        M "Oh well, that's on you now!"

        hide miku
        hide lyney
        with dissolve

    elif chosen.name == "lyney":
        show lyney fear
        L "WAAAAAIIITTT!"
        show lyney happy
        L "I wanna speak to yoooouu first~"
        show naoto fear exclamation
        N "Wow.. he's all over you-"
        show naoto -exclamation
        show lyney embarrassed question
        L "WHy, h-why wouldn't I be? We are like,, a thing ya know?"
        show miku embarrassed
        M "Is that how you tell us?"
        show lyney -question

        menu:
            "this was staged, we planned to tell you like this.":
                show lyney happy
                L "Abracadabra! Heheh~"
                show lyney neutral exclamation
                L "Yea, this is MY world wideeee confession!!!"
            "probably wouldn't have happened otherwise-":
                show lyney neutral
                L "Only needed… twoooo ish.. To get it to happen."
                show miku serious question
                M "2 ish what?"
                show lyney happy heart
                L "Heheheh. My surprise~"

        show lyney none
        show miku none
        show cyno disgust
        C "Yea miku take him away."
        show lyney sad
        L "NOOOOOOO!!"
        show miku angry
        M "Shush you can speak to your boyfriend later, lets go."

        hide miku
        hide lyney
        with dissolve

    elif chosen.name == "naoto":
        show lyney sad
        L "NOOOOOOO!"

        hide lyney
        hide miku
        with dissolve

        show naoto happy
        N "Well, its a relief he's gone for now."
        show naoto embarrassed
        N "Not in a rude way, I am just not fond of dealing with… ahem, drunkards…"
        show naoto neutral
        N "anyways, the rest of us are going to go share some drinks, and hopefully not end up like him…"
        show naoto embarrassed
        N "But, at some point I hope to steal you just for some final moments alone."
        show naoto happy heart
        N "you know… since we're romantic partners now."
        show naoto sad -heart
        N "…The thought of you leaving makes me a little sad."
        show naoto happy
        N "But alas, we are here to celebrate so let's not let melancholy get in the way."

    elif chosen.name == "cyno":
        show lyney sad
        L "NOOOOOOO!"

        hide lyney
        hide miku
        with dissolve

        show cyno fear
        C "Yeesh, I'm just glad my alcohol tolerance is much higher."
        show cyno neutral question
        C "…once things start to quieten down, will you be up for a game?"
        show naoto neutral
        N "a game? That sounds interesting…"
        show cyno happy -question
        C "sorry naoto, this game's reserved for my partner only!"
        show naoto embarrassed question
        N "…partner?"
        show cyno embarrassed exclamation
        C "UHM…!"

        menu:
            "that one slipped out.":
                pass
            "partner IN CRIME-":
                show naoto neutral none
                N "right…"
        
        show naoto neutral none
        N "well, I didn't mean to pry."
        show naoto happy
        N "enjoy your \"game,\" you two."
        show cyno fear
        C "W-WHY ARE YOU SAYING IT LIKE THAT?"
        show cyno embarrassed
        C "…I can't take this level of embarrassment, I'm gonna have another drink already."
    
    Y "The rest of us sit together on the roof, having some drinks."
    show scara neutral
    S "So I guess you and [properCase(chosen.name)] are a thing now.."

    menu:
        "you heard?":
            show scara neutral
            S "Well, you were quiet loud, so I took it as a public confession."
        "No… we were lying.":
            show scara neutral
            S "yea nice try, secret's out now."

    show scara happy
    S "Well, I am glad for you both."
    show scara happy glee
    S "It's nice to see you grow so close in such a short space of time."

    show scara -glee
    show cyno neutral
    C "It takes a bit of specifics to work around this facade, but hey, he got to it so.."
    show cyno happy
    C "Not trying to shift the light away from us, but I'm glad to have gotten to know you all better now."
    show cyno happy question
    C "Could you say, we are all trauma bonded now?"
    show naoto disgust
    show cyno -question
    N "Yea lets not…"
    show naoto neutral
    N "But I can agree. I am glad to have talked to everyone here more. Especially you, since you only are staying for such a short amount of time."
    show naoto happy
    N "though we only met recently, the time we have spent together has made me confront a whole new side of myself."
    show naoto happy glee
    N "And that's impacted my relations with others more positively too."
    show naoto happy none
    N "I'm sure everyone's glad that you joined our little group."

    Y "{i}hours later, the party quickly passes by, its already well into the middle of the night.{/i}"
    Y "{i}amidst all the fun and chaos, I step away to take a moment for myself.{/i}"

    scene roof stars with fade

    if chosen.name == "lyney":
        stop music fadeout 1.0
        queue music heartwarming

        show lyney with dissolve

        Y "{i}not long after, I find lyney at the railing, looking off at the horizon.{/i}"

        show lyney happy glee
        L "hey! Fancy seeing you here as well."
        show lyney sad sigh
        L "don't tell anyone I left the party early, or they might just make a fuss."
        
        Y "you sobered up quickly-"

        show lyney neutral none
        L "yea well that was mainly for plot convenience." 
        show lyney neutral
        L "…but also because I threw up pretty quickly, hehe."
        show lyney neutral question
        L "anyway, why are you here? The party's over there."
        show lyney embarrassed sigh
        L "I'm not in the mood to do a performance, so I don't wanna bore you."
        
        menu:
            "I came to find you.":
                show lyney happy glee
                L "oh, that's good. To tell the truth, I wanted you to find me."
                show lyney embarrassed heart
                L "actually, I may have been waiting for you all this time…"

            "I just wanted some space.":
                show lyney happy glee
                L "well, seems like our minds are in sync, don't you think?"
            
            "(stay silent)":
                show lyney neutral none
                L "hmm, silent type today? Very suspicious… but I'm fine with it nonetheless."
        
        show lyney fear exclamation
        L "wait… you're saying I asked to speak you earlier?!"
        show lyney embarrassed sigh
        L "ahh, this is so embarrassing, why did I have to get so drunk?"
        
        menu:
            "you don't have to be embarrassed.":
                pass
            "you can speak to me about anything.":
                pass

        show lyney fear none
        L "I…"
        show lyney happy glee
        L "thank you."
        show lyney neutral none
        L "to be honest, all I wanted was for us to share a final moment with each other before you have to leave."
        show lyney happy exclamation
        L "which… I guess we're doing right now! Haha…"
        show lyney neutral none
        L "on reflection, I keep thinking about everything we've been through this week."
        show lyney neutral
        L "it felt like one massive show, with a bunch of clues and illusions we've still yet to figure out."
        show lyney happy
        L "but along with the bizarre chaos of our research, you were there through all of it."
        show lyney neutral
        L "not necessarily on a stage, but just… there, with us… with me."
        show lyney neutral
        L "and its not just that, out of everyone in the investigation, you saw me falter backstage and onstage, but also encouraged me to try and make magic something meaningful to me."
        show lyney happy
        L "so I guess I just wanted to say, thanks for staying with me through all that."
        show lyney happy heart
        L "I couldn't ask for a better partner, hehe!"
        
        menu:
            "I love you, full stop.":
                show lyney fear heart
                L "!!..."
                show lyney happy none
                L "I must say, I like it when you're straightforward to me, because that triumphs over all illusion and doubt."
                show lyney neutral question
                L "though I have to ask, are you sure?"
                show lyney neutral none
                L "what I mean is, are you sure the hidden side of me that doesn't sparkle as bright will be enough for you?"
            "I like the act, and I like you on stage.":
                show lyney neutral
                L "indeed, the stage is my home."
                show lyney happy heart
                L "and honestly, I love that you love it, really I do."
                show lyney neutral none
                L "but there's a difference between being loved for a trick and being loved for the person behind the trick."
        
        show lyney sad
        L "ah, sorry, I'm doubting myself again, aren't I?"
        show lyney sad
        L "…"
        
        Y "{i}Lyney steps closer to me, his eyes soft.{/i}"

        show lyney neutral
        L "if I'm honest, and I want to be honest with you…"
        show lyney sad
        L "…i spent so long practicing how to be someone else that I sometimes forget how to be me."
        show lyney neutral question
        L "do you remember when I told you about the mask, as in, the mask I would wear during my performances?"
        show lyney neutral none
        L "whenever I wore it, it was like I was able to transform into someone one, almost like magic, but at the expense of losing… me."
        show lyney neutral
        L "but I thought it was worth it, after all, the mask provided me with everything I needed to become the ideal magician."
        show lyney neutral
        L "the jokes, the glamour, even the magician's swagger…"
        show lyney disgust
        L "though it got to the point where I thought wearing my mask was the only way anyone would ever care about me…"
        show lyney sad sigh
        L "…or even love me."
        show lyney neutral none
        L "still, my sister Lynette and I learned to survive that way, and it worked."
        show lyney sad
        L "but inside… I felt… well, it was a different story."
        show lyney sad sigh
        L "…"

        menu:
            "are you okay?":
                show lyney neutral none
                L "nono, I'm alright, I'm only thinking."
            "take your time.":
                show lyney neutral none
                L "nono, its alright, I'm only thinking."

        show lyney neutral
        L "its just, over the past week, the investigation caused everything inside me to crack a little."
        show lyney neutral
        L "I wouldn't say the mask has fully broken, but at least enough for someone to reach past the cracks."
        show lyney happy heart
        L "and that someone is you. You reached past the cracks."
        
        menu:
            "you don't have to be a hero for me.":
                show lyney neutral none
                L "that's not what I was trying to say."
                show lyney neutral
                L "I never wanted to be someone who felt like saving something… or someone."
                show lyney neutral
                L "as a magician, I wanted to make people forget their worries and troubles for a while."
                show lyney sad sigh
                L "…including myself."
                show lyney neutral none
                L "but with you, I can stop pretending that forgetting is the only thing I can do to cope."
            
            "I like it that way. Because that makes you more real.":
                show lyney happy none
                L "haha, what a crazy thing to say, and yet you still manage to make me feel touched.."
                show lyney neutral
                L "but yes, the cracks…"
                show lyney neutral
                L "if we're speaking metaphorically here, they let light in."
                show lyney neutral glee
                L "and to me, light is the best kind of magic."
        
        show lyney neutral none
        L "…"
        
        Y "{i}slowly, Lyney takes my hand, his gesture is gentle.{/i}"

        show lyney neutral
        L "this should be the part where magicians usually do something impressive, to show off."
        show lyney neutral
        L "maybe pull out a bouquet of flowers, fireworks, dramatic lines, the whole lot."
        show lyney happy
        L "and believe me, I could, right now… but maybe not tonight."
        
        Y "if you want to perform now, I'll be in the audience and backstage."
        
        show lyney happy glee
        L "well, a magician always appreciates a good stage manager, hehe…"
        show lyney neutral none
        L "but I don't want a trick, nor do I want to hide both sides to myself anymore."
        show lyney happy
        L "orrr… maybe I want you to see both of them!"
        show lyney neutral
        L "when I perform, and equally when I'm learning how not to perform."
        show lyney neutral heart
        L "both are mine for you to hold dearly."
        show lyney neutral none
        L "but for now, no tricks, its just me and you."
        show lyney neutral
        L "I want to ask you something that will make my heart melt, in a way I've never felt before."
        show lyney neutral
        L "will you let me be… me? To be small and loud, but to also smile and cry…"
        show lyney happy question
        L "…to be by my side even when I'm not just a mere magician, and instead someone who wants to forget the subtle techniques of a little trick?"
        
        menu:
            "I'll stay for the whole show, and after as well.":
                show lyney happy none
                L "you have no idea how much that means to me."
                show lyney neutral
                L "and all this time, I had this preconception that I had to make myself into someone presentable, and some… thing, to be enjoyed."
                show lyney happy glee
                L "but you helped me to change that falsehood, because I can learn to let my mask rest sometimes."
                show lyney neutral none
                L "and maybe even leave it for good."
            "(lean in and kiss him)":
                show lyney fear heart
                L "!!..."
                show lyney neutral none
                L "…"
                show lyney happy
                L "that was… a lovely kiss."
                show lyney neutral
                L "perhaps actions really do speak louder than words, and you just showed me that."
                show lyney happy
                L "I could play out a thousand endings on the stage and none of them would feel like this."
            "I promise to be honest as well, so tell me when you need space.":
                show lyney happy glee
                L "honesty… haha, I would like that."
                show lyney neutral none
                L "to be honest, that's a magic trick in and of itself."
                show lyney happy heart
                L "…two lovebirds who don't have to perform for each other. It's a nice feeling, one that can already be made into reality."
        
        show lyney neutral none
        L "…there's one more thing."
        show lyney neutral
        L "all that supernatural stuff, with the visions and cyno's condition, believe it not but, it changed me."
        show lyney neutral
        L "it made me realise that hiding from myself never did anything good for me. It actually made me want something more steadier in my life, a constant."
        show lyney neutral glee
        L "so thank you. For choosing to see me who I am right now, which is just… me!"
        show lyney neutral none
        L "as for our next steps… well, we needn't worry."
        show lyney happy heart
        L "I'll be with you to work it out, by your side, always."
        show lyney neutral none
        L "think about it, the world is like a stage, big and loud."
        show lyney neutral
        L "but we can navigate it together using our own kind of magic."
        show lyney neutral heart
        L "and that's our love for each other."
        show lyney neutral none
        L "one that can break through any kind of illusion."
        show lyney happy
        L "and like I always say, seeing is believing."
        
        Y "what about right now?"
        
        show lyney fear question
        L "huh… now?"
        show lyney neutral none
        L "then… perhaps we can watch the night sky, for a while longer…?"

    elif chosen.name == "miku":
        stop music fadeout 1.0
        queue music heartwarming

        Y "{i}…?{/i}"
        Y "{i}i feel like I'm being approached by someone from behind.{/i}"

        show miku happy glee with dissolve
        M "hehe, its only me silly!"
        show miku neutral question
        M "I was wondering though, do you have some time now?"
        show miku serious none
        M "I…I wanted to take you somewhere, just the two of us."
        show miku serious heart
        M "…if that's okay with you?"

        menu:
            "of course, lead the way.":
                show miku neutral none
                M "thanks a lot!"
                show miku happy glee
                M "come on then, its not that far."
                show miku neutral none
                M "in fact, its actually here on campus."
          
            "is everything okay first?":
                show miku serious heart
                M "after everything, you still worry too much…"
                show miku neutral none
                M "I promise you, its nothing concerning."
                show miku neutral question
                M "just… please, come with me?"

        show miku neutral none
        M "I wanted to show you this place one more time before you leave."
        
        scene park cherry
        show miku
        with fade

        Y "{i}Miku lets go of my hand, and turns to face me beneath the cherry tree.{/i}"
        Y "{i}she sits down, gesturing for me to sit next to her.{/i}"

        show miku neutral
        M "do you remember the first time you came here to see me?"
        show miku happy question
        M "I talked a lot, didn't I?"
        show miku neutral none
        M "to be honest, it was the first time I ever opened up to someone like that."
        show miku serious
        M "…at least, as far as I can remember in my memories."
        show miku sad sigh
        M "…"
        show miku serious none
        M "listen, there's this dumb little rumour about this tree."
        show miku serious
        M "they say that if two people confess here, their feelings will stay true forever."
        show miku neutral
        M "so that means, if someone confesses their love, the two of them will love each other forever."
        show miku neutral heart
        M "…do you get where I'm going with this? Hehe…"
        
        menu:
            "confess? You go first.":
                show miku fear exclamation
                M "m-me?!"
                show miku embarrassed none
                M "you're asking the worst possible thing right now… but I'm not exactly opposed to it."
                show miku neutral
                M "alright then, I'll do it! just to humour you, but only on the count of three!"
                show miku neutral
                M "1…"
                show miku neutral
                M "2…"
                show miku neutral
                M "3…"
                show miku happy heart
                M "I love you!"

            "you don't need a rumour. Just say what's on your mind.":
                show miku neutral none
                M "okay… then here's the truth."
                show miku serious
                M "I'm tired of pretending I can handle everything on my own."
                show miku serious
                M "I want someone who knows my imperfections and accepts me for them regardless."
                show miku serious
                M "I want someone who will tell me when I'm being impossible…"
                show miku happy
                M "and most of all, I… love you."
        
        show miku embarrassed none
        M "saying that felt strange… heavy and light all at the same time."
        show miku neutral exclamation
        M "but, I don't regret it, not one bit!"
        show miku serious none
        M "…"
        
        menu:
            "what's on your mind now?":
                pass
            "are you hiding something else from me?":
                pass
        
        show miku neutral
        M "ahh, stop reading my mind! But yes, there is something."
        show miku neutral
        M "I was thinking, naoto probably told you I would come here to 'compose myself' or some nonsense…"
        show miku serious
        M "which… yes, is partially true. But also because I'd like to sit and wait here, hoping for my 'special someone' to arrive."
        show miku serious sigh
        M "its such a contrived fantasy, I know. especially since I didn't know how to lean onto others for support."
        show miku serious none
        M "but as student council president, it was kinda like a source of escapism."
        show miku neutral
        M "I always wanted to be special to someone."
        show miku neutral
        M "and I thought my life would finally have meaning if I was special to someone."
        
        menu:
            "I can always be your special someone.":
                show miku fear exclamation
                M "d-did I not make it obvious from the start, you already are!"
                show miku neutral heart
                M "but still, I really do appreciate it."

            "you're special to so many people already.":
                show miku fear question
                M "r-really? You think so?"
                show miku neutral none
                M "…haha, what am I even saying…"
                show miku happy glee
                M "of course you're right, we've got the supernatural investigation club after all."
        
        show miku neutral none
        M "look, there's something I need you to understand from all this."
        show miku serious
        M "me admitting that I love you isn't some kind of desperate attempt to place your future here, with me."
        show miku neutral heart
        M "althoughhh, I do expect you to keep pitching in with the investigation from time to time."
        show miku neutral none
        M "alright, I was kinda joking, but anyway, my point stands."
        
        menu:
            "I love you too, we don't need to tie each other together, but we shouldnt have to worry about growing apart either.":
                show miku happy glee
                M "hearing that makes me more hopeful than I already am."
                show miku neutral none
                M "its not like I needed someone's constant presence in the first place."
                show miku neutral
                M "I can still stand on my own too feet, but you probably know that by now!"
        
            "I don't want us to be a short term thing. I want to keep supporting you, through and through, despite the setbacks.":
                show miku neutral
                M "yeah! I guess that's what I didn't know I needed at first."
                show miku happy glee
                M "just knowing that someone will always have my back unconditionally."
        
        show miku serious none
        M "y'know, I kept telling myself that showing any form of weakness would cause everything to fall apart."
        show miku sad sigh
        M "so, I learned to suck it up."
        show miku serious none
        M "but over the last week, you watched me almost fall apart but still treat me like the same person."
        show miku serious
        M "it sounds stupid, but I thought it never made sense,, until I met you."
        show miku neutral heart
        M "and that changed everything."
        show miku neutral none
        M "so here's what I promise to myself and to you…"
        show miku neutral
        M "I will keep being responsible, and I will keep caring about the council, and about the student body."
        show miku neutral
        M "but I am gonna change how I carry that weight going forward."
        show miku neutral
        M "and on top of that, I will let people help me."
        show miku happy glee
        M "that's on me!"

        menu:
            "that's what I want for you.":
                show miku neutral none
                M "thank you, that's exactly the point of why I'm making this promise."
                show miku happy
                M "which is to become someone more honest, because I also want to show that I can be imperfect too."
            "I'll still be here for if you do need me.":
                show miku happy none
                M "you saying that means a lot to me."
                show miku neutral
                M "even if its just for small things, that doesn't matter, not to me."
            "(pull her into a hug)":
                show miku fear heart
                M "!!..."
                Y "Miku melts into my hug in a heartbeat, almost as if she needed it more than anything."
                show miku neutral none
                M "this is nice…"
                show miku happy
                M "thank you for the gesture, hehe!"
        
        show miku neutral
        M "there's another thing we haven't quite said yet."
        show miku serious
        M "that is, you'll be leaving soon… since your transfer's already been finalised by me."
        show miku serious sigh
        M "I didn't want tonight to be about that though, but I wanna keep being honest with you, that's why I'm saying all these things now before… well, y'know."
        
        menu:
            "I'm here now. Lets enjoy the night while it lasts!":
                show miku neutral glee
                M "mhm! That's exactly what I wanted!"
                show miku happy none
                M "stay with me for this night, and that'll be more than enough for me."
                show miku happy heart
                M "…anddd hopefully for you as well, hehe!"
            
            "we can be intentional, however it may unfold.":
                show miku neutral glee
                M "sure! That suits us pretty well."
                show miku happy none
                M "we'll do what we can with the time we have left."
                show miku neutral
                M "and as for the rest, we don't have to pretend anything."
        
        Y "Miku offers me her hand."
        show miku neutral
        M "well, its about time we head back to the rooftop."
        show miku angry vein
        M "if I'm right, the party will already be in chaos without me supervising…"
        show miku neutral none
        M "though before we go, I just wanna say one more thing."
        show miku neutral
        M "I don't want to be dramatic, but I still want you to remember this…"
        show miku happy heart
        M "you helped me realise I can trust people, and that I could ask for help and not feel guilty for it."
        show miku neutral none
        M "it sounds so simple at the end of the day, but I wouldn't have dared think about it when I first took up council president."
        show miku neutral exclamation
        M "so, yeah…! that's the most important thing you have given me."
        show miku happy glee
        M "…and because of that, I'm filled with so much love and gratitude for you."
        show miku neutral none
        M "so when you go home and do your own thing. But please know this."
        show miku neutral
        M "whoever I am when you return, it will be the result of my own choices, as well as the kindness and support I have let into my life."
        show miku embarrassed
        M "this isn't me asking you to be my future, so don't think of it like that silly!"
        show miku neutral glee
        M "…instead, I hope you can be part of a better present, for the both of us…"
        show miku happy none
        M "now come on, lets go, honey!"

    elif chosen.name == "cyno":
        stop music fadeout 1.0
        queue music heartwarming

        Y "{i}…?{/i}"
        Y "{i}i feel like I'm being approached by someone from behind.{/i}"

        show cyno happy with dissolve
        C "{cps=4}yo.{/cps}"
        show cyno embarrassed sigh
        C "oh, did I catch you off guard? My bad…"
        show cyno neutral question
        C "anyway, you look quite lost in thought there, do you need a game to distract you?"
        
        menu:
            "I'm craving a round of cards-":
                show cyno happy sparkles
                C "haha, great minds think alike."
            "what are you thinking?":
                show cyno neutral none
                C "hmmm.."
                show cyno happy
                C "maybe another game of cards before you have to leave, just one last round of course."
        
        show cyno happy question
        C "in that case, fancy playing something a little more interesting than blackjack?"
        show cyno happy exclamation
        C "I'm talking poker, in the casino lounge, with actual stakes involved!"
        show cyno happy none
        C "so… what do you say?"
        
        menu:
            "bust… or maybe I'll take it all!":
                show cyno fear
                C "I wouldn't say the stakes are THAT extreme-"
                show cyno fear
                C "don't tell me you're some kinda compulsive gambler…"
            "I'm too broke to gamble..":
                show cyno neutral
                C "you don't know what broke feels like unless you're in the genshin society and used all the club funds and personal savings on primogems just to lose your 50/50 at hard pity."
        
        show cyno neutral
        C "anyway, think of it like a test of our relationship."
        show cyno embarrassed
        C "besides, I'm not any good at farewells, so this is the best you're gonna get from me-"
        
        show sparrow freaky at left with dissolve
        Sp "CYNOOOOOOOO~"
        show cyno angry vein
        C "…"
        show cyno disgust none
        C "what?"
        show sparrow fear
        Sp "n-not even a hello from my senpai?!"
        show sparrow neutral
        Sp "nevermind, that doesn't matter right now-"
        show sparrow neutral
        Sp "what I've come to tell you is that I'm now a major investor of this university!"
        show cyno neutral
        C "okay…?"
        show sparrow fear
        Sp "HUH?! NOT EVEN AN OUNCE OF EXCITEMENT?!"
        show cyno disgust question
        C "what do you want me to say then?"
        show cyno angry vein
        C "congrats, you just wasted a fuck ton of money donating to an institution that rejects groundbreaking research and downplays what's going on in the real world."
        show sparrow neutral
        Sp "well… uhm… I-I suppose you're right!"
        show sparrow freaky
        Sp "but all is not lost, for I have had enough power to introduce a heavy entry fee for incoming exchange students like him…"
        show sparrow freaky
        Sp "so next time you question the point of a tax apprenticeship, THINK AGAIN!"
        show sparrow fear
        Sp "…WHAT?! YOUR TRANSFER HAS ALREADY BEEN FINALISED?! BUT HOW CAN THIS BE??"
        show cyno disgust sigh
        C "ugh… c'mon, let's just get out of here."
        
        "{i}Cyno grabs hold of your hand without thinking.{/i}"

        show sparrow neutral
        Sp "……..?"
        show sparrow freaky
        Sp "c-c-c-c-cyno? ngh~"
        show sparrow neutral
        Sp "I-I-I-I mean, what do you think you're doing?"
        show cyno neutral question
        C "what do you think it looks like?"

        show cyno -question
        menu:
            "we're kinda boyfriends-":
                show sparrow fear
                Sp "…what-….I-…..no….n-n-n-n-no….."
            "{i}(stay silent){/i}":
                show sparrow fear
                Sp "…no… d-d-don't tell me…"
                show sparrow sad
                Sp "I'd much rather live a lie of falsehoods than face this cruel reality."
        
        show sparrow sad
        Sp "…"
        show sparrow angry
        Sp "RAGHHHHHHHHHHAAAAAAHAAAAHAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH!"
        Sp "{i}collapses{/i}"
        show cyno neutral
        C "…damn."
        
        stop music fadeout 1.0
        queue music hangout

        scene casino
        show cyno
        with fade
        
        show cyno neutral
        C "you ready?"
        
        menu .casino:
            "ya":
                show cyno happy sparkles
                C "good. Then lets begin."
            "na":
                show cyno sad sigh
                C "…"
                Y "{i}something in cyno's face is urging me to reconsider.{/i}"
                jump .casino

        show cyno neutral none
        C "if you don't know the rules, then for plot convenience just look them up on google or something."
        
        call poker from _call_poker

        stop music fadeout 1.0
        queue music heartwarming

        scene city night
        show cyno
        hide screen poker_ui
        with fade

        Y "{i}Me and Cyno walk out of the casino lounge.{/i}"

        show cyno happy glee
        C "hey, thanks for the game, I do appreciate it."
        show cyno embarrassed none
        C "i'll admit, you had me on the edge of my seat."
        show cyno happy
        C "so for that, I'd say you're a pretty good player."

        menu:
            "I've played these games before.":
                show cyno sad question
                C "oh? Have you secretly been training under someone else this whole time?"
                show cyno happy none
                C "hah, only joking."

            "it was purely guesswork-":
                show cyno neutral
                C "you're far too modest."
                show cyno happy
                C "either way, you put up a good fight, and that's what counts."
        
        show cyno neutral
        C "y'know… I find games like poker to be a good mirror in a sense."
        show cyno neutral
        C "people try to read each other. Sometimes theyre right, and other times theyre not."
        show cyno happy
        C "I could see it in your face… you practically gave it all your all."
        show cyno happy glee
        C "that… mattered to me."
        show cyno happy heart
        C "…if you get where I'm trying to go with this."
        
        menu:
            "you opened up first!":
                show cyno neutral none
                C "maybe, but I'm not one to use words to convey how I'm feeling."
                show cyno happy
                C "you've certainly got a keen eye to notice my intentions."
          
            "teach me genius invocation TCG next time-":
                show cyno happy none
                C "next time… yes, of course."
                show cyno neutral exclamation
                C "its kinda my specialism, so don't expect me to go easy on you!"
           
            "{i}(reach out and take his hand){/i}":
                show cyno fear exclamation
                C "!!..."
                show cyno fear none
                C "your hand…"
                show cyno fear question
                C "its… warm?"
                show cyno neutral none
                C "a nice temperature indeed."
       
        stop music fadeout 1.0
        queue music sentimental

        show cyno neutral none
        C "…"
        show cyno neutral question
        C "before we go back, do you have a moment to spare?"
        show cyno sad sigh
        C "there's been… things, on my mind over the past week."
       
        menu:
            "You don't have to ask!":
                pass
            "of course-":
                pass
        
        show cyno neutral none
        C "hm, where do I start?"
        show cyno neutral
        C "before you arrived, there was no sign my condition would ever get better, and I used to think the world would be better off without me."
        show cyno neutral
        C "when my 'episodes' started, I more or less convinced myself that I was a problem, and nothing more."
        show cyno sad
        C "and I thought…"
        show cyno sad sigh
        C "…"

        menu:
            "take your time.":
                pass
            "is everything okay?":
                pass

        show cyno neutral none
        C "hm."
        show cyno sad
        C "I thought maybe… ending it all… would be an act of mercy for everyone else."
        show cyno sad
        C "it sounds dramatic saying it now, and even more so out loud."
        show cyno neutral
        C "but that doesn't change how I felt before."
        
        menu:
            "you were never a burden to me.":
                show cyno neutral
                C "people always say that for the sake of saying it."
                show cyno happy
                C "but you… you're different."
                show cyno happy
                C "every word you say comes from a place of sincerity, and I know that from spending time with you."
                show cyno happy glee
                C "so, thank you."

            "you're still here, and that matters so much.":
                show cyno fear heart
                C "that's… the kind of thing I never thought I'd hear."
                show cyno neutral none
                C "I used to think otherwise, but you've managed to help change my outlook of things."
                show cyno happy glee
                C "so, thank you."
        
        show cyno neutral none
        C "in retrospect, getting this far feels like proof."
        show cyno happy
        C "proof that I can be more than this condition, and more than a weight on someone's shoulder."
        show cyno happy
        C "proof,, that someone actually wants me here."
        
        menu:
            "I don't need to fix you, I'll still be here for you.":
                pass
            "I stayed because you're the best person ever.":
                pass
        
        show cyno fear exclamation
        C "partner…"
        show cyno happy none
        C "that's the best thing anyone's ever said to me."
        stop music fadeout 1.0
        queue music heartwarming
        show cyno happy heart
        C "I… I love you."
        show cyno fear none
        C "…wow, I managed to say it this time."
        
        menu:
            "{i}draw him close to you{/i}":
                show cyno sad
                Y "{i}Cyno tears up a little, he grips onto me for a moment, then pulls back.{/i}"
            "{i}caress his cheek{/i}":
                show cyno embarrassed
                Y "{i}Cyno looks at me with warmness in his eyes, blushing slightly.{/i}"

        show cyno neutral
        C "I don't tend to engage in physical contact…"
        show cyno happy glee
        C "but that was nice, thank you."
        show cyno neutral none
        C "…one last thing, and don't tell the others, at least not right now."
        show cyno neutral sigh
        C "but… you can call me cyno dohguh if you want. That's my full name."
        
        menu:
            "cyno DOG?":
                show cyno angry question
                C "DO YOU HAVE SOMETHING AGAINST DOOOOOOOOOOOOOOOOOOOOOOOGGGGGGGGGGGGGGGGGGGGGGGGSSSSSSSSSSSSSSSSSSSSS"
                
           
            "I love you so much.":
                show cyno fear exclamation
                C "!!..."
                show cyno fear question
                C "y-you love my last name?"
                show cyno neutral none
                C "that's… definitely something."
            
            "I'm changing my legal name to jack dohguh now.":
                show cyno neutral none
                C "so you wanted it for marriage purposes all this time."
                show cyno happy
                C "hah, how ironic."
        show cyno happy none
        C "but good, make it embarrassing. I deserve that for not telling you until now."
        show cyno neutral
        C "…well? Shall we get heading now?"
        show cyno happy question
        C "I still want to enjoy some final moments with you, if that's okay with you?"

    elif chosen.name == "naoto":
        stop music fadeout 1.0
        queue music heartwarming

        Y "{i}…?{/i}"
        Y "{i}i feel like I'm being approached by someone from behind.{/i}"

        show naoto neutral exclamation
        N "Oh, its you!"
        show naoto embarrassed none
        N "Sorry… considering the circumstances, I'm not sure how best to approach you on a night like this-"
        show naoto neutral question
        N "…so is it okay if I could borrow a minute of your time."
        
        menu:
            "Yes!":
                pass
            "Of course!":
                pass
        
        show naoto happy glee
        N "Thank you."
        show naoto neutral none
        N "However I don't know if right here is the place to do so."
        show naoto neutral question
        N "So, may I ask to take you on one last adventure? Just around the school I mean."
        
        menu:
            "You don't have to ask!":
                show naoto happy none
                N "sorry, the illusion of choice is nice."
            "Yea sure-":
                show naoto happy none
                N "Very well, then follow me!"

        scene hallway evening
        show naoto
        with fade

        show naoto neutral
        N "This must of been what gave you your first impression of the school."
        show naoto happy
        N "at least, I know for me it did."
        
        menu:
            "this hallway is very unremarkable..":
                show naoto neutral
                N "I suppose, but sometimes there's value in actively trying to find what interests you, even if its not that appealing at first."
            
            "ah the good old days!":
                show naoto neutral
                N "It has only been a week really."
                show naoto happy
                N "But with all these fleeting emotions I understand the feeling of nostalgia that it gives."
                show naoto happy
                N "Like, wanting to be in a time loop and start it all over a fresh."
        
        show naoto neutral
        N "But in the end, I guess this isn't going to be your most memorable location that you've visited thus far."
        show naoto neutral
        N "Hmm lets go see the next then!"
        
        scene library
        show naoto
        with fade
        
        show naoto happy question
        N "Surely you must have more fond memories here?"
        
        menu:
            "Yea, that day had a lot of reading!":
                show naoto neutral none
                N "Well, this is a library-"
            
            "This was the longest day of my life..":
                show naoto neutral none
                N "It was a lot to take in at the time."
                show naoto embarrassed sigh
                N "and ironically most of that information was not that useful."
                show naoto neutral none
                N "But that's researching I guess!"
       
        show naoto happy thought
        N "This day felt like a turning point for the club!"
        N "Things began to look up for us, we started to figure things out."
        
        show naoto neutral sigh
        N "In hindsight though, knowing we were looking at it the wrong way…"
        
        menu:
            "that time was still valuable.":
                show naoto happy glee
                N "hehe"
                show naoto happy none
                N "You are correct indeed."

            "Our understanding of our world was tested, we tried to solve it at least.":
                show naoto neutral none
                N "This experience has made me think deeply about many things."
                show naoto happy glee
                N "And I am glad to have, actually."
        
        show naoto happy none
        N "You know, I've always loved the concept of a library, a vault of knowledge!"
        show naoto neutral thought
        N "so many topics to be understood…"
        show naoto embarrassed none
        N "If we stay any longer I may get carried away unfortunately."
        
        scene classroom evening
        show naoto
        with fade

        show naoto happy glee
        N "The most isolating place you've been in!"
        show naoto embarrassed sigh
        N "Sorry, that sounded grim."
        show naoto neutral none
        N "Classrooms to me feel empty however, even surrounded by people."
        show naoto neutral
        N "I feel as if I am not approachable in lectures-"
        show naoto neutral
        N "Whether that be because of my dedication to the lecture or my moreso formal and cold exterior, I don't know."
        show naoto happy
        N "I'd hope its the first."
        
        menu:
            "I don't talk to people in lectures anyway.":
                show naoto neutral thought
                N "I can recall the only lecture we had together, you were asleep."
                show naoto happy glee
                N "It was quite cute."
                show naoto neutral none
                N "Really, I'm not sure what purpose lectures were to you, especially as you jumped between courses a lot."

            "Of course its the first one! You give your all in your studies!":
                show naoto happy
                N "I do try my hardest."
                show naoto embarrassed
                N "Sometimes at the expense of a social life-"
                show naoto happy
                N "But now I have someone like you,i don't have to worry about people not wanting to talk to me."
        
        show naoto neutral
        N "Alas, maybe now we should head elsewhere."
        
        scene classroom 2
        show naoto
        with fade

        menu:
            "A new classroom! Full of possibilities, reflective of the future!":
                show naoto embarrassed question
                N "aaa, are you mocking me?"

            "Where the hell are we?":
                show naoto neutral exclamation
                N "Somewhere new! Although I'm not really sure."

        show naoto happy
        N "New places to me makes me feel… safe."
        show naoto neutral
        N "I feel like I have no standards and nobody around be has expectations of me."
        show naoto neutral
        N "I am but a stranger who they will never meet again."
        show naoto happy
        N "That ability to feel so much like yourself when you are not known…"
        show naoto neutral thought
        N "I wonder if that really is me or just some idealised verision with greater confidence."
        show naoto neutral none
        N "Because in the end, I do care about my image to an extent."
        show naoto happy
        N "I want to be liked, and in terms of my detective work, admired."
        
        menu:
            "I admire you!":
                show naoto embarrassed exclamation
                N "Ah, that's almost weird to believe.."
                show naoto happy none
                N "All the time we have spent together, I saw you as an ally but I am flattered you look up to me."

            "Soon the world will know your name.":
                show naoto fear question
                N "Are you being serious? I wouldn't know how to comprehend that…"
                show naoto neutral none
                N "well… Fame in this field is a positive."
                show naoto neutral
                N "But in all honesty I hope to make marks in my community first."
                show naoto happy
                N "Like how you have with this club."
                show naoto happy glee
                N "You've become a staple and no one could ever forget you!"
                show naoto neutral thought
                N "It makes me feel sentimental thinking about it."
        
        show naoto embarrassed sigh
        N "Ah, sorry, I'm being overcome by my emotions."
        
        menu:
            "Its okay, I'm here!":
                show naoto happy none
                N "Thank you!"
                show naoto embarrassed heart
                N "Although you may be the problem."

            "Wow, do I make your heart flutter that much?":
                show naoto happy none
                N "It doesn't take much to woo me."
                show naoto embarrassed heart
                N "and unfortunately I think you've subconsciously figured that out."
        
        show naoto happy
        N "I want to embrace this feeling."
        
        menu:
            "Should we wrap up the tour?":
                pass
            "lets take a break.":
                pass
        
        show naoto neutral
        N "Certainly!"
        show naoto sad
        N "..."
        show naoto sad sigh
        N "Now it feels like I have nothing to say."
        show naoto neutral none
        N "That tour I suppose was a way for us to reflect on the places you've been during your time here."
        show naoto neutral thought
        N "I feel I am someone who thinks a lot. And if I was in your position this is probably what I would have done to conclude my stay."
        show naoto neutral none
        N "It's like moving to a new house and viewing all the empty rooms, once full of life, soon die down."
        show naoto neutral
        N "And then the hustle and bustle of a home is gone, empty as it waits for its next family."
        show naoto happy
        N "Or maybe, I just wanted the adventure experience with you again."
        
        menu:
            "We achieved both, didn't we?":
                show naoto happy
                N "well yes, both of my desires aren't mutually exclusive, we can have a fun adventure and reflect! that's just life."
                show naoto fear
                N "Although I hope you enjoyed it aswell, I fear that I may have orientated this to be more focused on me rather than you."
            
            "I am glad you took me on that tour.":
                show naoto happy
                N "I'm glad you enjoyed it to even some extent. I hope its something from this chapter of your life that you'll remember."
        
        show naoto happy
        N "Thank you for letting me do this."
        show naoto happy glee
        N "I feel that its provided me with a lot of clarity."
        show naoto embarrassed sigh
        N "I still have so much to say to you yet every minute it seems I'm losing it quicker than the last!"
        show naoto sad sigh
        N "And when I panic my words, it's as if they start to not make sense-"
        
        menu:
            "Just say what's on your mind!":
                pass

            "Its okay, say the words and I'll make sense of them-":
                show naoto fear exclamation
                N "...!"
        
        show naoto happy none
        N "Thank you, I will try."
        show naoto neutral question
        N "So… where do I even begin?"
        show naoto neutral none
        N "Through this entire experience I've been made to test my understanding and also my own perception on situations."
        show naoto neutral
        N "What I feel I've learnt is to never settle on one answer, because you never can."
        show naoto neutral
        N "Yet the one thing I could decide was probably the most impactful of all."
        show naoto happy
        N "Who I choose to surround myself with!"
        show naoto neutral
        N "Since I choose to be in the club and more importantly-"
        show naoto happy heart
        N "since I choose to be with you.."
        show naoto neutral none
        N "In the span of a week the club has flipped my perception of reality as we know it."
        show naoto sad sigh
        N "None of us have truly reflected on it but that possibility is frightening."
        show naoto neutral none
        N "yet something grounds me knowing I have people-"
        show naoto happy glee
        N "No, more specifically I have you."
        show naoto happy none
        N "You've been the constant force that has surrounded be during the chaotic day to day."
        show naoto embarrassed
        N "I often feel like I end up day dreaming about you when I'm working on school council activities."
        show naoto happy
        N "When your in the club with me, I know I have someone by my side."
        show naoto happy sparkles
        N "That's all I could really ask for in a partner."
        show naoto happy glee
        N "I would never want you to be a secondary to me, or live in my shadow or anything!"
        show naoto neutral none
        N "But the time we have spent together has created a duo that works."
        show naoto happy
        N "I'll always see you as an equal."
        show naoto happy
        N "More than that even, maybe like my other half."
        show naoto happy
        N "Thank you for completing me."
        
        menu:
            "I will always!":
                pass
            "you do the same to me.":
                pass

        show naoto embarrassed
        N "…"
        show naoto neutral
        N "again I've lost my words…"
        
        menu:
            "Don't worry, just live through this moment!":
                pass
            "we don't need words right now.":
                pass

        show naoto embarrassed        
        "{i}naoto appears to be blushing.{/i}"

        menu:
            "{i}Place your head on her shoulder{/i}":
                show naoto fear exclamation
                N "...!"
                show naoto embarrassed none
                N "I hope that's comfortable, considering our height difference."

            "{i}Place her head on your shoulder{/i}":
                show naoto fear exclamation
                N "...!"
                show naoto embarrassed none
                N "Sorry, that just caught me by surprise."
        
        show naoto happy
        N "But this is nice."
        show naoto happy glee
        N "This was the moment I feel I needed."
        show naoto neutral none
        N "After every big moment you have in life, the moments of quite are the ones that ground you."
        show naoto neutral
        N "There feels like no better time to say this."
        show naoto happy heart
        N "I love you."
        show naoto happy none
        N "Such simple words, but I feel they encapsulated everything."

        menu:
            "I love you too naoto.":
                show naoto happy glee
                N "Hearing it said back makes it feel surreal."
            
            "{i}put your arm around her{/i}":
                show naoto fear
                N "oh, I've never been held like this before."
                show naoto happy
                N "though It feels very comforting."
            
            "{i}Kiss her on the head.{/i}":
                show naoto fear
                N "!"
                show naoto happy
                N "oh that felt…"
                show naoto embarrassed exclamation
                N "I-I- mean, that was nice!"
                show naoto embarrassed question
                N "erm… how do I go about doing this?"
                show naoto neutral
                N "…"
                "{i}She kisses you back.{/i}"

        show naoto happy none
        N "this moments feels like a fantasy really, I don't want it to end."
        Y "It doesn't have to yet, lets cherish this moment."
        show naoto happy
        N "I would want nothing more than just that."
        show naoto happy question
        N "but there's one more thing I'd like to do, if you don't mind-"
        
        scene office evening
        show naoto
        with fade
        
        show naoto neutral
        N "please, take a few of these bags."
        show naoto neutral
        N "and come with me to the insane asylum!"
        show naoto neutral
        N "or rather, the homeless shelter."

        scene asylum
        show naoto
        with fade
        
        Y "{i}Me and Naoto go to deliver bags of food donated by the students for the homeless.{/i}"
        N "Stay by my side, please, now and always."

    scene black with fade
    Y "{i}everyone's heart is connected to the people they know and trust.{/i}"
    Y "{i}it's those bonds…{/i}"
    Y "{i}the kind of bonds that let us all search for our purpose in life.{/i}"
    Y "{i}as long as it's a purpose you believe in…{/i}"
    Y "{i}then there will always be someone who can help you fulfil it.{/i}"
    Y "{i}me, them, and everyone else…{/i}"
    Y "{i}there are no barriers.{/i}"
    Y "{i}our hearts are one.{/i}"
    Y "{i}…and thus completes my project, to form strong connections with people.{/i}"
    
    ">> you have reached the good ending."

    $ renpy.set_return_stack([])
    return
    



# scara cyno naoto lyney miku sparrow
