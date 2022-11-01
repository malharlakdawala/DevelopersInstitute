import {connect} from "react-redux";

const Moviedetail = (props) => {

    return (
        <div>
            <h3>Movie Detail</h3>
            <p>{props.movie.title}</p>
        </div>
    )
}
const mapDispatchToProps = (state) => {
    return {
        movie: state.movie

    }
}

export default connect(mapDispatchToProps, null)(Moviedetail)