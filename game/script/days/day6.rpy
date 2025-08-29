label day6:
    call screen calendar(6) with fade

label day6morning:
    play music heartwarming

    show screen top_right_ui(6, "Morning")
    scene entrance day
    with fade

    call epilogue from _call_epilogue

label day6afternoon:
    stop music fadeout 1.0
    queue music main

    scene classroom day
    show screen top_right_ui(6, "Afternoon")
    show miku at r51
    show lyney at r52
    show cyno at r53
    show naoto at r54
    show scara at r55
    with fade

    show miku happy glee
    M "Final push before we present!!"
    show miku neutral -glee
    M "But no time to be sappy or anything we need to PLAN!"
    show scara angry
    S "Geez slow down.."
    show lyney neutral
    L "What, did you just wake up?"
    show scara disgust sigh
    S "No, just the energy is a bit much."
    show miku happy glee
    M "C'mon scara!! Just this then you're free!"
    show scara -sigh
    show miku -glee
    show naoto neutral
    N "We still have to run this club for it to count."
    show cyno neutral question
    C "what do we even have left to do, are you gonna make us practice with you or something?"
    show miku serious
    M "No but I mean do you even know what to say?"
    show cyno -question
    show naoto neutral
    N "I think we should start by highlighting the order that we speak of things."
    
    menu:
        "Give evidence in the order in which we found them.":
            pass
        "Give the largest discoveries last for impact.":
            pass
    
    show naoto neutral
    N "So that means we would start with the condition then the stuff in terms of records and locations then lead it up to the memories and probably the universe anomalies."
    show scara neutral
    S "then what, we decide on an order to speak?"
    show cyno happy
    C "Brings me back to primary school."
    show naoto neutral
    N "I thought you couldn't-"
    show cyno neutral
    C "Yea I was joking."
    show cyno sad sigh
    C "Unfortunately..."
    show cyno -sigh
    show miku neutral
    M "Orders and stuff just feel like they would come naturally."
    show scara angry
    S "You're saying that to a ton of people who don't understand social cues."
    show miku neutral
    M "Cyno, you're basically a walking piece of evidence, do you wanna speak up about your condition?"
    show cyno disgust
    C "Bit dehumanising much-"
    show cyno neutral sigh
    C "Also, it's awkward, I don't wanna basically vent to teachers bro-"
    show lyney neutral
    L "Do you even know if you're up to presenting?"
    show cyno disgust -sigh
    C "I'm not totally incapable of things you know."
    show naoto neutral
    N "I mean, he's been fine doing everything else, if anything occurs I'm sure we know to step aside and help."
    show scara neutral
    S "I don't know if I'm up to presenting.."
    show miku neutral
    M "C'mon scara!"
    show scara disgust
    S "I'm somewhat serious."
    show miku fear
    M "Huh?"
    show scara neutral
    S "Like, I don't mind going along with it as a club."
    show scara neutral
    S "But now we are making this a real thing that could possible be put out there in the world I'm just having my doubts."
    show naoto neutral
    N "Well, once you put an idea out there you kind of loose control of it."
    show naoto happy
    N "But that's just how ideas are built upon and improved upon even."
    show lyney happy glee
    L "Yea! Its a good thing really."
    show scara sad
    show lyney -glee
    S "I mean more so, I don't know how much I would truly believe it and if I don't have total faith in it I don't know if I feel good putting that idea in peoples heads."
    show naoto neutral
    N "The same statement still is true."
    show naoto neutral
    N "Maybe if this idea spread to the right people who actually expand upon it and make it into something more believable-"
    show cyno neutral
    C "We will never know unless we give that belief a chance, now's no time to shut it down."
    show scara neutral
    S "..."
    show scara neutral
    S "I guess."
    show miku happy exclamation
    M "Hey guys!! Lets not procrastinate more, the clock is ticking."
    show naoto neutral question
    N "What more do we have to do?"
    show miku embarrassed -exclamation
    M "Uhm well, is anyone unsure of anything?"
    show naoto -question
    show cyno neutral
    C "Yea can you run me through the entire thing real quick?"
    show miku disgust
    M "Cyno.."
    show cyno embarrassed
    C "My bad I just genuinely don't know what else is there to do."
    show lyney neutral
    L "Maybe you're just nervous and are trying to prepare yourself more even though there's nothing left to prepare really."
    show naoto disgust
    N "I mean, you did message us all constantly to remind us of everything so we were prepared."
    show miku embarrassed
    M "Yea, that's probably the case, I'm sorry guys."
    show scara happy
    S "Really, don't be, you have actual passion here. Nothing to be ashamed of."
    show miku neutral glee
    M "Hehe, yea."
    show naoto neutral
    show miku -glee
    N "If we don't have anything to wait for, why don't we go over and wait for the current group to finish?"
    show lyney neutral
    L "You'd never guess who's presenting right now."
    show cyno fear question
    C "G-G-Genshin society?!"
    show lyney disgust
    L "No, not even. Honkai star rail society. Apparently they are pitching that one of the story updates could be true and that we are living in a time loop."
    show cyno -question
    show naoto angry exclamation
    N "Seriously, you can't use video games as evidence for these things!"

    hide miku
    hide cyno
    hide lyney
    hide scara
    hide naoto
    with dissolve

    Y "{i}We all head over to where the pitch will occur.{/i}"


    Y "{i}Before we go in, [properCase(chosen.name)] pulls me aside.{/i}"

    if chosen.name == "miku":
        show miku with dissolve

        show miku embarrassed exclamation
        M "I'm so nervous!"
        show miku neutral -exclamation
        M "But, at the same time, I can't stop thinking about this morning."
        show miku neutral
        M "It feels like I've already experienced a massive win today."
        show miku happy
        M "I'm just going to continue riding that wave of optimism and wish for the best!"
        E "eepy (The next group may come in now.)"
        show miku neutral exclamation
        M "That's our cue."
        show miku neutral glee
        M "Thank you for always being beside me, even right now."
        show miku happy heart
        M "Good luck, honey!"

    elif chosen.name == "cyno":
        show cyno with dissolve

        show cyno happy
        C "Yo."
        show cyno neutral
        C "Now that we are about to present this, it feels like I'm getting closure to this whole 'condition' thing."
        show cyno neutral
        C "Even though it's not really over at all, this is just going to continue even after this presentation."
        show cyno happy
        C "But that fate does not even seem all that anymore."
        show cyno happy heart
        C "To know I have a partner who will support me through sickness and health is the support that can make you feel so much more grounded."
        show cyno embarrassed -heart
        C "Sounds like I'm reflecting on wedding vows huh."
        show cyno angry vein
        C "And no, before you ask you are not taking my last name."
        E "eepy (The next group may come in now.)"
        show cyno happy -vein
        C "I guess that's us, see you on the other side."

    elif chosen.name == "scara":
        show scara with dissolve

        show scara neutral
        S "Honestly, this isn't the most important thing thats happened today."
        show scara neutral
        S "Not by a long bit."
        show scara embarrassed
        S "Don't mention this to miku but instead of researching I spent most of last night thinking about you."
        show scara happy
        S "Hopefully with this out of the way we will get to spend more time together."
        E "eepy (The next group may come in now.)"
        show scara neutral sigh
        S "Boo, we gotta go do this now I guess."
        show scara neutral heart
        S "I love you, good luck."

    elif chosen.name == "lyney":
        show lyney with dissolve

        show lyney neutral
        L "I'm actually quite excited for this!"
        show lyney embarrassed
        L "Not sure if it's just the presentation or if its the thought of being up there with you."
        show lyney happy glee
        L "Either way, you being here makes this better."
        show lyney neutral -glee
        L "It reminds me of a certain feeling, one that makes me happy and reassures me."
        show lyney neutral
        L "I really do feel like myself around you."
        show lyney happy heart
        L "And it feels nice to be open about it."
        show lyney embarrassed -heart
        L "Hey you think we need to tell the others about our 'thing' or do you think they've already suspected something?"
        E "eepy (The next group may come in now.)"
        show lyney neutral exclamation
        L "Showtime for  us!"
        show lyney happy -exclamation
        L "Break a leg out there baby!"

    elif chosen.name == "naoto":
        show naoto with dissolve

        show naoto neutral
        N "Despite having to give several pitches like this, I feel unphased by this one compared to others."
        show naoto neutral
        N "Not because I don't care about it but I have people backing my ideas up."
        show naoto happy
        N "Assurance in your knowledge is all you need to be given confidence sometimes."
        show naoto happy glee
        N "Especially knowing you'll always provide me that confidence, well, that makes me feel like there's nothing to worry about at all."
        E "eepy (The next group may come in now.)"
        show naoto neutral -glee
        N "We best go in now."
        show naoto neutral
        N "I hope this goes well for us."
        show naoto embarrassed heart
        N "And in case things go bad, I love you."
        show naoto fear exclamation
        N "Wait, that makes it sound like we are about to die."
        show naoto neutral -exclamation
        N "Sorry, uhm, lets head inside."

