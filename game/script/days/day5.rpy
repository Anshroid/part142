label day5:
    call screen calendar(5) with fade

label day5morning:
    play music main

    show screen top_right_ui(5, "Morning")
    scene entrance day
    show miku happy glee at r53
    with fade

    M "there you are!"

    menu:
        "what happened to hi hello how are you?":
            show miku neutral none
            M "sorry, what I need to say is a little more important than simple greetings."
        
        "were you looking for me?":
            show miku disgust none
            M "well I'm actually looking for everyone, but you guys are all at completely different places in the morning."
    
    show miku neutral
    M "anyway, I have something quite important to tell you, it'll be quick, promise!"
    
    show miku neutral
    M "so basically I'm cancelling today's club meeting, so it won't take place at lunch."

    menu:
        "why?":
            show miku happy
            M "I'll just explain everything in the evening!"
        "good, I was actually starting to get sick of these meetings.":
            show miku angry
            M "for the benefit of the narrative I'm going to pretend you didn't say that."

    show miku happy
    M "so why? I hear you ask. Well because it'll be tonight at 9!"

    Y "…so we're still meeting?"
    
    show miku neutral
    M "well yea but also no."
    show miku serious
    M "I'll be off now, cyno's the only one I have yet to find,, I hope he's alright…"
    show miku neutral
    M "just remember to meet at the rooftop like usual, 'kay?"
    
    Y "{i}before Miku heads off, I hear some rustling in the bushes next to us.{/i}"
    
    show miku fear question
    M "huh? Did you hear that?"

    menu:
        "what the hell was that?":
            show miku serious none
            M "dunno, let's check it out."
        "no, its just you.":
            show miku angry vein
            M "oh c'mon, it was loud enough for me not to hallucinate."

    "{i}as miku walks over towards the bushes, a cat suddenly jumps out{/i}"
    show cat at offscreenright with None
    show cat at right with move

    play sound meow
    "Cat" "meow"
    
    show miku happy exclamation at r54 with move
    M "awww, its only a cat!"
    
    menu:
        "meow meow meow meowwwwwww~":
            "Cat" "meow?!"
            show miku fear question
            M "huh, can you speak cat or something?"
        "KITTYYYYYYUHHHHHHH!":
            "Cat" "meow?!"
            show miku disgust exclamation
            M "not so loud, you'll scare it away!"
    
    show miku none
    show cyno neutral at r53 with dissolve
    C "guys I let the voices get to me."
    show cyno happy
    C "also cool cat, I'll name you… uh…"
    show cyno happy glee
    C "car seat headrest!"
    show miku serious
    M "woah slow down, first of all, its good to see you cyno, and second, what do you mean the voices?"
    show cyno neutral none
    C "well I had another vision last night, but it was completely different to the ones before."
    show miku serious question
    M "can you elaborate?"
    show cyno neutral
    C "I mean, it wasn't much apart from {i}him{/i} and scara getting a room, not sure why, and then suddenly a massive elephant shows up in the room where me and everyone else is!"
    show miku -question
    show cyno happy
    C "I'm telling you, I couldn't stop tearing up when going to sleep, it was just the cutest thing ever."
    show cyno happy glee
    C "so… I took it upon myself before lectures began to head to the nearby zoo and take an elephant with me."
    
    show elephant at offscreenleft with None
    show elephant at left with move
    show cyno happy
    show miku happy

    play sound elephant
    "Elephant" "toot-"
    
    show miku fear
    M "what the actual fuck."
    show cyno sad none
    C "what? Do you not like him?"
    show miku serious
    M "no cyno… he is very cute. its just that, I wouldn't be so bothered if it wasn't a FEDERAL OFFENCE."
    show cyno angry
    C "and? What about the cat?"
    
    play sound meow
    "Cat" "meow!"

    show miku angry
    M "that's… THATS COMPLETELY DIFFERENT?!"
    
    play sound elephant
    queue sound elephant
    "Elephant" "tooooot!"

    show cyno happy
    C "yea!"
    show miku disgust
    M "oh my god cyno, we're gonna be in so much trouble now…"

    show eepy at r51
    Q "eepy (don't worry about that, ms. hatsune and cyno, I suppose I'll be on elephant duty today)"
    
    menu:
        "now we have a talking squishy chick toy?":
            pass

        "so cyno definitely doesn't have a last name then?":
            show cyno angry vein
            C "are we still not over this?"
            show cyno neutral none

    show miku fear glee
    M "eepy?!"

    "Eepy" "eepy (yes, that's me.)"
    "Eepy" "eepy (and you must be Jack, the new exchange student)"

    menu:
        "no need for introductions then.":
            show miku happy none
            M "eepy, I'm so glad you're okay, last time I heard you were missing for several days…"

        "I wouldn't say I'm new anymore..":
            show miku happy none
            M "eepy, I'm so glad you're okay, last time I heard you were missing for several days…"
    
    show miku serious
    M "the administration have been really worried about you, partially because youre a founder and also the face of the university… but also because well, no one ever heard from you."
    
    "Eepy" "eepy (yesyes, I'm aware, its all a bit of a blur for me to be quite honest)"
    
    show miku neutral
    M "oh… well please make sure to take it easy, there's a lot of strange things happening lately as you would've heard, and I'm doing everything in my power to investigate whatever's going on."
    
    "Eepy" "eepy (thank you, both of you, you two are some of my most beloved followers of eepyism)"
    "Eepy" "eepy (by the way, its almost time for lectures, is it not?)"
    
    show miku fear exclamation
    M "oh shit yea-"
    show miku angry none
    M "c'mon cyno, say goodbye to your elephant."
    show cyno sad
    C "g-goodbye?! {i}*sniffs*{/i}"
    show cyno sad
    C "I-I don't wanna say goodbye-"
    
    "{i}Miku grabs hold of cyno's arm and drags him to class{/i}"
    
    hide miku
    hide cyno
    with dissolve

    C "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!"
    "Eepy" "eepy (e… he doesn't need to worry, I'll be sure to take good care of them both)"
    "Eepy" "eepy (you should be going too Jack)"

    menu:
        "meow!":
            play sound meow
            "Cat" "meowwwwwww purr purr mwah nya"
        
        "toot!":
            play sound elephant
            queue sound [elephant, elephant]
            "Elephant" "tooooooooooooooooooooooooooooooooooooooooooooooooot!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

