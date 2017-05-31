import fresh_tomatoes
import media

# Movies being defined and added
dunkirk = media.Movie("Dunkirk",
                      "Dunkirk is an upcoming English-language war film \
                      written, co-produced, and directed by Christopher \
                      etc...",
                      "http://bit.ly/2scXeKd",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU",
                      "R",
                      "94 mins",
                      "2017")
justice = media.Movie("Justice League",
                      "Together, Batman and Wonder Woman work quickly \
                      to recruit  a team to stand against this newly \
                      awakened enemy. etc..",
                      "http://bit.ly/2r6j30w",
                      "https://www.youtube.com/watch?v=Fm3VgcyaPfo",
                      "R",
                      "94 mins",
                      "2017")
cirlce = media.Movie("The Circle",
                      "Mae Holland seizes the opportunity of a lifetime \
                      when she lands a job with the world's \
                      and social media company.  etc...",
                      "http://bit.ly/2rQclwB",
                      "https://www.youtube.com/watch?v=QUlr8Am4zQ0",
                      "U/A",
                      "94 mins",
                      "2017")
guardians = media.Movie("Guardians of the Galaxy Vol. 2",
                      "Peter Quill and his fellow Guardians are hired by a powerful alien race, \
                      the Sovereign, to protect their precious batteries \
                      etc...",
                      "http://bit.ly/2r6pFvy",
                      "https://www.youtube.com/watch?v=dW1BIid8Osg",
                      "U/A",
                      "94 mins",
                      "2017")
thor = media.Movie("Thor: Ragnarok",
                      "Imprisoned on the other side of the universe, \
                      the mighty Thor (Chris Hemsworth) \
                      etc...",
                      "http://bit.ly/2ribhAT",
                      "https://www.youtube.com/watch?v=v7MGUNV8MxU",
                      "U/A",
                      "94 mins",
                      "2017")
despicable_3 = media.Movie("Despicable Me 3",
                      "Gru (Steve Carell) and his wife Lucy (Kristen Wiig) must stop \
                      former '80s child star Balthazar Bratt \
                      etc...",
                      "http://bit.ly/2s8Paet",
                      "https://www.youtube.com/watch?v=oagwBHoh6Rs",
                      "U",
                      "94 mins",
                      "2017")

# Create movies container
movies = [dunkirk, justice, cirlce, guardians, thor, despicable_3]

# Generate HTML
fresh_tomatoes.open_movies_page(movies)
