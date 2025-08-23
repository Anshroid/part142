default cyno.points = 0
default cyno.level = 1

label hangoutcyno:
    call expression "hangoutcyno" + str(cyno.level) from _call_expression
    $ cyno.level += 1
    return

label day1hangoutcyno:
    stop music fadeout 1.0
    queue music hangout

    scene street evening
    show cyno fear exclamation
    with fade

    C "you're walking with me?"

    show cyno embarrassed -exclamation
    C "I hope you're not expecting a conversation. Small talk is not my forte…"
    show cyno happy
    C "but… I can try a joke, if that helps."

    menu:
        "give me the best you've got!":
            show cyno neutral
            $ cyno.points += 1
            play sound point
            C "alright…"
            C "actually, I don't know if you'll like it, because when I told everyone this joke in my chemistry class today…"
            C "there was no reaction."
            C "get it? No reaction. Because in chemistry you combine different elements, and they have reactions, but the joke about chemistry got no reaction."

            show cyno sad
            C "…why aren't you laughing?"

            menu:
                "LOL":
                    pass
                "shut ur fucking mouth":
                    pass

        "no, you don't have to.":
            show cyno neutral
            C "understood. Silence it is then."

    C "…"

    show cyno neutral
    C "most people see me as unapproachable because I always look kinda intense. Or boring because I don't like the things they do."

    show cyno sad
    C "they're not wrong I guess, but they don't know me fully either."

    menu:
        "there's more to you than people think, you just don't show it off.":
            show cyno happy
            $ cyno.points += 1
            play sound point
            C "hmph. Don't go thinking you've earned my trust just because of one good word."
        
        "you are approachable, but just a bit serious… and boring…":
            show cyno sad
            C "ouch."
    
    show cyno neutral
    C "I only brought that up because, despite how I appear, you still wanna talk to me."
    show cyno happy
    C "and to be honest, your company was better than expected."

    return

