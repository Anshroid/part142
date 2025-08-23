init python:
    class Triangle(renpy.Displayable):
        def __init__(self, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)

        def render(self, width, height, st, at):
                render = renpy.Render(500, 500)
                canvas = render.canvas()
                
                canvas.circle("#78c9ffDD", (440, -310), 500)

                return render