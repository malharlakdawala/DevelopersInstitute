export const MOVIE_SELECTED='MOVIE_SELECTED'

export const selectedMovie = (movie) => {
    console.log("from action", movie)
    return {
        type: 'MOVIE_SELECTED',
        payload: movie
    }
}