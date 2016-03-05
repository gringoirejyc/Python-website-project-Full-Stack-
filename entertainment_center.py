import media
import fresh_tomatoes

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
fresh_tomatoes.open_movies_page(movies)
