from turtle import Turtle , Screen
import random
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "gold", "silver", "violet",
    "indigo", "turquoise", "salmon", "navy", "maroon", "olive", "lime",
    "teal", "aqua", "coral", "orchid", "plum", "tan", "chocolate",
    "beige", "azure", "lavender", "khaki", "crimson", "slategray",
    "seagreen", "wheat", "tomato", "sienna", "peru", "mintcream",
    "ivory", "aliceblue", "antiquewhite", "bisque", "blanchedalmond",
    "burlywood", "cadetblue", "chartreuse", "cornflowerblue", "darkgreen",
    "darkorange", "darkorchid", "deepskyblue", "dodgerblue", "firebrick",
    "forestgreen", "gainsboro", "ghostwhite", "honeydew", "hotpink",
    "indianred", "lemonchiffon", "lightblue", "lightcoral", "lightcyan",
    "lightgoldenrodyellow", "lightgreen", "lightpink", "lightsalmon",
    "lightseagreen", "lightskyblue", "lightslategray", "lightsteelblue",
    "limegreen", "linen", "mediumaquamarine", "mediumblue", "mediumorchid",
    "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen",
    "mediumturquoise", "mediumvioletred", "midnightblue", "moccasin",
    "navajowhite", "oldlace", "olivedrab", "orange", "orangered", "palegoldenrod",
    "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff",
    "powderblue", "rosybrown", "royalblue", "saddlebrown", "sandybrown",
    "skyblue", "snow", "springgreen", "steelblue", "thistle", "yellowgreen"
]
t = Turtle()
directions = [0, 90, 180, 270]
t.speed("fastest")
t.pensize(10)
t.screen.bgcolor("black")


for _ in range (200):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
