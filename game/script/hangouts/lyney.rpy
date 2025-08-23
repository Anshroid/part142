default lyney.points = 0
default lyney.level = 1

label hangoutlyney:
    call expression "hangoutlyney" + str(lyney.level) from _call_expression_3
    $ lyney.level += 1
    return

label day1hangoutlyney:
    stop music fadeout 1.0
    queue music hangout
    
    scene street evening
    show lyney neutral
    with fade
    
    L "you're pretty bold, asking the greatest magician to ever grace this world to come on a walk with you. Most people just like to ask me about my tricks."

    show lyney embarrassed
    L "I mean, don't get me wrong, I don't mind… I like the unpredictable company."

    menu:
        "you're an easy person to talk to actually.":
            show lyney happy
            $ lyney.points += 1
            play sound point
            L "ohoho… careful now, don't think you can go around saying too many nice things to me."
            L "otherwise, I'll just think you're trying to steal my heart when my guard is down."

        "I thought you would make the walk more entertaining.":
            show lyney neutral
            L "entertaining, huh…"

            show lyney angry
            L "what am I? A puppet for your own amusement? Just kidding… obviously."

    show lyney neutral
    L "I wonder, do you think magicians like myself ever stop performing?"
    L "as in, maybe we just don't know how to act off stage anymore."
    
    menu:
        "maybe, but you don't have to impress me right now.":
            show lyney happy
            $ lyney.points += 1
            play sound point
            L "heh… maybe. Perhaps I can make an exception this time."

        "isn't that your whole thing though?":
            show lyney sad
            L "you have a point I guess. Admittedly, it does feel a little lonely."

    show lyney neutral
    L "well, here we are, back at your dorm. Not as dangerous as you expected when walking home with a magician, hm?"

    show lyney happy exclamation
    L "hehe… bonne nuit~"

    return

