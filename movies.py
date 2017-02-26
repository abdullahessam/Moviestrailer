import fresh
from Movie import Movie
kingsman=Movie("kingsman","spy ",
               "https://goo.gl/EnFWHn",
               "https://www.youtube.com/watch?v=xkX8jKeKUEA")
ironman3=Movie("iron man 3","iron man ",
               "https://goo.gl/cIXMtJ",
               "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
nemo=Movie("nemo","finding nemo",
           "https://goo.gl/ZkFyqM",
           "https://www.youtube.com/watch?v=wZdpNglLbt8")
movie=[kingsman,ironman3,nemo]
# This function call uses list of movie instances as input to generate an HTML file
# and open it in the browser.
fresh.open_movies_page(movie)
