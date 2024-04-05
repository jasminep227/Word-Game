from turtle import*
import turtle,random
y = 200
turtle.tracer(False) #Skips animation and directly draws


word_list = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGENT',  'ALBUM', 'ALERT'
    ,'ALIKE', 'ALIVE', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER',
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
    'WROTE', 'YIELD', 'YOUNG', 'YOUTH']

answer = random.choice(word_list)

def draw_square(x,y,color):
    speed(7)
    turtle.penup() #moves while not drawing anything
    turtle.goto(x, y)
    turtle.pendown()#moves while drawing
    turtle.fillcolor(color)
    turtle.begin_fill()#starts coloring the square

    for i in range(4):
        forward(50)
        right(90)
    turtle.end_fill() #stops coloring the square

def input_wordle(word):
    user_input = turtle.textinput("Enter a 5 letter word ", word)
    if user_input !=5:
        return user_input[0:5] #only the first 5 letters will be sent

# function for wordle, where the squares will go and what color they will turn too depending on the users input
def wordle(user_input, answer, y):
    count = 0
    x = -300 # x-axis of where the square should start off
    for i in user_input:
        if i == answer:
            draw_square(x, y, "green") #if user guesses the word correctly, squares should turn green
        elif i in answer:
            draw_square(x, y, "yellow") #if user gueeses a letter correctly, sqaure should turn yellow only for that letter
        else:
            draw_square(x, y, "red") #if user did not guess the word or letter correctly, squares should turn red

        count += 1
        x += 50 #square should move along the x-axis

# end of game where it tells user when they guessed correctly or not
for i in range(7):
    guess_word = ("Guess word # "+ str(1))
    user_input = input_wordle(guess_word)
    wordle(user_input, answer, y)
    y -= 60 #square should move down the y-axis
    if user_input == answer:
        turtle.penup()
        turtle.goto(-100,-230) #where the text should be written
        turtle.pendown()
        turtle.write("Good Job! you guessed the word correctly :)")

for i in range(7):
    guess_word = ("Guess word # "+ str(1))
    user_input = input_wordle(guess_word)
    wordle(user_input, answer, y)
    y -= 60 #square should move down the y-axis
    if user_input != answer:
        turtle.penup()
        turtle.goto(-100,-200)
        turtle.pendown()
        turtle.write("Out of tries, the correct word is: " + answer)
