const Secondname =(props)=> {
    return(
        <>
            <h2>Second Name</h2>
            <input type="text" name="secondname" onChange={props.handleChange}/>
        </>
    )

}
export default Secondname