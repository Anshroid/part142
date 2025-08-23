default miku.points = 0
default miku.level = 1

label hangoutmiku:
    call expression "hangoutmiku" + str(miku.level) from _call_expression_4
    $ miku.level += 1
    return

label day1hangoutmiku:
    stop music fadeout 1.0
    queue music hangout
    
    scene street evening
    show miku neutral glee
    with fade

    M "sure, I'll walk with you!"

    show miku neutral sparkles
    M "as student council president, its my responsibility to safeguard every member of the school community, and that includes you too."

    menu:
        "what about as a friend?":
            show miku exclamation
            $ miku.points += 1
            play sound point
            M "a friend? O-of course! I understand now, you just wanted to have a conversation with me."
            
            M "well, I suppose I can relax my duties for now, lectures for today have ended after all."

        "thank you for your hospitality.":
            show miku embarrassed sweat
            M "please, you don't need to be so formal."

            show miku happy -sweat
            M "and its really no problem, if you need any more help I'm usually around."

    show miku neutral none
    M "I'm used to staying quite late - student council things you know?"

    show miku happy
    M "but with just you, its kind of nice. Having the company unconditionally I mean, without having any expectations placed on me."
    
    menu:
        "it sounds like you must get tired of being the leader.":
            show miku neutral
            $ miku.points += 1
            play sound point
            M "maybe you're right, but if I don't look out for everyone, who will?"

        "you're acting like this is a revelation.":
            show miku angry vein
            M "tch, I'm just not used to it, that's all!"

    show miku neutral none
    M "but, thank you for letting me walk with you. it was certainly a nice change of pace."

    return

