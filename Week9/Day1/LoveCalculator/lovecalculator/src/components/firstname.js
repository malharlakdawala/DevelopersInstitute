const Firstname =(props)=> {
    return(
        <>
            <h2>First Name</h2>
            <input type="text" name="firstname" onChange={props.handleChange}/>
        </>
    )

}
export default Firstname