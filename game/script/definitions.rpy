## MISC CHARACTERS
define Q = Character("???")
define J = Character("Jack")
define Y = Character("You")
define Sp = Character("Sparrow")
define E = Character("Eepy")
define SLC = Character("Sheldon")
define W = Character("Whisper")

## MAIN CHARACTERS
define cyno.name = "cyno"
define cyno.colour = "#a827a2"
define C = Character("Cyno", who_color=cyno.colour)
define cyno.v = C

define miku.name = "miku"
define miku.colour = "#45deba"
define M = Character("Miku", who_color=miku.colour)
define miku.v = M

define lyney.name = "lyney"
define lyney.colour = "#a61e14"
define L = Character("Lyney", who_color=lyney.colour)
define lyney.v = L

define naoto.name = "naoto"
define naoto.colour = "#0cf482"
define N = Character("Naoto", who_color=naoto.colour)
define naoto.v = N

define scara.name = "scara"
define scara.colour = "#459cde"
define S = Character("Scara", who_color=scara.colour)
define scara.v = S

## LAYEREDIMAGES
init python:
    def layerfmt(what, name, group, variant, attribute, image, image_format, **kwargs):
        if group == "expression":
            return f"{name}/{name}_{attribute}.png"
        elif group == "mark" and attribute != "none":
            return f"mark/{attribute}.png"
        return layeredimage.format_function(what, name, group, variant, attribute, image, image_format, **kwargs)

layeredimage cyno:
    zoom 0.38
    yalign 1.0

    format_function layerfmt

    group expression:
        attribute neutral default
        attribute happy
        attribute sad
        attribute disgust
        attribute angry
        attribute fear
        attribute embarrassed

    group mark:
        attribute none null default
        attribute exclamation:
            xalign 0.37
            yalign -0.65
            zoom 3.0
        attribute question:
            xalign 0.37
            yalign -0.65
            zoom 3.0
        attribute heart:
            xalign 0.37
            yalign -0.65
            zoom 0.3
        attribute vein:
            xalign 0.2
            yalign 0.1
            zoom 0.15
        attribute glee:
            xalign 0.63
            yalign -0.15
            zoom 1.0
        attribute sigh:
            xalign 0.24
            yalign 0.1
        attribute sparkles:
            xzoom -1
            xalign 0.05
            zoom 0.4
        attribute sweat:
            xalign 0.5
            yalign 0.3
            zoom 0.5
        attribute thought:
            zoom 0.2
            xalign 0.6
            yalign -1.0

layeredimage miku:
    zoom 0.37
    yalign 1.06

    format_function layerfmt

    group expression:
        attribute neutral default
        attribute happy
        attribute sad
        attribute disgust
        attribute angry
        attribute fear
        attribute embarrassed
        attribute serious

    group mark:
        attribute none null default
        attribute exclamation:
            xalign 0.345
            yalign -0.6
            zoom 3.0
        attribute question:
            xalign 0.33
            yalign -0.65
            zoom 3.0
        attribute heart:
            xalign 0.33
            yalign -0.65
            zoom 0.3
        attribute vein:
            xalign 0.18
            yalign 0.1
            zoom 0.13
        attribute glee:
            xalign 0.05
            yalign -0.32
            rotate -90
            zoom 0.9
        attribute sigh:
            xalign 0.18
            yalign 0.2
        attribute sparkles:
            xzoom -1
            xalign 0
            yalign -0.1
            zoom 0.4
        attribute sweat:
            xalign 0.45
            yalign 0.3
            zoom 0.5
        attribute thought:
            zoom 0.2
            xalign 0.46
            yalign -1.0

layeredimage lyney:
    zoom 0.39
    yalign 1.0

    format_function layerfmt

    group expression:
        attribute neutral default
        attribute happy
        attribute sad
        attribute disgust
        attribute angry
        attribute fear
        attribute embarrassed

    group mark:
        attribute none null default
        attribute exclamation:
            xalign 0.245
            yalign -0.65
            zoom 3.0
        attribute question:
            xalign 0.234
            yalign -0.65
            zoom 3.0
        attribute heart:
            xalign 0.234
            yalign -0.65
            zoom 0.3
        attribute vein:
            xalign 0.07
            yalign 0.1
            zoom 0.13
        attribute glee:
            xalign 0.45
            yalign -0.2
            zoom 1.0
        attribute sigh:
            xalign 0.12
            yalign 0.12
        attribute sparkles:
            xalign 0.48
            zoom 0.3
        attribute sweat:
            xalign 0.37
            yalign 0.3
            zoom 0.5
        attribute thought:
            zoom 0.2
            xalign 0.38
            yalign -1.0