label hangoutlyney1:
    Y "{i}I heard lyney's a magician. Perhaps I should go check the stage to see if he's performing.{/i}"

    scene stage with fade

    Y "…"
    Y "{i}strange, I can't find lyney, maybe he's somewhere else-{/i}"

    Q "seeing is believing, friend!"
    
    Y "{i}that voice…{/i}"
    
    "{i}a flurry of cards appear on stage{/i}"
    
    show lyney neutral with dissolve
    L "{i}walks out from behind the cards and snaps his fingers causing the cards to vanish{/i}"
    L "what do you think?"
    
    menu:
        "that was awesome!":
            show lyney happy
            $ lyney.points += 1
            play sound point
            L "I knew you'd think so highly of me."
        
        "a bit extra might I add.":
            show lyney sad
            L "ah,, you think I overdid it? What a shame…"

    show lyney neutral
    L "anyway, I'd say that was good practice for my magic show later today!"

    Y "why didn't you tell me?"

    show lyney happy
    L "it was impromptu, I couldn't help myself!"
    show lyney sad
    L "besides, this is how I make ends meet, my weekly rent is a fortune y'know…"
    show lyney neutral
    L "well, I'll be making the final preparations now. you don't mind waiting a bit, do you?"

    Y "{i}guess I should take a seat at the front and wait for the show to begin{/i}"
    "{i}some time passes, other students start coming in{/i}"
    "{i}soon, the lights in the room start to dim, and everyone's attention is focused on the stage{/i}"
    
    show lyney happy
    L "Ladies and gentlemen, welcome to, dare I say, the MOST magical five minutes of your life. I promise it will be wondrous, even mysterious, but definitely not frauduleus!"
    L "{i}flips a hat upside down, visibly empty{/i}"

    show lyney neutral
    L "now, you see this hat? Quite dull… almost tragic really, much like our project deadline at the end of the week."

    Y "{i}I should get a closer look at this trick…{/i}"
    
    show lyney happy
    L "but,, with a little charm from yours truly…"
    L "{i}snaps his fingers, a cloud of red smoke bursts up from inside the hat, soon a bird appears and flies off{/i}"
    
    show lyney neutral with dissolve
    show lyney happy
    "{i}as the crowd cheers I notice lyney's smile flicker for a moment, before quickly going back to the usual, seemingly practiced smile{/i}"
    
    L "{i}pulls out a deck of cards from a velvet pouch, shuffles them and offers a hand to… you?{/i}"
    
    show lyney neutral
    L "you there, the silent one, and my assistant for the performance. Please, pick a tarot card and don't let me see it."

    Y "{i}I need to pay some more attention here{/i}"
    "{i}lyney's hand appears to be trembling…{/i}"
    
    menu:
        Y "nevertheless, what card should I pick?"

        "the lovers":
            L "now, this part's tricky. some say a magician is able to read the card from one's expression. But yours… is harder to read."
            L "hm…"
            show lyney neutral
            L "the lovers, bold choice."
            L "its not just about romance, if that's what you're thinking… moreso connection, and decisions that might just pull you in two directions."
            L "I wonder, are you the type of person to chase what your heart truly desires? If not, then don't expect to wait for me to chase you!"
        
        "the sun":
            L "now, this part's tricky. some say a magician is able to read the card from one's expression. But yours… is harder to read."
            L "hm…"
            show lyney happy
            L "ah, the sun!"
            show lyney neutral
            L "you emanate a warm and honest presence. This arcana is more than about happiness but also being seen completely, face to face…"
            L "if I looked you in the eyes a little bit closer, would you shine just as bright, or is there something else I must find in the shadows?"
        
        "the magician":
            L "now, this part's tricky. some say a magician is able to read the card from one's expression. But yours… is harder to read."
            L "hm…"
            show lyney neutral
            L "oh? The magician… are you picking the competition simply to spite me?"
            show lyney happy
            L "I must admit, the skill and charm… it might suit you y'know."
            L "but are you playing your own game, or trying to keep up with mine. If you're just trying to impress me, its working~"
        
        "the fool":
            L "now, this part's tricky. some say a magician is able to read the card from one's expression. But yours… is harder to read."
            L "hm…"
            show lyney neutral
            L "the fool, very interesting."
            L "“the one who steps forward without knowing where the road leads.” in other words, someone who is brave and reckless, yet also hopeful… a bit like you I think."
            show lyney happy
            L "or maybe you wanted to fall, and hoped that I'd be the one to catch you~"


    Y "{i}did he just… FLIRT WITH ME?{/i}"

    menu:
        "how did you do that?":
            show lyney neutral none
            $ lyney.points += 1
            play sound point
            L "magic 101, a magician never reveals his secrets… though, I must admit, I'm flattered by your bewilderment."
        
        "that was a lucky guess.":
            show lyney angry none
            L "the nerve, I can't believe you would say that to a magician like me!"

    show lyney neutral
    L "moving onto my final trick for tonight's show…"
    
    Y "{i}I can't miss this one, lets look carefully{/i}"
    
    show lyney sparkles
    L "{i}holds up a coin{/i} I will make all doubt, in and of itself, disappear just like this…"

    L "{i}tosses a coin into the air, it soon vanishes while spinning mid-air{/i}"

    "{i}a round of applause ensues, lyney bows{/i}"

    Y "{i}I can't help but notice how his smile isn't exactly reaching his eyes this time.{/i}"
    hide lyney with dissolve

    Y "{i}…something seemed off with lyney during the performance, might be best to go ask him about it.{/i}"
    
    scene backstage
    show lyney neutral
    with fade

    L "how was that as a taster of my magic? Best believe you enjoyed it because I have no choice but to start charging you for future shows…"

    Y "actually lyney…"

    show lyney happy
    L "huh? Is the price too high? Don't worry, ill give you a special discount from yours truly!"
    
    stop music fadeout 1.0
    queue music sentimental

    L "…"

    show lyney neutral
    L "ah, some keen observations-"

    show lyney angry vein
    L "I-I mean, trying to read the magician are we? That's pretty dangerous y'know…"

    menu:
        "I just want to know if you're okay.":
            show lyney neutral none
            $ lyney.points += 1
            play sound point
            L "I cherish your sentiment, but you don't need to be so serious."
        
        "you looked distracted the whole time…":
            show lyney disgust none
            L "that was… probably just an illusion. many people think I'm good at those."

    show lyney happy
    L "now, for my greatest trick yet, watch me vanish from this conversation!"

    hide lyney
    L "{i}snaps his fingers and disappears in an instant{/i}"
    Y "{i}theres not much point trying to find him now, I should probably talk to him again before his next show.{/i}"

    return

