import speech_recognition as sr

recognizer = sr.Recognizer()

hostile_mobs = ['blaze','bogged','breeze','creeper','elder guardian','ender dragon','endermite','evoker','ghast', 'gassed','guardian','hoglin','husk','magma cube','phantom','piglin brute','pillager','ravager','shulker','silverfish','skeleton','skeleton horseman','slime','spider jockey','stray','vex','vindicator','warden','witch', 'which','wither','wither skeleton','zoglin','zombie','zombie villager', 'bee', 'cave spider', 'dolphin', 'drowned', 'enderman', 'goat', 'iron golem', 'llama', 'piglin', 'panda', 'polar bear', 'wolf', 'zombified piglin']

FILE_PATH = 'C:\\Users\\tylep\\Downloads\\MinecraftServer2\\signal.txt' 

while True:
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio).split()
        for i in range(len(text) - 1):
            word1, word2 = text[i], text[i + 1]
            combined = word1 + " " + word2
            if combined.lower() in hostile_mobs:
                with open(FILE_PATH, "w") as file:
                    file.write(combined.upper().replace(" ", "_"))
                break
        else:
            #search for one word mobs
            for i in range(len(text)):
                if text[i].lower() in hostile_mobs:
                    with open(FILE_PATH, "w") as file:
                        if text[i].lower() == "which":
                            file.write("WITCH")
                        elif text[i].lower() == "gassed":
                            file.write("GHAST")
                        else:
                            file.write(text[i].upper())
                    break
        print(text)
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Could not request results; check your internet connection.", e)
