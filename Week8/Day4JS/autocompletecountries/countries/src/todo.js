import React from "react";

class Todo extends React.Component {
    constructor() {
        super();
        this.state = {
            todos: ["shopping", "flower the plants"]
        }
    }

    handleClick = (e) => {
        if (e.key === "Enter") {
            console.log(e.target.value)
            let existingTodos=this.state.todos
            existingTodos.push(e.target.value)
            this.setState({todos: existingTodos})
        }

    }


    render() {
        const {todos} = this.state
        console.log(todos)
        return (
            <div>
                <h1>Todo</h1>
                <input type="text" onKeyPress={this.handleClick}/>
                <br/><br/><br/>
                <h3>List of Todos</h3>
                {todos.map((item) => (
                    <div>{item}</div>
                ))}

            </div>
        )
    }

}

export default Todo