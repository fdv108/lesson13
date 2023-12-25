import os
#os.mkdir ("Harry Potter")

basic = r"C:\Users\12345\PycharmProjects\lesson13\Harry Potter"

films_titles = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}



def dir_movie(my_set, path):
    if my_set is None or path is None:
        print ("ВИ НЕ ПЕРЕДАЛИ ЖОДНОГО ФІЛЬМУ.")
    else:
        for film in films_titles ['results']:
            subdirectory = film ["title"].replace(":", "_")
            full_path = os.path.join(path, subdirectory)
            os.mkdir(full_path)
            print(f"Додано директорію: {full_path}")


dir_movie(films_titles,basic)