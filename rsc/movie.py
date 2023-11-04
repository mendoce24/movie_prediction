class movies:

    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

    



class ratings:

    def __init__(self, userId, movieId, rating, timestamp):
        self.userId= userId
        self.movieId= movieId
        self.rating= rating
        self.timestamp= timestamp

    def json_structure(self) -> str:
        mov = vars(self)
        mov_data = '{'

        for item in mov:
            mov_data += (item + ': ' + str(type(mov[item])).replace('class ', '') + ', ')
        
        mov_data += '}'

        return mov_data