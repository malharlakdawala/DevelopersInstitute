import {Link} from "react-router-dom";
import {NavLink} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import {Navbar, Nav} from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'

const Navbar1 = () => {
    return (
        <nav>
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/shop">Shop</Link>
        </nav>)
    //
    // )

    // return (
    //     <Navbar bg="light" expand="lg">
    //         <LinkContainer to="/">
    //             <Navbar.Brand>React-Bootstrap</Navbar.Brand>
    //         </LinkContainer>
    //         <Navbar.Toggle aria-controls="basic-navbar-nav"/>
    //         <Navbar.Collapse id="basic-navbar-nav">
    //             <Nav className="mr-auto">
    //                 <LinkContainer to="/service">
    //                     <Nav.Link>Service</Nav.Link>
    //                 </LinkContainer>
    //                 <LinkContainer to="/about">
    //                     <Nav.Link>About</Nav.Link>
    //                 </LinkContainer>
    //             </Nav>
    //         </Navbar.Collapse>
    //     </Navbar>
    // )
}

export default Navbar1