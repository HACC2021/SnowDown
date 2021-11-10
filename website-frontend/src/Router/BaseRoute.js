import {Navbar, Nav, Container, Button, Modal, Alert} from 'react-bootstrap';
import React, {useState} from 'react';
import { LinkContainer } from 'react-router-bootstrap';
import {
    Switch,
    Route,
    useHistory
} from "react-router-dom";
import axios from "axios";
import './footer.scss';
import '@fortawesome/fontawesome-free/js/solid';
import '@fortawesome/fontawesome-free/js/fontawesome';
import '@fortawesome/fontawesome-free/js/brands';
import Home from '../Template/BaseTemplate/Home/Home';
import FileReport from '../Template/BaseTemplate/Reports/Report';


const Basetemplate = () => {
    const[loginShow, setLoginShow] = useState(false);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const history = useHistory()
    const [loginError, setLoginError] = useState(false)

    const Login = () => {
        console.log('yes')
        axios({
            url:'/api/',
            method: 'post',
            data: {
                query: `
                    mutation tokenAuth {
                        tokenAuth(email: ${JSON.stringify(email)}, password: ${JSON.stringify(password)}) {
                        user {
                            firstName
                        }
                        }
                    }
                `
            }
        }).then((results)=> {
            if(results.data.errors){
                setLoginError(true)
            }
            else{
                history.push('/User?pagination=1')
            }
            
        })
    }

    const Close = () => setLoginShow(false)
    const Show = () => {
        console.log('working')
        setLoginShow(true)}

    return(
        <div>
            <Modal show={loginShow} onHide={Close} aria-labelledby="contained-modal-title-vcenter" centered>
                <Modal.Header closeButton>
                    <Modal.Title id="contained-modal-title-vcenter">Login</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <div>
                        {loginError && <Alert variant={'danger'}>Your password or username is wrong please try again</Alert>}
                        <div className="field">
                            <input type="email" value={email} onChange={(x) => setEmail(x.target.value)} name="email" className="input" placeholder=""/>
                            <label for="email" className="label">Email</label>
                        </div>
                        <div className="field">
                            <input type="password" value={password} onChange={(x) => setPassword(x.target.value)} className="input" placeholder=""/>
                            <label for="password" className="label">Password</label>
                        </div>
                    </div>
                    <div>
                        <LinkContainer to="/ForgotPassword"><a>Forget Your Password?</a></LinkContainer>
                    </div>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="primary" onClick={()=>Login()}>Login</Button>
                </Modal.Footer>
            </Modal>
            <Navbar fixed="top" bg="light" expand="lg">
                <Container>
                    <Navbar.Brand>
                        <img src="https://www.mauibath.com/wp-content/uploads/2019/10/596998840197290025-300x300.png" className="d-inline-block align-top" width="50" height="50" alt="HMAR logo"/>
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="ms-auto">
                            <LinkContainer to="/">
                                <Nav.Link>Home</Nav.Link>
                            </LinkContainer>
                            <Button variant="light" onClick={Show}>Login</Button>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            <Switch>
                <Route path='/' exact={true}>
                    <Home/>
                </Route>
                <Route path="/ReportInfo" exact={true}>
                    <FileReport/>
                </Route>
                <Route path="*">
                    <h1 className="mt-6">404 Error: Page does not exist</h1>
                </Route>
            </Switch>
        </div>
    )
}

export default Basetemplate;