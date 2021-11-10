import React, {useEffect, useState, useCallback} from 'react';
import {Container, Col, Row, Carousel} from 'react-bootstrap';
import {useParams} from 'react-router-dom'
import axios from "axios";
import {GoogleMap, useJsApiLoader, Marker, Rectangle} from '@react-google-maps/api';
import './Detail.scss';

const DisplayData = () => {
    const {ReportNumber} = useParams()
    const [data, setData] = useState({})
    const [, setMarkerMount] = useState()
    useEffect(() => {
        axios({
            url:'/api/',
            method: 'post',
            data: {
                query: `query dataCSV{
                    singleReport(TicketNum:${JSON.stringify(ReportNumber)}){
                      Date
                      Time
                      TicketNumber
                      HotlineOperatorInitials
                      TicketType{
                        acronym
                      }
                      firstName
                      lastName
                      email
                      phone
                      ObserverInitials
                      ObserverType{
                        observerType
                      }
                      Sector{
                        observerType
                      }
                      location
                      locationDetails
                      lat
                      lng
                      Top
                      Bottom
                      Left
                      Right
                      AnimalPresent
                      SealSize{
                        options
                      }
                      sex{
                        options
                      }
                      beachPosition
                      HowId{
                        options
                      }
                      BleachNumber
                      TagNumber
                      TagSide{
                        options
                      }
                      TagColor{
                        options
                      }
                      onIsland{
                        island
                      }
                      animalType{
                        subAnimal
                        animal{
                            animal
                          }
                      }
                      size
                      status{
                        options
                      }
                      CauseOfDeath{
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
                      Delivered
                      WhereTo{
                        options
                      }
                      description
                      animalImages
                    }
                  }`
            }
        }).then((results) => {
            setData(results.data.data.singleReport)
        })
    }, [])
    const [libraries] = useState(["places"])

    const { isLoaded } = useJsApiLoader({
        id: 'google=map-script',
        googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAP_API_KEY,
        libraries: libraries,
    })
    const MapHandling = {
        gestureHandling: 'false',
        draggable: false,
    }
    const markerOnLoad = useCallback((marker) => {
        setMarkerMount(marker)
    }, [])
    const containerStyle = {
        width: '100%',
        height: '400px',
    };
    return data.Date ? (
        <Container className="mt-6">
            <Row>
                <Col>
                    <h2>Ticket Number: {ReportNumber}</h2>
                </Col>
            </Row>
            <Row>
                <Col className="imageback">
                    <Carousel>
                    {data.animalImages && data.animalImages.map((x, key)=>{
                        return(
                        <Carousel.Item>
                                <img className="d-block w-100" key={key} src={x} alt="some incident Report"/>
                        </Carousel.Item>)
                    })}
                    </Carousel>
                </Col>
            </Row>
            <Row className="mt-4">
                <Col lg={3} md={12}><h6><b>Date:</b>{data.Date}</h6></Col>
                <Col lg={3} md={12}><h6><b>Time:</b>{data.Time}</h6></Col>
                <Col lg={3} md={12}><h6><b>Hot Line Operator Initials:</b>{data.HotlineOperatorInitials}</h6></Col>
                <Col lg={3} md={12}><h6><b>Ticket Type:</b>{data.TicketType.acronym}</h6></Col>
            </Row>
            <Row className="mt-4">
                <Col lg={3} md={12}><h6><b>Observer First Name:</b> {data.firstName}</h6></Col>
                <Col lg={3} md={12}><h6><b>Observer Last Name:</b> {data.lastName}</h6></Col>
                <Col lg={3} md={12}><h6><b>Email:</b>{data.email}</h6></Col>
                <Col lg={3} md={12}><h6><b>Phone Number:</b><a href={'tel:'+data.phone}>{data.phone}</a></h6></Col>
            </Row>
            <Row className="mt-4">
                <Col lg={3} md={12}><h6><b>Observer Inistails:</b> {data.ObserverInitials}</h6></Col>
                <Col lg={3} md={12}><h6><b>Observer Type:</b> {data.ObserverType.observerType}</h6></Col>
                <Col lg={3} md={12}><h6><b>Sector:</b>{data.Sector.observerType}</h6></Col>
                <Col lg={3} md={12}><h6><b>location:</b>{data.location}</h6></Col>
            </Row>
            <Row className="mt-4 mb-4">
                <Col lg={6} md={12}>
                {isLoaded && <GoogleMap
                    mapContainerStyle={containerStyle}
                    center={{lat:parseFloat(data.lat), lng:parseFloat(data.lng)}}
                    zoom={15}
                    options={MapHandling}>
                        <Marker position={{lat:parseFloat(data.lat), lng:parseFloat(data.lng)}} onLoad={markerOnLoad}/>
                        <Rectangle onload bounds={{north:parseFloat(data.Top), south:parseFloat(data.Bottom), east:parseFloat(data.Right), west:parseFloat(data.Left)}}/>
                    </GoogleMap>}
                </Col>
                <Col lg={6} md={12}>
                <h6><b>location Detail:</b>{data.locationDetails}</h6>
                </Col>
            </Row>
            <Row className="mt-4">
                <Col lg={4} md={12}><h6><b>Animal Present:</b> {data.AnimalPresent?'Yes':'No'}</h6></Col>
                <Col lg={4} md={12}><h6><b>Description:</b> {data.description}</h6></Col>
                <Col lg={4} md={12}><h6><b>Amount of Reports:</b> {String(data.incident.length)}</h6></Col>
            </Row>
            {data.animalType.animal.animal === 'Seal' &&
            <div>
                <Row className="mt-4">
                    <Col lg={3} md={12}><h6><b>Size:</b> {data.SealSize.options}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Sex:</b> {data.sex.options}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Beach Position:</b> {String(data.beachPosition?'Land':'Water')}</h6></Col>
                    <Col lg={3} md={12}><h6><b>How Identified:</b> {data.HowId.options}</h6></Col>
                </Row>
                <Row className="mt-4">
                    <Col lg={3} md={12}><h6><b>ID Temp (Bleach #):</b> {data.BleachNumber}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Tag Number:</b> {data.TagNumber}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Tag Side:</b> {data.TagSide && data.TagSide.options}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Tag Color:</b> {data.TagColor && data.TagColor.options}</h6></Col>
                </Row>
                <Row className="mt-4">
                    <Col lg={3} md={12}><h6><b>ID Perm:</b> {data.IDPerm}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Molt:</b> {data.Molt?'Yes':'No'}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Additional Notes on ID:</b> {data.IDDescription}</h6></Col>
                    <Col lg={3} md={12}><h6><b>ID Verified By:</b> {data.IDVerifiedBy}</h6></Col>
                </Row>
                <Row className="mt-4">
                    <Col lg={3} md={12}><h6><b>Seal Logging:</b> {data.SealLogging}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Mom & Pup Pair:</b> {data.MomPup}</h6></Col>
                    <Col lg={3} md={12}><h6><b>SRA Set Up:</b> {String(data.SRASetUp?'Yes':'No')}</h6></Col>
                    <Col lg={3} md={12}>{data.SRASetUp && <h6><b>SRA Set By:</b> {data.SRASetBy}</h6>}</Col>
                </Row>
                <Row className="mt-4 mb-4">
                    <Col lg={3} md={12}><h6><b># of Volunteers Engaged:</b> {data.VolunteersEngaged==null?'0':String(data.VolunteersEngaged)}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Seal Depar Info Avail:</b> {data.SealDepart?'Available':'Not Available'}</h6></Col>
                    <Col lg={3} md={12}>{data.SealDepart&&<h6><b>Seal Depart Date:</b> {data.SealDepartDate}</h6>}</Col>
                    <Col lg={3} md={12}>{data.SealDepart&&<h6><b>Seal Depart Time:</b> {data.SealDepartTime}</h6>}</Col>
                </Row>
            </div>}
            {data.animalType.animal.animal === 'Sea Turtle' && 
            <div>
                <Row className="mt-4">
                    <Col lg={3} md={12}><h6><b>Type of Turtle:</b> {data.animalType.subAnimal}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Size:</b> {data.size}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Status (deceased or alive):</b> {data.status.options}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Primary issue or cause of dath:</b> {data.CauseOfDeath.options}</h6></Col>
                </Row>
                <Row className="mt-4">
                    <Col lg={3} md={12}><h6><b>Responder (only when reponse is needed):</b> {data.Responder}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Time Responder left:</b> {data.ResponderLeft}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Time Responder Arrived:</b> {data.ResponderArrived}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Outreach Provided by operator:</b> {data.OutreachProvided ? 'Yes':'No'}</h6></Col>
                </Row>
                <Row className="mt-4 mb-4">
                    <Col lg={6} md={12}><h6><b>F.A.S.T:</b> {data.FAST !== null && data.FAST.options}</h6></Col>
                    <Col lg={6} md={12}><h6><b>Island:</b> {data.onIsland.island}</h6></Col>
                </Row>
            </div>
            }
            {data.animalType.animal.animal === 'Sea Birds' && 
            <div>
                <Row className="mt-4">
                    <Col lg={3} md={12}><h6><b>Type of Birds:</b> {data.animalType.subAnimal}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Responder (only when reponse is needed):</b> {data.Responder}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Delivered:</b> {data.Delivered? 'Yes': 'No'}</h6></Col>
                    <Col lg={3} md={12}><h6><b>Where to?:</b> {data.WhereTo !== null && data.WhereTo.options}</h6></Col>
                </Row>
                <Row className="mt-4 mb-4">
                    <Col lg={12} md={12}><h6><b>Outreach Provided by operator:</b> {data.OutreachProvided ? 'Yes':'No'}</h6></Col>
                </Row>
            </div>
            }
        </Container>
    ):(<div></div>)
}

export default DisplayData;