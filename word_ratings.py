import string

# get data from file

file = open("data/movie_reviews.txt", "r")
data = file.read()
file.close()


# cut apart each review into a list
allreviews = data.split("\n")

# set up a dictionary words
words = {}

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
  cleanWords = clean.split(" ")
  for w in cleanWords:
    if w not in words:
      words[w] = [1, point]
    else:
      words[w][0] += point
      words[w][1] += 1

print (words)
