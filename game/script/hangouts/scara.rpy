default scara.points = 0
default scara.level = 1

label hangoutscara:
    call expression "hangoutscara" + str(scara.level) from _call_expression_6
    $ scara.level += 1
    return

label day1hangoutscara:
    stop music fadeout 1.0
    queue music hangout
    
    scene street evening
    show scara neutral
    with fade
    
    S "…ugh. If I don't do this, miku might kill me."
    show scara angry
    S "just, don't be too annoying… k?"

    menu:
        "so I can still be a little annoying?":
            show scara happy
            $ scara.points += 1
            play sound point
            S "ha… keep talking like that and I might almost not hate this."

        "you could've just said you wanted someone to talk too…":
            show scara angry
            S "don't go putting words in my mouth, got it?"

    show scara neutral
    S "look, I just don't get people like you. The kind that are always just so persistent, getting their noses in places where they shouldn't."
    S "why do you even bother walking with someone who clearly doesn't want to be walked with?"

    menu:
        "you don't actually mean it…":
            show scara angry
            $ scara.points += 1
            play sound point
            S "shut up."

        "I regret it already.":
            show scara neutral
            S "go on, turn around. I'm not gonna stop you."

    show scara happy
    S "you're irritating, but maybe its not the worst thing in the world."
    show scara angry
    S "whatever… forget I said anything."
    show scara neutral
    S "see you around."

    return

