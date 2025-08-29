label hangout:
    Y "{i}maybe after class I should spend time with someone…{/i}"

    $ unavailable = set(properCase(c.name) for c in [cyno, lyney, scara, naoto, miku] if c.level == 3)

    menu:
        set unavailable

        Y "{i}Who should I hang out with?{/i}"

        "Cyno":
            stop music fadeout 1.0
            queue music hangout
            call hangoutcyno from _call_hangoutcyno
        "Miku":
            stop music fadeout 1.0
            queue music hangout
            call hangoutmiku from _call_hangoutmiku
        "Lyney":
            stop music fadeout 1.0
            queue music hangout
            call hangoutlyney from _call_hangoutlyney
        "Naoto":
            stop music fadeout 1.0
            queue music hangout
            call hangoutnaoto from _call_hangoutnaoto
        "Scara":
            stop music fadeout 1.0
            queue music hangout
            call hangoutscara from _call_hangoutscara