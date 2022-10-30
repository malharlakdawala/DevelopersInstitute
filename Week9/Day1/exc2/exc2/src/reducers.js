const initState = {
    property1: "Prop4_from_reducer",
    property2: "Prop2_from_redux",
    text: "Text from Redux"
}

export const reducer = (state = initState, action = {}) => {

    switch (action.type) {
        case 'CHANGE_PROP_ONE':
            return {...state, property1: action.payload}
        case 'CHANGE_PROP_TWO':
            return{...state, property2: action.payload}
        case 'CHANGE_TEXT':
            return{...state, text: state.property2}
        default:
            return {...state}

    }
}