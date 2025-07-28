def sitara_response(name, prediction):
    import pyttsx3
    import random

    engine = pyttsx3.init()
    engine.setProperty('rate', 120)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Adjust index if needed

    sassy_survive = [
        "Lucky duck! This one made it.",
        "Survived like a boss.",
        "Oh yes, they lived to spill the tea.",
        "This one danced their way to safety.",
        "They found the lifeboat and a happy ending.",
        "Oof! This one's lucky. Impressive!",
        "This one dodged the iceberg like a pro.",
        "They must have had a guardian angel on board."
    ]

    sassy_sunk = [
        "No lifeboat could save this one.",
        "Down with the ship... tragically.",
        "They had no plot armor today.",
        "Gone with the waves." ,
        "This one didn't make the sequel.",
        "Sunk like a stone, bless their heart.",
        "Nope, this one's doomed.",
        "They must have missed the lifeboat drill."
    ]

    if prediction == 1:
        message = f"{name}, {random.choice(sassy_survive)}"
    else:
        message = f"{name}, {random.choice(sassy_sunk)}"

    print("Sitara 🦉:", message)
    engine.say(message)
    engine.runAndWait()