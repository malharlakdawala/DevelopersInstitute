import {Button} from "bootstrap";
const SearchBox = (props)=>{
    console.log(props)
    return(
        <div>
            Search: <input type="text" onChange={props.searchFunction}/>
            {/*Search: <input type="text" id="search_text"/>*/}
            {/*<Button onClick={props.searchFunction}>Search</Button>*/}
            <button onClick={props.clickFunction}>Search</button>
        </div>
    )
}

export default SearchBox