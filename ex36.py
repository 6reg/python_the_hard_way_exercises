

def begin():
    print("You look out at a snowy peak.")
    print("You ponder whether to grab your skiis or your board.")
    print("Which do you grab?")

    grab = input("Skiis or Board?")

    if "Skiis" in grab:
        skiing()
    elif "Board" in grab:
        boarding()
