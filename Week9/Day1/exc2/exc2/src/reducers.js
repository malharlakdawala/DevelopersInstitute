const initState = {
    property1: "Prop4_from_reducer",
    property2: "Prop2"
}

export const reducer=(state=initState,action)=>{
    return{...state}
}