label hangoutscara1:
    Y "{i}now that I think about it…{/i}"

    default checkset = set()
    menu .wheretocheck:
        set checkset
        Y "{i}where would scara usually be after school?{/i}"

        "check his dorm room":
            scene room scara evening with fade
            Y "{i}I came out all this way and he's not even hiding here?{/i}"
            Y "{i}I'd better leave quickly or else people might think I'm trespassing…{/i}"
            jump .wheretocheck

        "check the lecture hall":
            scene lecture with fade
            Y "{i}no one's here but me, guess people only come here when they actually have to…{/i}"
            Y "{i}there's no point in me staying here any longer…{/i}"
            jump .wheretocheck

        "check the library":
            scene library with fade
            Y "{i}what did I expect, he's certainly not the academic kind of guy…{/i}"
            Y "{i}I should leave, I don't wanna disturb anybody studying.{/i}"
            jump .wheretocheck

        "check the rooftop":
            scene roof evening with fade
            Y "{i}is that him?{/i}"

    show scara neutral with dissolve
    S "…"

    Y "{i}maybe I should say something…{/i}"

    menu .whattosay:
        "…":
            jump .whattosay
        "scara?":
            pass
        "are you okay?":
            pass
        "meow?":
            pass

    show scara angry
    S "…tch, you just had to open your mouth, huh?"

    show scara neutral
    S "I knew you were here, I'd just rather avoid unnecessary conversation, especially with someone as persistent as you."

    menu:
        "how rude…":
            show scara neutral
            S "actually, its my way of trying to be nice"

            $ scara.points += 1
            play sound point
            S "so… you're welcome."

        "that makes two of us then.":
            show scara angry
            S "c'mon, you're just contradicting yourself now. If you were actually trying to avoid me then you wouldn't have come up here."

    show scara neutral
    S "anyway, what do you want?"
    
    Y "let's hang out!"

    show scara neutral
    S "…fine."

    show scara happy
    S "hah, you look so surprised. You probably thought I would take some extra convincing."

    show scara neutral
    S "look, I'm only doing this so that you can stop bothering me again, that's all…"
    S "well? where should we go?"

    menu:
        "how about the cinema?":
            show scara happy
            S "hmph, alright. but you're paying."
            
            scene cinema
            show scara angry
            with fade

            S "you didn't even check what was on did you?"

            show scara neutral
            S "'no promises to keep' sounds like a romance if you ask me…"
            
            menu:
                "I thought you'd complain either way…":
                    $ scara.points += 1
                    play sound point
                    S "seems like you do know me pretty well. Hmph."

                "I thought you might enjoy being bored out of your mind!":
                    S "if I wanted to kill some time, I'd do something else. Besides, its not like I HATE these kinds of films."

            show scara happy
            S "but seriously, taking me of all people to see a romance? Don't expect me to be all lovey dovey with you afterwards."

            menu:
                "you're not gonna leave tho, right?":
                    show scara angry
                    S "I might start having second thoughts if you don't shut your mouth."

                "its like you read my mind…":
                    show scara embarrassed
                    S "I-... j-just shut it and watch the film!"

            "{i}the film ends, scara and I walk back outside{/i}"

            show scara happy
            S "huh. that was better than I expected."
            show scara angry
            S "hey! Why are you looking at me like that? Don't read too much into it."
            show scara neutral
            S "it was decent… barely."

        "there's this buffet nearby…":
            show scara happy
            S "hmph, alright. but you're paying."
            
            scene restaurant
            show scara angry
            with fade

            S "ugh, there's too much noise… so chaotic."
            show scara neutral
            S "is this really your idea of 'hanging out?' in that case, don't expect me to talk and eat at the same time."

            menu:
                "you don't have to talk at all, honestly.":
                    show scara happy
                    $ scara.points += 1
                    play sound point
                    S "I didn't think you would be capable of going without a conservation for more than a second, I'm impressed."

                "maybe try and enjoy yourself for once.":
                    show scara neutral
                    S "and how about you stop trying to psychoanalyse me for once. I'm fine."

            show scara neutral
            S "…"

            show scara happy
            S "you don't talk as much when you're eating."
            S "trust me, I'm not gonna complain, its quite peaceful like this."

            menu:
                "would you like me to ruin it?":
                    show scara angry
                    S "I mean, you just did."
                    show scara neutral
                    S "but… ill allow it, I suppose."

                "the food is just SOOO good!":
                    show scara angry
                    S "at least finish chewing before you open your mouth, where are your basic manners…?"
            
            "{i}we finish eating, scara and I walk back outside{/i}"

            show scara neutral
            S "the food was fine I guess. But only cuz you paid for it…"
            S "just, don't get used to it, k?"

            show scara happy
            S "though I guess the grating voices around our table were more of a headache than you, which is something."

    scene park
    show scara neutral
    with fade

    "{i}scara and I sit beside each other on an isolated bench just outside the campus{/i}"

    stop music fadeout 1.0
    queue music sentimental

    S "…you really don't know how to leave people alone, do you?"
    show scara sad
    S "most people choose to stop talking to me once they realise I'm no good."
    show scara neutral
    S "but you… you're different. Its as if you've decided I'm actually worth something."
    show scara angry
    S "what am I even talking about… you're just being annoying, and pretty darn stupid."

    menu:
        "its because I already understand you.":
            show scara fear exclamation
            $ scara.points += 1
            play sound point
            S "!!..."
            show scara angry -exclamation
            S "y-you know nothing about me! and besides, its like you don't know when to stop, huh?"
            show scara neutral
            S "…i suppose that's not the worst thing about you though."

        "hehe, I like a challenge y'know.":
            show scara angry
            S "what the hell are you getting at? is this just some kind of game to you?"
            show scara neutral
            S "…ill just forget you said that, okay?"

    show scara neutral
    S "come to think of it, I've felt this before."
    show scara happy
    S "this… strange warmth. Just sitting beside someone who…"
    show scara angry
    S "…"

    menu:
        "its okay, take your time.":
            pass
        "is this your way of confessing to me?":
            pass

    show scara neutral
    S "nah, forget it. I'm just tired."
    S "Jack, what we did today, it doesn't mean anything. We're not friends. We just spent some time together… that's all."
    S "I'd rather you didn't invite me again, it saves us both the trouble."

    show scara happy
    S "still, I didn't hate it."

    return

