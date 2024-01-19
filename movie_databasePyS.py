import PySimpleGUI as sg

movies = []


def add_movie(values):
    title = values['title']
    director = values['director']
    year = values['year']

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
    window['-OUTPUT-'].print(f"Title: {title}\nDirector: {director}\nRelease year: {year}\n\n")


def show_movies():
    window['-OUTPUT-'].update('')
    for movie in movies:
        title = movie['title']
        director = movie['director']
        year = movie['year']
        window['-OUTPUT-'].print(f"Title: {title}\nDirector: {director}\nRelease year: {year}\n\n")


def find_movie(values):
    search_title = values['search']
    search_results = []

    for movie in movies:
        if movie["title"] == search_title:
            search_results.append(movie)

    return search_results


layout = [
    [sg.Text("Title:", justification='right', pad=((10, 10), (10, 0))),
     sg.Input(key='title', size=(20, 1), pad=((0, 10), (10, 0)), tooltip='Enter the movie title')],
    [sg.Text("Director:", justification='right', pad=((10, 10), (10, 0))),
     sg.Input(key='director', size=(20, 1), pad=((0, 10), (10, 0)), tooltip='Enter the movie director')],
    [sg.Text("Release Year:", justification='right', pad=((10, 10), (10, 0))),
     sg.Input(key='year', size=(20, 1), pad=((0, 10), (10, 0)), tooltip='Enter the release year')],
    [sg.Button("Add Movie", key='add'), sg.Button("Show Movies", key='show'),
     sg.Button("Remove Movie", key='remove')],
    [sg.Text("Search Title:", justification='right', pad=((10, 10), (10, 0))),
     sg.Input(key='search', size=(20, 1), pad=((0, 10), (10, 0)), tooltip='Enter the movie title to search')],
    [sg.Button("Find Movie", key='find')],
    [sg.Output(size=(50, 10), key='-OUTPUT-')]
]

window = sg.Window("Movie Database", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'add':
        add_movie(values)
    elif event == 'show':
        show_movies()
    elif event == 'find':
        search_results = find_movie(values)
        sg.popup_scrolled(f"Search Results:\n{search_results}", title='Search Results', size=(60, 15))
    elif event == 'remove':
        remove_title = sg.popup_get_text("Enter the title of the movie to remove:", title="Remove Movie")
        if remove_title:
            movies = [movie for movie in movies if movie["title"] != remove_title]

window.close()
