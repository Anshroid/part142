# ^( *)\d?(?s:(M)(?=.*(miku))|(L)(?=.*(lyney))|(N)(?=.*(naoto))|(S)(?=.*(scara))|(C)(?=.*(cyno))): (.+) \((.*)\)
# $1show $3$5$7$9$11 $13\n$1$2$4$6$8$10 "$12"

# [\s"]i(?:'[md]|ve|ll)?[\s]|[\s"][Ii](?:[md]|ve|ll)[\s]|["\s]hes\s|\w(?:{/i})?"|nt\s

label start:
    scene casino
    show cyno happy
    with fade

    call poker
label prologue:
    scene black with fade
    J "Somewhere, sometime in this new univers…"
    J "ity, this new university that I'm transferring to."
    J "Oh right, my name is Jack Cruise! I am the new exchange student here for-"
    J "No that doesn't sound right."
    J "The name's Cruise…"
    J "Jack Cruise."
    J "Hmm no-"
    J "How about just-"
    J "'hello I'm the new exchange student'"
    J "I'm only really here for a week, I don't have much to lose."
    J "But hopefully if I play my cards right, I will be able to complete my project and along with that-"
    J "{i}Form strong connections with people.{/i}"

    $ i = 1
    while i <= 7:
        call expression f"day{i}"
        $ i += 1


label dayend:
    scene your room
    with fade

    stop music fadeout 1.0
    
    Y "{i}Time to go to sleep...{/i}"

    scene black
    hide screen top_right_ui
    with fade