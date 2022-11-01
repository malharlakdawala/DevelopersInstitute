import {connect} from "react-redux";
import {selectedMovie} from '../redux/action'

const Movielist = (props) => {
    return (
        <>
            <h1>Movie List</h1>
            <div>
                {
                    props.movies.map((item, i) => {
                        return (
                            <div key={i}>
                                <h6>{item.title}</h6>
                                <button onClick={()=>props.movieDetails(item)}>Submit</button>
                            </div>
                        )
                    })
                }

            </div>
        </>
    )
}

const mapStateTOProps = (state) => {
    return {
        movies: state.movies
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        movieDetails: (movie) => dispatch(selectedMovie(movie))

    }
}

export default connect(mapStateTOProps, mapDispatchToProps)(Movielist)