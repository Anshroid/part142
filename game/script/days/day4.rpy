label day4:
    call screen calendar(4) with fade

label day4morning:
    play music main
    
    show screen top_right_ui(4, "Morning")
    scene entrance day
    with fade

    Y "…"
    show cyno neutral with dissolve
    C "hi."

    menu:
        "I know what happened last night.":
            show cyno fear question
            C "what in the fourth wall break?"
            show cyno disgust -question
            C "I MEAN, that's a little freaky… you might have seen me doing some very private business."
        "GOOOOOOOD MOOOOOOORRRRRRRNING!":
            show cyno happy glee
            C "GOOOOOOOD MOOOOOOORRRRRRRNING to you as well!"
        "hey bro what's up?":
            show cyno neutral
            C "nothing much, but… um… how do I put this…?"

    show cyno neutral none
    C "just listen to me, If anyone asks where I am please just say I killed myself."
    
    Y "?!"

    show cyno happy heart
    C "bless your soul, I'll see you at lunch."
    
    show sparrow neutral at right with dissolve
    Q "where do you think you're going, cyno…"
    show cyno angry vein
    C "fuck me…"
    show sparrow freaky
    Q "oh… sure thing."
    show cyno disgust sigh
    C "…what do you want now, sparrow?"
    
    "{i}Cyno leans in to talk to me privately.{/i}"

    show cyno neutral none
    C "btw this guy has been following me around campus, its kind of creepy..."

    menu:
        "Maybe, you don't know this yet, but he could potentially be your soulmate that you were destined to meet and this is the universe's way of trying to bring you two together because you were MADE for him because he is more supreme than you and only deserves nothing but respect due to his sheer power and authority within society!":
            show cyno angry
            C "…"
        "yeah, that's weird.":
            show cyno happy
            C "you can say that again."

    show sparrow sad
    Sp "look, cyno… my love- I-I MEAN… my student… n-no, that sounds a bit too possessive…"
    show sparrow neutral
    Sp "ANYWAY, I just have one question, and I'll stop bothering you for today…"
    show cyno angry
    C "and what is that?"
    show sparrow neutral
    Sp "hold on, gimme a sec, I can't fumble this."
    show sparrow neutral exclamation
    Sp "…AHEM.."
    show sparrow freaky question
    Sp "d-do you have snap perchance… nya~?"
    show cyno disgust
    C "uhm, no?"
    show sparrow fear exclamation
    Sp "W-WHAT?!?!?!"
    show sparrow fear none
    Sp "THEN CYNO, PLEASE, IM BEGGING YOU… WHERE CAN I ADD YOU?"
    show cyno neutral
    C "you said only one question."
    show sparrow sad
    Sp "…pwease?"
    show cyno neutral
    C "…uhhhhh, I'm pretty sure I have the normal messages app."
    show cyno happy
    C "and yeah that's about it."
    show sparrow fear
    Sp "…?!"
    show sparrow fear
    Sp "no insta?"
    show cyno neutral
    C "nope."
    show sparrow sad
    Sp "not even grindr??"
    show cyno fear
    C "no- WAIT WHAT?!"

    menu:
        "that's because he communicates with carrier pigeons!":
            show cyno fear
            C "?! y-yeah! Who needs phones anyway?"
        "he has a discord account though.":
            show cyno disgust
            C "I do not…"
            show sparrow neutral
            Sp "what is a discord?"
        "chronically offline ahh.":
            show cyno neutral
            C "life has greater experiences to be made than using a manmade electronic device, you should try to expand your limits and step out of your comfort zone sometime."
    
    show cyno neutral
    C "look, sorry about this, but I'm going to try and get out of this conversation."
    
    menu:
        "what about me?":
            pass
        "okay cool.":
            pass

    show cyno sad
    C "good luck…"
    
    hide cyno with dissolve
    "{i}Cyno leaves{/i}"

    show sparrow fear
    Sp "NO CYNO, DONT LEAVE ME!"
    show sparrow sad
    Sp "…"
    show sparrow neutral
    Sp "!! ah-"
    show sparrow freaky
    Sp "hello, EXCHANGE student-"

    menu:
        "why the emphasis on exchange?":
            show sparrow neutral
            Sp "just making sure you know your place in our school community."
        "I love you can I match your freak?":
            show sparrow neutral
            Sp "sure, but you're never gonna be that bitch, you understand?"
        "hello.":
            show sparrow angry question
            Sp "pft, how lame. Where's the substance? the tonal whiplash?"
            show sparrow -question
    
    Y "{i}I notice Scara walk by. out of pure desperation I make a signal to him pleading for help.{/i}"
    
    show scara neutral at left
    S "jack. and who the hell is th-"
    show scara disgust
    S "{i}*sniffs*{/i} EWWWW, what the FUCK is that stench?"
    show sparrow neutral
    Sp "that \"stench\" is my lynx spray, I buy it in bulk to get fucking emos like you away from me."
    show sparrow freaky
    Sp "and speaking of, do I smell any aftershave on you? {i}*sniffs*{/i}"
    show scara angry vein
    S "GET OFF ME!"
    show sparrow angry
    Sp "well NO, I DONT. because YOU don't put on ANY deodorant. How typical. Y'know, cause you're an EMO."
    show sparrow angry
    Sp "so DONT talk as if you're able to understand my VERY MATURE adult habits!"
    show scara neutral none
    S "…"
    show scara angry
    S "I'm probably a lot older than you."
    show sparrow neutral
    Sp "what the fuck's that supposed to mean, don't tell me you're some 500  year old tsundere who lives in an 18 year old's body."
    show sparrow angry question
    Sp "also what is up with that look, the bowl cut's really starting to piss me off."
    
    menu:
        "the person itself or just the hairstyle?":
            show sparrow neutral none
            Sp "hm, now that you say it, probably… both!"
            show scara disgust
            S "ugh, why are you encouraging him?"

        "justice for bowl cuts.":
            show sparrow neutral none
            Sp "there was actually a society for that in the last academic year."
            show scara disgust
            S "what the fuck."
            show sparrow neutral
            Sp "I know right? I took it down, of course."
            show sparrow angry
            Sp "now my next target is genshin society…"

        "what happened to treat others as you would treat yourself… bitch.":
            show sparrow neutral none
            Sp "it was found dead in a ditch."
            show sparrow freaky
            Sp "any golden rule is now my rule!"

    show scara angry
    S "this guy is SO obnoxious."
    show scara angry vein
    S "anyway, I'll just tell it like it is. You're NOT that guy, you NEVER have been, and you should get the FUCK away from me and wacky jacky."
    
    Y "wacky jacky?"

    show scara fear exclamation
    S "w-what about it? It just slipped out of my mouth, that's all… dunno why-"
    show sparrow angry
    Sp "…"
    show scara happy -exclamation
    S "what's wrong? Can you not handle such a simple insult? Wow, you really are just a fragile piece of shit."
    show scara happy
    S "what a god damn waste of space…"
    show sparrow angry
    Sp "h… h-how…. HOW…."
    show sparrow angry vein with hpunch
    show scara fear
    Sp "HOW {size=+40}{b}DARE{/b}{/size} YOU!"
    S "?!"
    show sparrow angry -vein
    Sp "HOW DARE YOU CHALLENGE MY AUTHORITY, I WILL NOT TOLERATE THIS DISOBEDIENCE ANYMORE."
    show sparrow angry
    Sp "I HAVE CONNECTIONS, AND I'LL USE ALL MEASURES AT MY DISPOSAL TO GET YOU EXPELLED, IMMEDIATELY."
    show scara embarrassed
    S "hah, you have to be joking right?"
    show sparrow angry
    Sp "…"
    show scara fear
    S "n-no? C'mon, lets reconsider this, or at least come back to it next week…"

    hide sparrow with dissolve
    "{i}Sparrow turns away from scara and struts off.{/i}"

    show scara angry
    S "HEY, COME BACK."
    show scara fear
    S "I SAID COME BACK!"
    
    hide scara with dissolve
    "{i}Scara runs after sparrow helplessly{/i}"
    Y "{i}it's probably best to leave them to it, I'm almost late for my morning lecture.{/i}"

