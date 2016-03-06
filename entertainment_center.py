import media
import fresh_tomatoes

#these 5 object includes info of the movie"
m1 = media.Movie("Vita e bella",
                 "Life is beautiful",
                 "https://la-vie-est-belle.wikispaces.com/file/view/La_vie_est_belle_affiche.jpg/272769820/363x431/La_vie_est_belle_affiche.jpg",
                 "https://www.youtube.com/watch?v=hbQvTEV5qXY")
m2 = media.Movie("Vita e bella",
                 "Life is beautiful",
                 "https://la-vie-est-belle.wikispaces.com/file/view/La_vie_est_belle_affiche.jpg/272769820/363x431/La_vie_est_belle_affiche.jpg",
                 "https://www.youtube.com/watch?v=hbQvTEV5qXY")
m3 = media.Movie("Vita e bella",
                 "Life is beautiful",
                 "https://la-vie-est-belle.wikispaces.com/file/view/La_vie_est_belle_affiche.jpg/272769820/363x431/La_vie_est_belle_affiche.jpg",
                 "https://www.youtube.com/watch?v=hbQvTEV5qXY")
m4 = media.Movie("Vita e bella",
                 "Life is beautiful",
                 "https://la-vie-est-belle.wikispaces.com/file/view/La_vie_est_belle_affiche.jpg/272769820/363x431/La_vie_est_belle_affiche.jpg",
                 "https://www.youtube.com/watch?v=hbQvTEV5qXY")
m5 = media.Movie("Vita e bella",
                 "Life is beautiful",
                 "https://la-vie-est-belle.wikispaces.com/file/view/La_vie_est_belle_affiche.jpg/272769820/363x431/La_vie_est_belle_affiche.jpg",
                 "https://www.youtube.com/watch?v=hbQvTEV5qXY")

movies = [m1,m2,m3,m4,m5]

# Uses list of movie instances as input to generate an HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)

#Print the document in the file "media" Movie class
#print (media.Movie.__doc__)
