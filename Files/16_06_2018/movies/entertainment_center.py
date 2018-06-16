import media
import tv_show
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        90,
                        "A story of a boy and his toys that comes alive",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    90,
                    "A marine on an alient planet",
                    "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                            90,
                            "Using rock music to learn",
                            "http://barkerhost.com/wp-content/uploads/sites/4/2017/08/cREN222Yw78zvSQ9bg17Y9QZS0c-0.jpg",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouile = media.Movie("Ratatouile",
                        90,
                        "Rat is a chef in paris",
                        "http://www.impawards.com/2007/posters/ratatouille_xlg.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

young_sheldon = tv_show.Tvshow("Young Sheldon",
                                30,
                                "Season 1",
                                22,
                                "CBN")

movies = [toy_story, avatar, school_of_rock, ratatouile]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print("***********************")
print(avatar.title)
print(avatar.duration)
print("***********************")
print(young_sheldon.title)
print(str(young_sheldon.duration))