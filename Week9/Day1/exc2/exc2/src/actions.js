export const handleChangeFromRedux =(value)=>{
    return{
        type:'CHANGE_PROP_ONE',
        payload:value
    }
}

export const handleChangeFromReduxProp2 =(value)=>{
    return{
        type:'CHANGE_PROP_TWO',
        payload:value
    }
}

export const changeTextFromRedux =(value)=>{
    return{
        type:'CHANGE_TEXT',
        payload:value
    }
}