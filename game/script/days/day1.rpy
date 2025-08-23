label day1:
    call screen calendar(1) with fade

label day1morning:
    play music main

    show screen top_right_ui(1, "Morning")
    scene entrance day
    with fade

    ">> Po University International"

    Y "{i}It's my first day here and this place seems weird already! Oh well, guess I'll fit in...{/i}"

    show cyno neutral
    with dissolve

    Q "{cps=4}Yo."

    menu:
        "Who tf are you?":
            show cyno disgust
            Q "Do you need help finding the special needs department?"

        "HAIIIIII!":
            Q "yo wsp my guy."

    Y "{i}oops, I went totally off the script!{/i}"

    show cyno neutral
    C "anyways you're the new exchange student right? I was instructed to be your guide. Call me Cyno, or don't I really don't mind."

    menu:
        "why?":
            show cyno disgust
            C "why am I your guide? Bro idk I was forced to."

        "okay cyno!":
            show cyno embarrassed
            C "You're chirpy aren't you..."

    show cyno neutral
    C "well anyways, I will get you to your classroom."

    scene hallway day
    show cyno neutral
    show miku neutral at right
    with fade

    Q "woah who the hell is this?"
    C "the new transfer student."

    show miku disgust
    Q "uh why did he transfer?"
    
    show cyno disgust
    C "to study idk don't question everything in this place it is left ambiguous for a reason"
    
    show miku neutral glee
    M "oh shit, I forgot to introduce myself. I'm the one and only hatsune miku!"

    menu:
        "does cyno not have a last name?":
            show cyno disgust sigh
            C "why do you care? do you want my last name for marriage purposes or something?"
        "Miku? I think I've heard of you before.":
            show miku neutral none
            M "yea well I am quite well known."

    show miku neutral none
    M "anyways, you'll hear a lot more about and from me because I'm the student council president."
    
    show cyno neutral none
    C "why do we have a student council isn't this supposed to be a uni?"

    show miku angry
    M "shushhh you said don't question it."

    show cyno neutral
    C "I'm studying econ"

    show miku embarrassed
    M "uhm-"

    show lyney neutral at left with dissolve
    Q "save it, don't worry I'll save you from the awkwardness!"

    menu:
        "why is there a freak show overload?":
            show lyney sad
            Q "tch, guess my acting isn't really that good!"

        "aww really?":
            show lyney happy glee
            Q "of course! anything for an old friend!"

            show miku neutral
            M "you guys know eachother?"

            show lyney embarrassed none
            Q "no I have no clue who he is, I just overheard him say his name. glad he went along with the joke or it would've been awkward."

    show miku neutral
    M "well duh, anyways lyney why are you here? By the way, this is lyney a famous performer in the school."
    
    show lyney neutral
    L "To answer your question I'm here looking for my sister lynette!"
    
    show miku neutral
    M "well why don't you come in and I introduce you to everyone!"
    
    show cyno sad
    C "this was my tour..."

    scene classroom day
    show cyno neutral at left
    show miku neutral
    with fade

    M "so this is uhmmm..."
    C "its okay he doesn't matter we can skip him."

    show miku embarrassed
    M "and this! is-"
    C "she's not in today."

    show miku embarrassed sigh
    M "and this is uhm-"

    menu:
        "you're a horrible class president.":
            show miku embarrassed vein
            M "you couldn't do any better!"
        "it's okay miku just introduce me to people you know.":
            show miku neutral none
            M "well uhm."

    show scara neutral at right with dissolve

    M "ah here's one I know! This is scara, he's emo that's why he sits alone at the back of the class."

    show scara angry vein
    S "shut up."

    show cyno embarrassed
    C "this one's my favourite."

    show scara disgust
    S "what, who the hell even are you?"

    menu:
        "does he not have a last name as well?":
            show cyno angry
            C "what's your obsession with last names?"
        "I like your name scara!":
            show scara embarrassed none
            S "its a nickname I guess."

    show scara neutral none
    S "anyways... what's your name again?"
    S "jack.. Hm."

    show cyno disgust
    C "bro it ain't that deep stop overthinking a name."

    "Teacher" "alright kids sit down we need to register you, whilst I set that up a word from one of our student Council."

    scene classroom day
    with dissolve

    show naoto neutral at r53
    with dissolve

    "{i}you sit down next to cyno with miku infront of you.{/i}"

    C "that's naoto shirogane btw. She's in another class."
    N "hello everyone..."

    show cyno at r51
    with dissolve

    menu:
        "so do only girls get last names?":
            show cyno angry
            C "if you ask once more I'm letting my demons out."
        "student council member?":
            C "TBH idk what they do so don't ask me."

    show miku at r54
    with dissolve

    M "psst naoto!"
    N "huh?"
    M "come to the roof at lunch!"
    M "Cyno you too!"
    C "huh?"
    M "and you exchange student!"

    menu:
        "Are you asking me out?":
            show miku fear
            M "huh? no weirdo.. just show up, 'kay?"
        "only if you can take me there!":
            show miku happy
            M "hehe of course!"

    show cyno disgust
    C "what is that about?"

    show cyno happy glee
    C "hm well anyways. uh you play cards?"

    show scara angry at r55 with dissolve
    S "stop boring him and get to economics class."
    S "{i}nods at jack as he walks off.{/i}"

    scene black with fade

    Y "{i}what a weird first day... and its only first period. I have a lot ahead of me, better atleast make it to lunch{/i}"