label day6presentation:
    scene audition
    show screen top_right_ui(6, "Presentation")
    show whisper at left
    show eepy
    show sheldon at right
    with fade

    E "Eepy (Welcome 'the supernatural investigation club'...?)"
    E "Eepy (Are you in the right place, this is for academic research after all)"
    N "I can assure you that all of our research is scholastic and rooted in academic fields."
    E "Eepy (I trust your word, naoto)"
    E "Eepy ( I shall introduce you to the panel here with me today and myself seeing as you have one of our exchange students in your group.)"
    
    menu:
        "You are my idol!":
            E "Eepy (I'm Honoured)"
            E "Eepy (but also confused considering I am not the current standing president of this school and we have spoken only once before)"
        "Pleased to spend my last full day here presenting to you.":
            E "Eepy (I am pleased to see you've enveloped yourself in our university completely)"
    
    E "Eepy (which leads me to introduce myself formally)"
    E "Eepy (As you know, I am Eepy. I am the founder and former president of this school. Currently, I am retired however as an investor in this school I am still eagerly involved in the schools activities)"
    E "Eepy (with my connections, I was the one who pitched this programme to the university and I will be taking the lead on co-ordination and connecting students to people in their respective academic fields)"
    E "Eepy (With us is the current standing president of the school, Mr Sheldon Lee Cooper)"
    SLC "Barzingar!"
    E "Eepy (And this is whisper)"
    W "…"
    E "Eepy (thank you for being one of the groups to come on the first audition day, your dedication is noted)"
    E "Eepy (Whenever you are ready you may commence)"
    
    menu:
        ">> would you like to skip the presentation?"

        "Yes":
            jump .afterpresentation
        "No":
            pass

    hide eepy
    hide sheldon
    hide whisper
    with dissolve

    show miku at r51
    show lyney at r52
    show cyno at r53
    show naoto at r54
    show scara at r55
    with dissolve
    
    show miku neutral glee
    M "Thank you for this opportunity."
    show miku neutral -glee
    M "I'd like to first remark that this club was founded on the basis of solving a more personal issue."
    show miku serious
    M "One that's been experienced by more people daily, making its way into the lives of people, even within our school community."
    show miku serious
    M "Symptoms exerted by this condition are categorised by unusual behaviour, fainting, paralysis and most notably the occurrence of new memories."
    show lyney neutral
    L "This condition isn't just infecting the population, it's infecting our society causing misreported medical documentations, incorrect data, detailed accounts of events that had never occurred many more."
    L "Our world itself has been shaken by this, the memories of the earth physically are becoming mixed with inaccurate GPS and the slow emergence of places that never existed before."
    show naoto neutral
    N "All of these cases are examples of anomalies in our world, inconsistencies that are too strange to be explained with our current understanding of reason and rationale yet also too prominent to be discarded as just oddities."
    show scara neutral
    S "The answer we found may have been what started this journey of ours."
    show miku serious
    M "Seen within these 'memories' are visions of an alternative universe. One probably parallel to our own and many people documenting seeing these."
    M "From what we gathered, we were able to piece together these memories to build the larger picture of this universe."
    show scara neutral
    S "These visions appearing here seemed strange,at least to me, but we questioned if there was more behind it."
    show lyney disgust
    L "Why were these appearing to so many people? And so vividly, it was almost as if they were transferred here directly."
    show cyno neutral
    C "This 'possibility' leads us down to more research. From what it seemed, there was a possibility that the rising consciousness of this universe was appearing to be a sign of the events occurring on a larger scale."
    show scara fear
    S "On a MUCH larger scale."

    menu:
        "The memories were being integrated into people as the universe was being merged and so was people's consciousness.":
            pass
        "When considered on a wider level, what was seemingly proved was that universes were merging, resulting in people's consciousness' with an alternative version of themself merging ":
            pass

    show cyno neutral
    C "See, with all of these anomalies, they also appear to occur in the universe itself. Directly analysing the universe is not possible but the evidence we have gathered connects to a feasible reality."
    show miku neutral
    M "Lately studies have disproven well established laws of physics, such as in the national astronomy facility it was found that there are areas within this universe that sporadically spawn and destroy high levels of energy, as its substance was being moved between places."
    show naoto neutral
    N "As well as a sudden increase in the number of anisotropies in cosmic microwave background radiation. This sudden change in the observable universe indicates that something has changed, which has resulted in these anomalies which causes fluctuations in energy levels likely due to matter combining and others being lost."
    show lyney neutral
    L "Other astrological oddities are seen by the accelerated emergence and death of stars and interstellar objects passing through our solar system at an increased rate"
    show scara neutral
    S "The suspected reasoning behind this is that because it is an alternative universe that is combining with our own, there are likely cosmic differences in these cycles between universes that are now resulting in confusing rates that are different from our own."
    show cyno neutral
    C "Seeing the entire universe slowly deviate from what we considered ordinary does not occur in such a short time frame without reason."
    show naoto neutral
    N "Combined with the psychological impact, the links between the merging worlds and merging selves seems to be due to the fact that they stem from the same issue."
    show miku serious
    M "This, however, is only the start of our research into this endeavor. In our club we aim to fully uncover the mysteries of this case and other strange cases like this."
    M "By combining the realms of the supernatural and scientific, we can better understand the events that will occur and impact us on a personal and universal level."
    
    menu:
        "So yea that's lowkey it let me know your thoughts.":
            E "Eepy (Thank you.)"
            E "eepy (I would have appreciated a more formal ending however.)"
        "Thanks, and remember we are all in this together.":
            E "Eepy (Thank you.)"
            E "eepy (The ending seemed slightly irrelevant to the main message, but was nice)"
        "Thanks for listening.":
            E "Eepy (Thank you.)"
            E "eepy (A short and sweet ending is always nice)"
        "thank you ever so much for taking the time out of our day to listen to us please consider this thoroughly.":
            E "Eepy (Thank you.)"
            E "eepy (I appreciate the solid conclusion)"
        "{i}stand there in silence{/i}":
            E "Eepy (Thank you.)"
            E "eepy (I am assuming that was it, the end was a bit awkward)"
        "cough one singular time.":
            E "Eepy (Thank you.)"
            SLC "GET UR FILTHY GERMS AWAY FROM ME!"

