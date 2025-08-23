default naoto.points = 0
default naoto.level = 1

label hangoutnaoto:
    call expression "hangoutnaoto" + str(naoto.level) from _call_expression_5
    $ naoto.level += 1
    return

label day1hangoutnaoto:
    stop music fadeout 1.0
    queue music hangout
    
    scene street evening
    show naoto neutral
    with fade
    
    N "honestly, you didn't need to accompany me, though I can make an exception if its you, after all, you're just a transfer student who doesn't know any better."
    show naoto happy
    N "but… I suppose your presence is quite grounding, to say the least."
    
    menu:
        "I'm happy I can provide some kind of support.":

            show naoto embarrassed
            N "that's not what I meant…!"

            show naoto neutral
            $ naoto.points += 1
            play sound point
            N "but, you're unusually self aware, which is refreshing."
        
        "is this getting too awkward for you?":
            show naoto neutral
            N "not really, should I be concerned?"
            N "what I meant to say was, I'm usually quite fond of being in my own company."

    show naoto neutral
    N "sorry, its just… I've always preferred conversations that say something that actually has value and meaning."

    show naoto sad
    N "for that reason, I don't enjoy idle chatter."
    
    menu:
        "trust me, I won't waste your time.":
            show naoto happy
            $ naoto.points += 1
            play sound point
            N "I appreciate your consideration."
        
        "relax, this is just a dorm walk.":
            show naoto neutral
            N "relax? I believe I'm quite calm. I worry for your future lectures if that's your way of interpreting things."

    show naoto happy
    N "well, despite my better judgement, that wasn't a bad use of my time."
    show naoto happy
    N "thank you for walking with me."

    return

label hangoutnaoto1:
    Y "{i}if I recall correctly, naoto's a student council member. Let me check their office to see if I can find her.{/i}"

    scene office day
    show naoto happy
    with fade

    N "ah, welcome!"
    show naoto neutral
    N "good timing actually, I wanted to talk to someone else about this and your opinion will do just fine."

    menu:
        "did something bad happen?":
            N "that depends on how you define 'bad'"
        "actually I'm pretty bad at making judgements.":
            N "its alright, its not like the universe is at the brink of collapse or anything like that…"

    N "recently, a rumour has been circulating about a building, coined by the other students as an 'insane asylum' not too far away from campus."
    N "it started with an online article written by shareholders of the university, and seems to have just blown up from there."
    
    Y "hold on, its an asylum now?"
    
    N "yes, or at least that's the claim. Students are bombarding the council with concerns about their safety, and even the general public are starting to avoid going anywhere near."

    show naoto angry
    N "as you can imagine, it's quite troublesome."

    show naoto neutral
    N "so earlier today, I went to the school's archive and found reports of missing faculty records, all pointing to the same “offsite building”"
    N "I've deemed this situation to be quite serious, so I intend to investigate myself."
    
    menu:
        "how about I come with you?":
            show naoto happy
            $ naoto.points += 1
            play sound point
            N "hm. I appreciate your initiative in this matter. You may prove useful to the investigation as well."

        "that sounds dangerous though, I could go instead-":
            show naoto neutral
            N "maybe so, but it's the student council's responsibility to attend to such matters promptly. you're welcome to come with me though."
    
    stop music fadeout 1.0

    scene forest day
    show naoto neutral
    with fade
    
    Y "{i}Naoto and I decide to head off to the 'insane asylum'{/i}"

    N "we're close, I can tell. this path is what the students have been talking about in relation to this facility."
   
    show naoto angry
    N "if it does exist, and was apart of the university for that matter, there should be evidence. Enough to bring debunk this rumour for good."
    
    menu:
        "but what if there's nothing there?":
            show naoto neutral
            N "then sooner or later the rumour will die and we won't have to deal with it any longer, but I'd be surprised considering."

        "you sound like you've already made up your mind.":
            show naoto neutral
            $ naoto.points += 1
            play sound point
            N "of course I have. The truth isn't something I treat lightly. Its a rather methodical approach."
            show naoto happy
            N "some people think my way of thinking is quite stubborn and fixed, but time and time again its always yielded results."

    show naoto neutral
    N "so, for that reason, it's imperative that we solve this, the student council's reputation is on the line after all."
    
    menu:
        "no pressure right? hehe… ":
            pass
        "I'd prefer if you didn't shoulder all the responsibility on me if we do fail.":
            pass
    
    show naoto fear exclamation
    N "…wait. There it is!"

    queue music tense

    scene asylum
    show naoto fear exclamation
    with fade

    Y "{i}upon hearing naoto's reaction, I turn to see a large building standing over me. the walls look cracked, the entrance is sealed shut and the windows are covered by boards.{/i}"

    show naoto neutral -exclamation
    N "at first glance, it does appear to be abandoned, but…"
    N "hmph, lets get a closer look."
    
    Y "{i}I decide to peer through one of the window boards{/i}"
    Y "{i}…{/i}"
    Y "{i}I can make out the outline of a shadow, and the smell of something burning{/i}"

    menu:
        "I think there's something going on in there.":
            N "indeed."
        "okay now I'm scared-":
            N "try to stay calm, we haven't been spotted yet."

    show naoto neutral
    N "someone is using this place, that's for certain."
    show naoto angry
    N "but this scent of smoke, who knows what they're doing…"
    
    menu:
        "should we sneak in now?":
            show naoto neutral
            N "no, given the situation we now find ourselves in, I'd say we're unprepared. Besides, I want the full truth, I'm not going to rush this."

        "lets come back at night":
            show naoto happy
            $ naoto.points += 1
            play sound point
            N "yes. The night will give us some decent cover. Since we'd have to rely on defending ourselves, I'll make sure to bring proper gear, and I won't leave until I know what this place really is."
    
    stop music fadeout 1.0
    queue music hangout

    show naoto neutral
    N "now that I think about it, the uncertainty surrounding this case is a strangely familiar feeling,, huh…"
    N "nevertheless, whatever is hidden here, I will unearth it, and make sure of it."
    N "when you're ready, meet me at my office just after sunset, then we'll carry out our plan of action."
    
    menu:
        "sounds good.":
            show naoto happy
            N "hm."
        "understood ma'am.":
            show naoto embarrassed
            N "I-... why so formal all of a sudden?"
        "is it possible to back out?":
            show naoto angry
            N "huh, I thought we struck some kind of deal. I'd be very disappointed if you didn't come."

    show naoto neutral
    N "just remember to bring some gloves and an object that can hit hard."

    return

