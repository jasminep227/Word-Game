import random

print("""welcome to wordle! you have 6 attempts to guess today's wordle!
your progress guide is "✔︎✘➕"
"✔︎" means you have guessed the correct letter at the correct place
"➕" means you have guessed the correct letter but at the wrong place
"︎✘" means you have incorrectly guessed the letter  """)

word_list = [
    'ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT',
    'AFTER', 'AGENT',  'ALBUM', 'ALERT',
    'ALIKE', 'ALIVE', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER',
    'ANGLE', 'ANGRY',  'ARGUE', 'ARISE', 'ASIDE', 'AUDIO', 'AUDIT', 'AVOID',
    'BADLY', 'BAKER', 'BASIC', 'BEACH', 'BEGAN', 'BEGIN',
    'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BIRTH', 'BLACK', 'BLAME',
    'BLIND', 'BLOCK', 'BOARD', 'BOUND', 'BRAIN',
    'BRAND', 'BREAD', 'BREAK', 'BRIEF', 'BRING', 'BROAD', 'BROKE',
    'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CATCH',
    'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST',
    'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CLAIM', 'CLEAN',
    'CLEAR', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT',
    'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROWD',
    'CROWN', 'CURVE', 'DAILY', 'DANCE', 'DEALT', 'DEATH',
    'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT',
    'DRAWN', 'DREAM', 'DRINK', 'DRIVE', 'DROVE', 'DYING',
    'EARLY', 'EARTH', 'EIGHT',  'EMPTY', 'ENJOY',
    'ENTRY', 'EQUAL', 'EXACT', 'EXIST',
    'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD',
    'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH',  'FLUID',
    'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK',
    'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FUNNY', 'GIANT', 'GIVEN',
    'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT',
    'GREAT',  'GROUP', 'GROWN', 'GUARD', 'GUEST',
    'GUIDE', 'HEART', 'HEAVY',  'HENRY', 'HORSE',
    'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INPUT',
     'JAPAN', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL',
    'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEAST',
    'LEGAL', 'LEWIS', 'LIGHT',  'LINKS', 'LIVES',
    'LOCAL', 'LOGIC',  'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC',
    'MAJOR', 'MAKER', 'MARCH', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT',
    'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY',
    'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC',
     'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL',
    'NURSE', 'OCEAN',  'OFTEN', 'OTHER', 'OUGHT',
    'PAINT', 'PANEL',  'PARTY', 'PHASE', 'PHONE',
     'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT',
    'PLATE', 'POINT', 'POUND', 'POWER', 'PRICE', 'PRIDE', 'PRIME',
    'PRINT', 'PRIOR', 'PRIZE', 'PROUD', 'PROVE', 'QUICK',
    'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH',
    'READY', 'RIGHT', 'RIVAL', 'ROBIN', 'ROMAN',
    'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCOPE',
    'SCORE', 'SHAPE', 'SHARE', 'SHARP',
     'SHELF', 'SHIFT', 'SHIRT', 'SHOCK', 'SHORT',
    'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED',  
    'SLIDE', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE',
     'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEND',
    'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAGE', 'STAKE', 'STAND',
     'STEAM', 'STICK', 'STOCK', 'STONE',
     'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY',
    'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'TABLE', 'TAKEN',
    'TAXES', 'TEACH', 'TEXAS', 'THANK', 'THEFT', 'THEIR',
     'THICK', 'THING', 'THINK', 'THIRD', 'THOSE',
     'THREW', 'THROW',  'TIMES', 'TIRED',  'TODAY',
    'TOPIC', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN',
    'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY',
    'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL',
    'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS',
     'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER',
     'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD',
   'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG',
    'WROTE', 'YIELD', 'YOUNG', 'YOUTH'
]

def word_generator():
    random_word_position = random.randint(0, 389)
    random_word = word_list[random_word_position]
    return random_word


word = word_generator()

def word_in(string):
    index_of_char = 0
    for char in string:
        position = word.rfind(char)
        if position == -1:
            print(char + '✘' + "\t")
        elif position != index_of_char:
            print(char + '➕' + "\t")
        elif position == index_of_char:
            print(char + '✔︎' + "\t")
        index_of_char += 1


def wordle():
    x = 5
    while x >= 1:
        guess = input("Enter Guess \n" + "Attempts Left: " + str(x) + "\n")
        if len(guess) == 5:
          word_in(guess.upper())
          x -= 1
          if guess.upper() == word:
            print("YOU WON!!!")
            break
        else:
          print("5 letter words only")
    if guess.upper() != word:
      print("You Lost :( \n" + "The answer was: " + word)

def again():
    x = 1
    while x == 1:
        wordle()
        global word
        word = word_generator()
        yes = input("Play again? (Y/N)")
        if yes.upper() != "Y":
            x += 1
            print("Goodbye :)")

again() 