label hangoutmiku1:
    Y "{i}since Miku's the student council president, she's most likely in their office after her lectures, I'll check there first.{/i}"

    scene office day
    show miku neutral
    with fade
    
    "{i}looks like Miku's on the phone{/i}"

    show miku neutral
    M "yes, we'll need several signs around the front gates, and some directional arrows to point visitors to the main hall…"
    show miku angry
    M "I understand that goes slightly beyond our budget… just,, lemme handle it, okay?"
    show miku neutral
    M "thanks."

    M "{i}puts down the phone{/i}"
    
    show miku fear exclamation
    M "!!.."

    show miku neutral -exclamation
    M "Oh Jack, I'm sorry. I didn't see you come in."
    M "though you arrived at just the right time, I could use some help since all the other members are currently occupied."
    
    menu:
        "just let me know what I can do.":
            show miku happy
            $ miku.points += 1
            play sound point
            M "you'd really help me out? Thank you so much!"

        "is it urgent?":
            show miku sad
            M "Unfortunately so. If you wanted to spend some quality time with me, then say goodbye to that for the remainder of this week."
    
    scene hall
    show miku neutral
    with fade
    
    show miku neutral
    M "I suppose I should give you a bit of background information first."
    show miku neutral
    M "I've been tasked with organising a multi-club event for the upcoming open evening. The aim is to show what our campus culture is like to potential applicants and offer holders."
    show miku neutral
    M "it also gives clubs the chance to showcase their talents to the rest of the school."
    show miku sad
    M "as you might expect, over 20 of our societies are participating, ranging from martial arts to even gaming. They all require their own booth and individual needs, so juggling that with advertising the event to our target audience is quite… taxing."
    
    menu:
        "you seem to know what you're doing. You've got this.":
            show miku happy
            M "you're right, I do, and this is certainly not the first event I've planned."
            show miku sad
            M "I just never appreciated how much I was meant to be doing until the administration had another go at me."
    
        "why does it all fall on your shoulders?":
            show miku happy
            M "because I'm the president, the face of the student body. Its my job to make sure that everything goes well."
            show miku neutral
            M "This is what I signed up for after all, so I have no room to complain."
    
    show miku sad
    M "…"
    
    Y "everything okay?"

    show miku happy
    M "oh,, yeah! Here, take this piece of paper and sketch out a floor plan of the main hall for me."
    show miku neutral
    M "okay, so, the stage should be at the back to not obstruct traffic. There should also be an information stand at the front for any general questions not related to clubs."
    show miku neutral
    M "club booths along both the west and east sides of the hall, don't worry about labeling each club for now, that can be sorted out on the day."
    show miku neutral
    M "there should also be a one-way system going round the hall, kinda like a circle, which should avoid the issue of bottlenecks and gives the chance for all visitors to check out each club."
    
    menu:
        "this makes sense.":
            show miku happy
            M "oh, are you done with the sketch, let me have a look…"

            $ miku.points += 1
            play sound point
            M "yes, this is exactly how I wanted it!"
        
        "I'm so lost.":
            show miku happy
            M "oh, are you done with the sketch, let me have a look…"
            show miku embarrassed
            M "ah… this is definitely a draft!"

    show miku neutral
    M "now, we're short on volunteers to run the information stand. As you're a transfer student who has arrived only recently, I can't expect you to help out visitors with queries."
    
    menu:
        "I'll go around and ask.":
            show miku happy
            M "yes, that would be helpful. If more of the students step up, then this might actually come together."

        "shouldn't you ask the council members first?":
            show miku embarrassed
            M "they're already doing what they can, and I'm trying not to share too much of the burden with them. Asking help from someone outside the council is quite new for me."

    show miku neutral
    M "perhaps you can try and find someone in our club? they should still be around campus."

    scene hallway evening
    with fade

    $ whowasfound = renpy.random.choice(["Scara", "Lyney"])

    Y "I search around campus and eventually find [whowasfound]"

    if whowasfound == "Scara":
        show scara neutral with dissolve

        S "hah, seriously? You want me to give up my sweet, precious time to talk to some new students who don't know any better?"

        show scara angry
        S "…"
        S "okay, maybe you are being serious. Hm. fine!"
    
    else:
        show lyney happy with dissolve

        L "the open evening? Of course I'll help out."
        L "just put me centre stage and soon everyone's eyes will be cast on me!"

        show lyney embarrassed
        L "…huh? I just need to stand behind the information booth? That wasn't entirely what I was expecting, but as long as I can be of use…"

    scene hall
    show miku happy
    show expression whowasfound.lower() + " neutral" at right
    with fade

    show miku happy
    M "you found someone? That's great!"
    M "You've been a huge help today, thank you."

    stop music fadeout 1.0
    queue music sentimental

    show miku neutral
    M "admittedly, I thought I could handle it all without feeling overwhelmed."
    M "but even if one student finds their place in a club because of this event, it will be worth it to me."
    
    menu:
        "I'm sure they will appreciate what you're doing":
            show miku happy
            M "you think so?"

            $ miku.points += 1
            play sound point
            M "that's… very kind of you to say."

            show miku neutral
            M "much of my work does go unnoticed, but maybe you're an exception." 

        "what if they don't come?":
            show miku sad
            M "that's highly unlikely given how much we've spent advertising it. Still, attendance is the only metric the administration will consider, so that's a risk we're taking."

    show miku neutral
    M "…its only been prep work so far, but I feel like I can't afford to mess anything up."
    M "after all, the execution of this event is on me this time. I cannot afford to depend on anyone else."

    show miku happy
    M "but don't worry about coming, you can rest assured that it'll all work out!"

    show miku neutral
    M "anyway, thanks for the help."

    return