label day5lunch:
    scene classroom day with fade
    show screen top_right_ui(5, "Lunch") with Dissolve(2)

    Y "{i}This is the first lunch time I will spend without the club.{/i}"
    Y "{i}This may be my only opportunity to get to know people outside of my club!{/i}"
    Y "{i}I'll head to the dining hall and see who is there.{/i}"

    scene hall with fade

    show sparrow freaky
    Sp "You again.."

    menu:
        "What should I do?"
        
        "leave immediately.":
            pass

        "stay and chat.":
            show sparrow neutral
            Sp "I'm really making my mark on this university."
            show sparrow neutral
            Sp "Soon, my mark will be too large to ignore."
            show sparrow freaky
            Sp "He will have to notice me."
            show sparrow neutral
            Sp "I'd LOVE to chat but I'm actually becoming an investor in this school and will have to head to this meeting."
            show sparrow neutral
            Sp "I love you, byeee!"
            Y "{i}I don't think this could mean well for me...{/i}"

    play sound bark

    $ renpy.pause(4)

    Y "{i}What is that sound?{/i}"
    
    scene entrance day
    show cyno at center
    show scara at left
    show lyney at right
    with fade

    show cyno embarrassed
    C "Oh hey-"
    show scara angry
    S "Are you not going to explain that?!"
    show cyno neutral
    C "I think that was pretty self explanatory."

    menu:
        "Please explain what that was.":
            show lyney disgust
            L "It's a long story unfortunately."
        "I'm lowkey into that.":
            show scara fear exclamation
            S "Woah don't make it weirder than it already was."
            show scara neutral none

    show lyney neutral sparkles
    L "Anyways you must be wondering why the three of us are here!"
    show cyno happy
    C "well me and lyney were on our way to the music rooms to hang out as bros when we stumbled across scara who was tragically on his way to genshin society until we heroically saved him from such a tragic fate."
    show scara angry
    S "What?? That's not how it was at all."
    show lyney neutral none
    L "That's because he followed us here."
    show scara disgust
    S "Ugh these guys, anyways what are you doing here?"

    menu:
        "on my way to genshin society.":
            show cyno angry
            C "Well if you all want to go so bad why don't you?"
            show scara angry
            S "No don't make him do that to himself."

        "actively trying to avoid you guys.":
            show lyney sad
            L "What did we do?"
            show scara disgust
            S "What did you guys not do?"

    show lyney happy
    L "Well either way you aren't doing anything that special so may as well come with us."
    
    menu:
        "stranger danger...":
            show lyney angry
            L "Shush we have known you long enough just come."
        "depends...":
            show lyney neutral question
            L "Depends on what?"
            show cyno happy
            C "Just depends."
            show lyney angry none
            L "I don't really care, just come with us."
    
    show scara neutral question
    S "Before we kidnap him, why are we going to the music rooms."
    show cyno neutral
    C "It's just quiet there if a room's not taken."
    show scara disgust
    S "We can literally leave campus, let's just go."
    
    scene city
    show cyno at center
    show lyney at right
    show scara at left
    with fade

    show cyno neutral exclamation
    C "the real world…"
    show lyney fear
    L "Yea.."
    show scara angry
    S "Stop acting weird."
    show lyney sad
    show cyno neutral none
    L "Ah yes we need to uphold his reputation to people who he's never met."
    S "Why did I willingly come with these 3 weirdos?"

    menu:
        "what'd I do bro-":
            show scara neutral vein
            S "Guilt by association."
            show cyno neutral
            C "Makes you guilty as well I don't see your point?"
            show lyney disgust
            L "Oh my gosh scara your tsundere act is killing me."

        "says the bowl-cut looking ahh.":
            show scara angry
            S "Yea you're saying that with a choppy looking blonde shag that looks like it was in the wind your entire life."
            show cyno fear
            C "The girls are fighting!"
            show scara angry vein
            S "Shut up or I'll fight you too."
            show cyno happy glee
            C "You are half my height, what are you going to do bro?"

    show lyney fear
    L "If we anger him anymore we will have to deal with someone who's even more bratty than this."
    show cyno neutral none
    C "So should we console him or something?"
    show cyno embarrassed
    C "Its okay, scara, we are here for you!"
    show scara disgust none
    S "..."
    show lyney neutral
    L "Nah I'm just saying now we are out here lets go somewhere!"
    C "Where?"
    show scara happy glee
    S "How about that penguin cafe?"
    show lyney neutral
    L "Oka!"

    scene penguin cafe
    show scara at left
    show cyno at center
    show lyney at right
    with fade

    show lyney happy
    L "This place is so cute!"
    show cyno neutral
    C "Okay I'm bored now."
    show lyney angry
    L "We just got here!"
    show cyno neutral
    C "Yea you are right, I'm yet to see this penguin plush."
    show cyno happy
    C "Wow… this penguin plush!!!"
    show cyno happy sparkles
    C "This is amazing lets stay here forever!!!"
    show cyno -sparkles
    show lyney disgust
    L "The switch up was quick-"
    show scara neutral
    S "I guess this is our table now."
    show lyney neutral
    L "Hey you two, come sit down!"
    S "..."
    L "..."
    C "..."

    "{i}the conversation seems to have died down a bit.{/i}"

    show cyno neutral
    C "Can we order?"
    show scara fear exclamation
    S "Wait, I haven't even seen the menu yet."
    show cyno angry
    C "Don't care, WAITER!!"

    "{i}Cyno ends up putting an order for all of us.{/i}"

    show scara angry -exclamation
    S "Could have at least let me order.."
    show lyney sad
    L "Yea, I wanted the penguin marshmallows!"
    C "It will be worth it trust guys."
    S "Wait our orders here already? That was quick."
    L "We are the only people here."
    show cyno neutral
    C "And the main demographic is like children who are probably at school right now and not 4 college men."
    show lyney neutral
    L "Cyno, why on earth is there SO MUCH FOOD?"
    show scara neutral
    S "Wait.."
    show scara fear
    S "IS THIS THE WHOLE MENU?"
    C "Yea."
    show scara angry
    S "WHY?"
    show scara fear
    S "Where did you even get the money for this??"
    show cyno neutral
    C "I don't know, apparently some guy named nanook died and I inherited his will or something."
    show lyney disgust question
    L "And you spent it all at a penguin cafe??"
    show cyno happy
    C "Nah he must've been rich or something because it was a lot."
    show scara disgust
    S "Who is that guy? Are you even related to him?"
    show cyno sad
    C "I've seen him in visions quite a few times."
    show cyno happy
    show lyney neutral none
    C "Whatever, let's eat!"
    show cyno happy glee
    C "itadakimasu!"
    show scara angry
    S "That's not how you say it…"
    show cyno sad -glee
    C "My bad gang..."
    show lyney neutral
    L "Hey, you've barely eaten, is there something wrong?"

    menu:
        "is this not a lot?":
            show cyno happy
            C "Well there's 4 of us so it works out!"
        
        "The food is ass.":
            show scara angry
            S "How dare you!"
            show lyney sad
            L "How can you not like it! It has penguins on it.."
            show lyney happy
            L "Like on everything, so many penguins everywhere."
            show lyney happy sparkles
            L "ABSOLUTELY EVERYWHERE!"
        
        "just savouring every bite!":
            show cyno angry
            C "Less savouring and more eating we have a lot to get through."

    show scara disgust
    S "I mean, this is a lot though. Are we sure we can finish this?"
    show scara neutral
    S "This is enough to feed someone for like a week."
    show cyno neutral
    C "Well, it counts as meal prep."
    show lyney neutral -sparkles
    L "No, it doesn't. We need to find a way to not waste all this food."
    show scara angry
    S "Just why did you buy so much?"
    show cyno neutral sparkles
    C "50\% of the profits go to penguin charities!"
    L "I mean that's good but now we have too much food!"
    show lyney thought
    show cyno -sparkles
    L "What do we do with all this?"

    menu:
        "We can give it to the rest of the club members!":
            show lyney neutral
            L "Yea! Good idea. I mean even if its a lot we have eaten most of it."
            show scara angry
            S "More like you did."
            show lyney neutral question
            L "Are you just mad I ate the last few penguin cookies?"
            show scara angry sigh
            S "Hmph."
        "I don't know give it to teachers or something...":
            show scara neutral
            S "Why though?"
            show lyney sad sigh
            L "I mean, what else do we have to do with it."

    show cyno neutral
    C "Well let's just pack the rest and get out."

    scene city
    show scara at r51
    show cyno at r53
    show lyney at r52
    with fade

    show lyney disgust
    L "So we have to carry this all the way back to school?"
    show cyno sad sigh
    C "Yea.."
    
    show miku at r55
    show naoto at r54
    with dissolve

    show cyno -sigh
    show naoto fear exclamation
    N "What are you guys doing out here?"
    show scara neutral
    S "It's your lucky day!"
    show lyney neutral
    L "Oh hey you two! I thought you had a meeting to go to with the investors."
    show miku neutral
    M "Nah, I got bored so I told the teacher running it that I had to get stuff."
    show miku embarrassed
    M "Then I convinced naoto to skip with me!"
    show naoto embarrassed none
    N "Well, we weren't doing much there anyways..."
    show naoto angry
    N "The investors aren't really interested in the students at all."
    show cyno neutral sigh
    C "I don't know if that's the best move for the student council."
    show miku angry
    M "It's fine, we are heading back now!"
    show cyno -sigh
    show naoto neutral
    N "If we return with something they will forgive us either way!"
    show naoto happy glee
    N "So we bought 37 staplers."
    S "Why that many?"
    show naoto sad sigh
    N "Uh, I'm not sure."
    show lyney sad
    L "Always thought you'd be more financially responsible, naoto but turns out you are just like cyno..."
    show miku disgust
    M "Wait, why do you say that? Is that why you guys have so many take out boxes?"
    show scara angry
    S "We went to a penguin cafe and cyno ordered the entire menu.."
    show cyno happy
    C "For the greater good."
    show miku fear
    M "Cyno this is the second catastrophic decision you've made today."
    show miku sad
    M "Please tell me this is a part of the condition or something.. Please tell me you're not just like this."
    show scara sad
    S "I don't even want to ask about the first one."
    show naoto neutral
    N "If you guys don't have a use for all this food, we may as well take it off your hands."
    show cyno neutral
    C "What would you do with so much of it?"
    show naoto happy sparkles
    N "Give it to investors and staff!"
    show scara neutral
    S "I mean, we were gonna do that anyways so may as well just take it now."
    show naoto -sparkles
    show miku angry
    M "Nuh-UH! You guys brought all this, you four idiots are carrying it to the meeting."
    S "Hey, it was just cyno why make us do it?"
    show miku angry vein
    M "GUILT BY ASSOCIATION!"
    show lyney fear
    L "O, karma.."
    show miku serious -vein
    M "Now let's go we have a meeting to be at!"
    show cyno disgust
    C "Didn't you skip it though?"
    show miku neutral vein
    M "Lets just go!"

    Y "{i}We all head to the student council meeting to give penguin themed cakes to the investors, staff and student council.{/i}"
    Y "{i}After that, we decided it's best to split off and head to class as to not cause more trouble.{/i}"