label hangoutnaoto2:
    Y "{i}as we had agreed, I wait until evening before meeting naoto in the student council office{/i}"
    
    scene office evening
    show naoto happy
    with fade

    N "as expected, youre on time."

    menu:
        "this case is just as important to you as it is to me":
            $ naoto.points += 1
            play sound point
            N "your commitment is quite admirable, indeed, I couldn't have picked a better accomplice to help me solve this case"

        "once this is done can you put in a good word about me to the student council-":
            N "haha,, if you're seriously asking to join, then unfortunately I cannot guarantee a place. You'll find its more trouble than its worth anyways."

    show naoto neutral
    N "now, we haven't got a moment to lose, lets get going."

    scene forest night
    show naoto neutral
    with fade
    
    N "I found a side passage we could enter through, better to head in there than barge into the main entrance."
    N "from this point, we need to proceed quietly and with caution to avoid being seen."
    N "ready?"

    Y "time to reach out for the truth!"

    show naoto happy
    N "exactly."
    
    scene asylum hallway
    show naoto neutral
    with fade

    Y "{i}Naoto and I head into the building and find ourselves in a large hallway.{/i}"
    
    stop music fadeout 1.0
    queue music tense

    default searched = set()
    menu .search:
        set searched
        "where should I search?"

        "the storage room":
            scene storage with fade

            "{i}its quite a dusty room, but appears to have several boxes filled with food and materials labelled by the campus.{/i}"
            "{i}there are also some student council posters beneath them. With this evidence, its safe to conclude these goods likely belong to the university.{/i}"
            Y "{i}theres no point searching through the boxes any further, I should leave.{/i}"
        
        "the living quarters":
            scene empty room with fade

            "{i}just an empty room, but there are several sleeping bags on the floor.{/i}"
            "{i}there are also sketches and drawings across the walls, they look like they were drawn by children{/i}"
            Y "{i}there is nothing else of importance here, I should leave.{/i}"
       
        "the utility room":
            scene asylum hallway with fade

            Y "{i}looking through the cracked door, I can hear shuffling. Someone appears to be inside, could it be the same person from before?{/i}"
            Y "{i}I can't make it out clearly, but the person appears to be sitting beside the fireplace, layering cardboard or the likes of it.{/i}"
            Y "{i}they don't seem to notice me, but I can't tell if they are dangerous or not{/i}"
            
            menu:
                "what should I do?"
                
                "leave quietly":
                    pass
                "knock":
                    Q "who's there?!"
                    Q "huh… you're just a student."
                    Q "then go, before anyone else finds you here."
                    
                    Y "{i}I should do as the person says.{/i}"

    stop music fadeout 1.0

    scene asylum hallway
    show naoto neutral
    with fade

    N "tell me. What did you find?"

    show naoto angry
    N "…"
    N "I see, its just as I suspected myself."

    queue music sentimental

    show naoto neutral
    N "this isn't an asylum at all. In fact, its merely a shelter for the poor. What's worse is that the school article which started this rumour was likely to have been fabricated."
    N "indeed, what you found aligns with the theft reports on campus recently."

    show naoto angry
    N "but how could it be? The only possible explanation is that the higher ups of the university tried to cover all of this up with the rumour about the insane asylum. …why would they do such a thing?"
    
    menu:  
        "they redirected everyone's attention to protect their image.":
            show naoto happy
            $ naoto.points += 1
            play sound point
            N "that makes the most sense, and we have the evidence to back up that conclusion. Good insight."

        "are you sure that's the full story?":
            show naoto neutral
            N "I'm not trying to jump to conclusions here. My interpretation of events are certain."

    show naoto angry
    N "…how despicable of them. I should report this immediately."
    show naoto neutral
    N "but this is the administration were talking about. If I do go ahead with this, the student council will be implicated in the cover up."
    
    show naoto fear
    N "they probably undermined the competency of the student council to investigate this, so they would likely interrogate me,, and you. And we'd end up jeopardising our place in the university."
    N "my sincerest apologies, I should not have involved you in this."
    
    Y "{i}I can sense Naoto's apprehension{/i}"

    show naoto fear
    N "what's worse still is the fact that, if I don't report this, that doesn't make me any better than the ones who let this happen."
    show naoto angry
    N "shit… there really is no answer that works here."
    
    menu:
        "its not about the answer.":
            show naoto sad
            N "but I've never not had an answer."
            N "a morally ambiguous conclusion will be the end of me."
        "you're scared, and that just shows how much you care.":
            show naoto angry
            N "!!... I am NOT-"
            show naoto neutral
            N "…"

    show naoto angry
    N "tch, now I'm letting my emotions overcome my rationality."
    show naoto neutral
    N "its just, I have built my resolve up to be unshakable, and that if I didn't, no one would able to trust or rely on me."
    show naoto fear
    N "but I fear the outcome, no matter what kind of 'truth' I fit into my report."
    
    menu:
        "these feelings don't make you any weaker. It actually makes me trust you more.":
            show naoto fear exclamation
            $ naoto.points += 1
            play sound point
            N "!!..."
            show naoto happy -exclamation
            N "I can tell your words come from a place of certainty. You have my gratitude."
            
        "you shouldn't be this perfect person trying to do the right thing all the time.":
            show naoto neutral
            N "then what was the point of all my hard work and preparation?"

    show naoto neutral
    N "hm. I think I now know what I must do."
    N "it will have to involve me creating my own truth, so as to protect our positions and the safety of the shelter."

    show naoto angry
    N "as for the higher ups, I'll find my own way to deal with them."
    show naoto happy
    N "your help was invaluable, please get some well deserved rest."

    return

