#  English to African/Nigerian language dictionary translator
# Each group member contributed one dictionary of 20 words.
yoruba = {
   "water" : "omi",
     "good morning" : "E kaaaaro",
      "good evening" : " E kaale",
       "come" : "wa",
       "take" : "gba",
       "food" : "ounje",
       "child" : "Omo",
       "friend" : "ore",
       "mother" : "iya",
       "father" : "baba",
       "news" : "iroyin",
       "book" : "iwe",
       "knowledge" : "imo",
       "city" : "ilu",
       "time" : "igba",
       "family" : "idile",
       "head" : "ori",
       "love" : "ife",
       "waist" : "ibadi",
       "road" : "ono",
}

igbo = {
    "water": "mmiri",
    "sun": "anyanwu",
    "love": "ifuru",
    "food": "nri",
    "friend": "enyi",
    "day": "ubochi",
    "fire" : "oku",
    "night": "abali",
    "moon /month": "onwa",
    "house": "ulo",
    "dog": "nkita",
    "please": "biko",
    "river":"osimiri",
    "mountain": "ugwu",
    "peace": "udo",
    "lie": "asi",
    "truth": "eziokwu",
    "medicine": "ogwu",
    "head":"isi",
    "thank you":"daalu"
}

idoma =  {
    "hello": "awo",
    "welcome": "awo ole",
    "thank you": "ojale",
    "please": "kpo kpo",
    "yes": "ee",
    "no": "ko",
    "good morning": "awo oni",
    "good afternoon": "awo ocha",
    "good evening": "awo olo",
    "how are you": "ole kpa?",
    "I am fine": "m kpa",
    "name": "nyian",
    "water": "ami",
    "food": "inyam",
    "house": "owa",
    "friend": "ogele",
    "love": "iyolo",
    "money": "owo",
    "work": "ukpa",
    "God": "Owoicho"
}

hausa ={
    "water" : "ruwa",
    "food" :"abinci",
    "house": "gida",
    "person": "mutum",
    "child" : "yaro",
    "girl" : "yarinya",
    "money" : "kudi",
    "work" : "aiki",
    "road" : "hanaya",
     "book" : "littafi",
    "market" : "kasuwa",
    "to see" : "gani",
    "to listen" : "saurara",
    "speech/talk" : "magana",
    "time" : "lokaci",
    "day/sun" : "rana",
    "night" : "dare",
    "walking/journey" : "tafiya",
    "heart/mind" : "zuciya"
}
mwaghavul = {
             "goodmorning": "teerianga",
             "God": "naan",
             "food": "biise",
             "welcome": "mwale",
             "cane": "kam",
             "bible": "po naan",
             "song": "koghg",
             "chair": "bi tong",
             "food": "bisee",
             "medicine": "yen",
             "cloud": "nluu",
             "please": "kusugk",
             "salt": "kiin",
             "run": "zsu",
             "come": "ji",
             "go": "so",
             "friend": "shaarr",
             "money": "shagal",
             "how are you": "aaere",
             "God is good": "da naaan diret",
             "what is your name?": "suum fugha a wee"}


#  All dictionaries in one big dictionary
languages = {
    "yoruba": yoruba,
    "hausa": hausa,
    "igbo": igbo,
    "idoma": idoma
}

choice = input("Choose a language: ").lower()
if choice not in languages:
    print("Language not found.")
    exit()

word = input("Enter an English word: ").lower()

translation = languages[choice].get(word)

if translation:
    print("Translation:", translation)
else:
    print("Word not found in dictionary.")








