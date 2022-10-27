import React from "react";

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fname: '',
            lname: '',
            phno: '',
            email: '',
            formSubmitted: false
        }
    }

    submitButton = (e) => {
        const etarget = e.target
        // console.log(e.target.fname.value)
        this.setState({
            fname: etarget.fname.value,
            lname: etarget.lname.value,
            phno: etarget.phno.value,
            email: etarget.email.value,
            formSubmitted: true
        })
    }
    resetButton = (e) => {
        // console.log(e.target.fname.value)
        this.setState({
            fname: "",
            lname: "",
            phno: "",
            email: "",
            formSubmitted: false
        })
    }

    render() {
        if (this.state.formSubmitted === false) {
            console.log(this.state.formSubmitted)
            return (
                <div>
                    <h1>Welcome !</h1><br/><br/>
                    <h4>Please provide info below:</h4><br/><br/>
                    <form onSubmit={this.submitButton}>
                        fname: <input type='text' name='fname' placeholder="fname"/> <br/><br/>
                        lname: <input type='text' name='lname' placeholder="lname"/> <br/><br/>
                        Phone: <input type='text' name='phno' placeholder="phno"/> <br/><br/>
                        email: <input type='email' name='email' placeholder="email"/> <br/><br/>
                        <input type="Submit"/>


                    </form>
                </div>
            )
        } else {
            return (
                <div>
                    <h1>Hello World</h1>
                    <h3>Fname: {this.state.fname}</h3><br/><br/>
                    <h3>Lname: {this.state.lname}</h3><br/><br/>
                    <h3>Phno: {this.state.phno}</h3><br/><br/>
                    <h3>Email: {this.state.email}</h3><br/><br/>
                    <button type="reset" onClick={this.resetButton}>Reset</button>

                </div>
            )
        }
    }


}

export default Form