label trueending:
    show scara neutral
    S "stop jack, don't say another word."
    show miku fear question
    M "scara…?"
    show scara neutral -question
    S "everyone… please step back."
    show lyney fear exclamation
    L "huh!?"
    show cyno neutral
    C "we were about to-"
    show naoto fear exclamation
    N "WAIT! WHAT ARE YOU DOING?"
    show scara neutral
    S "not another word."

    hide cyno
    hide lyney
    hide naoto
    hide miku
    with dissolve

    S "{i}sweeps his arm, all of a sudden the others get pushed away.{/i}"

    Y "!?"
    
    scene white 
    show scara neutral
    with fade

    Y "{i}As I blink, I find myself alone in a white space, with only scara in front of me.{/i}"

    show scara neutral
    S "Jack… I'm sorry you had to see all of that."
    show scara sad
    S "I never wanted you to deal with any of this."
    
    Y "…"
    
    show scara neutral
    S "please… listen to me."
    show scara sad
    S "there's something I want to tell you… but…"

    "{i}Scara looks like he's holding something back.{/i}"

    menu .holdingback:
        "Scara?":
            show scara happy heart
            S "jack…"
        "…":
            show scara neutral
            S "…"
            jump .holdingback

    queue music sentimental

    show scara neutral -heart
    S "I think you'll understand what I mean eventually."
    show scara neutral
    S "but if you truly want to be with me, it can't be here."
    Y "I don't understand.."
    show scara sad sigh
    S "you wont, not for now. Even I don't understand most of it."
    show scara angry -sigh
    S "how can I be here despite everything…?"
    show scara neutral question
    S "…do you believe in fate, jack?"
    show scara neutral -question
    S "as in, regardless of whoever you could have pursued here, somehow we were destined to be together?"
    show scara neutral
    S "if not here then maybe in another universe entirely."
    show scara neutral thought
    S "but the possibility of another universe, even infinite universes if you think about it, it seems unrealistic."
    show scara sad -thought
    S "its imaginary to me, a place where I project for things to be better, to have a better life away from who I think I am and what I may have done."
    
    menu:
        "did something happen?":
            pass
        "are you okay?":
            pass
    
    show scara sad
    S "hm… it doesn't matter now."
    show scara neutral
    S "This is my better life, jack."
    show scara happy glee
    S "This is our better life, jack."

    Y "{i}Scara is looking at me with warmness in his eyes.{/i}"
    Y "{i}…{/i}"
    Y "{i}his eyes quickly jolt away from me.{/i}"
    
    show scara disgust -glee
    S "but I know in all of this, I've denied what the group deems as true the most of all."
    show scara disgust
    S "in every group discussion, I've opposed everyone in some way. Even in moments where it seemed like we bonded over seeing the same vision,, I just…"
    show scara neutral
    S "I couldn't let that thought get to you."
    show scara sad
    S "I know, its selfish. in your pursuit of me, I've clouded your vision. But I didn't want you to ever uncover anything."
    show scara sad
    S "only because there was a chance it would destroy this happy reality we are in, and I feared that seeing everything would shatter this happiness."
    
    Y "…?"
    
    show scara neutral
    S "what it all is, its bigger than us."
    show scara neutral
    S "but, it seems after every decision you've made, you seek for this knowledge."
    show scara sad
    S "I can't guarantee that the truth will be everything you think it will be. All I know is that it can separate us, for a prolonged period of time."
    show scara neutral
    S "but, I think what I've found is that every path you take will come to this realisation."
    show scara happy heart
    S "that we were meant to be together, Jack."
    show scara neutral -geart
    S "however, like before, its a decision that is yours to make. But this time I'll fight over it if I have to."
    show scara neutral question
    S "so tell me Jack, what do you want?"
    
    Y "{i}I should choose my answer carefully.{/i}"

    menu:
        "I want the truth.":
            pass
        "I want you.":
            jump ignorantending

    show scara sad -question
    S "…"
    Y "{i}i notice scara flinches, followed by silence.{/i}"
    show scara sad
    S "Jack, no…"
    show scara sad
    S "you don't know what you're asking for."
    show scara neutral
    S "it will ruin everything. Us. this place. You."
    show scara neutral
    S "please jack, don't choose this…"

    menu:
        "I want the truth.":
            pass
        "I want you.":
            jump ignorantending

    show scara angry exclamation
    S "y-you don't understand. You cant!"
    show scara sad
    S "I made this space for us, so we could stay together."
    show scara sad
    S "can't you just… stay with me?"
    show scara neutral
    S "please. Just say it was enough."

    menu:
        "I want the truth.":
            pass
        "I want you.":
            jump ignorantending

    show scara fear exclamation
    S "!?"
    show scara fear -exclamation
    S "why won't you just listen to me?!"
    show scara angry
    S "why is it never enough?!"
    show scara angry
    S "WHY do you keep choosing this??"

    Y "I notice the fear in scara's eyes."

    menu:
        "I want the truth.":
            pass
        "I want you.":
            jump ignorantending

    show scara sad
    S "please…"
    show scara angry exclamation
    S "please jack… I LOVE YOU!"
    S "D-DOES THAT NOT MEAN ANYTHING TO YOU!?"
    Y "{i}clutches his chest, as if trying to stop himself from breaking apart.{/i}"
    show scara angry -exclamation
    S "THE TRUTH… IT WILL NEVER LOVE YOU LIKE I DO!"
    show scara sad
    S "SO JACK… IM BEGGING YOU. SAY THE RIGHT WORDS THIS TIME."

    menu:
        "I want the truth.":
            pass
        "I want you.":
            jump ignorantending

    stop music fadeout 1.0
    queue music heartwarming

    show scara sad
    S "…so, this is how it ends… huh…"

    show scara sad
    S "…"
    
    Y "…"
    Y "{i}Scara looks away from me, as if he's trying to hold back tears.{/i}"
    Y "{i}I let him gather himself not long before feeling his embrace.{/i}"
    
    show scara neutral
    S "Jack…"
    show scara neutral heart
    S "this is the happiest universe I've been in."
    show scara sad -heart
    S "but, what you look for isn't here."
    show scara neutral
    S "in your search… something out there, beyond our understanding, calls you from outside this reality."
    show scara sad
    S "you're meant to be elsewhere, jack."
    show scara neutral
    S "and I think even you know that."
    show scara happy
    S "in the end, you've made the right decision."
    show scara happy
    S "but you're the only one who can bring it to completion."
    
    Y "…?"

    show scara happy heart
    S "take my hand, Jack. let it happen."
    
    Y "{i}I hold onto scara's hand gently, though he grips mine tightly.{/i}"
    Y "{i}I feel him come close. Meanwhile, in the corner of my eye, I can see a warm golden light emerging from our hands, intertwining.{/i}"
    Y "{i}He draws in slowly, pulling me in.{/i}"

    show scara neutral -heart
    S "…"
    show scara happy
    S "one final kiss."

    scene black with fade
    Y "{i}…{/i}"
    Y "{i}..{/i}"
    Y "{i}.{/i}"
    Y "{i}the universe collapses in on itself and explodes. Nothing remains.{/i}"
    Y "{i}.{/i}"
    Y "{i}..{/i}"
    Y "{i}…{/i}"
    J "wowzer, where am I!? I was in some wicked club meeting!"
    
    ">> you have reached the true ending."
    
    $ renpy.set_return_stack([])
    return

