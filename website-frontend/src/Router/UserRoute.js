import {Navbar, Nav, Container, Button, Modal, NavDropdown, Alert} from 'react-bootstrap';
import React, {useState, useEffect} from 'react';
import { LinkContainer } from 'react-router-bootstrap';
import { createAvatar } from '@dicebear/avatars';
import * as style from '@dicebear/avatars-initials-sprites';
import SVG from 'react-inlinesvg';
import {
    Switch,
    Route,
    useHistory,
    Redirect
} from "react-router-dom";
import axios from "axios";
import './footer.scss';
import '@fortawesome/fontawesome-free/js/solid';
import '@fortawesome/fontawesome-free/js/fontawesome';
import '@fortawesome/fontawesome-free/js/brands';
import CSVFile from '../Template/UserTemplate/ExportCSV/Export';
import FileReport from '../Template/UserTemplate/MakeReports/Report';
import Home from '../Template/UserTemplate/Home/Home';
import DisplayData from '../Template/UserTemplate//DisplayData/DisplayData';


const Usertemplate = () => {
    const [invite, setInvite] = useState(false);
    const [email, setEmail] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [superUser, setSuperUser] = useState(true);
    const [inviteUser, setInviteUser] = useState(false);
    const [inviteSuccess, setInviteSuccess] = useState(false);

    const history = useHistory();

    let svg = createAvatar(style, {
        seed: firstName + ' ' + lastName
    })
    const logout = () => {
        axios({
            url:'/api/',
            method: 'post',
            data: {
                query: `
                    mutation deleteTokenCookie{
                        deleteTokenCookie(input: {}) {
                        deleted
                        }
                    }
                `
            }
        }).then((results)=> {
            history.push('/');
            
        })
    }
    const userInvite = () => {
        axios({
            url:'/api/',
            method: 'post',
            data: {
                query: `
                    mutation inviteUser{
                        inviteUser(email:"kobeuyeda@outlook.com"){
                        info
                        }
                    }
                `
            }
        }).then((results)=> {
            if(results.data.errors){
                setInviteUser(true)
                
            }
            else{
                setInviteSuccess(true)
            }
            
        })
    }
    const Close = () => {
        setInviteSuccess(false)
        setInvite(false)
        setInviteUser(false)
    }
    const Show = () => setInvite(true)

    useEffect(() => {
        axios({
            url:'/api/',
            method: 'post',
            data: {
                query: `
                query currentUser {
                    currentUser{
                      firstName
                      LastName
                      isSuperuser
                    }
                  }
                `
            }
        }).then((results)=> {
            if(results.data.errors){
                //history.push('/');
            }
            else{
                setSuperUser(results.data.data.currentUser.isSuperuser)
                setFirstName(results.data.data.currentUser.firstName)
                setLastName(results.data.data.currentUser.LastName)
            }
        }).catch((error)=> {
            //history.push('/');
        })
    }, [])

    return(
        <div>
            <Modal show={invite} onHide={Close} aria-labelledby="contained-modal-title-vcenter" centered>
                <Modal.Header closeButton>
                    <Modal.Title id="contained-modal-title-vcenter">Login</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <div>
                        {inviteUser && <Alert variant={'danger'}>Error: There seems to be an error sending out the email</Alert>}
                        {inviteSuccess && <Alert variant={'success'}>Success: An Invite email has been sent</Alert>}
                        <p>Put in the email of the user you would like to create an account for. Send one invite out at a time.</p>
                        <div className="field">
                            <input type="email" value={email} onChange={(x) => setEmail(x.target.value)} name="email" className="input" placeholder=""/>
                            <label for="email" className="label">Email</label>
                        </div>
                    </div>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="primary" onClick={()=>userInvite()}>Create an Account</Button>
                </Modal.Footer>
            </Modal>
            <Navbar fixed="top" bg="light" expand="lg">
                <Container>
                    <Navbar.Brand>
                        <img src="https://www.mauibath.com/wp-content/uploads/2019/10/596998840197290025-300x300.png" className="d-inline-block align-top" width="50" height="50" alt="HMAR logo"/>
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav>
                            <LinkContainer to="/User">
                                <Nav.Link>Reports</Nav.Link>
                            </LinkContainer>
                            <LinkContainer to="/User/Make-Report">
                                <Nav.Link>Make Reports</Nav.Link>
                            </LinkContainer>
                            <LinkContainer to="/User/Export-Report">
                                <Nav.Link>Export Reports</Nav.Link>
                            </LinkContainer>
                        </Nav>
                        <Nav className="ms-auto">
                            <NavDropdown title={<SVG src={svg} width={40}/>} id="basic-nav-dropdown">
                                {/*superUser && <NavDropdown.Item onClick={Show}><i class="fas fa-user-circle"></i>  Create Accounts</NavDropdown.Item>*/}
                                {/*<LinkContainer to="/User/settings"><NavDropdown.Item><i class="fas fa-cog"></i>  Settings</NavDropdown.Item></LinkContainer>*/}
                                <NavDropdown.Item onClick={()=>{logout()}}><i class="fas fa-sign-out-alt"></i>  Log Out</NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            <Switch>
                <Route path='/User' exact={true}>
                    <Home/>
                </Route>
                <Route path="/User/Make-Report" exact={true}>
                    <FileReport firstName={firstName} lastName={lastName}/>
                </Route>
                <Route path="/User/Export-Report" exact={true}>
                    <CSVFile/>
                </Route>
                <Route path="/user/report/:ReportNumber">
                    <DisplayData/>
                </Route>
                <Redirect from="/user" to="/User" />
            </Switch>
        </div>
    )
}

export default Usertemplate;