label hangoutmiku2:
    Y "{i}the open evening is starting soon, I should go check up on Miku beforehand{/i}"

    play music tense
    scene office day
    show miku angry at left
    show naoto angry at right
    with fade
    
    "{i}miku's here, along with naoto, but they look like they're in a heated argument.{/i}"

    N "miku, I don't want to keep telling you this. But, you can't do everything by yourself. That's not what leadership is."
    M "it is when everything's on the line. that includes the council's reputation, the clubs… heck, even the entire student body!"
    M "you and I both know how fucked up the administration is, they can do anything they want. So, I need to deliver perfection. I can't let this open evening fail because the student council has an incompetent president!"

    show naoto neutral
    N "but I can see it in your face, you're burning out. Just listen to me miku."

    M "and how about u just drop it?"

    "{i}…{/i}"
    "{i}Miku seems to be looking at me now.{/i}"

    show miku serious
    M "…you didn't need to come."
    show naoto neutral
    N "maybe they came because you needed them to."
    show miku angry
    M "that's not for you to say."

    hide miku with dissolve
    "{i}Miku storms out of the room.{/i}"

    show naoto sad
    N "she's trying to shoulder everything alone… again."
    show naoto neutral
    N "I can never get through to her, but perhaps you can. If you're going to try and find Miku, check near the courtyard, beneath the cherry trees. That's usually where she goes to regulate herself."
    
    stop music fadeout 1.0

    scene park cherry
    show miku fear exclamation
    with fade

    M "you came…"

    show miku sad -exclamation
    M "I thought I told you before not to worry about today."

    menu:
        "I was worried anyway.":
            show miku fear exclamation
            $ miku.points += 1
            play sound point
            M "!…"

            show miku neutral -exclamation
            M "knowing you, I should've guessed you would see right through me."

        "sorry. I didn't mean to intrude.":
            show miku sad
            M "no, you're not intruding. it's just, I didn't want you to see me like this."

    queue music sentimental

    show miku angry
    M "I tried to keep everything organised and follow every plan to detail. but even now, I've got the administration making extra requests and more clubs doing last minute sign ups. It's screwing everything over."
    show miku neutral
    M "everything's already underway. the booths are being set up as we speak, and most of the volunteers have already arrived. I want to think they'll manage but I don't know how I can make myself sure of it."
    show miku sad
    M "I didn't want you to help because if anything went wrong then I wanted the responsibility to fall on only me."

    menu:
        "you should learn to trust others.":
            show miku neutral
            M "of course I know that I just…"
            M "maybe you're right, I haven't been doing that much at all recently, if not ever."

        "you're not the only one who cares.":
            show miku neutral
            M "of course I know that I just…"
            show miku sad
            M "I don't know what I think anymore, to be honest."

    show miku sad
    M "the thing is, if this event doesn't go as well as I had hoped, it means that I will have failed myself."
    show miku neutral
    M "I mean, this whole event is not even about me. It's supposed to be about the community we have built. but for me it's always been more than that."
    
    Y "what do you mean?"

    M "…I wanted to execute things flawlessly and prove to everyone I was capable of doing the right thing. And by extension, my ability to lead the student body."

    show miku sad
    M "this event is testament to that, and I feel like I keep putting myself down."
    M "but if I need help, and admit that I can't do this on my own, then I'm not good enough to lead at all."

    menu:
        "you're not above the student body, you're a part of it.":
            show miku fear exclamation
            $ miku.points += 1
            play sound point
            M "perhaps that's the part I forgot…"
            show miku neutral -exclamation
            M "I have the tendency to try and carry everything, but that's not what leadership is really about, huh…"

        "that's not a sign of weakness, it's just being human.":
            show miku neutral
            M "hm… Yes. I think I just needed someone to say that to me out loud."
            M "and now I understand that it shouldn't be something to be ashamed of."

    show miku neutral
    M "maybe, in the end, I was simply afraid of needing you."
    show miku happy
    M "thank you. I appreciate you for showing up anyway."

    scene office day
    show miku serious at left
    show naoto neutral at right
    with fade

    stop music fadeout 1.0
    queue music hangout

    N "there you are. Are you ready for us to help you now?"
    M "yes naoto, and sorry… for earlier."

    show naoto angry
    N "don't be. Now c'mon you two, the genshin society's monitor display stopped working again…"
    show miku angry
    M "seriously? Ugh, they'd rather spend their club funds on primogems than better equipment."

    scene hall with fade

    Y "{i}the open evening passes by rather quickly. Me, miku, and naoto were able to shuffle between tasks efficiently. I managed to help out some visitors while miku and naoto would step in to run damage control wherever necessary.{/i}"
    
    "{i}meanwhile, at the information booth{/i}"

    if whowasfound == "Scara":
        "Visitor" "um, hi! Do you know where the science club booth is?"

        show scara angry with dissolve
        S "tch, go look for it already. I'm not gonna hold your hand."
        
        "Visitor" "but isn't this the information stand?"

        show scara neutral
        S "yes, not emotional support."
        
        "Visitor" "right, okay…"
        
        S "…down the west side, you'll know you're close when you smell something funny."

        show scara angry
        S "idiot…"

    else:
        "Visitor" "um, hi! Do you know where the science club booth is?"

        show lyney happy with dissolve
        L "why of course I do… but first, pick a card, any card!"
        
        "Visitor" "uhh, is this part of the open evening?"
        
        show lyney neutral
        L "no, but ill tell you what it is a part of… your destiny."
        
        "Visitor" "…"
        
        show lyney embarrassed
        L "ahem, science club's that way…"
        show lyney sad
        L "tis a shame, these future students have no appreciation for magic…"

    "{i}soon, the event comes to a close{/i}"

    scene office evening
    show miku happy
    with fade

    M "it actually went okay. Better than okay even."
    show miku neutral
    M "and that's all thanks to you."
    
    menu:
        "see, you never had to do this all by yourself":
            show miku happy
            $ miku.points += 1
            play sound point
            M "yes, i can see why now."
            show miku neutral
            M "its weird actually, because I've spent so long trying to become the one who people would want to rely on,, to the point where I forgot what its like to rely on someone else."
        
        "I knew it was the right thing to do.":
            show miku happy
            M "hehe… that's very you."
            show miku neutral
            M "that kind of instinct… I admire it."

    show miku neutral
    M "anyways, thanks for showing up, even though I told you not to… I really mean that."
    show miku happy
    M "goodnight!"

    return