label .afterpresentation:
    stop music fadeout 1.0

    hide miku
    hide lyney
    hide cyno
    hide naoto
    hide scara
    with dissolve

    show whisper at left
    show eepy
    show sheldon at right
    with dissolve

    E "eepy (I will now open up the panel to provide feedback."
    SLC "Yes thank you."
    SLC "To start strong, you all probably have worked the hardest on this project more than any club I've seen so far."
    SLC "The research you have done is extensive and is provided by many sources."
    SLC "I can understand why you'd think that would help your conclusion to be more realistic."
    SLC "But, how should I, put this."
    SLC "It has many flaws."

    queue music tense

    hide eepy
    hide sheldon
    hide whisper
    with dissolve

    show miku serious at r51
    show lyney sad at r52
    show cyno neutral at r53
    show naoto neutral at r54
    show scara neutral at r55
    with dissolve

    "All" "!"

    hide miku
    hide lyney
    hide cyno
    hide naoto
    hide scara
    with dissolve

    show whisper at left
    show eepy
    show sheldon at right
    with dissolve
    
    SLC "As it seems even with your evidence you are only in a 'theory' stage therefore I cannot fully confirm nor deny it."
    SLC "yet my own scientific endeavors make me doubt that you see the full picture."
    SLC "it reads more as a conspiracy poorly put together with evidence you yourself don't fully understand."
    E "eepy (I would have to agree)"
    E "eepy (It sometimes felt like the points were slightly hard to follow)"
    E "eepy (The whole concept feels too extreme from our current knowledge to even begin to be palatable)"
    SLC "Nothing has yet suggested this, really."
    W "I would argue that you're just wrong."
    W "You link some astronomy stuff to alternate universes because of why exactly? Are some of your friends hallucinogenic?"
    W "You college kids should lay off the DMT, would be beneficial to your studies and yourself."
    M "So the issue is just, our idea overall?"
    N "What part specifically did not make sense?"
    W "Generally just the whole thing-"
    W "I think you're just too far up your own asses."
    S "Yikes, surely that's no way to talk!"
    W "Apologies, well thank you for coming."
    E "eepy (I suppose we will wrap up there)"
    S "No hey wait, they weren't done yet!!"
    E "eepy (sorry, we will get back to you.)"

    stop music fadeout 1.0
    queue music sentimental
    
    show screen top_right_ui(6, "Evening")
    scene classroom evening
    show miku at r51
    show lyney at r52
    show cyno at r53
    show naoto at r54
    show scara at r55
    with fade

    show lyney fear exclamation
    L "That was it? It felt like they didn't consider us at all!"
    show naoto angry
    N "Not even allowing us to elaborate."
    show cyno disgust
    show lyney -exclamation
    C "Hm."
    show naoto neutral
    N "What is it?"
    show cyno neutral
    C "Nothing, just a lot to take in."
    show cyno sad
    C "The reaction was kind of hard to comprehend."
    show scara neutral
    S "You okay, Miku?"
    show miku serious sigh
    M "Yea, just tired and trying to understand how that went and all."
    show miku -sigh
    show lyney fear
    L "Is that really just it?"
    show cyno neutral
    C "It seems like it, well what else is there."
    show naoto neutral
    N "I hate to admit so as well but I guess that's just it."
    show lyney sad
    L "Just like that?"
    show cyno neutral
    C "Yea."
    show scara neutral
    S "Hey come on now, it just means we can move onto other things."
    show cyno angry vein
    C "Scara you don't need to hide it, I know this doesn't mean a lot to you."
    show scara disgust
    S "Well yea, but I'm not going to just leave you like this. I'm not that much of an asshole."
    show cyno -vein
    show scara angry
    S "But this isn't something we need to grieve."
    show naoto disgust
    N "I don't know. It feels like such an incomplete note to leave this on."
    show lyney sad
    L "I mean, its not fully shaken my belief."
    show cyno disgust
    C "Maybe not for you but that probably just means I'm back to where I began with this."
    show miku sad sigh
    M "We really did just loose something."
    show miku serious -sigh
    M "Even if you think it's stupid scara, its something we worked towards, something that brought us together."
    show miku sad
    M "The response given was so.. Shallow and short."
    show naoto neutral
    N "I'd would  have at least like more critiques rather than dismiss."
    show lyney fear question
    L "But then what, do we just leave it like that?"
    show miku serious
    show lyney -question
    M "I mean, probably."
    show miku serious
    M "Sorry, I can't give any action for this club at the moment."
    show miku sad
    M "I need to get to preparing some stuff for the student council."
    
    hide miku with dissolve
    
    show scara neutral
    S "…"
    show lyney neutral
    L "it's not really your fault scara."
    show naoto neutral
    N "This is really a hard thing to move past."
    show scara neutral
    S "Yea, I understand that much."
    show scara sad
    S "But you know, I don't think it should let it fracture you guys."
    show lyney neutral
    L "I can't be the only one who just, still believes it."
    show lyney neutral
    L "The memories, the universe stuff, it made sense to me."
    show lyney neutral
    L "it made me make more sense of other things."
    show lyney sad question
    L "You guys aren't just going to ignore that now, are you?"
    show cyno disgust
    show lyney -question
    C "I'm sorry, lyney I just can't really see that right now."
    show cyno neutral
    C "I will head out too."
    
    hide cyno with dissolve
    
    show lyney sad
    L "I'll go talk to him-"
    show naoto neutral
    N "No, leave him. He's probably got the most valid reason to be upset right now."
    show naoto neutral
    N "Because even if this was something that helped us as a group, that's a part of him that he has to live with."
    show lyney sad
    L "Hmph I get that I just-"
    show lyney disgust
    L "I don't know."
    show lyney sad sigh
    L "I'll probably go as well."
    show lyney sad
    L "I'll see you guys."

    hide lyney with dissolve

    show scara angry
    S "So, you're just going to let this group fall apart."
    show naoto disgust
    N "It's not what I want but how else are we meant to deal with this?"
    show naoto angry
    N "It seemed like you were never on board to begin with."
    show scara neutral
    S "I still showed up."
    show naoto angry
    N "But thats not-"
    show naoto angry
    N "Augh."
    show naoto neutral
    N "I'll never get why you or them will deny this."
    show naoto disgust
    N "I don't know what truth we could be missing."
    show scara neutral
    S "I don't think overthinking this now is a good idea."
    show scara neutral
    S "For your own sake, I will head out."
    
    hide scara with dissolve

    show naoto sad
    N "…"
    show naoto sad
    N "I don't know what to say anymore."
    show naoto neutral
    N "I don't want this to be the last experience you have in this school."
    show naoto neutral sigh
    N "I'm sorry it had to be like this. I didn't expect all of us to suddenly be so divided."
    show naoto sad -sigh
    N "Not sure how tomorrow will be, considering how quickly that seemed to affect some people personally."
    show naoto embarrassed
    N "Ah, I'm not making this better."
    show naoto neutral
    N "I'll see you tomorrow. Good night."

    hide naoto with dissolve

    Y "{i}At the end of the day, all of my friends have left. Everyone seems to have their beliefs split.{/i}"
    Y "{i}I am now met at a crossroads, as my time at this school draws to an end. All I can do now is hope for the best for tomorrow.{/i}"

    call dayend from _call_dayend_5

# cyno scara miku lyney naoto sparrow
