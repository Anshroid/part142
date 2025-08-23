label day7:
    call screen calendar(7) with fade

label day7morning:
    play music main

    show screen top_right_ui(7, "Morning")
    scene roof day
    show miku at r51
    show lyney at r52
    show cyno at r53
    show naoto at r54
    show scara at r55
    with fade

    show miku serious
    M "thank you all for coming at such short notice."
    show miku serious
    M "This will be our last chance to meet together before his transfer is finalised later this evening."
    show miku sad
    M "and to be honest, this may be our last ever meeting as the supernatural investigation club"
    show lyney fear
    L "huh? Are you saying that we're disbanding as a group, just like that?"
    show miku serious
    M "that's not what I meant, its just… after yesterday, I feel like this club has lost a lot of its purpose."
    show miku sad
    M "Its only a matter of time until I will be forced to shut it down."
    show naoto neutral sigh
    N "indeed, our presentation is still met with… well, profound disbelief."
    show naoto neutral -sigh
    N "The administration in particular refuses to acknowledge anything beyond the status quo."
    show naoto sad
    N "Its like we're the only ones who aren't afraid to admit that something is deeply wrong."
    show cyno disgust
    C "and now more than ever, all our evidence that we've gathered adds up."
    show cyno angry vein
    C "Still, they're dying to prove us wrong."
    show cyno -vein
    L "maybe they want to believe we're wrong. Its easier than accepting the truth."
    N "or maybe they're just too afraid of the consequences of funding something like this."
    N "if they admitted right then and there that we were right, everything they know would collapse!"
    N "but still, us discussing this doesn't change anything."
    show scara neutral
    S "maybe you guys might finally understand."
    show lyney angry
    L "what's that supposed to mean?"
    show scara neutral
    S "that everything we're 'investigating' is just an elaborate tapestry of falsehoods and speculation."
    show scara neutral
    S "To continue our argument now is just pure ignorance."
    show miku angry vein
    M "scara?! The nerve!"
    show scara neutral
    S "I rest my case."
    show miku -vein
    show scara neutral
    S "at the end of the day, if you keep this up, you'll all end up chasing answers because you want to see them."
    show lyney angry
    L "hey… this was never about what we 'wanted' to see in the first place."
    show scara angry
    S "no, its about what you refuse to admit."
    show cyno angry
    C "enough already, I'm already getting tired of this pointless arguing!"
    show miku serious
    M "look scara, I get it, we're all upset, and I know you were never that interested in the investigation in the first place."
    show miku sad
    M "but you were never like this before, at least not THIS bad."
    show miku angry vein
    M "I mean, c'mon… one moment of failure and you already turn your backs and call everything we've done \"ignorance?\""
    show scara disgust
    S "I'm afraid you're exaggerating a little."
    show miku -vein
    show scara angry
    S "yesterday just confirmed to me how pointless this all is, despite everything, nothing has changed and will ever change."
    show scara angry
    S "I'm only saying this so you guys stop wasting your time now!"
    show miku angry
    M "ugh, I seriously can't be dealing with you any longer!"

    menu:
        "you can't disprove everything we've found.":
            show scara neutral
            S "hmph, speak for yourself."
        "scara's just trying to be realistic right now.":
            show miku angry
            M "you seriously can't be siding with him as well!"

    show miku sad
    show lyney sad
    show naoto angry
    N "guys, its not worth fighting over now."
    show naoto neutral
    N "putting personal feelings aside for a moment, the one thing we all have to accept is that our findings and interpretation of events we have experienced thus far are not going to get validation from outside of us."
    show lyney sad sigh
    L "…it really is just us then."
    show naoto sad
    show lyney -sigh
    N "it always has been. The only difference now is that we know for sure."
    show cyno sad
    C "so what now? Right now we can't rely on anyone else to take us seriously, even with my condition."
    show miku serious
    M "we just have to prove it ourselves, however long that may take."
    show lyney neutral
    L "right! Especially now that we're closer than ever, I just feel it."
    show naoto neutral
    N "a feeling is not necessarily proof though."
    show naoto neutral thought
    N "though I won't deny the evidence keeps piling up, what we're missing is where it points to, and I don't just mean the universe."
    show cyno neutral question
    C "then what?"
    show naoto sad -thought
    N "i… don't know."
    show cyno -question
    show naoto neutral
    N "at least, its not something we can find out right now."
    show naoto disgust
    N "worst case scenario its something we will never be able to understand in our lifetime."
    show miku sad
    M "naoto…"
    show naoto neutral
    N "what? I'm only trying to be logical."
    show miku serious
    M "and that's the problem."
    show lyney sad sigh
    L "uhm, excuse me for a moment, I just need a minute or two."
    hide lyney with dissolve

    show cyno disgust
    C "me too, I need a breath of fresh air."
    show miku serious question
    M "but we're already on the rooftop?"
    show cyno disgust
    C "…"
    show miku serious -question
    M "oh, right."
    hide cyno with dissolve

    show miku sad
    M "well in that case, I'll take a moment for myself as well."
    hide miku with dissolve

    show scara angry
    S "hmph. Well if you guys have nothing to say, then I may as well take my leave."
    hide scara with dissolve

    show naoto sad
    N "hm…"
    hide naoto with dissolve

    Y "…"
    Y "{i}I can't help but notice the group slowly tearing apart.{/i}"

    stop music fadeout 1.0

    Y "{i}perhaps it might be best to talk to everyone privately.{/i}"
    
    default endingtalked = set()

    menu .endingtalk:
        set endingtalked

        "who should I talk to?"

        "cyno":
            queue music sentimental

            show cyno neutral with dissolve
            C "hi."
            show cyno neutral heart
            C "…thanks for looking out for me, I appreciate your concern."
            
            "{i}Cyno looks like he's been holding his breath.{/i}"

            show cyno sad -heart
            C "look, I didn't mean to leave like that. It just… hurt."
            show cyno neutral
            C "I had nothing but high hopes for the presentation, because I thought my condition might finally be recognised and understood."
            show cyno sad sigh
            C "now faced with rejection that affects how I'm able to live my life going forward, and by extension the rest of you, I'm not so sure how to cope."
            
            menu:
                "you don't have to carry this all alone.":
                    show cyno disgust -sigh
                    C "hmph. You're making me sound soft."
                    show cyno neutral
                    C "but still. Thanks. To be honest, I'm getting quiet tired of being the cause of concern to all of you."
                    show cyno neutral
                    C "and then I keep thinking that if I choose to admit it, everything will fall apart."
                    show cyno happy
                    C "but hearing you say that helps. Next time I'll try not to push you guys away as quickly."
                
                "do you want to keep believing in any of this?":
                    show cyno sad -sigh
                    C "I'm not sure. Before you arrived, I wasn't sure how to make sense of any of this."
                    show cyno neutral
                    C "but I feel as if that's changed recently, like I'm understanding everything about myself slowly but surely."
                    show cyno neutral
                    C "even if its not real in the right way, I choose to remember these memories and believe that something's wrong with me. And that's something."
                    show cyno happy
                    C "and with that, I guess I can stand by that, and you, even if I'm afraid."
            
            Y "{i}…{/i}"
            Y "{i}…?!{/i}"

            stop music fadeout 1.0
            
            Y "{i}I feel a surge of memories rushing inside my head.{/i}"
            
            scene black with fade
            
            C "we aren't meant to be here-"
            C "jack… where did you send us?"
            J "IDK!"
            J "can you get us back to the ship-"
            Q "Welcome, you both."
            C "nanook…"
            C "…NANOOK!"

            scene roof day 
            show cyno fear exclamation
            with fade
            
            C "!!..."
            show cyno disgust -exclamation
            C "from your expression, I can tell you felt something too."
            show cyno disgust
            C "nanook… them again."
            show cyno neutral
            C "I can't shake the feeling that they play a role in all the memories we have experienced."
            show cyno neutral
            C "but in time, perhaps we will find out."

            hide cyno with dissolve
            jump .endingtalk

        "miku":
            queue music sentimental

            show miku sad with dissolve
            M "oh, hey…"
            show miku serious
            M "sorry about earlier, I don't like to be angry in front of others."

            "{i}Miku looks like she's trying to be composed.{/i}"
            
            show miku sad
            M "I know its not an excuse, but its because I'm scared."
            show miku serious
            M "if the club shuts down, then I'm not so sure how I'll cope after everything we've been through."
            show miku serious
            M "it was never just a project to me. Its more than that. And I hope you feel the same as well."
            
            menu:
                "you've done everything you could. That counts.":
                    show miku serious
                    M "yeah, I suppose you're right."
                    show miku neutral glee
                    M "that means a lot actually… hehe."
                    show miku neutral -glee
                    M "I don't wanna overstep my expectations, but hearing you say that makes me feel less like I failed."
                    show miku happy
                    M "okay, I'll keep working hard on this. But I need you and everyone else with me first!"
                
                "I'll back you all the way, you don't have to do this alone.":
                    show miku serious question
                    M "wow, you'd do that for me?"
                    show miku neutral glee
                    M "thanks, that means a lot actually… hehe."
                    show miku neutral -glee
                    M "if you stand with me, then maybe I can be better than who I already am."
                    show miku neutral
                    M "fine. Together, we'll make this right, because at the end of the day it matters to all of us."
            
            Y "{i}…{/i}"
            Y "{i}…?!{/i}"

            stop music fadeout 1.0

            Y "{i}I feel a surge of memories rushing inside my head.{/i}"

            scene black with fade
            
            M "you have the audacity to be here, to EXIST all this time…"
            M "do you not have any regret?"
            J "you've got it all wrong… I will end the suffering."
            M "you… youre the cause of our suffering…"
            M "YOU LIED TO US. ALL THIS TIME I WAS STANDING BESIDE A MURDERER."
            J "…murderer?"

            scene roof day 
            show miku fear exclamation
            with fade 

            M "…w-what?!"
            show miku fear question
            M "that wasn't just me right? You felt that too? Almost like we were both together in that moment, right then and there."
            show miku sad -question
            M "that… that was terrifying. I don't wanna believe in anything I said."
            show miku sad
            M "but if we choose to accept these memories as real, then…"
            show miku serious exclamation
            M "we'll just have to keep pushing!"

            hide miku with dissolve
            jump .endingtalk

        "lyney":
            queue music sentimental

            show lyney neutral with dissolve
            L "hi there!"
            show lyney sad sigh
            L "I have to say, now's not a good time."

            "{i}Lyney looks quite vulnerable.{/i}"
            
            show lyney sad -sigh
            L "y'know, I get the impression that everything we've experienced is like a trick of fate."
            show lyney disgust
            L "as in the show had a script that explained everything, but now I don't know where to find it."
            show lyney angry question
            L "and if that's well and truly gone, then what am I in all of this?"
            
            menu:
                "your choices make you who you are, not a grand narrative.":
                    show lyney neutral glee
                    L "oho, an existential line I hear."
                    show lyney neutral -glee
                    L "but seriously, you're quite right. Our experiences… our memories, they're way more than something that needs to be explained."
                    show lyney neutral
                    L "I, we, can create meaning in all of this, we'll rewrite this story on our own terms."
                    show lyney happy
                    L "haha… alright, I'll stop being so angsty for now."
                
                "so what if people don't believe in the 'magic?' Lets keep it special to us.":
                    show lyney happy glee
                    L "haha, yes,, I quite like that idea."
                    show lyney neutral -glee
                    L "not everything needs a spotlight. If at the end of the day we have to preserve what we've found, then I'll do just that."
                    show lyney neutral
                    L "and I'll keep what grounds me, and stop demanding everyone else believe the whole spectacle."
                    show lyney neutral
                    L "because after all, seeing is believing."
            
            Y "{i}…{/i}"
            Y "{i}…?!{/i}"

            stop music fadeout 1.0

            Y "{i}I feel a surge of memories rushing inside my head.{/i}"
            
            scene black with fade
            
            Y "jack… I was just checking in."
            Y "its just… we are so far in it's too late to ever change my mind."
            Y "my fate in this universe is sealed… but I'm so unsure of everything. Why, just why am I trying to protect {font=DOSIyagiBoldface.ttf}█████████████{/font}?"
            Y "jack… things are outside of your control. Remember, its your own life you're living. You're here for a reason, that purpose, its for you to find."
            Y "…guide yourself forward."
            
            scene roof day 
            show lyney fear
            with fade

            L "?!"
            show lyney neutral
            L "hah,, incredible. Its like both of our minds were in sync just then."
            show lyney neutral glee
            L "the context is way past us, but it still felt real."
            show lyney happy -glee
            L "if anything, I could learn a thing or two from this other self, whoever I was."

            hide lyney with dissolve
            jump .endingtalk

        "naoto":
            queue music sentimental

            show naoto neutral glee with dissolve
            N "ah, its you."
            show naoto neutral -glee
            N "…"

            "{i}Naoto seems quieter than usual.{/i}"
            
            show naoto sad
            N "I keep thinking we missed something, and that's why we've ended up where we are right now."
            show naoto disgust
            N "we didn't fully process these anomalies or even the alternate universe argument, and there's no doubt we rushed segments to get the presentation in on time."
            show naoto angry
            N "I just don't want to end up repeating the same mistakes, whether that means continuing our investigation or not."
            
            menu:
                "you've done more than enough, you don't have to keep proving yourself.":
                    show naoto neutral
                    N "I'm not so sure if I believe that yet."
                    show naoto happy
                    N "but your words certainly take the edge off, like I'm not left to do this alone."
                    show naoto neutral
                    N "maybe I can let myself breathe and forget everything for a moment."
                    show naoto happy exclamation
                    N "…and then soon after I'll be ready to support you guys wherever necessary!"
                
                "I'm here for you, and its not like I'll let you get lost in this alone.":
                    show naoto neutral
                    N "you say it like its something obvious…"
                    show naoto happy
                    N "but I didn't realise I needed to hear that."
                    show naoto neutral
                    N "I'm not one to admit I'm scared about the whole process, especially when faced with rejection, so its difficult for me to express this in words."
                    show naoto happy glee
                    N "but thank you for staying."
            
            Y "{i}…{/i}"
            Y "{i}…?!{/i}"

            stop music fadeout 1.0

            Y "{i}I feel a surge of memories rushing inside my head.{/i}"

            scene black with fade

            N "you've changed Jack. I thought maybe it was for the better… after all you have saved my life several times. But I guess I was wrong…"
            J "thing have gotten bad, and its because of me. I get that. That's why we need to start again."
            N "you can't go back."
            N "I'm afraid I cannot follow you on this path anymore."
            J "NAOTO,, NO!"
            
            scene roof day 
            show naoto fear question
            with fade
            
            N "what was that? I'm guessing you felt that as well."
            show naoto sad question
            N "this memory… did I really turn my back on you?"
            show naoto disgust -question
            N "ugh, this leaves way more questions than answers."
            show naoto neutral
            N "but know that I don't ever intend on leaving you, or this group, like the other 'me' did."

            hide naoto with dissolve
            jump .endingtalk

        "scara":
            queue music sentimental

            show scara neutral with dissolve
            S "jack…"

            "{i}Scara looks like he's trying to close himself off.{/i}"
            
            show scara disgust
            S "the way I see all of this, its pathetic."
            show scara angry
            S "I like the relationship we've all built, I just don't want it to fall to mindless idiosyncrasies."
            show scara sad
            S "especially those we cannot grasp, nor understand."
            
            menu: 
                "its not like you have to believe in everything, just don't shut us down.":
                    show scara disgust
                    S "hmph. So am I meant to provide emotional support or something?"
                    show scara neutral
                    S "well, if you want me here because I'm useful, then fine, I'll stick around I guess."
                    show scara neutral
                    S "don't go expecting any words of affirmation from me though."
                
                "whats really behind your distance?":
                    show scara fear
                    S "huh? What's it to you?"
                    show scara neutral
                    S "…"
                    show scara neutral
                    S "look, I'm not ready to tell you everything yet, that's all."
                    show scara happy
                    S "but that being said, I'll try not to hide away from you guys either."
            
            Y "{i}…{/i}"
            Y "{i}…?!{/i}"

            stop music fadeout 1.0

            Y "{i}I feel a surge of memories rushing inside my head.{/i}"
            
            scene black with fade
            
            J "hey!! Wake up scara, you have to tell me what happened."
            J "H-HUH?! SCARA YOU'RE {font=DOSIyagiBoldface.ttf}████{/font}!"
            S "jack…stop…"
            S "…am I {font=DOSIyagiBoldface.ttf}████████{/font}?"
            S "I thought… I was… a {font=DOSIyagiBoldface.ttf}██████{/font}…"
            J "WHERE IS {font=DOSIyagiBoldface.ttf}████{/font}?"
            S "I said stop… jack…"
            S "…you are the best of all of us…"
            S "don't let anyone… tell you different."
            J "…"
            S "why do I… feel so… {font=DOSIyagiBoldface.ttf}████{/font}?"

            scene roof day 
            show scara fear question
            with fade
            
            S "??"
            Y "…"
            show scara sad -question
            S "hmph."
            show scara neutral
            S "c'mon then. lets figure something out together."

            hide scara with dissolve
            jump .endingtalk

    queue music sentimental

    scene roof day
    show miku at r51
    show lyney at r52
    show cyno at r53
    show naoto at r54
    show scara at r55
    with fade

    Y "{i}after talking to everyone, we all start to reconvene in our usual spot on the rooftop.{/i}"

    show miku neutral
    M "alright. I think we're… mostly in agreement now."
    show miku serious
    M "listen, I don't wanna drop this investigation now more than ever, because its our chance to prove everyone wrong."
    show naoto neutral
    N "indeed. the memory fragments… along with the inconsistencies in our universe… its certainly enough to keep going."
    show naoto happy
    N "even without external validation, its still an internally cohesive argument."
    show lyney happy glee
    L "one thing's for certain, without our dearest exchange student, none of us would've made it this far."
    show lyney -glee
    show cyno neutral
    C "hm. I agree. Regardless of whether you meant to or not, you helped to keep us together."
    show cyno happy
    C "when you came along it was like we suddenly had a sense of direction, which ultimately led to this club."
    show miku happy
    M "and its not just that, you gave us a reason to keep going. And I don't just mean the investigation."
    show miku neutral
    M "I mean… think about it guys, all the time we have spent with each other."
    show miku neutral glee
    M "and also the way we continue to believe in each other… even now."
    show miku happy glee
    M "so because of those times, I would never doubt the experiences we shared together, in fact, I'll continue to treasure the connections we have more than anything in this world!"
    show miku -glee
    
    show naoto neutral
    N "and that's why I think its only sensible for him to decide what this all means."
    show scara fear question
    S "huh…? What are you talking about?"
    show naoto neutral
    N "you see, although we have a lengthy amount of theoretical evidence to back up our argument, none of the anomalies we have encountered fit into a neat category, at least not well enough for the general public to side with us."
    show naoto neutral
    N "Even when explaining away subjective territory we always took an objective stance."
    show naoto neutral
    N "so instead, we need someone to interpret the emotional truth we have lived."
    show scara -question
    show cyno neutral
    C "hm. And in all of the memories we've each experienced, he has been the only constant throughout all of them."
    show cyno happy
    C "there is something special to be said about you, however that may be."
    show lyney happy
    L "I have no objections to that, after all I couldn't think of a better person than him."
    show miku sad question
    M "but… wouldn't this be a heavy burden to handle?"
    show miku sad -question
    M "I mean, don't you think how we treat this now will go on to determine everything, even our futures?"
    show scara neutral
    S "…hmph."
    N "I'm aware. there are consequences as to how we approach this situation."
    show naoto neutral
    N "but out of everyone here, I think we can all agree his judgement is best."
    show miku serious
    M "hm. That's true."
    show miku serious
    M "so… I guess its on you now."
    L "no pressure, hehe…"
    N "well considering the stakes, there is obviously some degree of pressure on him."
    L "hey, you don't think I know that? I'm just trying to alleviate his worries, that's all."
    L "who knows? His stress levels might be through the roof right now!"
    N "oh, right, I didn't consider that."
    N "if it brings you any comfort, we will respect your decision no matter what you choose."
    M "well then, on behalf of all of us…"
    show miku serious
    M "please choose how we make sense of this world and all of our experiences."

    Y "….."

    stop music fadeout 1.0
    
    Y "{i}I should choose my answer carefully.{/i}"

    menu .endingchoice:
        "what we experienced together is the real truth, even though it doesn't make sense.":
            Y "{i}…{/i}"
            Y "{i}if I accept this, and admit that what we lived through carries its own kind of importance…{/i}"
            Y "{i}then maybe every moment of doubt and clarity we had throughout this investigation can be recognised as a testament of our determination to unravel the anomalies plaguing our society.{/i}"
            Y "{i}and if there's a truth in all of this, its found in our bond, and nothing else.{/i}"
            Y "{i}turning away now would be like telling ourselves that our connection never mattered.{/i}"
            Y "{i}and that may just be the highest betrayal of all.{/i}"
            Y "{i}…..{/i}"
            Y "{i}something is bothering me.{/i}"

            # [BG change, flashback to screenshots of throughout the game, memories that the player has made with the characters]
            
            menu:
                "{i}is this the decision I want to make?{/i}"

                "yes, this is the truth I choose.":
                    if chosen.name == "scara":
                        jump trueending
                    else:
                        jump goodending

                "no, I need to rethink.":
                    jump .endingchoice

        "none of this is real. Our experiences hold no truth, and we need to let it all go.":
            Y "{i}…{/i}"
            Y "{i}if I let it all go, I preserve a world free of paradoxical memories and events.{/i}"
            Y "{i}the administration will have peace of mind, and everyone else will never have to know how close reality came to unravelling itself.{/i}"
            Y "{i}but at what cost? {/i}"
            Y "{i}choosing to deny what we have discovered now would also mean discarding every moment we have shared together.{/i}"
            Y "{i}but considering the circumstances, some truths may have to be let go in the end.{/i}"
            Y "{i}and as the weight of the universe now lies in our hands, some things may be too dangerous to believe in.{/i}"
            Y "{i}…..{/i}"
            Y "{i}something is bothering me.{/i}"

            # [BG change, flashback to screenshots of throughout the game, memories that the player has made with the characters]
            
            menu:
                "{i}is this the decision I want to make?{/i}"
                
                "yes, I must let it go.":
                    if chosen.name == "scara":
                        jump trueending
                    else:
                        jump badending

                "no, I need to rethink.":
                    jump .endingchoice

# cyno scara miku lyney naoto sparrow