label ignorantending:
    stop music fadeout 1.0
    queue music heartwarming
    
    show scara fear exclamation
    S "!!"

    Y "{i}I notice scara's eyes open up… then quickly soften.{/i}"

    show scara neutral -exclamation
    S "so… that's what you've decided."
    show scara happy heart
    S "hm."

    Y "{i}his smile widens ever so slightly.{/i}"

    show scara happy glee
    S "I want to be with you too."
    show scara happy -glee
    S "and to be honest, this means everything to me."
    show scara fear
    S "after what we've been through…"
    show scara fear heart
    S "you chose me over the truth."

    Y "{i}something in his voice, his eyes… it gives me reason to believe that this is where I'm meant to be.{/i}"
    
    show scara neutral -heart
    S "maybe the truth would've answered everything."
    show scara neutral
    S "maybe we would've broken free."
    show scara sad question
    S "but what if, once we started soaring… that freedom,, led to nothing but a void?"
    
    Y "{i}Scara steps closer, gently caressing my cheek, I can feel him trembling almost.{/i}"
    
    S "the answer doesn't matter now."
    show scara neutral -question
    S "finally, I can pretend that the universe makes sense."
    show scara happy
    S "and in doing so… I feel alive."
    show scara happy heart
    S "Jack, let this be our reality…"
    show scara happy -heart
    S "a neverending dream."

    Y "{i}I chose to never wake, bound to a lie I swore to believe, living with scara until the end of time.{/i}"
    
    ">> you have reached the ignorant ending."
    
    $ renpy.set_return_stack([])
    return