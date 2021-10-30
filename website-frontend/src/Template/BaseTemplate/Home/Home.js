import React from 'react';
import './Home.scss';
import {Button, Container, Row, Col, Accordion} from 'react-bootstrap';
import Section2 from './Section-2'
import { LinkContainer } from 'react-router-bootstrap';

const Home = () => {
    return(
        <div>
            <div className="Section-1">
                <div>
                    <h1 className="Header">Make a Report</h1>
                    <p className="Header">If you feel like the animal is in danger please Click on Emergency<br/> This site allows you to report for Sea Turtles,<br/> Monk Seal, and Sea birds</p>
                    <LinkContainer to="/ReportInfo"><Button className="ReportButton">File Report</Button></LinkContainer>
                    <Button className="ReportButton" variant="danger" href={'tel:888-256-9840'}>Emergency</Button>
                </div>
            </div>
            <Section2 text={"The Hawaiian monk seal is one of the most endangered seal species in the world. The population overall had been declining for six decades and current numbers, though increasing, are only about one-third of historic population levels. Hawaiian monk seals are found in the Hawaiian archipelago which includes both the main and Northwestern Hawaiian Islands and rarely at Johnston Atoll which lies nearly 1,000 miles southwest of Hawai'i. These monk seals are endemic to these islands, occurring nowhere else in the world. Hawaiian monk seals are protected under the Endangered Species Act, the Marine Mammal Protection Act, and State of Hawai'i law."} header={'Monk Seal'} img={"https://h-mar.org/wp-content/uploads/2018/12/Monk1-min-300x225.jpg"}/>
            <div className="Section-3">
                <div>
                    <h1 className="Header">Our Mission</h1>
                    <h5>To undertake substantial actions that result in the preservation, recovery and stewardship of Hawaii’s marine protected species and the ocean ecosystem we share.</h5>
                </div>
            </div>
            <Section2 text={"The green turtle (Chelonia mydas) is listed as threatened under the Endangered Species Act and is found throughout the main Hawaiian Islands. Historically, green sea turtles were abundant and nested throughout the entire Hawaiian Archipelago. However, after European colonization (around 1819), the kapu prohibition system began to erode. During the 20th century, the numbers of Hawaiian sea turtles dropped precipitously as harvests intensified and became commercialized. In 1978, green turtles received protections under the Endangered Species Act (ESA) and harvest was prohibited."} header={"Hawaii's Sea Turtles"} img={"https://h-mar.org/wp-content/uploads/2018/12/SeaTurtle-min-300x225.jpg"}/>
            <div className="Section-4">
                <div>
                    <h1 className="Header">Join our Team</h1>
                    <Container>
                    <h5>We are the largest Hawaii-based non-profit marine species response organization, covering the islands of Oahu and Molokai with our team of dedicated and hard-working volunteers, interns and staff. Our team spends thousands of hours each year responding to calls involving protected marine species such as Hawaiian monk seals, sea turtles and seabirds to provide shoreline response, stranding assistance, outreach, health management and rescue. Our work helps save these animals from deaths and injuries caused by hookings, entanglement, disease, and potentially dangerous or inappropriate interaction with humans and pets. This extensive presence in the field, combined with regular outreach and education activity in schools, community events and public venues allows us to engage with tens of thousands of people each year to build understanding, stewardship and support for Hawaii’s protected marine species and the coastal ecosystem we share.</h5>
                    </Container>
                </div>
            </div>
            <Section2 text={"There are many different types of seabirds in Hawaii. People of Hawaii have used seabirds to find fish, for navigation and for clues to changes in weather. often young seabirds stay near their nests or burrows and should be left alone."} header={"Seabirds"} img={"https://h-mar.org/wp-content/uploads/2019/06/Bird-300x225.jpg"}/>
            <div className="Section-5">
                <h1>FAQ:</h1>
                <Container>
                    <Accordion>
                        <Accordion.Item eventKey="0">
                            <Accordion.Header>How do I make a Report?</Accordion.Header>
                            <Accordion.Body>
                            <b>There are two ways to make a report:</b><br/>
                            <b>1.</b> If it is an emergency click on the emergency button on the top. This will get you in contact with one of our operators who will be on the line with you
                            to make this report.<br/>
                            <b>2.</b> Press the Fill out report button on the top of this website. Once clicked fill out the form to the best of your knowledge
                            </Accordion.Body>
                        </Accordion.Item>
                        <Accordion.Item eventKey="1">
                            <Accordion.Header>What is a Tag?</Accordion.Header>
                            <Accordion.Body>
                            Tags are identifiers place on animals to help identify them. This can be done with bleach, or actual tags.
                            </Accordion.Body>
                        </Accordion.Item>
                        <Accordion.Item eventKey="2">
                            <Accordion.Header>When is something deemed an an emergency?</Accordion.Header>
                            <Accordion.Body>
                            Emergencies depend on the situation. If at any point you are unsure if something is an emergency please use the emergency feature any way.
                            </Accordion.Body>
                        </Accordion.Item>
                    </Accordion>
                </Container>
            </div>

        </div>
    )
}

export default Home;