label epiloguemiku:
    define miku.opening = "hey, do you have a moment?"

    show miku happy
    M "I was hoping I'd get a chance to talk to you properly, one on one. Just as me, not the student council president."

    menu:
        "you seem different today.":
            show miku fear exclamation
            M "huh, maybe I am. I suppose its because I've been reflecting a lot since the open evening."
        "did you resign?":
            show miku fear exclamation
            M "of course not! Far from it actually. But this isn't about the council."

    show miku serious -exclamation
    M "you know, I used to think that taking a leadership role meant standing above others, and being able to take all the weight so that no one else has to suffer for mistakes. And also that… if i stuck to the rule book, and did everything that was expected of me, then that would be enough."
    show miku sad
    M "but in reality, all I ever did was shut everyone out at times when I most needed help, including you."
    
    menu:
        "its nothing you need to apologise for.":
            show miku serious
            M "I guess not,, but that doesn't mean I still regret the way I behaved, even if I did have selfless intentions."
        "you didn't shut me out completely though.":
            show miku embarrassed
            M "that's what you think, but you're just… persistent. Not in a bad way, its just, even when I told you not to worry that day, you showed up anyway."

    show miku neutral
    M "and to be honest, you helped me realise something that I had forgotten."
    M "that a leader who doesn't learn how to trust their companions, can't ever truly lead."

    show miku sad
    M "its not an easy thing to admit, because I was once afraid of what would happen if people saw me fail."

    show miku neutral
    M "but when you were there, treating me like I was no different as a person, I felt appreciated and respected, like a human."

    show miku happy
    M "and I liked that feeling."
    
    Y "{i}I should choose my words carefully.{/i}"

    menu .reconsider:
        "I'll always be here, and you no longer have to shoulder everything alone. (romance option)":
            show miku neutral
            M "…then I want to be here with you too. To be someone who can grow with you."
            M "So… will you stay with me, as something more than just a friend?"

            Y "{color=#EC80EC}{i}I am now in a relationship with Miku.{/i}{/color}"

            show miku happy
            M "I think I've wanted this more than I realised."

            show miku neutral
            M "…"
            M "I think I'm starting to like this new me, who I'm becoming. And I also think a lot of that is to do with your support."

            show miku happy
            M "well, see you around, hehe!"

        "you've changed a lot, I'm sure the council will be proud of you.":
            Y "{i}…{/i}"
            Y "{i}I suddenly get the feeling that friendzoning isn't the right option.{/i}"
            Y "{i}perhaps I should reconsider.{/i}"
            jump .reconsider

    return