label hangoutscara2:
    scene roof evening
    show scara neutral
    with fade
    
    Y "{i}I head up to the rooftop and to my surprise I find scara still at the same spot.{/i}"

    S "…"

    Y "{i}maybe I should say something…{/i}"

    menu:
        "…":
            show scara neutral
            S "jack, I know you're here, no use being silent."
        "did you even try to pick a new hiding place?":
            show scara angry
            S "why would I? This is a good spot… except if I was trying to hide from you."
        "meow~":
            show scara fear
            S "m-meow?"

    show scara neutral
    S "anyway, what do you want this time?"

    Y "lets hangout again-"

    show scara angry
    S "did you forget what I told you last time?"
    S "it was just a one off, I can't do it again."
    
    menu:
        "cant?":
            show scara neutral
            S "maybe that was a wrong choice of words."
        "its not that you can't do it. You just can't do it YET!":
            show scara disgust
            S "growth mindset propaganda isn't going to work on me."

    show scara neutral
    S "point is, I don't want to be closer to you. In fact, I don't need anyone."
    show scara sad
    S "that's the reason why I keep my distance. I'm scared."
    S "scared that I might be betrayed again…"

    menu:
        "maybe not needing people is how you protect yourself.":
            show scara neutral
            S "tch, I'm not gonna deny that."
        "that sounds kinda lonely.":
            show scara angry
            S "what's it to you? This is just how its supposed to go."

    show scara neutral
    S "getting close to people like you, its only gonna complicate things."
    show scara sad
    S "you start to have wants, even desires. You also expect a lot of things from them. But in the end, you just get disappointed."
    show scara angry
    S "so just because you think you understand what I'm going through doesn't make it any different for me."

    menu:
        "I won't expect anything, I only want to know you.":
            show scara neutral
            S "god you really are an idiot. Either that or you're just too stupid for your own good."
            show scara happy
            $ scara.points += 1
            play sound point
            S "I've met worse people though, so take that how you will."

        "makes sense, you're a lot of work after all.":
            show scara angry
            S "then don't waste your time, its not like I asked for this or anything."

    show scara neutral
    S "…fine. You've proven to be more persistent than ever before."
    S "one more hangout. Only cause I'm bored"
    S "and, I guess I'll feel kinda bad leaving you now."

    show scara angry
    S "huh? I-i didn't say anything, k?"
    
    scene mall
    show scara angry
    with fade

    "{i}scara and I arrive at a busy shopping district{/i}"

    show scara angry
    S "why does it have to be so crowded? This was your idea."
    show scara neutral
    S "I'm telling you, if we get lost, I'm blaming you for the rest of my life, and that's a long time!"
    show scara angry
    S "what are you even trying to do anyway? Don't tell me I'm being forced into some kind of retail therapy!"
    
    "{i}we pass a small shop, and several things grab my attention.{/i}"
    "{i}perhaps I could get something for scara, but what would he like, and would he even accept it?{/i}"

    $ scara.points += 1

    menu:
        "a silver feather tassel":
            play sound point
            S "huh, what's this?"
            show scara fear exclamation
            S "a feather? How… sentimental."
            show scara neutral -exclamation
            S "I'll keep it I suppose, don't ask why. It just, brings back some old memories."

        "a black cat plushie":
            play sound point
            S "huh, what's this?"
            show scara fear
            S "this cat, you're saying 'this is so me?'"
            show scara neutral
            S "how absurd, but it looks kinda cute, so I'll take it."

        "animal crossing new leaf":
            play sound point
            S "huh, what's this?"
            show scara neutral
            S "!!... hmph. You're lucky I have a 3DS to play this on."
            show scara fear exclamation
            S "but seriously, I've always wanted this game, how did you know?"

        "an iridescent ring":
            play sound point
            S "huh, what's this?"
            show scara happy
            S "how bold of you, is this meant to be some sort of proposal?"
            show scara fear exclamation
            S "n-no? Ahem, its oddly fitting to say the least. Wait… how much did you pay for this?"

    scene street evening
    show scara neutral
    with fade

    "{i}after walking around the shopping district for a while, scara and I head back to our dorms together{/i}"

    stop music fadeout 1.0
    queue music sentimental

    show scara neutral
    S "…jack, I never got the chance to say thank you, for the gift I mean."
    S "but remember, this is a just another one time thing. I'll probably forget the gift sooner or later, and it'll be sitting there in my room forever."

    show scara angry
    S "starting to regret your act of kindness now?"
    
    menu:
        "you say all that but you haven't once stopped holding it.":
            show scara angry
            S "shut up! Do you really want me to push you into traffic?"

        "that doesn't matter to me, as long as you liked it.":
            show scara disgust
            S "that's just… ugh, you're really confusing, Jack."

    show scara neutral
    S "I was thinking that I would finally get tired of you, same goes for you too."
    show scara angry
    S "guess what? It didn't work. Again."
    show scara neutral
    S "its just so annoying, how easy it is be around you, to talk to you I mean."
    
    $ scara.points += 1

    menu:
        "thanks for the compliment~":
            show scara happy
            play sound point
            S "it wasn't meant to be one, but sure."
        "the feeling's mutual.":
            show scara fear exclamation
            play sound point
            S "c'mon, you have to be lying… wait, you're not?"

    show scara neutral none
    S "the weird thing is, it doesn't feel like we're total strangers, or even people who just know each other. It feels quite natural."
    S "I find myself slowly getting into something I shouldn't be. I don't know what's going on but, I'm not sure if I want it to stop or not."

    show scara happy
    S "hah, you've made a big mistake y'know."
    
    show scara neutral
    S "because now I don't know if I can go back to the old me."
    
    show scara angry
    S "though if you tell anyone I said this, then I'll make your life hell, got it?"

    return