label hangoutcyno1:
    Y "oh wait, that reminds me, there's an evening lecture later that all students must attend… wonder what that's about."
    Y "I'll catch cyno after that I suppose…"

    scene lecture
    with fade

    Y "{i}Waiting for the lecture to start{/i}"

    show cyno neutral with dissolve
    C "{i}sits beside you{/i}"
    C "…"

    menu: 
        "aren't you gonna say hi?":
            show cyno embarrassed
            C "oh mb… AHEM…… hi."
        "why the silent treatment?":
            show cyno embarrassed
            C "I thought silence was the best 'small' talk…"

    show cyno neutral
    C "…sorry, it's just that I don't wanna be here right now."
    show cyno angry
    C "I have better use of my time than listening to him…"

    Y "who's him?"

    show cyno neutral
    C "sparrow, he's part of the alumni of this university."
    show cyno disgust
    C "unless this guy has magically changed his profession, be prepared for a boring talk on tax apprenticeships or what not."
    
    menu:
        "should we ditch the lecture before its too late?":
            show cyno neutral
            C "listen, no matter how opposed we are to them, we must always follow the rules, as these are the foundations which uphold the basic principles of justice in our school community."
            show cyno angry
            C "in other words, no."

        "well, I wanna do a career in taxes…":
            show cyno happy
            C "bro what- uhm I mean yes king!"
    
    hide cyno with dissolve
    show sparrow with dissolve
    Q "apologies for the wait, and my regards to all of you for coming to my bimonthly talk on the intricate, unsung beauties of tax."
    Q "(not like you had much of a choice anyway…)"
    
    Y "so this must be sparrow…"
    
    Sp "yes yes, I'm sure none of you need any introductions, so I believe we can start the presentation."
    Sp "most people may hear the word 'tax' and turn to the view that its just a lifeless, cold-hearted system built of paper and numbers, a financial weapon used by governments to extort our hard earned wealth."
    Sp "and to that I say…"
    Sp "you don't see it."
    Sp "at least, not the way I do, and not the way you will."
    Sp "to me, there is something deeply intimate about it… how, no matter what place you take in society, tax will find a way to intervene in your very corner, touching every person indiscriminately."
    Sp "as for me, I've given my life to this world. I surrendered everything to it, and it changed me. I have bound myself to legislation,, audits… checks….."
    Sp "not because I had to… I-... I needed to."
    Sp "there's just something so intoxicating, yet so fulfilling, about being the one who understands the order and chaos but also the one who makes it make sense,, b-because-"
    
    Y "!?"
    Y "{i}my eyes start to drift off…{/i}"

    scene black with fade
    
    Y "…"
    Q "{font=DOSIyagiBoldface.ttf}███ ████ ██ █████ █████ ██ ██████{/font}"
    Q "{font=DOSIyagiBoldface.ttf}███ ██ █████ ███ ██████ ████{/font}"
    Y "…!"

    scene lecture 
    show sparrow
    with fade

    Sp "so don't underestimate what I'm talking about, this job I mean,, because if you really think about it, its a purpose, because it will make you matter."
    Sp "and, perhaps, a career in tax wants you… sooo bad,, heh…"
    Sp "thank you for listening."

    hide sparrow with dissolve
    show cyno neutral with dissolve
    
    C "…"
    C "I see you slept through all of it too…"

    menu:
        "yeah, it was kinda boring…":
            show cyno happy
            C "hah, I don't blame you!"

        "strange, I was pretty interested…":
            show cyno fear exclamation
            C "really? I see…"
    
    show cyno neutral none
    C "well, its getting late, I'm gonna head back now."
    
    menu:
        "I'll come with you!":
            show cyno happy
            $ cyno.points += 1
            play sound point
            C "I would appreciate your company."

        "how boring.":
            show cyno sad
            C "sorry, we can do something else another time, but you're welcome to join me."
    
    C "I'll just be outside, so whenever you're ready."

    hide cyno with dissolve

    menu:
        "I should head after cyno.":
            pass
        "before I go…":
            Y "{i}…?{/i}"
            Y "{i}I'm supposed to be hanging out with cyno, what else do I need to do right now?{/i}"

            menu:
                "actually, nevermind.":
                    pass
                "start a club meeting.":
                    Y "{i}huh? Its too late to do that, and I'm not even club leader!{/i}"
                    pass
                "go back to my dorm.":
                    Y "{i}but what about cyno? I don't wanna look like a shut in!{/i}"
                "I want to speak with sparrow.":
                    show sparrow

                    Sp "{i}packing his notes away{/i}"

                    menu:
                        "excuse me…":
                            Sp "oh? I didn't expect anyone to stay behind."
                        "yo.":
                            Sp "could it be!?"
                            Sp "…ah, my apologies, I thought you were someone else."

                    menu:
                        "Actually, I should go.":
                            Sp "I see, please look forward to my next presentation."
                            pass
                        "I had a question about your talk.":
                            Sp "a question… huh,, no one has ever asked me that."
                            Sp "well? something about taxes I presume?"

                            menu:
                                "I just wanted to let you know your talk was so shit.":
                                    Sp "you think I care? piss off."
                                "what kind of experience will I gain with real world tax policy during an apprenticeship?":
                                    Sp "oh yeah uhm so yea!"
                                "actually, nevermind.":
                                    Sp "I see, please look forward to my next presentation."
                                "what was your talk really about?":
                                    stop music fadeout 1.0

                                    Sp "what do you mean?"

                                    menu:
                                        "look, I'm a professional and I can tell you know nothing about taxes.":
                                            Sp "well I finished my apprenticeship and am now working as a data analyst so it really doesn't matter what you think. Piss off."
                                        "well I slept the whole time so…":
                                            Sp "thats not my fault, is it? Maybe pay more attention next time."
                                        "actually, nevermind":
                                            Sp "I see, please look forward to my next presentation."
                                        "I don't think your talk was about taxes.":
                                            Sp "then maybe you are starting to realise."
                                            Sp "I mean, you noticed it? That moment when you drifted."
                                            
                                            menu:
                                                "I probably just imagined it.":
                                                    Sp "I see, well… please look forward to my next presentation."
                                                "I couldn't quite make it out but…":
                                                    Sp "then in reality you saw nothing."
                                                "this isn't making any sense.":
                                                    Sp "then don't pretend you know what you're talking about."
                                                "what was that?":
                                                    queue music tense

                                                    Sp "hm… it seems you didn't forget like everyone else."
                                                    Sp "you weren't supposed to notice anything, but something in you looked too closely into this matter. Because you kept listening even after that fleeting moment of emptiness."
                                                    Sp "in truth, you were not meant to hear the rest. Nevertheless, you're still here. Still asking these meaningless questions."
                                                    Sp "and so I tell you this. In this university, you may fill your life with mundane choices, but despite all your successes and friendships, you'll return to the point where everything is predetermined."
                                                    Sp "…all for nothing."

                                                    menu .another_try:
                                                        "what do you really mean?":
                                                            Sp "don't pretend to know what you're talking about."
                                                        "but this could be the start of something new…":
                                                            Sp "it feels so right for you to GO AWAY."

                                                        "I finally figured it out…":
                                                            Sp "hm? Do share."

                                                            menu:
                                                                "that all our dreams have no limitations.":
                                                                    pass
                                                                "everyone's special in their own way.":
                                                                    pass
                                                                "we're all in this together.":
                                                                    pass
                                                                "wait actually-":
                                                                    Sp "..hmm?"
                                                                    jump .another_try

                                                            Sp "…leave."

                                                        "are you saying I'm trapped?":
                                                            Sp "you always were."
                                                            Sp "but,, you were not meant to ask me this question."
                                                            Sp "so how?"
                                                            Sp "how can you understand the gravity of your situation?"
                                                            Sp "…perhaps, you know something you shouldn't, anomaly."
                                                            
                                                            menu:
                                                                "please help me-":
                                                                    Sp "…"
                                                                    
                                                                    scene black with fade

                                                                    Sp "with pleasure."
                                                                    Sp "what a shame that it had to come to this."
                                                                    Sp "my role was simply to balance the ledger of fate."
                                                                    Sp "and now, the balance is yours to keep."
                                                                    Sp "with you disposed of for good, I can finally pursue what truly matters."
                                                                    Sp "that is, my love for cyno… for evermore."

                                                                    ">> you have reached the secret ending."

                                                                    $ renpy.set_return_stack([])
                                                                    return
                                                                "actually, nevermind.":
                                                                    pass
                                                                "actually, nevermind.":
                                                                    pass
                                                                "actually, nevermind.":
                                                                    pass
                                                                
                                                            Sp "if you go now, I'll overlook this error."

    play music hangout if_changed

    scene entrance evening
    show cyno happy
    with fade

    C "ah, there you are."
    show cyno neutral
    C "I was only going to head back to my dorm. So I figured I'd ask if you wanted to join me for a game night?"

    menu:
        "games? With you? Is that all right?":
            show cyno embarrassed
            C "yes… why do you sound so bemused?"

        "you're feeling okay for that?":
            show cyno sad
            C "I wasn't planning on collapsing again while playing, if that's your concern."

    show cyno neutral
    C "its just cards, and you're new,, a transfer student i mean."
    C "and because of that, you're not going to treat me the way others do."

    show cyno embarrassed
    C "…nevermind, cmon, the walk's not long."

    scene room cyno day
    show cyno neutral
    with fade

    Y "{i}I head inside Cyno's dorm room.{/i}"
    Y "{i}…{/i}"
    Y "{i}it's remarkably tidy and well decorated too. But on one side of the room I can see a meticulously arranged shelf full of genius invocation TCG cards and sleeves.{/i}"

    menu:
        "you collect these?":
            show cyno embarrassed
            C "its just small hobby I have… nothing worth mentioning."
        "you play genius invocation?":
            show cyno embarrassed
            C "that depends. Do you mean play as in being able to memorise every gameplay mechanic and create 24 optimised decks of my very own character card? …then yes."
   
    show cyno neutral
    C "I won't bore you with the rules of this game for now, it would take too long. Instead, lets play something simpler, blackjack."
    
    menu:
        "not gonna test me with the real thing?":
            show cyno neutral
            C "don't question it. Just… consider this the tutorial."

            show cyno fear exclamation
            C "besides, whats wrong with blackjack?"

        "sounds good, lets do this.":
            show cyno happy
            $ cyno.points += 1
            play sound point
            C "hm. Lets."
            show cyno neutral
            C "I anticipate how well you will carry such resolve into your strategy."

    show cyno neutral none
    C "need me to explain the rules?"
    
    menu:
        "ya":
            show cyno neutral
            C "the goal is simple, your hand needs to be as close to 21 without going over."
            show cyno happy
            C "hit to draw, and stand to stay. The choice is yours."
        "na":
            show cyno fear exclamation
            C "oh? Maybe you're not as much of an amateur as I thought."
            show cyno happy -exclamation

    Y "{i}Cyno deals the cards himself, and the game begins.{/i}"
    Y "{i}I notice something odd about the way his hands move, its quite mechanical. his gaze keeps moving away whenever I look at him too long.{/i}"
    Y "{i}He looks… distant, even while sitting right there. maybe this is just how he always is... but it doesn't feel right.{/i}"
    Y "{i}hm. lets see… I've got a 10 and a 7. What should I do?{/i}"
    
    menu:
        "hit me":
            $ selected_card = renpy.random.randint(1, 10)

            "{i}Cyno hands me another card, I flip it to reveal a [selected_card]{/i}"

            if selected_card > 4:
                menu:
                    Y "{i}I bust, but I could try to bluff…{/i}"
                    
                    "don't bluff":
                        show cyno neutral
                        C "I'm gonna stand, if you're ready, lets reveal our hands."
                        
                        "{i}Cyno flips his cards to reveal a 6 and 8.{/i}"

                        show cyno sad
                        C "you bust, that's a shame. I don't enjoy these type of victories."
                        show cyno neutral
                        C "you were just too aggressive, but quite bold."

                    "bluff my hand":    
                        Y "{i}I've got a strong hand already, so its worth a try…{/i}"

                        Y "I pick out a card from my hand, gazing at it while it longs for mercy."
                        Y "immediately, I put the card inside my mouth…"
                        Y "and eat it."
                        play sound eating
                        Y "…"
                        Y "{i}gulps{/i}"
                        Y "…"
                        Y "{i}burps{/i}"


                        show cyno neutral
                        C "hm…"
                        C "I'm gonna stand, if you're ready, lets reveal our hands."

                        "{i}Cyno flips his cards to reveal a 6 and 8{/i}"
                        
                        show cyno happy
                        C "hah, I should've known, maybe I was thinking too hard."
                        $ cyno.points += 1
                        play sound point
                        C "well played."

            else:
                show cyno neutral
                C "I'm gonna stand, if you're ready, lets reveal our hands."
                
                "{i}Cyno flips his cards to reveal a 6 and 8.{/i}"

                show cyno happy
                C "seems like the gamble paid off, you won."
                show cyno neutral
                C "I respect your impulse, quite bold of you."

        "I'll stand":
            show cyno neutral
            C "alright, I'm gonna hit."
            
            "{i}Cyno draws one card, and quickly draws another.{/i}"

            C "if you're ready, lets reveal our hands."
            
            "{i}Cyno flips his cards to reveal a 6, 8, 2 and 5{/i}"
            
            C "you played it safe, which was a little predictable to say the least."


    Y "{i}after several more rounds, the game quickly passes by{/i}"
    Y "{i}Cyno begins collecting the cards. I notice his posture closes up and his whole presence shifts. His shoulders hunch as if he's folding back into himself.{/i}"
    Y "{i}That flat look returns to his face, looking empty. I can't tell if he's okay or not, but I don't wanna assume…{/i}"

    menu:
        "you okay? you seem different when you play.":
            show cyno fear exclamation
            C "you think?"
            
            show cyno neutral -exclamation
            C "I guess its because there are rules. And with rules, I know what people expect from me."
            show cyno disgust
            C "but I have to admit, I don't like being watched so intently."

        "you okay? don't push yourself like this for me.":
            show cyno fear exclamation
            C "huh? I wasn't pushing anything. You're not a burden."
            
            show cyno neutral -exclamation
            C "quite the opposite in fact."

    stop music fadeout 1.0
    queue music sentimental
    
    show cyno sad
    C "…seems like I'm back to this again."
    show cyno angry
    C "look, it was only meant to be just a game, but somehow it managed to turn into something else."
    
    menu:
        "I just want to make sure you're okay.":
            show cyno disgust
            C "that's what they all say."
            show cyno neutral
            C "…sorry, I know you mean that, it just looks all too similar, that's all."

        "I wasn't trying to do anything.":
            show cyno neutral
            C "sure, I believe you. intentions do matter, especially those that are good, but…"
            show cyno sad
            C "sometimes I just wish I could be in peace without someone being concerned for my health."
    
    show cyno sad
    C "I thought maybe this would be normal for a change."
    show cyno neutral
    C "but I guess its too complicated when I'm in the equation."
    
    "{i}Cyno walks to the door and opens it for me{/i}"
    
    show cyno sad
    C "thanks for the game…"
    
    Y "{i}…{/i}"
    Y "{i}what just happened? I thought I was being helpful.{/i}"
    Y "{i}…did I do something wrong?{/i}"

    return