label day5afternoon:
    scene entrance evening
    show screen top_right_ui(5, "After School")
    with fade

    call hangout

label day5evening:
    stop music fadeout 1.0

    $ bad_ending = not any((c.level == 3 and c.points >= 5) for c in [cyno, lyney, scara, naoto, miku])
    
    scene roof evening
    if bad_ending:
        show screen vignette_screen
    else:
        queue music main

    show screen top_right_ui(5, "Evening")
    with fade

    Y "{i}as per Miku's request, I head up to the rooftop to attend the club meeting.{/i}"

    if bad_ending:
        Y "{i}…{/i}"
        Y "{i}no one's here.{/i}"
        Y "{i}…strange, miku said we would meet here at this time, where else could they be?{/i}"
        Y "{i}…{/i}"
        Y "{i}I'm getting the feeling that something's not right.{/i}"
        Y "{i}perhaps I should investigate around the campus...{/i}"
        Y "{i}where should I go?{/i}"

        # [from this point onwards, a low hum sound should build up, no music or muffled music, an occasional shaky static/glitch effect on the screen]

        # [each decision changes BG to the respective location, a filter should be applied to give a dark eerie feel to the location, in the corners or shadows of the image there should be a faint, small silhouette of a whisper, not immediately obvious or observable though]
        
        default bad_ending_searched = set()

        menu .bad_ending_search:
            set bad_ending_searched

            "student council office":
                scene office evening with fade:
                    matrixcolor SaturationMatrix(1 - 0.2 * len(bad_ending_searched))
                pass
            "campus entrance":
                scene entrance evening with fade:
                    matrixcolor SaturationMatrix(1 - 0.2 * len(bad_ending_searched))
                pass
            "library":
                scene library with fade:
                    matrixcolor SaturationMatrix(1 - 0.2 * len(bad_ending_searched))
                pass
        
        Y "{i}the atmosphere here feels heavy.{/i}"
        Y "{i}…{/i}"
        Y "{i}seems like there's no one here.{/i}"

        if len(bad_ending_searched) != 3:
            jump .bad_ending_search

        Y "{i}…{/i}"
        Y "{i}I'll look around one more time.{/i}"

        scene hallway evening:
            matrixcolor SaturationMatrix(0.4)

        # [BG change - hallway, silhouette appearance looks more obvious now, still same effect as before, maybe more frequent and intensified]
        
        Y "{i}the atmosphere feels even heavier than before.{/i}"
        Y "{i}I can make out something in the distance, like its moving closer toward me before I can even move myself.{/i}"
        
        Q "Jack…"
        
        Y "{i}the distorted voice echoes inside my head, it's barely recognisable.{/i}"
        Y "who's there?"
        Y "more importantly, what even are you?!"

        Q "never mind that."
        Q "Jack, you have disentangled yourself from the threads of fate, and failed to walk along the intended path as foretold."
        Q "and so… your friends have lost themselves to chaos and disorder."
        Q "now you must bear the weight of their suffering."

        Y "?!"
        Y "no… this can't be real…"
        Y "miku, scara,, …they're all… gone?"

        Y "I thought I was helping them… what could I have done wrong?!"

        # [BG change to silhouette glitching closer/enlarging]

        menu:
            "tell me what to do!":
                pass
            "I won't let this happen!":
                pass
            "I'm begging you, bring them back!":
                pass

        Q "it is too late."
        Q "now you have no choice but to surrender to your fate."
        Q "you must hang your soul upon the threads once more, and start over again,, from the very beginning."
        
        # [BG change to silhouette glitching closer/enlarging]

        menu:
            "no! I'll still remember them.":
                pass
            "I submit… I cannot continue fighting.":
                pass

        Q "no matter what, you will forget. after defying all meaning, and trying to help no one, this is the greatest solace that can be bestowed upon you."
        Q "just remember…"
        Q "to establish a bond."
        Q "with those you choose."
        Q "or lose yourself forever."
        
        # [BG change to silhouette glitching closer/enlarging, this instance it should be near towards covering the entire screen]
        
        Y "{i}the presence of the silhouette is suffocating, I feel like I'm losing all control{/i}"
        
        Q "the truth you vowed to seek remains far out of reach."
        
        Y "{i}i feel like im… slipping away…{/i}"
        Y "{i}…{/i}"
        Y "{i}..{/i}"
        Y "{i}.{/i}"

        Q "try again. someone is still waiting for you."

        ">> you have reached the failed ending."

        $ renpy.set_return_stack([])
        return

    else:
        show lyney sad at r55
        show miku angry at r51
        show naoto neutral at r52
        show scara neutral at r54
        show cyno neutral at r53
        with dissolve

        L "miku, why on earth did you summon us at this hour, I thought we were meeting much earlier…"
        show miku angry
        M "shush it and help me set this up!"
        show naoto neutral
        N "I can help!"
        show naoto fear
        N "So this is your telescope…"
        show miku neutral glee
        M "Yeah, have you used one before?"
        show miku -glee
        show naoto neutral
        N "when I was younger but not exactly recently."
        show lyney happy sparkles
        L "I think I recall going to a park to observe stars with my sister before."
        show lyney -sparkle
        show naoto neutral
        N "Is there anything special today that we can look out for?"
        show scara neutral
        S "Not that I know of.."
        show miku angry vein
        M "Scara! You were meant to research this before you came!"
        show lyney disgust
        L "Why did you task him with that?"
        show cyno neutral
        C "we could easily look out for venus?"
        show miku neutral none
        show naoto disgust
        N "and how do you know that?"
        show cyno happy
        C "I just searched up which was the easiest to see."
        
        show scara disgust
        S "I don't get how that's relevant to what we are finding."
        show lyney happy
        L "Sometimes, you don't need to actively search for what you want to see, maybe the answer will come to us if we look."
        show miku happy glee
        M "well now me and naoto have finished setting this up so we can try!"
        show miku neutral
        M "Naoto you can try first."
        show naoto embarrassed
        N "I don't really have that much experience in astronomy.."
        show miku happy
        M "Well let me see this for myself then!"
        show cyno neutral
        C "What do you see?"
        show miku neutral
        M "Stars…"
        show cyno embarrassed
        C "Well, yea."
        show miku serious
        M "No but it's strange..."
        show miku serious
        M "V572 Velorum. It's a star in the 'Vela' constellation."
        show miku serious
        M "It's only the start of April but this stars reached its peak brightness."

        show miku serious thought
        M "At this time of the year, it shouldn't be this bright."
        M "and an increase in brightness in this case can only be caused by one thing."

        show miku fear question
        M "it's moving closer to us?"
        show lyney fear question
        L "What, like a comet?"
        show miku neutral none
        M "not at all! That's the strange thing,"
        show lyney -question
        show miku neutral exclamation
        M "this star is defying the universe itself and all laws of physics."
        show miku neutral
        M "and I don't even think that's the only one!"
        show miku serious none
        M "Interstellar objects are passing through our solar system more rapidly."
        show miku serious
        M "Comets are defying their natural orbit."
        show miku serious
        M "Stars that we have observed the formation and life of for years have had accelerated formations and deaths."
        show miku serious thought
        M "The evidence is only becoming more real every second."
        show miku disgust none
        M "I mean, I had a hunch. But the more this evidence piles up the more suspicious it all becomes."
        
        Y "..."
        show cyno neutral
        C "It really feels like we have figured this all out!"
        show naoto neutral
        N "I think, however, we are still missing an essential bit of information."
        show lyney neutral question
        L "and what's that?"
        show naoto neutral exclamation
        N "I don't know, but perhaps its like what you said lyney."
        show lyney neutral none
        show naoto neutral none
        L "maybe if we just look, we will find it?"

        Y "{i}There's silence between us.{/i}"
        
        play sound running

        $ renpy.pause(4.5)

        scene black with fade

        Y "!!!"
        L "Naoto, did you just turn off the lights on the roof?"
        N "maybe we don't need that telescope, just look up!"

        scene stars with fade

        Y "{i}we all look up in unified amazement.{/i}"
        L "You know I've never been that much into astronomy and figuring out the universe. A magician must keep their secrets! And so must the world around us sometimes..."
        L "But sometimes engaging with this fascination with the sublime is fascinating... We are really small when it comes to it..."
        N "In a way it's scary. But also I disagree, we don't know the full extent of our purpose but we exist in a web of interconnectivity with the world around us."
        S "I'm guessing you must have strong links with nature then."
        N "kind of... I've never really thought about it."
        S "I did like what you said though naoto. I feel like me personally, I'm always seeking something, belonging, a purpose, something bigger than myself... its easy to forget that I'm already doing something for the world around me."
        M "I mean we all have our place in this world. What we do with it is what we choose! For me, I want to connect the worlds somehow."
        L "In what way?"
        M "In any way I can! Connecting our world in order to ensure harmony in our lifetimes would be nice, but I'm also fascinated with connecting humanity to life out there... if it's possible."
        M "whatever is able to bring lifeforms together is something worth achieving in my book."
        C "Life here is so divided already, I wonder if contacting others out there could ever end well."
        L "Well when we come together we can make beautiful things happen."
        C "I guess what unites us the most is shared emotions and experiences, like this right now, as corny as that sounds."
        C "But to me at least, its moments like these that make a big difference to us as living beings. Moments of passiveness that makes us feel a sense of being, but also drives us to achieve something."
        C "when people are too active in their roles of action they can get carried away thinking about themselves."
        L "That's a lot of talk coming from you..."
        C "oh c'mon."
        N "Cyno's right..."

        scene roof stars
        show lyney neutral at r55
        show miku neutral at r51
        show naoto neutral at r52
        show scara neutral at r54
        show cyno neutral at r53
        with fade

        show naoto embarrassed
        N "it reminded me of an instance.. but I just don't remember it."
        show miku neutral
        M "happens to the best of us.."
        show cyno neutral
        C "Are you sure this isn't a vision from another universe?"
        S "If we are going to believe that, it's going to make understanding our own memories a lot harder."
        show naoto sad exclamation
        N "But it was a big event! someone has got to remember."
        show naoto -exclamation
        show scara neutral thought
        S "…"
        show scara neutral none
        S "I don't recall anything.."
        show miku serious
        M "I mean, sometimes I do feel like a large part of my life is missing."
        show miku serious
        M "Like I can only remember so far back."
        show lyney disgust
        L "I mean, before I came here, my life has been a mess of disconnected events."
        show lyney neutral
        L "Before this, it was so very different. I remember different people, a whole organisation and not even being in education."
        show lyney neutral
        L "The only thing brought forth from that is me and my sister."
        show naoto neutral
        N "Well, when I was younger I pursued a few murder cases, I had made a name for myself."
        show naoto neutral thought
        N "There was a point when I probably decided to get a degree in order for my career to progress more, but I don't remember that moment."
        show naoto neutral none
        N "I only really remember coming here."
        show miku neutral
        M "I don't remember why I ended up here. But now I am and now it's my life."
        show cyno sad
        C "I don't remember anything."
        show cyno sad
        C "I don't remember much day to day unless it matters."
        show cyno neutral
        C "Like meeting all of you."
        show cyno sad
        C "I don't remember any of my past either."

        Y "?!"

        C "Yet weirdly now I'm remembering this other life more visually than my own."
        C "In a weird way, it makes me feel like I know you all a lot more intimately."

        show naoto neutral
        N "Although it's not as extreme, the only clear memories I have are from when we got you, our new exchange student."
        show lyney disgust
        L "The rest is like, you know of it but you don't think you were there, right?"
        
        show scara sad
        S "I…"
        S "get that."

        show scara neutral
        S "I remember a lot. But they all just seem like visions of someone else's life."
        show cyno neutral
        C "And maybe they are."
        show scara sad
        S "I would want to believe that."
        show scara disgust
        S "as much as I'd like to hide it, I feel like the real me doesn't even feel like I'm truly here."
        show lyney sad
        L "It's like someone's infiltrated our memories and taken most of our lives away."
        show cyno neutral thought
        C "Maybe our memory is getting replaced with these new ones!"
        show scara neutral
        S "Rewriting a significant chunk of our lives?"
        show scara sad
        show cyno -thought
        S "That means we are losing a part of ourselves."
        show scara sad
        S "And if all your research or whatever if true, that probably means there's nothing we can do to stop it."
        show miku neutral
        M "I mean it doesn't have to be bad!"
        show scara angry
        S "How can that not be bad, that's almost like our lives being erased!"
        show cyno happy
        C "It has brought us closer, we all now retain this experience and understanding of another universe."
        show scara angry
        S "But do I even like that universe?"
        show lyney happy
        L "Is it not amazing that we have discovered this about the universe though?"
        show lyney embarrassed
        L "It's a bittersweet narrative but maybe, scara, we have figured out ourselves better this way."
        show scara embarrassed
        S "..."
        show scara neutral
        S "To know about myself would be good."
        show scara neutral
        S "And even with this merge, I don't feel different, not compared to cyno."
        show scara happy
        S "And maybe that's because across universes I am already whole.."
        show scara embarrassed
        S "but that's something I can believe if I want and not anything I need to elaborate on."
        show cyno angry
        C "But that also implies I'm not?"
        show scara neutral
        S "Well what do you think that difference is?"
        show cyno disgust
        C "dunno, I'm not me in another universe."
        show cyno happy
        C "But I can say what's made a difference to me recently is just having people."
        show cyno happy
        C "Since when he transferred here, I got to figure out what was wrong with me and I found people who cared."
        show cyno happy
        C "And now when we are so close to finalising this.."
        show cyno embarrassed
        C "It makes me thankful for you all."
        show miku happy heart
        M "We are a great team aren't we!"
        show miku -heart
        show lyney happy
        L "This whole universe thing makes me think we were all destined to come together."
        show lyney neutral glee
        L "I mean even him, we probably would not have guessed to become so close to an exchange student."
        show lyney happy none
        L "But now with this memory stuff it makes me feel like I've known you my entire existence!"
        show naoto happy
        N "In any case, I don't think I would have talked to most of you otherwise."
        show naoto disgust
        N "especially cyno."
        show naoto embarrassed
        N "But I'm thankful I have."
        show cyno happy glee
        C "But most grateful of all is scara, as we finally gave him friends."
        show cyno -glee
        show scara angry
        S "I had my sentimental moment. You can lay off."
        show cyno happy
        C "Nah I'm good-"
        show miku neutral
        M "Hey it's getting dark though."
        show cyno fear
        C "Really?"
        show miku angry
        M "I mean, its getting really late, we are probably going to be kicked out soon."
        show scara disgust
        S "What a way to end off this night huh."
        show naoto fear question
        N "Did you not get permission to be here?"
        show miku embarrassed
        M "No…"
        show naoto -question
        show lyney sad
        L "That can't be good-"
        show cyno neutral
        C "Well then we better hurry and get the hell out of here!"
        show miku neutral
        M "Well we will meet tomorrow at lunch to prepare for our presentation then!"
        
        Y "{i}We all rush off from the rooftop.{/i}"

        hide lyney
        hide miku
        hide scara
        hide cyno
        with dissolve

        Y "{i}Before we leave, I'm approached by Naoto.{/i}"
        
        N "Now that I think about it though.."
        N "Weren't we arguing in that other universe?"
        
        Y "Huh?"

        N "Its weird, we have just spoken about how we all feel so close because of our shared memories being established."
        N "I mean nothing appeared that good, we were fighting, lyney was leaving us, miku was alone in some building, cyno was bleeding out and scara, well, his wasn't bad in a conventional sense, but if you heard it, it was weird."
        N "It feels like something we brushed over rather fast."
        N "Maybe if we aren't careful, we will end up like.. Ourselves?"
        N "Not to scare you or anything! I'm just thinking out loud, ignore me."
        N "Good night."

        call dayend

# cyno scara miku lyney naoto sparrow