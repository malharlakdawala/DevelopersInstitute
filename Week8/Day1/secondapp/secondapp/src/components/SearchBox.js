const SearchBox = (props)=>{
    console.log(props)
    return(
        <div>
            Search: <input type="text" onChange={props.searchFunction}/>
        </div>
    )
}

export default SearchBox