label hangoutcyno2:
    Y "{i}cyno and I left on a bad note when we last spent time with each other, and I got the impression that I made things worse.{/i}"
    Y "{i}nevertheless, I should go check on him and see if he's okay, he might be in his dorm{/i}"

    scene park 
    show cyno neutral
    with fade
    
    Y "{i}before I head outside campus, I see cyno seated beside a fountain, quietly shuffling his deck.{/i}"
    
    C "…"
    C "hm. By that look on your face, I can tell you were coming to find me."
    
    menu:
        "are you mad at me?":
            show cyno disgust
            C "not really… moreso frustrated, or disappointed. Not with you, in fact maybe with myself."
        "I wanted to check in.":
            show cyno sad
            C "but you didn't have to…"
    
    show cyno neutral
    C "its just… I thought that this would feel different… that maybe I would feel different, because you don't know me like most people."
    show cyno disgust
    C "at least, enough to not treat me like a liability."
    show cyno sad
    C "but maybe that was unfair to place such expectations onto you."
    
    menu:
        "you thought I would see you differently.":
            show cyno neutral
            $ cyno.points += 1
            play sound point
            C "that's right."
            C "now I realise it was brash of me to do so."

        "I thought I was doing the right thing.":
            show cyno neutral
            C "I know, and you tried."
            show cyno sad
            C "still, I figured you might…"
    
    show cyno neutral
    C "you know what? lets play again, just one more time."
    show cyno happy
    C "if nothing else, I find that its easier to talk with cards at our arsenals."
    show cyno neutral
    C "like before, its another round of blackjack, but I'm changing the objective slightly."
    C "you're not playing to win… this time, you're trying to match my hand and my total."
    
    menu:
        "so is this a guessing game?":
            C "I wouldn't say that, its merely about trying to meet me where I am."

        "I'm not good at reading people…":
            C "then this will be good practice, no? As well as for me too."
    
    C "it all relies on your intuition, and also no peeking, not like you were going to anyway."
    
    "{i}Cyno deals the cards himself, and the game begins.{/i}"
    
    Y "{i}hm. Looks like I've got a 7 and a 6 this time. What should I do to match cyno?{/i}"
    
    menu:
        "hit":
            "{i}Cyno hands me another card, I flip it to reveal a 5{/i}"
            
            C "if you're ready, lets reveal our hands."
            
            "{i}Cyno flips his cards to reveal a pair of 9s{/i}"

            show cyno fear exclamation
            $ cyno.points += 1
            play sound point
            C "matched… huh."
            
            show cyno happy -exclamation
            C "I must admit, I didn't expect you to be that close."

        "hold":
            C "if you're ready, lets reveal our hands."

            "{i}Cyno flips his cards to reveal a pair of 9s{/i}"

            show cyno disgust
            C "seems like you stayed behind, and maybe too afraid to go further."
            show cyno neutral
            C "that caution speaks a lot of words to me."

        "hit twice":
            "{i}Cyno hands me two cards, I flip it to reveal a 5 and a 3.{/i}"

            C "if you're ready, lets reveal our hands."
            
            "{i}Cyno flips his cards to reveal a pair of 9s{/i}"
            
            show cyno neutral
            C "a perfect 21… but even then, in this game you overstepped your goal."
            C "though I appreciate you understand that the aim wasn't about being ahead, right?"

    stop music fadeout 1.0
    queue music sentimental

    show cyno embarrassed
    C "…"
    show cyno neutral
    C "looks like you really did try to match me."

    menu:
        "that was the point, right?":
            show cyno happy
            C "yes, it was, and for what its worth I feel like we got to understand each other through this."
        "it was purely a guess.":
            show cyno happy
            C "so long as the guess holds meaning from someone who cares."
    
    show cyno neutral
    C "maybe you've caught onto my intention behind this game."

    show cyno embarrassed
    C "because how you played is all I've ever wanted from someone."
    C "someone who just tries to sees me, for me."

    show cyno neutral
    C "outside the club, I want to be more than a thing that needs fixing."

    show cyno sad
    C "I want to just exist, feel free, even if I may not be like everyone else. And not feel like that's a burden on anyone."
    
    menu:
        "I want to try again.":
            show cyno happy
            C "as far as I see it, you already have."
            show cyno neutral
            C "just stay, like the way you did today and so will I."
    
        "I'm sorry I didn't before.":
            show cyno neutral
            C "I don't need your guilt, but I think I understand you."
            show cyno happy
            C "and it means something that you're saying this now."
    
    show cyno embarrassed
    C "maybe this is what connection is meant to be like."
    show cyno neutral
    C "even if its awkward, or quiet, there will be still be some meaning attached to it."
    
    menu:
        "I'd rather play beside you anyway.":
            show cyno happy
            $ cyno.points += 1
            play sound point
            C "I appreciate that more than I can say."
    
        "you're not broken to me.":
            show cyno happy
            C "Maybe you're not like the others then."
    
    show cyno neutral
    C "hm. perhaps I should continue to reflect on my thoughts to gain a proper answer…"
    
    scene street evening
    show cyno neutral
    with fade

    "{i}Cyno and I walk outside campus{/i}"
    
    C "lets part ways here. Don't worry, I can head back to my dorm just fine."
    show cyno embarrassed
    C "if you don't mind, I'd like to keep playing with you, another time of course."
    show cyno happy
    C "anyway… do take care."

    return

