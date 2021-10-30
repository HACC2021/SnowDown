import {Navbar, Nav, Container, Button, Modal, Col, Row} from 'react-bootstrap';
import React, {useState} from 'react';
import { LinkContainer } from 'react-router-bootstrap';
import {
    Switch,
    Route,
} from "react-router-dom";
import './footer.scss';
import '@fortawesome/fontawesome-free/js/solid';
import '@fortawesome/fontawesome-free/js/fontawesome';
import '@fortawesome/fontawesome-free/js/brands';
import Home from '../Template/BaseTemplate/Home/Home';


const Basetemplate = () => {
    const[loginShow, setLoginShow] = useState(false)

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
                        <div class="field">
                            <input type="email" name="email" class="input" placeholder=""/>
                            <label for="email" class="label">Email</label>
                        </div>
                        <div class="field">
                            <input type="password" class="input" placeholder=""/>
                            <label for="password" class="label">Password</label>
                        </div>
                    </div>
                    <div>
                        <LinkContainer to="/ForgotPassword"><a>Forget Your Password?</a></LinkContainer>
                    </div>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="primary">Login</Button>
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
                <Route to='/' exact={true}>
                    <Home/>
                </Route>
                <Route to="/ReportInfo" exact={true}>

                </Route>
            </Switch>
            <div className="Footer">
                <Container>
                    <Row>
                        <Col>
                        <p>© 2020 Hawaii Marine Animal Response All rights reserved</p>
                        </Col>
                        <Col>
                            <a href="https://www.facebook.com/HawaiiMarineAnimalResponse/"><i aria-hidden="true" className="logofooter fab fa-facebook-f fa-lg"/></a>
                            <a href="https://www.instagram.com/hawaiimarineanimalresponse/"><i class="logofooter fab fa-instagram fa-lg"></i></a>
                            <a href="https://twitter.com/HIMarineAnimal"><i class="logofooter fab fa-twitter fa-lg"></i></a>
                        </Col>
                    </Row>
                </Container>
            </div>
        </div>
    )
}

export default Basetemplate;