import React, {useEffect, useState} from 'react';
import TableViewer from 'react-js-table-with-csv-dl';
import {Container, Row, Col, Tabs, Tab} from 'react-bootstrap';
import Filter from 'react-searchable-filter';
import {useHistory, useLocation } from 'react-router-dom';
import axios from "axios";
const CSVFile = () => {


    const Sealheaders = ["Date", "Time", "Ticket Number", "Hotline Operator Initials", "Ticket Type", "Observer", "Observer Contact Number", "Observer Initials", "Observer Type", "Sector", "Location", "Location Notes", "Seal Present?", "Size", "Sex", "Beach Position", "How Identified?", "ID Temp (Bleach #)", "Tag Number", "Tag Side", "Tag Color", "ID Perm", "Molt", "Additional Notes on ID", "ID Verified By", "Seal Logging", "Mom & Pup Pair", "SRA Set Up", "SRA Set By", "# of Volunteers Engaged", "Seal Depart Info Avail?", "Seal Departed Date", "Seal Departed Time", "Number of Calls Received", "Other Notes"];
    const TurtleHeaders = ["Date", "Time", "Ticket Number", "Hotline Operator intials", "Ticket Type", "Observer", "Phone number", "Observer Initials", "Observer Type", "Island", "Sector", "Beach/location", "Location Notes", "Type of Turtle", "Size", "Status (deceased or alive)", "Primary issue or cause of death", "Responder (only when response is needed)", "Time responder left", "Responder arrival time", "Outreach provided by operator", "F.A.S.T", "Number of calls received", "Other notes"]
    const BirdHeaders = ["Date", "Time", "Ticket Number", "Hotline Operator intials", "Ticket Type", "Observer", "Phone number", "Observer Initials", "Observer Type", "Sector", "Location", "Location Notes", "Type of Bird", "Responder's name", "Delivered", "Where to?", "Outreach provided by operator", "Number of calls received", "Other notes"]
    const [filter, setFilter] = useState({})
    const [sealTable, setSealTable] = useState([])
    const [turtleTable, setTurtleTable] = useState([])
    const [birdTable, setBirdTable] = useState([])
    const [animal, setAnimal] = useState([])
    const history = useHistory()

    useEffect(()=>{
        let queryed = `query dataCSV{
            seal:allFilterreports(Animals:"Seal"`
        if (filter.StartDate){
            queryed += `, StartDate:${JSON.stringify(filter.StartDate)}`
        }
        if (filter.EndDate){
            queryed += `, EndDate:${JSON.stringify(filter.EndDate)}`
        }
        queryed+=`){
              Date
              Time
              TicketNumber
              HotlineOperatorInitials
              TicketType{
                acronym
              }
              firstName
              phone
              ObserverInitials
              ObserverType{
                acronym
              }
              Sector{
                observerType
              }
              location
              locationDetails
              lat
              lng
              AnimalPresent
              SealSize{
                acronym
              }
              sex{
                options
              }
              beachPosition
              HowId{
                acronym
              }
              BleachNumber
              TagNumber
              TagSide{
                options
              }
              TagColor{
                options
              }
              IDPerm
              Molt
              IDDescription
              IDVerifiedBy
              SealLogging
              MomPup
              SRASetUp
              SRASetBy
              VolunteersEngaged
              SealDepart
              SealDepartDate
              SealDepartTime
              incident{
                firstName
              }
              description
            }
            SeaTurtle:allFilterreports(Animals:"Sea Turtle"`
        if (filter.StartDate){
            queryed += `, StartDate:${JSON.stringify(filter.StartDate)}`
        }
        if (filter.EndDate){
            queryed += `, EndDate:${JSON.stringify(filter.EndDate)}`
        }
        queryed+=`){
              Date
              Time
              TicketNumber
              HotlineOperatorInitials
              TicketType{
                acronym
              }
              firstName
              phone
              ObserverInitials
              ObserverType{
                acronym
              }
              onIsland{
                island
              }
              Sector{
                observerType
              }
              location
              lat
              lng
              locationDetails
              animalType{
                acronym
              }
              size
              status{
                options
              }
              CauseOfDeath{
                options
              }
              Responder
              ResponderArrived
              ResponderLeft
              OutreachProvided
              FAST{
                options
              }
              incident{
                firstName
              }
              description
            }
            SeaBird:allFilterreports(Animals:"Sea Birds"`
        if (filter.StartDate){
            queryed += `, StartDate:${JSON.stringify(filter.StartDate)}`
        }
        if (filter.EndDate){
            queryed += `, EndDate:${JSON.stringify(filter.EndDate)}`
        }
        queryed+=`){
              Date
              Time
              TicketNumber
              HotlineOperatorInitials
              TicketType{
                acronym
              }
              firstName
              phone
              ObserverInitials
              ObserverType{
                acronym
              }
              Sector{
                observerType
              }
              location
              lat
              lng
              locationDetails
              animalType{
                subAnimal
              }
              Responder
              Delivered
              WhereTo{
                options
              }
              OutreachProvided
              incident{
                firstName
              }
              description
            }
          }`
        console.log(queryed)
        axios({
            url:'/api/',
            method: 'post',
            data: {
                query: queryed
            }
        }).then((results) => {
            if(results.errors){
              history.push("/User")
            }
            let Seal = []
            let Turtle = []
            let Bird = []
            results.data.data.seal.forEach((obj) => {
                let presented = ""
                let Beach = ""
                if (obj.AnimalPresent){
                    presented = "Y"
                }
                else{
                    presented = "N"
                }
                if (obj.BeachPosition){
                    Beach = "1"
                }
                else{
                    Beach = "0"
                }
                console.log(obj)
                let value = {"Date": obj.Date, "Time": obj.Time,"Ticket Number":obj.TicketNumber, "Ticket Type": obj.TicketType.acronym, "Hotline Operator Initials":obj.HotlineOperatorInitials, "Observer": obj.firstName, "Observer Contact Number":obj.phone, "Observer Initials":obj.ObserverInitials, "Observer Type": obj.ObserverType.acronym, "Sector":obj.Sector.observerType, "Location":obj.location, "Location Notes": "lat: "+ obj.lat + ", lng: "+obj.lng+", "+obj.locationDetails, "Seal Present?":presented, "Size":obj.SealSize.acronym, "Sex":obj.sex.options, "Beach Position":Beach, "How Identified?": obj.HowId.acronym, "ID Temp (Bleach#)": obj.BleachNumber, "Tag Number": obj.TagNumber, "Tag Side": obj.TagSide, "Tag Color": obj.TagColor, "ID Perm": obj.IDPerm, "Molt":String(obj.Molt), "Additional Notes on ID":obj.IDDescription, "ID Verified By": obj.IDVerifiedBy, "Seal Logging": String(obj.SealLogging), "Mom & Pup Pair": String(obj.MomPup), "SRA Set Up":String(obj.SRASetUp), "SRA Set By":obj.SRASetBy, "# of Volunteers Engaged":obj.VolunteersEngaged, "Seal Depart Info Avail?": String(obj.SealDepart), "Seal Departed Date": obj.SealDepartDate, "Seal Depart Time": obj.SealDepartTime, "Number of Calls Received": obj.incident.length, "Other Notes": obj.description}
                Seal.push(value)
            })
            results.data.data.SeaTurtle.forEach((obj)=>{
                let turtleData = {"Date":obj.Date, "Time":obj.Time, "Ticket Number":obj.TicketNumber, "Ticket Type": obj.TicketType.acronym, "Hotline Operator intials":obj.HotlineOperatorInitials, "Ticket Type":obj.TicketType.acronym, "Observer": obj.firstName, "Phone number":obj.phone, "Observer Initials":obj.ObserverInitials, "Observer Type": obj.ObserverType.acronym, "Island":obj.onIsland.island, "Sector":obj.Sector.observerType, "Beach/location":obj.location, "Location Notes": "lat: "+ obj.lat + ", lng: "+obj.lng+", "+obj.locationDetails, "Type of Turtle":obj.animalType.acronym, "Size":obj.size, "Status (deceased or alive)":obj.status.options, "Primary issue or cause of death":obj.CauseOfDeath.options, "Responder (only when response is needed)":obj.Responder, "Time responder left":obj.ResponderLeft, "Responder arrival time":obj.ResponderArrived, "Outreach provided by operator":String(obj.OutreachProvided), "F.A.S.T":obj.FAST.options, "Number of calls received":obj.incident.length, "Other notes":obj.description}
                Turtle.push(turtleData)
            })
            results.data.data.SeaBird.forEach((obj)=>{
                let seaBirdData = {"Date":obj.Date, "Time":obj.Time, "Ticket Number":obj.TicketNumber, "Ticket Type": obj.TicketType.acronym, "Hotline Operator intials":obj.HotlineOperatorInitials, "Observer": obj.firstName, "Phone number":obj.phone, "Observer Initials":obj.ObserverInitials, "Observer Type": obj.ObserverType.acronym, "Sector":obj.Sector.observerType, "Location":obj.location, "Location Notes":"lat: "+ obj.lat + ", lng: "+obj.lng+", "+obj.locationDetails, "Type of Bird":obj.animalType.subAnimal, "Responder's name":obj.Responder, "Delivered":obj.Delivered, "Where to?":obj.WhereTo?obj.WhereTo.options:"", "Outreach provided by operator":String(obj.OutreachProvided), "Number of calls received":obj.incident.length, "Other notes":obj.description}
                Bird.push(seaBirdData)
            })
            setSealTable(Seal)
            setTurtleTable(Turtle)
            setBirdTable(Bird)
        })
    }, [filter])

    const data = [
        {
            filterBy: 'StartDate',
            description: 'The start date you are looking for',
            values: []
        },
        {
            filterBy: 'EndDate',
            values: [],
            description: 'The end date you are looking for'   
        },
    ]
    const submitHandler = (x) => {
        let filterData = {}
        x.forEach((x) => {
            filterData[x.filterBy]=x.values[0]
        })
        setFilter(filterData)

    }
    let overallStyle = {"width":'100%'};
    return (
        <div className="mt-6">
            <Container>
                <Row>
                    <Col>
                        <h5>Filter</h5>
                        <Filter options={data} onSubmit={submitHandler} placeholder='Filter Reports'/>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Tabs defaultActiveKey="Seals">
                            <Tab eventKey="Seals" title="Seals">
                                <TableViewer
                                title="Seals"
                                content={sealTable}
                                headers={Sealheaders}
                                minHeight={0}
                                maxHeight={400}
                                activateDownloadButton={true}
                                pagination={25}
                                renderLineNumber
                                reverseLineNumber
                                searchEnabled
                                sortColumn={"Date"}
                                topPagination
                                tableStyle={overallStyle}
                                titleStyle={{'textAlign':'left'}}
                                />
                            </Tab>
                            <Tab eventKey="Sea Turtles" title="Sea Turtles">
                                <TableViewer
                                title="Sea Turtles"
                                content={turtleTable}
                                headers={TurtleHeaders}
                                minHeight={0}
                                maxHeight={400}
                                activateDownloadButton={true}
                                pagination={25}
                                renderLineNumber
                                reverseLineNumber
                                searchEnabled
                                sortColumn={"Date"}
                                topPagination
                                tableStyle={overallStyle}
                                titleStyle={{'textAlign':'left'}}
                                />
                            </Tab>
                            <Tab eventKey="Sea Birds" title="Sea Birds">
                                <TableViewer
                                title="Sea Birds"
                                content={birdTable}
                                headers={BirdHeaders}
                                minHeight={0}
                                maxHeight={400}
                                activateDownloadButton={true}
                                pagination={25}
                                renderLineNumber
                                reverseLineNumber
                                searchEnabled
                                sortColumn={"Date"}
                                topPagination
                                tableStyle={overallStyle}
                                titleStyle={{'textAlign':'left'}}
                                />
                            </Tab>
                            <Tab eventKey="NOAA" title="NOAA">
                                <TableViewer
                                title="NOAA (Seals)"
                                content={sealTable}
                                headers={Sealheaders}
                                minHeight={0}
                                maxHeight={400}
                                activateDownloadButton={true}
                                pagination={25}
                                renderLineNumber
                                reverseLineNumber
                                searchEnabled
                                sortColumn={"Date"}
                                topPagination
                                tableStyle={overallStyle}
                                titleStyle={{'textAlign':'left'}}
                                />
                            </Tab>
                        </Tabs>
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default CSVFile;