label epiloguecyno:
    define cyno.opening = "hm. You're here. I think I had enough time to reflect on our last game."

    menu:
        "want to discuss this over a couple matches?":
            show cyno happy
            C "hah, its alright. What I want to say will be better conveyed in words."
    
        "I'm here to listen.":
            show cyno neutral
            C "good, because I'm about to get /srs…"
    
    show cyno neutral
    C "I think spending time with you has made me realise that connection doesn't have to be something that undermines me and how I want to feel."
    show cyno sad
    C "even if it may not seem like it, I spent my time convincing myself I didn't need anyone, and that keeping to myself would be the safest thing, for both me and everyone else."
    show cyno neutral
    C "asking you to join me after that lecture was because I knew you wouldn't treat me the way miku and the rest of the group try to do."
    show cyno happy
    C "it's strange, we built this whole thing on simple card games. its almost laughable, don't you think?"
    show cyno embarrassed
    C "but I think somewhere amidst it all, I think I found something real, and that was you."
    
    menu:
        "and what do you want it to mean?":
            show cyno fear
            C "that depends…"
        "so what now?":
            show cyno fear exclamation
            C "i… don't know."
    
    show cyno embarrassed none
    C "listen, I'm not the type of person who's outspoken when it comes to their feelings"

    show cyno neutral
    C "but you've seen a part of me that's otherwise vulnerable, one that I would usually keep hidden. and my final answer still needs input from you."
    C "so, I guess the real question is…"

    show cyno embarrassed
    C "is this us… us to keep playing as it is. Or something else… something more?"
    
    Y "{i}I should choose my words carefully.{/i}"
    
    menu .reconsider:
        "I want more, cyno, I want you.":
            show cyno happy
            C "I figured, I just needed to hear it out loud, from you."
            C "then please, let me walk with you, and be your partner. In more ways than just cards…"
            C "because if this is what love looks like for us, then I'd like to try it with you."
            
            Y "{color=#EC80EC}{i}I am now in a relationship with Cyno.{/i}{/color}"

        "I care about you. But beside you now feels just right.":
            "{i}…{/i}"
            "{i}I suddenly get the feeling that friendzoning isn't the right option.{/i}"
            "{i}perhaps I should reconsider.{/i}"
            jump .reconsider

    show cyno embarrassed
    C "so… shall we play one more round before lectures start? Just for fun, of course."

    return
