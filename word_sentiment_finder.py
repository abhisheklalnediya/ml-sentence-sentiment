# get data from file

file = open("data/movie_reviews.txt", "r")
data = file.read()
file.close()



# cut apart each review into a list
allreviews = data.split("\n")

# set up dictionary to hold ALL words and point values

sentiment = {}



for review in allreviews:
  if(not len(review)): continue               # some lines are empty, skip them
  # get the point value
  point = int( review[0] )

  # clean up the review
  clean = ""

  for c in review[2:]:
    if c.isalpha() or c == " ":
      clean += c

  clean = str.lower(clean)

  # isolate each word
  words = clean.split(" ")
  for w in words:
    if w not in sentiment:
      sentiment[w] = [1, point]
    else:
      sentiment[w][0] += 1
      sentiment[w][1] += point

phrase = input("enter a phrase: ")

# isolate each word in the phrase
words = phrase.split(" ")

total = 0
num   = 0

for w in words:
  if w in sentiment:
    num += 1
    score = sentiment[w][1] / sentiment[w][0]
    total += score
    print (w, "has a value of", score)

if num and total/num >= 2:                                            #num can be some time 0
  print ("This is a POSITIVE phrase")
else:
  print ("This is a NEGATIVE phrase")
