# get data from file

file = open("data/movie_reviews.txt", "r")
data = file.read()
file.close()

# cut apart each review into a list
allreviews = data.split("\n")

def populate_sentiments():
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
        words[w] = [point, 1]
      else:
        words[w][0] += point  # point
        words[w][1] += 1      # count

  return words

words_rating = populate_sentiments()

def sentiment(input):
  inpWords = input.lower().split()
  ratings = []
  for iw in inpWords:
    rating = words_rating[iw] if iw in words_rating else None
    if not rating: continue
    wrating = rating[0]/rating[1]
    ratings.append(wrating)
    #print ('\'' ,iw, '\' appearears', rating[1] , 'times with an average rating of ', wrating)
  return sum(ratings)/float(len(ratings))

s1 = "The happy dog and the sad cat"
s2 = "It made me want to poke out my eyeballs"
s3 = "I loved this movie"
print (s1)
print (s2)
print (s3)
print (sentiment(s1), sentiment(s2), sentiment(s3))

inp = input('Enter a sentence: ')
print (sentiment(inp))