label hangoutlyney2:
    Y "{i}lyney's next show should be starting soon. I need to hurry backstage and talk to him about his last performance.{/i}"
    
    scene backstage
    show lyney happy
    with fade

    show lyney happy
    L "oh, fancy seeing you here!"
    show lyney sad
    L "unfortunately, this area is reserved for performers and the crew, otherwise I would've let you stay, what a shame…"

    menu:
        "I'm still worried about you.":
            show lyney neutral
            $ lyney.points += 1
            play sound point
            L "!!..."

        "it's urgent.":
            show lyney embarrassed
            L "I'm sure it can wait, besides, my personal feelings aren't that important, right…?"
            L "…"

    stop music fadeout 1.0
    queue music sentimental
    
    show lyney neutral
    L "alright, I'll drop the act, just for now at least."
    L "indeed, you were right to suggest I looked 'off.'"
    L "even though I'm far beyond an amateur, as a magician I still find myself lacking the ability to blend truth and illusion, at least in my own heart."
    L "in other words, I put on a front to appeal to the audience, unsure if the 'other' me would ever be able to captivate their hearts."
    L "because a magician must steal the attention of their audience so as to carry out the perfect trick, and deceive them while they're not aware."
    L "thus, lyney's magic shows are never truly my own, but rather a persona I play."
    
    show lyney sad
    L "despite my efforts, the only person I can find who doesn't enjoy my performances, is myself."
    show lyney angry
    L "and it hurts."
    
    menu:
        "people will like you for you, there's no need to pretend.":
            show lyney sad
            L "but that's the whole point of magic, no?"

        "people watch your shows for you, not your tricks.":
            show lyney embarrassed
            L "but that's why they may never like me for who I really am."
    
    show lyney sad
    L "…sorry."
    show lyney neutral
    L "I suppose its the weight I carry from my childhood. lynette and I grew up as orphans. it was very rough going to put it simply."
    show lyney sad
    L "in truth, I'm nowhere near as outgoing or chatty as I appear, nor do I project as much confidence when no ones looking."
    show lyney neutral
    L "but people believe what they see."
    L "after all, seeing is believing…"
    
    menu:
        "then let me see the real you.":
            show lyney happy
            $ lyney.points += 1
            play sound point
            L "heh… be careful with what you wish for-"

        "then if they can't see past the act, that's their fault.":
            show lyney neutral
            L "perhaps, but in the end its been my choice to use this persona."
    
    menu:
        "even illusions still hold some truth.":
            show lyney neutral
            $ lyney.points += 1
            play sound point
            L "as much as I'd hate to admit it, you're right."
            L "no matter how hard I try, part of me still finds a way to reach through the cracks of my mask, so to speak. maybe that's why you noticed."

        "you don't need to show anyone anything.":
            show lyney neutral
            L "that sounds comforting, but I also don't want to feel like I'm giving up."
            show lyney sad
            L "I'm just afraid… afraid of what they'll see, is all."
    
    show lyney fear exclamation
    L "ah! The show will be starting very soon, I'm afraid I can't chat with you any longer."
    show lyney neutral -exclamation
    L "but, I think I'm gonna try."
    Y "try?"
    L "try to be myself this time."

    stop music fadeout 1.0
    
    scene stage with fade

    Y "{i}I wait in my seat and before long, the curtains open to reveal lyney centre stage{/i}"

    show lyney neutral with dissolve

    L "…"
    L "magic is a conversation, where I speak and you watch, but its the tricks that really matters."
    L "of course, you're here to be amazed, to see what might have seemingly impossible appear right before your eyes."

    show lyney happy
    L "but tonight, I'd like to try something a bit different with you all."
    L "{i}shuffles a deck of cards, picks one out and holds it between his fingers, before gently placing the card on a table{/i}"

    show lyney neutral
    L "I won't be touching this card until the end. Don't worry, this isn't me trying to deceive all of you. Instead, let me tell you a story."
    L "I've been asked before, whats the secret to becoming a good magician?"
    L "clever illusions? Calculated movements? Or even just a simple charm?"

    show lyney happy
    L "in different ways they're right, though I think the real trick is being able to convince the audience to believe in you even when you don't believe in yourself."

    show lyney neutral
    L "there was once a boy who had very little, only a few old tricks just to earn a living."
    L "Early on, he learnt how to smile even when it hurt as well as how to charm his way through life, regardless of the setbacks."

    show lyney happy
    L "in the end, he had a dream. A dream to make others feel wonder, when he couldn't for himself."

    show lyney sad
    L "after a while, he started to reflect. It's much easier to become what people expect from you, but what if it is was just himself. he then questioned, if no one ever sees the real you, do you even exist after the curtains finally come to a close?"
    L "{i}he walks back to the table and reveals the card - The magician{/i}"

    show lyney happy
    L "ladies and gentlemen, I will not be hiding from you tonight. I'm still me. Its still magic. I just want to be more real with you this time."
    
    "{i}silence ensues, but soon after the audience erupts into applause.{/i}"
    
    show lyney fear exclamation
    L "…"
    show lyney happy -exclamation
    L "THANK YOU!"
    
    "{i}the rest of lyney's performance goes off without a hitch.{/i}"

    return

