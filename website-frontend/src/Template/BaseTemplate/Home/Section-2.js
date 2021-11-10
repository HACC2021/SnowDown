import React from 'react';
import {Container, Row, Col} from 'react-bootstrap';

const Section2 = (props) => {
    return(
        <div className="Section-2">
            <div>
                <Container>
                    <Row>
                        <Col lg={6} md={12} sm={12}>
                            <img className="section-img" src={props.img} width="300px" height="200px" alt="Monk Seal"/>
                        </Col>
                        <Col lg={6} md={12} sm={12}>
                            <h2 className="Section-2-header"><b>{props.header}</b></h2>
                            <p className="Section-2-info">
                                {props.text}
                            </p>
                        </Col>
                    </Row>
                </Container>
            </div>
        </div>
    )
}

export default Section2;