export const addCounter = (value) => {
    // console.log("addcounter")
    return {
        type: 'ADD',
        payload: value
    }
}



export const subtractCounter = (value) => {
    // console.log("addcounter")
    return {
        type: 'SUBTRACT',
        payload: value
    }
}

export const filterContentFromStatements = (value) => {
    // console.log("addcounter")
    return {
        type: 'FILTER',
        payload: value
    }
}