label epiloguelyney:
    define lyney.opening = "hey, can I talk to you about something?"

    menu:
        "is everything okay?":
            show lyney happy
            L "don't worry now, I'm doing just fine."
            L "thanks for asking though."

        "do I need to be your assistant again?":
            show lyney happy
            L "haha, its got nothing to do with my show."
            show lyney neutral
            L "unless, you mean you miss being my little helper?"

    show lyney happy
    L "I just wanted to express my gratitude for your help during my recent performance."
    show lyney neutral
    L "because of you, I was finally able to feel a connection with my dear audience."
    

    menu:
        "it wasn't much-":
            pass
        "it was all your effort.":
            pass

    show lyney happy
    L "even so, it felt like I was being recognised for who I truly am, rather than a mere performer."

    show lyney neutral
    L "y'know… there's something else I've been wondering since then."
    L "you've seen past my act more than once now, even hearing all the thoughts I wouldn't normally say out loud."
    L "and despite all that, you still stayed."

    show lyney sad
    L "but, what if I took my mask off forever, would you still stay then?"

    Y "{i}I should choose my words carefully.{/i}"

    menu .reconsider:
        "I'd stay because its you, and nothing will ever change that.":
            show lyney fear exclamation
            L "!!..."
            show lyney happy -exclamation
            L "are you trying to steal this magician's heart by any chance?"
            L "hah, I see how it is."
            L "for what its worth, I don't want to wear the mask around you anymore."
            L "because… you saw through my little trick and still chose me."
            
            Y "{color=#EC80EC}{i}I am now in a relationship with Lyney.{/i}{/color}"

        "with or without, you're my friend, and I'm not gonna go anywhere.":
            "{i}…{/i}"
            "{i}I suddenly get the feeling that friendzoning isn't the right option.{/i}"
            "{i}perhaps I should reconsider.{/i}"
            jump .reconsider

    
    show lyney neutral
    L "…maybe it doesn't have to be about abandoning the act for good, but just finding comfort in knowing there's someone who can see both sides, yet still believe in the magic."
    L "and right now?"

    show lyney happy
    L "that's more than enough for me."

    return