label epiloguescara:
    define scara.opening = "jack, can you spare me some time?"

    show scara angry
    S "…what am I saying, of course you will."

    menu:
        "what's up?":
            pass

        "are we hanging out 'one more time?'":
            show scara neutral
            S "no, its just…"
    
    show scara neutral
    S "there's something I've been meaning to say, and if I don't do it now then I won't ever."

    menu:
        "then say it!":
            show scara disgust
            S "tch, still annoying as always."

        "you can talk to me about anything.":
            show scara neutral
            S "hm, better to get it over with I guess."

    show scara neutral
    S "look, I thought keeping you away would protect us both and that if I acted detached, then you'd just get bored, and leave me before things would hurt."

    show scara sad
    S "I tried so many times, but you never gave up. You stayed."
    S "now… I'm not sure if I ever want you to go."

    show scara neutral
    S "jack, you're different from everyone else. Y'know that right?"
    S "you just see me as a person, and that I'm worth something."

    show scara sad
    S "and I gotta be honest, that terrifies me. Because I'm not used to it."
    
    menu:
        "I'm still here, and I'll never leave you.":
            pass
        "You don't have to keep pushing people away forever.":
            pass

    show scara fear exclamation
    S "!!..."

    show scara neutral none
    S "I didn't expect this, nor did I really want this… but.."

    show scara happy
    S "I love you."
    S "and I think, this time, I'm not gonna run away from my feelings."

    Y "scara…"
    
    Y "{i}I feel an inextricable connection towards scara, a connection that transcends life and death itself{/i}"
    Y "{i}could this… be the truth I've been searching for?{/i}"
    
    Y "I love you too, Scara."

    show scara neutral
    S "jack…"
    
    Y "{color=#EC80EC}{i}I am now in a relationship with Scara{/i}{/color}"

    show scara happy
    S "hah, screw it, now it's real. And there's no turning back for both of us."
    S "but now that I think about it, I don't feel so scared anymore."
    
    Y "{i}I take Scara's hand slightly{/i}"
    
    show scara fear exclamation
    S "…?"

    show scara -exclamation
    
    Y "{i}both scara and I lean into each other, and exchange a kiss, followed by a warm embrace.{/i}"

    return   
