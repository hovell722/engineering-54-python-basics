# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.


#  as a user I should be able to keep being prompted for input until I say 'exit'

rating = ''
while rating != 'exit':
    rating = input("1: Please select the age rating for the movie: ")
    if 'pg' in rating:
        print("General viewing, but some scenes may be unsuitable for young children.")
    elif 'u' in rating:
        print("Everyone can watch.")
    elif '12' in rating:
        print("Films classified 12A and video wNo one younger than 18 may see an 18 film in a cinema.orks classified 12 contain material that is not generally suitable for children aged under 12. \nNo one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
    elif '15' in rating:
        print("No one younger than 15 may see a 15 film in a cinema.")
    elif '18' in rating:
        print("No one younger than 18 may see an 18 film in a cinema.")
    else:
        print("Please enter a valid age rating.")