label day1lunch:
    scene roof day
    show screen top_right_ui(1, "Lunch")
    show miku neutral glee at r52
    show cyno neutral at r54
    with fade
    
    M "I'm so glad you actually showed up!"

    show lyney neutral at r53 with dissolve
    L "of course we would!"

    show cyno disgust
    C "when was the magician invited?"
    
    show miku neutral none
    M "I asked him in our economics lecture?"

    show scara neutral sigh at r51 with dissolve
    S "why are we here?"
    
    show miku angry vein
    M "more like why are you here! who invited you!"

    show scara neutral glee
    S "I tagged along."
    
    show cyno neutral
    C "he has no friends."

    show scara angry none
    S "shut up-"
    
    show naoto neutral at r55 with dissolve
    show miku neutral none
    M "and naoto-"

    show cyno neutral
    C "she also has no friends."
    
    show naoto disgust sigh at r55
    N "ugh, this guy.."
    
    show lyney sad
    L "you all are making horrible first impressions of yourselves."
    
    show naoto angry none
    N "its not my first though-"
    
    show miku happy
    M "whatever anyways! welcome to my club!"
    
    show cyno neutral
    C "I don't remember you having a club?"
    
    show miku angry
    M "I'm giving an introduction!"

    show naoto neutral question
    N "what's this club for?"

    show miku disgust
    M "All students are required to attend some form of club. I thought that being the leader of the school council was enough but I was confronted by faculty"

    show miku neutral glee
    M "I didn't really like any clubs here. So I decided to put my leadership skills in action and create my own!"

    show naoto neutral none
    show cyno neutral
    C "Isn't the school council enough for you to be running?"

    show lyney neutral question
    L "Yea, I mean you already have so many responsibilities running that anyways, why would you want to do this as well?"

    show naoto neutral
    N "That is true. We have to help plan the upcoming open days and other events!"
    
    show miku neutral sparkles
    M "Well I don't think there's a place to discuss what truly matters, what people feel actually intrigued about extra-circularly!"
    M "There's so much going on in the world with so many ideas to explore. I want a space for that to cultivate and grow into something never seen before by a club!"
    
    show miku disgust
    M "Besides, what other clubs are there in this University again, genshin society? Ugh.."

    show lyney neutral none
    show naoto neutral
    N "Well, I'm not objected to that. It's just rather we don't have a purpose for this club and your explanation was rather.."

    show scara neutral sigh
    S "Vague?"
    
    show miku embarrassed
    M "I will decide that! eventually.."

    show miku neutral sparkles
    M "Right now I just need some form of commitment and interest so I can get the school's approval."
    M "That's where you guys come in! I have a sign up list right here."
    M "As the leader of the student council you have my promise to figure out the purpose of this club, so just - sign here!"

    show cyno happy
    C "Yeah sure, why not. I will sign up."

    show naoto happy
    N "From being in the school council with you, I have absolute trust in you to run anything of that sort. I will pledge too."
    
    show lyney happy
    L "Don't leave me out guys! I will be joining too!"

    show miku neutral glee
    M "Yay! So many already!"

    show miku neutral
    M "What about you two?"
    M "Oh wait, you’re only here on exchange, right?"

    menu:
        "Nah I lied to get more attention.":
            show cyno disgust
            C "No, I was given an introduction from the teachers when I was forced to tour you."
            C "You're definitely not staying."

            show scara disgust
            S "are we just ignoring the second part?"

        "Yes actually.":
            show miku serious
            M "I figured as much."
            show miku neutral
            M "Well I was actually told that but whatever-"

    show naoto sad
    N "So then does he even qualify as a student?"
    
    show lyney neutral
    L "Well, it's in the title itself."
    L "And I thought as an exchange student he was meant to experience this university to the fullest!"
    L "Surely in your project somewhere-"
    
    show cyno neutral
    C "Prove that you have friends is a part of the qualifications, yea."
    
    N "If we want to give him an accurate perspective of that he should be allowed to join."

    show scara neutral
    S "and do a weeks worth of activities?"

    show naoto happy sparkles
    N "You can utilise a week to the fullest if you try!"

    show naoto -sparkles
    M "well, I don't see a reason why he shouldn't be allowed to join.."

    M "what do you say?"

    menu .question:
        "Of course! It sounds fun!":
            show miku happy
            M "thank you!"

        "I'm not too sure...":
            M "Aw really? Do reconsider?"
            jump .question

    M "and you scara?"

    show scara happy
    S "You're asking me even though I wasn't invited? that's funny.."
    
    show scara neutral
    S "I'm sure you've gotten enough already-"

    menu:
        "It wouldn't be the same without you.":
            show scara embarrassed
            S "...!"

            show scara disgust vein
            S "what a dramatic way of putting it, especially over some petty club-"

        "the more the merrier!":
            show scara neutral
            S "Sure. whatever you say captain!"

    show scara angry none
    S "Well, anyways I guess I may as well sign it.."

    show miku neutral glee
    M "Everyone, thank you so much! I'll keep you updated if I come up with anything!"

    hide miku with dissolve
    "{i}Miku runs off...{/i}"

    show naoto neutral
    N "I think it's time for class now."

    Y "{i}guess I should head to class now as well..{/i}"

    N "Oh.. it's you!"

    menu:
        "who are you again?":
            N "naoto? I don't recall if we have properly talked. Well.. I'm naoto shirogane, vice president of the student council."
        "Oh look it's the student council guy!":
            show naoto embarrassed exclamation
            N "oh wow! you remembered. Didn't think I'd leave such an impression, eheh."

    show naoto neutral none
    N "well anyways, lyney and I have the same lecture as you next, want to come with us?"

    menu:
        "Yes":
            scene hallway day
            show lyney neutral
            show naoto neutral at right
            with fade

            N "oh I'm glad you joined us! So, how was your first day..."

            show lyney happy
            L "My dear naoto save the small talk, lets get to it! Are you gay?"

            show naoto fear exclamation
            N "Lyney?!"
            L "well I'm just getting right to it, you know the name of the game!"

            show naoto embarrassed -exclamation
            N "mister... I'm so sorry!"

            menu:
                "No actually, I'm gay, I'm coming out, I'm on the right track baby I was born this way!!":
                    show lyney happy sparkles
                    L "YASSS king SLAYYY"
                "invasion of privacy smh":
                    show naoto embarrassed sigh
                    N "I am really sorry for this..."

            show lyney neutral
            show naoto embarrassed
            N "well anyways.."

            show naoto neutral question
            N "do you find this club weird?"
            L "well it hasn't come into play yet, so let it take its shape and then we can judge."
            
            show naoto none
            N "I guess..."

        "No":
            pass

    Y "Well uh cya after class!"

label day1afternoon:
    scene classroom evening
    show screen top_right_ui(1, "Afternoon")
    with fade
    Y "{i}Now that that's over, I just need to power through this final lecture!{/i}"

    scene entrance evening
    show screen top_right_ui(1, "After School")
    with fade
    Y "{i}Maybe after class I should walk with someone to my dorm...{/i}"

    menu:
        Y "{i}Who should I walk with?{/i}"

        "Cyno":
            call day1hangoutcyno from _call_day1hangoutcyno
        "Miku":
            call day1hangoutmiku from _call_day1hangoutmiku
        "Lyney":
            call day1hangoutlyney from _call_day1hangoutlyney
        "Naoto":
            call day1hangoutnaoto from _call_day1hangoutnaoto
        "Scara":
            call day1hangoutscara from _call_day1hangoutscara

    call dayend