layeredimage naoto:
    zoom 0.38
    yalign 1.09

    format_function layerfmt

    group expression:
        attribute neutral default
        attribute happy
        attribute sad
        attribute disgust
        attribute angry
        attribute fear
        attribute embarrassed

    group mark:
        attribute none null default
        attribute exclamation:
            xalign 0.29
            yalign -0.65
            zoom 3.0
        attribute question:
            xalign 0.27
            yalign -0.65
            zoom 3.0
        attribute heart:
            xalign 0.27
            yalign -0.65
            zoom 0.3
        attribute vein:
            xalign 0.14
            yalign 0.13
            zoom 0.11
        attribute glee:
            rotate -90
            xalign 0
            yalign -0.25
            zoom 1.0
        attribute sigh:
            xalign 0.17
            yalign 0.14
        attribute sparkles:
            xzoom -1
            xalign 0
            yalign 0.1
            zoom 0.4
        attribute sweat:
            xalign 0.4
            yalign 0.35
            zoom 0.4
        attribute thought:
            zoom 0.2
            xalign 0.3
            yalign -1.0

layeredimage scara:
    zoom 0.39
    yalign 1.03

    format_function layerfmt

    group expression:
        attribute neutral default
        attribute happy
        attribute sad
        attribute disgust
        attribute angry
        attribute fear
        attribute embarrassed

    group mark:
        attribute none null default
        attribute exclamation:
            xalign 0.235
            yalign -0.65
            zoom 3.0
        attribute question:
            xalign 0.2
            yalign -0.65
            zoom 3.0
        attribute heart:
            xalign 0.2
            yalign -0.65
            zoom 0.3
        attribute vein:
            xalign 0.08
            yalign 0.1
            zoom 0.12
        attribute glee:
            xalign 0.41
            yalign -0.22
            zoom 0.9
        attribute sigh:
            xalign 0.08
            yalign 0.1
        attribute sparkles:
            xalign 0.4
            zoom 0.3
        attribute sweat:
            xalign 0.34
            yalign 0.34
            zoom 0.4
        attribute thought:
            zoom 0.2
            xalign 0.28 
            yalign -1.0

layeredimage sparrow:
    zoom 0.4
    yalign 1.0

    format_function layerfmt

    group expression:
        attribute neutral default
        attribute freaky
        attribute sad
        attribute angry
        attribute fear

    group mark:
        attribute none null default
        attribute exclamation:
            xalign 0.55
            yalign -0.65
            zoom 3.0
        attribute question:
            xalign 0.55
            yalign -0.65
            zoom 3.0
        attribute vein:
            xalign 0.65
            yalign 0.1
            zoom 0.1

## MISC IMAEGS

image elephant:
    "elephant.png"
    zoom 2.0

image cat:
    "cat.png"
    zoom 0.15

image eepy:
    "eepy.png"
    zoom 0.5
    yalign 0.6

image whisper:
    "whisper.png"
    zoom 0.6

image sheldon:
    "sheldon.png"
    zoom 0.8

image prologue:
    "bg/prologue.png"
    zoom 0.70
    yalign -0.0

image silhouette:
    "whisper.png"
    zoom 0.3

    matrixcolor Matrix([ 1.0, 0.0, 0.0, -1.0,
                         0.0, 1.0, 0.0, -1.0,
                         0.0, 0.0, 1.0, -1.0,
                         0.0, 0.0, 0.0, 1.0, ])


## POSITIONS

transform r51:
    xalign 0.0
    zoom 0.93

transform r52:
    xalign 0.25
    zoom 0.93

transform r53:
    xalign 0.5
    zoom 0.93

transform r54:
    xalign 0.75
    zoom 0.93

transform r55:
    xalign 1.0
    zoom 0.93

## OTHER

image black = Solid("#000")
image white = Solid("#fff")

define audio.main = "<volume 0.45>music/main.mp3"
define audio.tense = "<volume 0.6 loop 57.536 to 76.715>music/tense.mp3"
define audio.heartwarming = "<volume 0.7 loop 23.985 to 48>music/heartwarming.mp3"
define audio.hangout = "<volume 0.5 loop 11.995 to 108>music/hangout.mp3"