label day4lunch:
    scene classroom day with fade
    show screen top_right_ui(4, "Lunch") with Dissolve(2)

    show miku at r51
    show lyney at r52
    show scara at r55
    with fade

    Y "{i}Today we are meeting back at the club room to discuss our findings from yesterday.{/i}"
    Y "{i}Cyno and naoto don't seem to be here yet.{/i}"

    show miku happy
    M "First of all, I'd like to thank you all for the effort you put into researching yesterday!"
    show lyney disgust
    L "Uhm Miku aren't we missing people?"
    show scara neutral
    S "Yea, there's only four of us."
    show scara happy glee
    S "I'm not complaining though-"
    
    show scara disgust -glee
    show naoto neutral at r53 with dissolve
    show cyno neutral at r54 with dissolve
    N "Sorry we are late!"
    show lyney disgust question
    L "Huh? Were you doing something together?"
    show cyno neutral
    show lyney -question
    C "Yes, we have something to say."
    show miku angry
    M "Ahem! I have stuff to announce first."
    show miku serious
    M "And Naoto I didn't see you at the council meeting earlier-"
    show naoto fear
    N "I have reasons for that, you see it's what cyno and I-"
    show miku angry
    M "Not right now!!! Let me finish first!"
    show cyno angry
    C "Make it quick."
    show miku disgust
    M "Rude."
    show miku neutral
    M "But anyway-"

    show miku happy glee
    M "Now we have made it deeper into the semester the school has announced unique club opportunities!"
    show miku neutral -glee
    M "The university is offering publishing and funding for research and academic based clubs and societies."
    show scara disgust
    S "Do we really count as that.."
    show miku neutral sparkles
    M "Not only that but the publishing opportunities also lead to a chance to be recognised by professionals in certain fields."
    show miku happy -sparkles
    M "There's never been better timing for what we are doing!"
    show miku neutral
    M "If we want to try and go forward with this, we have a deadline for next week in which all club members who have contributed need to pitch their studies to members of faculty."
    show lyney neutral
    L "I think our deadline might be sooner than that though-"
    show lyney sad
    L "likee a lot sooner."
    show miku disgust question
    M "Huh?"

    show lyney neutral thought
    L "Well he's only here on exchange and he's done as much work as the rest of us when it comes to this."
    show lyney -thought
    show naoto neutral
    N "And he was one of the members who helped this club even exist."
    show miku serious none
    M "So you're saying we need to get this done even sooner."
    show cyno neutral
    C "Well, if we want to include him, we have to pitch this as soon as possible."
    show scara neutral
    S "Can we even include an exchange student? He's only here temporarily and besides, I'm sure his project takes priority over a club-"
    show miku neutral glee
    M "Well nothing said we couldn't include him."
    show miku sad -glee
    M "But you're right on the second part, considering this isn't the main reason why he's here he may not even want to do this."
    show naoto neutral
    N "Well, do you want to be credited?"

    menu:
        "You're not going to exploit my labour without at least crediting me?":
            show cyno happy
            C "The passion speaks for itself."

        "I would like to be included!":
            show miku happy
            M "That's the spirit!"

        "I honestly don't care.":
            show lyney angry
            L "Well you played a part in this!"
            show cyno neutral
            C "Agreed, I think either way it's unjust for him not to receive any credit. Even if its temporary, he is a club member."
        
        "I didn't do any work.":
            show scara disgust
            S "That must be a horrible attempt at being humble, you were too eager to be in this club."
            show scara angry
            S "Just give him the damn credit!"

    show miku neutral
    M "Well then! That settles things!"
    show miku embarrassed
    M "Though it does mean we have a tighter deadline." 
    show lyney neutral glee
    L "But it also means we have more people working on it!"
    show lyney -glee
    show miku fear exclamation
    M "There's only one possible day we can pitch our idea this week, and that's saturday!"
    show scara disgust
    S "That gives us a day and a half."
    show naoto fear exclamation
    N "But we are on the edge of a break through!"
    show miku neutral question
    M "Huh?"
    show naoto neutral none
    N "Sorry, Cyno and I have waited long enough."
    show miku disgust none
    M "Well I guess you'll start us off with the research stuff."

    show scara neutral
    show miku neutral
    show naoto neutral
    N "Yesterday in the library, I experienced something weird."
    N "It was like after I talked to him, I saw this vision."
    N "I saw an alternative reality so life-like it was like it was one of my own memories."
    show naoto disgust sigh
    N "This is really awkward to explain."

    show naoto -sigh

    show cyno happy
    C "Don't worry, you get used to it-"
    show cyno neutral
    C "What naoto was experiencing is something I've experienced many times before."
    C "my own 'visions' have all shown the same reality."
    C "And what we discovered yesterday is that the visions seem to connect somehow."
    C "We both experienced it after talking to {i}him{/i}."

    Y "Me?!"

    show cyno disgust
    C "Yes, and what we saw occurred at the same place, presumably at roughly the same time."
    show cyno neutral
    C "It occurred in a desert, I was alone but up ahead I saw the two of them."
    show naoto neutral
    N "For me, it was in this desert and me and you were in an argument."
    show lyney neutral
    L "Now that you mention it I saw something similar."
    show lyney neutral thought
    L "It occurred in the library too, not exactly sure when."
    show naoto neutral question
    N "What did you see?"
    show lyney sad none
    L "I was leaving you all for some reason and I had a moment to say my goodbyes."
    show lyney neutral
    L "I think you all were heading off to go to some desert."
    show lyney neutral
    L "Maybe I was just imagining the end of the week."
    show naoto disgust none
    N "So then did we all experience this?"
    show cyno neutral question
    C "How about you, Miku?"
    show miku neutral
    M "Well yea, it occurred to me as well but I didn't think much of it."
    show miku serious
    M "I was more focused on the research considering I thought we would discuss that today."
    show cyno -question
    show scara neutral
    S "We will get round to it."
    show lyney neutral question
    L "So what did you see?"
    show miku fear exclamation
    M "the whole desert thing! Except I was in some building, and I can't remember why but I was mad at naoto."
    show lyney -question
    show miku neutral -exclamation
    show scara disgust
    S "Wow Naoto seems like this version of you is really unlikeable!"
    show naoto neutral
    N "I wonder what I must have done to make you all feel that way."
    show lyney neutral
    L "Scara did you see anything?"
    show scara neutral
    S "Yea but it's not useful."
    show naoto neutral
    N "Anything that helps us piece it together is useful."
    show scara angry vein
    S "No, trust me when I say it's not useful."
    show scara -vein

    menu:
        "Come on, tell us!":
            show scara neutral
            S "Well I saw you pull out a pregnancy test."
            show scara disgust
            S "and then some white boy got mad at you."
            show lyney fear
            L "Yea, so not helpful."
            show scara neutral
            S "I think we were near a desert though-"

        "If its not important lets brush over it.":
            show scara happy
            S "Good choice!"
            show naoto angry
            N "I'd prefer if we know."
            show scara disgust
            S "On Cyno's life it was not important."
            show cyno angry question
            C "Why on my life?"
            show scara neutral
            S "Why not?"
            show cyno sad none
            C "I'm offended..."

    show naoto disgust
    N "Well, moving on from that-"
    show lyney neutral
    L "How about you?"
    Y "I haven't experienced anything.."
    show scara neutral
    S "So you're an isolated case."
    show naoto neutral
    N "We at least know mostly everyone experienced this."
    show cyno neutral thought
    C "What me and naoto's theories are is that these all string together to tell some sort of story."
    show lyney neutral
    L "and?"
    show cyno happy none
    C "And just that, we thought it would be useful."
    show lyney disgust
    L "So wait, this only provides more questions than answers.."
    show lyney fear question
    L "If this is something Cyno experienced a lot, was it due to his condition? And if so, are WE all now infected?"
    L "What do these visions even mean anyways? Why are we seeing them or is everyone under this condition seeing them?"
    show cyno angry
    C "Slow down."

    show lyney -question

    show cyno neutral
    C "I can't say you all have this condition suddenly because it didn't start like this."
    show cyno neutral
    C "I experienced physical side effects before all these visions."
    show scara neutral
    S "But do we think this condition is linked to this at all?"
    show cyno neutral
    C "Again that's as far as we got-"
    show miku serious
    M "I don't think we are the only ones with a tainted memory."
    show miku serious
    M "After my research in the library I went online to see more stuff."
    show miku fear
    M "Medical records have been reported to have false information that were previously not recorded."
    show miku serious
    M "For example, doctors have reported patients contracting illnesses or undergoing surgeries that they had never gone through."
    show miku disgust
    M "There was around 340 separate incidents of it in this week alone."
    show scara disgust
    S "Are you saying this to move the conversation towards the research-"
    show miku serious
    M "Not exactly.."

    show naoto neutral
    N "I don't know how applicable my research was here however."
    show naoto neutral
    N "but the mental shutdowns, specifically cyno's condition, don't match current day explanations of psychology, like cognitive neuroscience."
    show naoto neutral
    N "latest reports show that fMRI, EEGs, and even mind mapping techniques such as brain fingerprinting are ineffective in revealing the cause of their symptoms, which is likely why the doctors couldn't find anything wrong with cyno in the first place."
    show naoto neutral
    N "only psychodynamics offered the most similarities to cyno's account, albeit very outdated."
    show naoto fear
    N "for instance, severe stress and trauma can disable conscious control over the mind to protect people from psychological harm."
    show naoto neutral
    N "unfortunately that's as far as I got."
    show lyney neutral
    L "By the end of mine, I ended up concluding that some of us were too grounded in reality."
    show lyney neutral
    L "To understand these 'memories' and this condition we need to accept that there's something supernatural at play."
    show scara disgust
    S "So looking into fiction turned out to be the best option."
    show cyno neutral
    C "Oh no, you accidentally helped us."
    show scara neutral
    S "I read this book where doppelgangers of people started appearing."
    show scara neutral
    S "And it was caused by the death of an alternate, more advanced, universe dying off which lead people to migrate here."
    show lyney disgust question
    L "Was your research just reading fiction?"
    show scara angry
    S "Fiction reflects reality or something."

    show lyney neutral none
    show naoto neutral
    N "What if something like that was occurring though?"
    show naoto neutral thought
    N "Like, maybe these visions are real and are being seen here as a way to preserve themselves?"
    show naoto -thought
    show miku serious
    M "So this is like a message from an alternate universe."
    show cyno neutral question
    C "That could explain the memories, but what about matter?"
    show lyney neutral
    L "The 'matter' could just be a side effect of the memories though."
    show cyno -question
    show lyney neutral
    L "Like those doctors reports, maybe those were written down because of a mix up between memories from this reality and memories from an alternative universe."
    show miku serious
    M "But that's the thing, it goes beyond just medical documents."
    show miku serious
    M "There have been more frequent 'inconsistencies'."
    show miku fear
    M "In some areas, the altitude of hills or even in plains have adjusted slightly."
    show miku fear
    M "Roads are appearing on GPS maps that don't exist."
    show scara disgust
    S "Everything affected seems so mundane and ordinary."
    show cyno neutral
    C "But what about the condition?"
    show scara neutral
    S "That's if we are categorising that into this."
    show scara neutral
    S "If we are then it probably is the most extreme aspect.."
    show scara neutral thought
    S "From what it seems, minor parts of the alternate reality are also being brought here."
    show scara -thought
    show naoto neutral thought
    N "But that can't be explained with the whole 'memory merge'!"
    show naoto -thought
    show lyney fear
    L "What if that reality is merging with our own?"

    show cyno disgust
    C "What"
    show lyney fear question
    L "Like the universes are merging?"
    show miku serious
    M "That's a big claim..."
    show lyney -question
    show scara neutral
    S "Even harder to prove!"
    show naoto neutral
    N "Well thus far we have looked into our memories, then objects but then also geographically."
    show naoto neutral
    N "We haven't explored anything outside of this universe."
    show cyno neutral
    C "I'd imagine universes merging would be a much bigger event."
    show cyno happy glee
    C "Like the big bang part two?"
    show naoto neutral
    show lyney neutral
    show cyno -glee
    N "I've heard we're not meant to mention the 'big bang' around some teachers."
    show naoto fear
    N "apparently it brings back memories.."
    show scara neutral question
    S "Wouldn't you know about that, miku?"
    show scara -question
    show miku neutral
    M "Well it depends on how you model the universe."
    show miku neutral
    M "Hypothetically if we combined two branes, it could ignite a spark of energy which would cause something similar to the big bang."
    show miku serious
    M "They could also possibly collapse in on each other."
    show miku serious sigh
    M "Its honestly hard to theorise let alone model and prove it."
    show scara angry
    S "Uh, we are here to figure this out not study quantum mechanics-"
    show miku serious none
    M "When you start to suggest the universe, altering possibilities it's hard not to discuss that."
    show naoto neutral
    N "We would at least be able to see things in our observable universe that suggest that."
    show cyno neutral
    C "Has there been anything notable in the universe then?"
    show miku serious
    M "Well we can see right now.."
    show miku neutral exclamation
    M "Hey you, pull out your phone and check for us!"

    Y "Lets see…"

    show miku -exclamation

    default universe_chosen = set()

    menu .universe_choose:
        set universe_chosen

        "There has been an increasing number of anisotropies in the cosmic microwave background.":
            show miku neutral
            M "Well that proves something!"
            show scara neutral question
            S "Is it enough proof?"

            jump .universe_choose
    
        "There have been recently discovered areas that defy conservation laws as energy is sporadically being created and destroyed.":
            show miku neutral
            M "Well that proves something!"
            show scara neutral question
            S "Is it enough proof?"

            jump .universe_choose


    show scara -question    
    show cyno neutral question
    C "Well these events are abnormal enough to help prove something at least right?"
    show naoto disgust
    N "I'm also unsure if this is enough evidence.."
    show cyno -question
    show lyney neutral
    L "Compared with everything we have established before it should be, right?"
    show naoto neutral
    N "But this is in reference to the entire universe, shouldn't there be more that occurs in the universe?"
    show cyno neutral
    C "Well all of these articles are fairly new, meaning more is probably going to be discovered..."
    show scara angry
    S "But we don't have time to wait for that new stuff to come out."
    show miku neutral question
    M "So why don't we go look at that ourselves?"
    show scara disgust
    S "More research?"

    show miku neutral glee
    M "Whenever the sky is clear next, we can go out in the evening and try to observe things together!"
    show naoto neutral
    N "It seems luck is on our side as well, the next clear sky is tomorrow."
    show miku -glee
    show scara neutral
    S "So we just sit and wait until then?"
    show cyno disgust
    C "Well, the condition still hasn't been addressed fully.."
    show naoto neutral
    N "if we are going through with this theory then maybe we have."
    show lyney neutral exclamation
    L "Hold on."
    show lyney neutral none
    L "In my research yesterday I was reading about possession."
    show lyney neutral
    L "And what I found out was accounts of people 'fighting' the demonic spirit possessing them for control of the consciousness. These documents seemed to be almost identical to cyno's condition."
    show scara neutral
    S "What are you saying?"
    show lyney fear exclamation
    L "I'm saying, maybe in this case, cyno isn't fighting a spirit for consciousness, but himself."
    show lyney neutral none
    L "The one from the other universe! Maybe they are combining together."
    show cyno fear question
    C "So I'm fighting myself to control myself?"
    show scara neutral
    S "Unfortunately it does explain the blacking out and witnessing memories."
    show cyno -question
    show scara disgust
    S "maybe its only time until we all become like that.."
    show lyney fear
    L "Scary!"

    show miku serious
    M "If that's the case it serves as more evidence and only makes our theory stronger."
    show scara neutral
    S "So that's it, you guys solved everything now?"
    show cyno disgust
    C "You helped, you know!"
    show miku serious
    M "Well, we haven't cracked this entirely."
    show miku neutral
    M "But it seems everything is falling into place!"
    show miku neutral glee
    M "and tomorrow, if we are correct it should only build a stronger case for us!"

    show naoto happy
    N "It feels almost surreal that everything's coming together now."
    show scara neutral
    S "I can't believe you might actually make that absurd deadline possible!"
    show lyney happy
    L "Well it's good for us at least!"
    show miku neutral
    M "But seriously guys-"
    show cyno disgust sigh
    C "Corny speech incoming..."
    show miku angry vein
    M "Shut up cyno."
    show cyno -sigh

    show miku serious -vein
    M "Anyways, I'm just glad we somehow all came together for this."
    show miku neutral
    M "It's almost a miracle really!"
    show miku neutral
    M "Cyno, Naoto, Lyney, Scara and you.."
    show miku happy glee
    M "Makes a good team ya think?"
    show miku neutral none
    M "Maybe we were one in that alternative universe!"
    show scara disgust
    S "Yea I'm going."
    show miku neutral heart
    M "Aw come on, I know you like being here!"
    show cyno neutral
    C "I'm sure he does, but I think it's time to wrap things up for today."
    show lyney happy
    L "Scara must be so happy for his freedom."
    show scara angry vein
    S "Shut up."
    show naoto neutral
    N "I guess we will call it there then."
    show miku happy glee
    M "I'll be seeing you all tomorrow at lunch!"
    
    Y "{i}We end this session with high hopes for tomorrow.{/i}"


label day4afternoon:
    scene entrance evening
    show screen top_right_ui(4, "After School")
    with fade

    call hangout from _call_hangout_2

    call dayend from _call_dayend_3

# cyno scara miku lyney naoto sparrow