label epiloguenaoto:
    define naoto.opening = "ah, you're here, I was about to go look for you."
    
    menu:    
        "how are you doing?":
            show naoto happy
            N "I'm doing much better."
        "is this about the 'insane asylum?'":
            show naoto neutral
            N "yes, I have an update on the situation."
    
    show naoto happy
    N "I thought you would want to know that I managed to take care of the rumour that the higher ups were spreading."
    show naoto neutral
    N "all it took was an anonymous report with sufficient evidence. Don't worry, I didn't mention our names nor the investigation we conducted."
    show naoto happy
    N "I've got to tell you, the administration are on their knees now that someone knows about their heinous acts, so that will keep them busy for a while."
    show naoto neutral
    N "its not the justice that I wanted, but its something I can live with."

    menu:
        "you did the right thing.":
            show naoto sad
            N "maybe so, but what is 'right' feels a lot more complicated now."
        "you sound disappointed.":
            show naoto angry
            N "hm… the truth isn't clean and wasn't as I had hoped for."

    show naoto neutral
    N "I once believed that if I did everything perfectly and acted rationally, then I'd have it easy going. I thought that I would be safe and respected."
    show naoto sad
    N "and when that mindset that I had built fell apart, I wasn't even sure who I was."
    show naoto neutral
    N "but what gave me confidence in that moment was you being there, still by my side."

    show naoto happy
    N "you gave me a reason by staying with me."
    N "so… thank you."
    
    Y "{i}I should choose my words carefully.{/i}"
    
    menu .reconsider:
        "I didn't stay for an answer. I stayed for you.":
            show naoto fear exclamation
            N "for me…?"
            show naoto neutral -exclamation
            N "perhaps the answer that I needed to discover was really your spoken words."

            show naoto happy
            N "now I believe I have more than enough closure."
            N "and to be honest, I never expected you to say such words, but I think I like that…"
            
            Y "{color=#EC80EC}{i}I am now in a relationship with Naoto{/i}{/color}"
            
            show naoto fear exclamation
            N "…this rush of emotions I'm experiencing."
            
            N "are these my true feelings?"
            N "its… um,, err…"
            N "G-Goodbye!"

            hide naoto with dissolve

        "you don't need to be perfect to feel like you're worth something.":
            Y "{i}…{/i}"
            Y "{i}I suddenly get the feeling that friendzoning isn't the right option.{/i}"
            Y "{i}perhaps I should reconsider.{/i}"