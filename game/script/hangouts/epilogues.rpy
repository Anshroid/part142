define properCase = lambda s: s[0].upper() + s[1:]

label epilogue:
    scene entrance day

    python:
        eligible = [c for c in [cyno, lyney, scara, naoto, miku] if c.level == 3]
        choice = False

        if len(eligible) == 2:
            if eligible[0].points != eligible[1].points:
                eligible = [max(eligible, key=lambda c: c.points)]
            else:
                choice = True

    if choice:
        show expression eligible[0].name + " neutral" at left with dissolve
        eligible[0].v "[eligible[0].opening]"

        show expression eligible[1].name + " neutral" at right with dissolve
        eligible[1].v "[eligible[1].opening]"

        menu:
            "who should I talk to?"

            "[properCase(eligible[0].name)]":
                $ chosen = eligible[0]

            "[properCase(eligible[1].name)]":
                $ chosen = eligible[1]

        scene entrance day
        show expression chosen.name + " neutral"
        with fade
        
        call expression "epilogue" + chosen.name from _call_expression_1

    else:
        $ chosen = eligible[0]

        show expression chosen.name + " neutral" with dissolve
        chosen.v "[chosen.opening]"

        call expression "epilogue" + chosen.name from _call_expression_2

    Y "{i}I feel a strong bond between me and [properCase(chosen.name)], one that cannot be broken.{/i}"
    Y "{i}this bond, shall be my eyes to see the truth.{/i}"

    return
