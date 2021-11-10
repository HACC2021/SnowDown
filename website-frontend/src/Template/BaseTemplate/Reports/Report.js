import React, {useState, useEffect, useCallback} from 'react';
import {Nav, Navbar, Container, Button, Row, Col} from 'react-bootstrap';
import {GoogleMap, useJsApiLoader, StandaloneSearchBox, Marker, Rectangle} from '@react-google-maps/api';
import {useHistory} from 'react-router-dom';
import Select from 'react-select';
import Geocode from "react-geocode";
import PhoneInput from 'react-phone-number-input';
import { Dropzone, FileItem } from "@dropzone-ui/react";
import axios from "axios";
import 'react-tagsinput/react-tagsinput.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'react-phone-number-input/style.css';
import './report.scss';
require('dotenv').config();


const FileReport = () => {
    const [phone, setPhone] = useState(null);
    const [marker, setMarker] = useState({lat:null, lng:null})
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [mapSearch, setMapSearch] = useState('None');
    const [pictures, setPicture] = useState([])
    const [images, setImages] = useState([])
    const [animalsType, setAnimalsType] = useState([])
    const [submitQuery, setSubmitQuery] = useState(true)
    const [description, setDescription] = useState('')
    const [sector, setSector] = useState('')
    const [locationDescription, setLocationDescription] = useState('')
    const [animalPresent, setAnimalPresent] = useState(null)
    const [sealSize, setSealSize] = useState(null)
    const [sex, setSex] = useState(null)
    const [landWater, setLandwater] = useState(null)
    const [IDedType, setIdType] = useState(null)
    const [tagedSide, setTagedSide] = useState(null)
    const [tagColor, setTagColor] = useState(null)
    const [tagNumber, setTagNumber] = useState(null)
    const [bleachNum, setBleachNum] = useState(null)
    const [IdPerm, setIdPerm] = useState(null)
    const [IdDescription, setIdDescription] = useState(null)
    const [molting, setMolting] = useState(null)
    const [sealLogging, setSealLogging] = useState(null)
    const [momPup, setMomPup] = useState(null)
    const [SRASetUp, setSRASetUp] = useState(null)
    const [sealDepart, setSealDepart] = useState(null)
    const [size, setSize] = useState(null)
    const [status, setStatus] = useState(null)
    const [issue, setIssue] = useState(null)
    const [island, setIsland] = useState(null)
    const [FAST, setFAST] = useState(null)
    const [SRAName, setSRAName] = useState(null)
    const [departDate, setDepartDate] = useState(null)
    const [departTime, setDepartTime] = useState(null)
    const [delivered, setDeleivered] = useState(null)
    const [outReach, setOutReach] = useState(null)
    const [deliveryLocation, setDeliveryLocation] = useState(null)
    const [responderName, SetResponderName] = useState('')
    const [amountOfResponder, setAmountOfResponder] = useState(null)
    const [timeArrived, setTimeArrived] = useState(null)
    const [timeLeft, setTimeLeft] = useState(null)

    const [center, setCenter] = useState({lat: 19.8968, lng:155.5828});
    const [markerMount, setMarkerMount] = useState()
    const [shape, setShape] = useState({coords: {norht: null, south: null, east:null, west: null}, type:'square'})
    const [libraries] = useState(["places"])
    const [animaloptions, setAnimalOptions] = useState([])
    const [responderPresent, setResponderPresent] = useState(false)
    const [sectorOptions, setSectorOptions] = useState([])
    const [sealSizeOption, setSealSizeOption] = useState([])
    const [sexOptions, setSexOptions] = useState([])
    const [howIdOption, setHowIdOption] = useState([])
    const [tagSideOption, setTagSideOption] = useState([])
    const [tagColorOption, setTagColorOption] = useState([])
    const [statusOption, setStatusOption] = useState([])
    const [issueOption, setIssueOption] = useState([])
    const [islandOption, setIslandOption] = useState([])
    const [FASTOption, setFASTOption] = useState([])
    const [locationOption, setLocationOption] = useState([])
    const history = useHistory()

    const SubmitIncident = () => {
        console.log(images)
        let value = `
        mutation add_Incident{
            addIncident(`
        value += `firstName:${JSON.stringify(firstName)}, lastName:${JSON.stringify(lastName)}, phoneNumber:${JSON.stringify(phone)}, email:${JSON.stringify(email)}, location:${JSON.stringify(mapSearch)}, lat:${JSON.stringify(marker.lat)}, lng:${JSON.stringify(marker.lng)}, locationDescription:${JSON.stringify(locationDescription)}, sector:${JSON.stringify(sector.value)}, animalType:${JSON.stringify(animalsType.value)}, animalPresent:${JSON.stringify(animalPresent)}`
        if (sealSize !== null)
        {
            value += `, sealSize:${JSON.stringify(sealSize)}`
        }
        if (sex !== null)
        {
            value += `, sex:${JSON.stringify(sex)}`
        }
        if (landWater !== null)
        {
            value += `, landOrWater:${JSON.stringify(Boolean(landWater))}`
        }
        if (IDedType !== null)
        {
            value += `, howIdentified:${JSON.stringify(IDedType)}`
        }
        if (tagedSide !== null)
        {
            value += `, tagSide:${JSON.stringify(tagedSide)}`
        }
        if (tagColor !== null)
        {
            value += `, tagColor:${JSON.stringify(tagColor)}`
        }
        if (tagNumber !== null)
        {
            value += `, tagNumber:${JSON.stringify(tagNumber)}`
        }
        if (bleachNum !== null)
        {
            value += `, bleachNum:${JSON.stringify(bleachNum)}`
        }
        if (IdPerm !== null)
        {
            value += `, IDPerm:${JSON.stringify(IdPerm)}`
        }
        if (IdDescription !== null)
        {
            value += `, IDNotes:${JSON.stringify(IdDescription)}`
        }
        if (molting !== null)
        {
            value += `, molting:${JSON.stringify(molting)}`
        }
        if (sealLogging !== null)
        {
            value += `, sealLogging:${JSON.stringify(sealLogging)}`
        }
        if (momPup !== null)
        {
            value += `, animalWithBaby:${JSON.stringify(momPup)}`
        }
        if (sealDepart !== null)
        {
            value += `, sealDeparted:${JSON.stringify(sealDepart)}`
        }
        if (SRAName !== null)
        {
            value += `, SRAPerson:${JSON.stringify(SRAName)}`
        }
        if (departDate !== null)
        {
            value += `, dateDeparted:${JSON.stringify(departDate)}`
        }
        if (departTime !== null)
        {
            value += `, timeDeparted:${JSON.stringify(departTime)}`
        }
        if (size !== null)
        {
            value += `, turtleSize:${JSON.stringify(size)}`
        }
        if (FAST !== null)
        {
            value += `, FAST:${JSON.stringify(FAST)}`
        }
        if (status !== null)
        {
            value += `, status:${JSON.stringify(status)}`
        }
        if (issue !== null)
        {
            value += `, issue:${JSON.stringify(issue)}`
        }
        if (delivered !== null)
        {
            value += `, delivered:${JSON.stringify(delivered)}`
        }
        if (deliveryLocation !== null)
        {
            value += `, deliverdLocation:${JSON.stringify(deliveryLocation)}`
        }
        if (outReach !== null)
        {
            value += `, OperatorOutReach:${JSON.stringify(outReach)}`
        }
        if (island !== null)
        {
            value += `, onIsland:${JSON.stringify(island)}`
        }
        if (responderName !== null)
        {
            value += `, responderName:${JSON.stringify(responderName)}`
        }
        if (amountOfResponder !== null)
        {
            value += `, amountOfResponders:${JSON.stringify(amountOfResponder)}`
        }
        if (timeArrived !== null)
        {
            value += `, timeArrived:${JSON.stringify(timeArrived)}`
        }
        if (timeLeft !== null)
        {
            value += `, timeLeft:${JSON.stringify(timeLeft)}`
        }
        value += `, description:${JSON.stringify(description)}, images:${JSON.stringify(images)}){succcesses}}`
        axios({
            url:'/api/',
            method: 'post',
            data: {
                query: value
            }
        }).then((results)=> {
            history.push('/')
            
        })
    }
    const updateFiles = (incomingFiles) => {
        setPicture(incomingFiles)
    };

    const Present = [{value: true, label:'Yes'}, {value: false, label:'No'}]
    const LandWaterOptions = [{value:true, label:'Land'}, {value:false, label:'Water'}]

    const removeFile = (id) => {
        setPicture(pictures.filter((x) => x.id !== id));
    };
    
    const { isLoaded } = useJsApiLoader({
        id: 'google=map-script',
        googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAP_API_KEY,
        libraries: libraries,
    })
    const MapHandling = {
        gestureHandling: 'greedy',
    }

    const containerStyle = {
        width: '100%',
        height: '400px',
    };

    const markerOnLoad = useCallback((marker) => {
        setMarkerMount(marker)
    }, [])


    useEffect(() => {
        if(mapSearch !== 'None'){
            Geocode.setApiKey(process.env.REACT_APP_GOOGLE_MAP_API_KEY);
            Geocode.setLanguage("en");
            Geocode.setRegion("us");
            Geocode.setLocationType("ROOFTOP");
            Geocode.fromAddress(mapSearch).then(
                (response) => {
                    const { lat, lng } = response.results[0].geometry.location;
                    setCenter({
                        lat: lat,
                        lng: lng,
                    });
                    setMarker({
                        lat: lat,
                        lng: lng,
                    })
                    setShape({north: lat+0.0005, south: lat-0.0005, east:lng+0.0005, west: lng-0.0005})
                },
                (error) => {
                }
            );

        }
    }, [mapSearch])
    useEffect(() => {
        const options = {
            enableHighAccuracy: true,
            timeout: 5000,
            maximumAge: 0
        };
        const success = (pos) => {
            var crd = pos.coords;
            setCenter({lat:crd.latitude, lng:crd.longitude});
        }
        const error = (err) => {
        }

        navigator.geolocation.getCurrentPosition(success, error, options);
        function fetchFormData() {
            axios({
                url:'/api/',
                method: 'post',
                data: {
                    query: `
                        query getForm{
                            allSubanimals{
                                subAnimal
                                animal{
                                    animal
                                }
                            }
                            allSectors{
                                observerType
                            }
                            allStatus{
                                options
                            }
                            allDeath{
                                options
                            }
                            allIsland{
                                island
                            }
                            allSealsize{
                                options
                            }
                            allSex{
                                options
                            }
                            allHowId{
                                options
                            }
                            allTagside{
                                options
                            }
                            allTagcolor{
                                options
                            }
                            allFast{
                                options
                            }
                            allLocation{
                                options
                            }
                        }
                    `
                }
            }).then((results)=> {
                let animalTypeData = []
                let Section = []
                let SealSize = []
                let Sex = []
                let HowID = []
                let TagSide = []
                let TagColor = []
                let Status = []
                let Issue = []
                let Island = []
                let fast = []
                let Location = []
                results.data.data.allSubanimals.forEach((obj) => {
                    let interge = true
                    if (animalTypeData.length === 0){
                        animalTypeData.push({label: obj['animal']['animal'], options:[]})
                    }
                    else{
                        animalTypeData.forEach((x) => {
                            if (x.label === obj['animal']['animal']){
                                interge = false
                            }
                        })
                        if(interge){
                            animalTypeData.push({label: obj['animal']['animal'], options:[]})
                        }
                    }
                    animalTypeData.forEach((info) => {
                        if(info['label'] === obj['animal']['animal']){
                            info['options'].push({ value: obj['subAnimal'], label: obj['subAnimal'], family:obj['animal']['animal']})
                        }
                    })
                })
                results.data.data.allSectors.forEach((obj) => {
                    Section.push({value:obj['observerType'], label:obj['observerType']})
                })
                results.data.data.allSealsize.forEach((obj) => {
                    SealSize.push({value: obj['options'], label:obj['options']})
                })
                results.data.data.allSex.forEach((obj) => {
                    Sex.push({value: obj['options'], label:obj['options']})
                })
                results.data.data.allHowId.forEach((obj) => {
                    HowID.push({value: obj['options'], label:obj['options']})
                })
                results.data.data.allTagside.forEach((obj)=>{
                    TagSide.push({value: obj['options'], label:obj['options']})
                })
                results.data.data.allTagcolor.forEach((obj) => {
                    TagColor.push({value: obj['options'], label:obj['options']})
                })
                results.data.data.allStatus.forEach((obj) => {
                    Status.push({value: obj['options'], label:obj['options']})
                })
                results.data.data.allDeath.forEach((obj) => {
                    Issue.push({value: obj['options'], label:obj['options']})
                })
                results.data.data.allIsland.forEach((obj)=>{
                    Island.push({value: obj['island'], label:obj['island']})
                })
                results.data.data.allFast.forEach((obj) => {
                    fast.push({value: obj['options'], label:obj['options']})
                })
                results.data.data.allLocation.forEach((obj) => {
                    Location.push({value: obj['options'], label:obj['options']})
                })
                setAnimalOptions(animalTypeData)
                setSectorOptions(Section)
                setSealSizeOption(SealSize)
                setSexOptions(Sex)
                setHowIdOption(HowID)
                setTagSideOption(TagSide)
                setTagColorOption(TagColor)
                setFASTOption(fast)
                setIslandOption(Island)
                setIssueOption(Issue)
                setStatusOption(Status)
                setLocationOption(Location)
            })
        }
        fetchFormData()
    }, []);
    useEffect(() => {
        if(phone != null || document.getElementById('phoneField') === document.activeElement){
            document.getElementById('phoneLabel').style.transform = "translateY(-4rem) scale(0.8)";
        }
        else{
            document.getElementById('phoneLabel').style.transform = null;
        }
    }, [phone]);

    useEffect(()=>{
        if(phone !== null){
            if(marker !== {lat:null, lng:null}){
                if(firstName !== ''){
                    if(lastName !== ''){
                        if(email !== ''){
                            if(mapSearch !== 'None'){
                                if(pictures.length > 0){
                                    if(description !== ''){
                                        setSubmitQuery(false)
                                    }
                                    else{
                                        setSubmitQuery(true)
                                    }
                                }
                                else{
                                    setSubmitQuery(true)
                                }
                            }
                            else{
                                setSubmitQuery(true)
                            }
                        }
                        else{
                            setSubmitQuery(true)
                        }
                    }
                    else{
                        setSubmitQuery(true)
                    }
                }
                else{
                    setSubmitQuery(true)
                }
            }
            else{
                setSubmitQuery(true)
            }
        }
        else{
            setSubmitQuery(true)
        }
        if (pictures.length > 0){
            let pictured = []
            for(var x = 0; x < pictures.length; x++){
                let Reader = new FileReader();
                Reader.onload = function (event) {
                    let image = pictures.slice();
                    image.push(event.target.result);
                    pictured.push(image[pictures.length])
                    
                };
                Reader.readAsDataURL(pictures[x].file);
            }
            setImages(pictured)
        }
    }, [phone, marker, firstName, lastName, email, mapSearch, pictures, description])

    

    return(
        <div>
            <div className="mt-6 mb-6">
                <Container>
                    <Row>
                        <Col>
                            <div className="field">
                                <input className="input" name="first name" value={firstName} onChange={(event) => {setFirstName(event.target.value)}} type="text" placeholder=" "/>
                                <label for="first name" className="label">First Name</label>
                            </div>
                        </Col>
                        <Col>
                            <div className="field">
                                <input className="input" value={lastName} onChange={(event) => {setLastName(event.target.value)}} name="last name" type="text" placeholder=" "/>
                                <label for="last name" className="label">Last Name</label>
                            </div>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <div id="phoneField" on className="field">
                                <PhoneInput defaultCountry="US" onChange={(x) => {
                                    setPhone(x)
                                }} name="phone number" value={phone} placeholder=" "/>
                                <label for="phone number" id={"phoneLabel"} className="phonelabel">Phone Number</label>
                            </div>
                        </Col>
                        <Col>
                            <div className="field">
                                <input className="input" value={email} onChange={(event) => {setEmail(event.target.value)}} name="email" type="email" placeholder=" "/>
                                <label for="email" className="label">Email</label>
                            </div>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            {isLoaded && <StandaloneSearchBox onPlacesChanged={(value) => {
                            if(document.getElementsByName('Location')[0].value !== '') {
                                setMapSearch(document.getElementsByName('Location')[0].value)
                            }
                            else{
                                setMapSearch('')
                            }
                            }}>
                                <div className="field">
                                    <input className="input" name="Location" type="text" placeholder=" "/>
                                    <label for="Location" className="label">Location</label>
                                </div>
                            </StandaloneSearchBox>}
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <div className="field more-border">
                                <textarea className="input" value={locationDescription} onChange={(event) => {setLocationDescription(event.target.value)}} name="LocationDes" placeholder=" "/>
                                <label for="LocationDes" className="label">Location Description...</label>
                            </div>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            {isLoaded && <GoogleMap
                            mapContainerStyle={containerStyle}
                            center={center}
                            zoom={15}
                            options={MapHandling}>
                                <Marker position={marker} draggable={true} onLoad={markerOnLoad} onDragEnd={()=>{
                                    setMarker({lat: markerMount.position.lat(), lng: markerMount.position.lng()})
                                    setShape({north: markerMount.position.lat()+0.0005, south: markerMount.position.lat()-0.0005, east:markerMount.position.lng()+0.0005, west: markerMount.position.lng()-0.0005})
                                    }}/>
                                <Rectangle onload bounds={shape}/>
                            </GoogleMap>}
                        </Col>
                    </Row>
                    <Row className="mt-5 mb-5">
                        <Col>
                            <Select className="bringUp5" options={sectorOptions} onChange={(info)=>setSector(info)} name="animal" placeholder="Sector" />
                        </Col>
                        <Col>
                            <div>
                                <Select className="bringUp5" options={animaloptions} name="animal" onChange={(info)=>setAnimalsType(info)} placeholder="Animal Type..." />
                            </div>
                        </Col>
                        <Col>
                            <div>
                                <Select className="bringUp5" options={Present} onChange={(info)=>{setAnimalPresent(info.value)}} name="animal" placeholder="Animal Present" />
                            </div>
                        </Col>
                    </Row>
                    {animalsType.family === 'Seal' && 
                        <div>
                            <Row className="mb-5">
                                <Col>
                                    <Select className="bringUp4" options={sealSizeOption} onChange={(info)=>{setSealSize(info.value)}} name="animal" placeholder="Seal Size" />
                                </Col>
                                <Col>
                                    <Select className="bringUp4" options={sexOptions} onChange={(info)=>{setSex(info.value)}} name="animal" placeholder="Sex" />
                                </Col>
                                <Col>
                                    <Select className="bringUp4" options={LandWaterOptions} onChange={(info)=>{setLandwater(info.value)}} name="animal" placeholder="On Land or Water" />
                                </Col>
                            </Row>
                            <Row>
                                <Col>
                                    <Select className="bringUp3" options={howIdOption} onChange={(info)=>{setIdType(info.value)}} name="animal" placeholder="How Identified" />
                                </Col>
                                {IDedType === 'Tag' &&
                                <Col>
                                    <Select className="bringUp3" options={tagSideOption} onChange={(info)=>{setTagedSide(info.value)}} name="animal" placeholder="Tag Side" />
                                </Col>}
                                {IDedType === 'Tag' &&
                                <Col>
                                    <Select className="bringUp3" options={tagColorOption} onChange={(info)=>{setTagColor(info.value)}} name="animal" placeholder="Tag Color" />
                                </Col>}
                            </Row>
                            <Row>
                                {IDedType === 'Tag' &&
                                <Col>
                                    <div className="field">
                                        <input className="input" value={tagNumber} onChange={(event) => {setTagNumber(event.target.value)}} name="TagNumber" type="text" placeholder=" "/>
                                        <label for="TagNumber" className="label">Tag Number</label>
                                    </div>
                                </Col>}
                                {IDedType === 'Applied bleach' &&
                                <Col>
                                    <div className="field">
                                        <input className="input" value={bleachNum} onChange={(event) => {setBleachNum(event.target.value)}} name="BleachNum" type="text" placeholder=" "/>
                                        <label for="BleachNum" className="label">ID Temp (Bleach#)</label>
                                    </div>
                                </Col>}
                            </Row>
                            <Row>
                                <Col>
                                    <div className="field">
                                        <input className="input" value={IdPerm} onChange={(event) => {setIdPerm(event.target.value)}} name="IDPerm" type="text" placeholder=" "/>
                                        <label for="IDPerm" className="label">ID Perm</label>
                                    </div>
                                </Col>
                                <Col>
                                    <div className="field">
                                        <input className="input" value={IdDescription} onChange={(event) => {setIdDescription(event.target.value)}} name="IDNotes" type="text" placeholder=" "/>
                                        <label for="IDNotes" className="label">Additional Notes on ID</label>
                                    </div>
                                </Col>
                            </Row>
                            <Row className="mb-5">
                                <Col>
                                    <Select className="bringUp2" options={Present} onChange={(event) => {setMolting(event.value)}}name="animal" placeholder="Molting" />
                                </Col>
                                <Col>
                                    <Select className="bringUp2" options={Present} onChange={(event)=>{setSealLogging(event.value)}} name="animal" placeholder="Seal Logging" />
                                </Col>
                                <Col>
                                    <Select className="bringUp2" options={Present} onChange={(event)=>{setMomPup(event.value)}} name="animal" placeholder="Mom and Pup pair"/>
                                </Col>
                            </Row>
                            <Row className="mb-5">
                                <Col>
                                    <Select className="bringUp1" options={Present} onChange={(event)=>{setSRASetUp(event.value)}} name="animal" placeholder="SRA Set up"/>
                                </Col>
                                <Col>
                                    <Select className="bringUp1" options={Present} onChange={(event)=>{setSealDepart(event.value)}} name="animal" placeholder="Seal Departed"/>
                                </Col>
                            </Row>
                            <Row>
                                {SRASetUp && <Col>
                                    <div className="field">
                                        <input className="input" value={SRAName} onChange={(event) => {setSRAName(event.target.value)}} name="SetUp" type="text" placeholder=" "/>
                                        <label for="SetUp" className="label">SRA Set Up By</label>
                                    </div>
                                </Col>}
                                {sealDepart && <Col>
                                    <div className="field">
                                        <input className="input" value={departDate} onChange={(event) => {setDepartDate(event.target.value)}} name="dateDeparted" type="date" placeholder=" "/>
                                        <label for="dateDeparted" className="label">Date Departed</label>
                                    </div>
                                </Col>}
                                {sealDepart && <Col>
                                    <div className="field">
                                        <input className="input" value={departTime} onChange={(event) => {setDepartTime(event.target.value)}} name="TimeDeparted" type="time" placeholder=" "/>
                                        <label for="TimeDeparted" className="label">Time Departed</label>
                                    </div>
                                </Col>}
                            </Row>
                        </div>
                    }
                    {animalsType.family === 'Sea Turtle' && 
                        <div>
                            <Row>
                                <Col>
                                    <div className="field">
                                        <input className="input" value={size} onChange={(event) => {setSize(event.target.value)}} name="tutleSize" type="number" placeholder=" "/>
                                        <label for="tutleSize" className="label">Size of tutle(in Feet)</label>
                                    </div>
                                </Col>
                            </Row>
                            <Row className="mb-5">
                                <Col className="mb-1" md={12} lg={3}>
                                    <Select className="bringUp1" options={statusOption} onChange={(event) => {setStatus(event.value)}} name="animal" placeholder="Status"/>
                                </Col>
                                <Col className="mb-1" md={12} lg={3}>
                                    <Select className="bringUp" options={issueOption} onChange={(event) => {setIssue(event.value)}} name="animal" placeholder="Issue or Cause of Death"/>
                                </Col>
                                <Col className="mb-1" md={12} lg={3}>
                                    <Select className="bringUp-1" options={islandOption} onChange={(event) => {setIsland(event.value)}} name="animal" placeholder="On What Island" />
                                </Col>
                                <Col className="mb-1" md={12} lg={3}>
                                    <Select className="bringUp-2" options={FASTOption} onChange={(event) => {setFAST(event.value)}} name="animal" placeholder="F.A.S.T" />
                                </Col>
                            </Row>
                        </div>
                        
                    }
                    {animalsType.family === 'Sea Birds' && 
                        <div>
                            <Row>
                                <Col>
                                    <Select className="bringUp1" options={Present} onChange={(event)=>{setDeleivered(event.value)}} name="animal" placeholder="Delivered"/>
                                </Col>
                                {delivered && <Col>
                                    <Select className="bringUp1" options={locationOption} onChange={(event)=>{setDeliveryLocation(event.value)}} name="animal" placeholder="Delivered"/>
                                </Col>}
                            </Row>
                            <Row className="mb-5">
                                
                            </Row>
                        </div>
                    }
                    <Row>
                        <Col>
                            <div>
                                <Select className="bringUp-3" options={Present} name="VolunteerPresent" onChange={(info)=>setResponderPresent(info.value)} placeholder="Responders/Volunteers Present" />
                            </div>
                        </Col>
                        <Col>
                            <div>
                                <Select className="bringUp-3" options={Present} onChange={(event)=>{setOutReach(event.value)}} name="animal" placeholder="OutReach Provided by Operator" />
                            </div>
                        </Col>
                    </Row>
                    {responderPresent && 
                        <div>
                            <Row>
                                <Col>
                                    <div className="field">
                                        <input className="input" value={responderName} onChange={(event) => {SetResponderName(event.target.value)}} name="ResponderName" type="text" placeholder=" "/>
                                        <label for="ResponderName" className="label">Responders Name</label>
                                    </div>
                                </Col>
                                <Col>
                                    <div className="field">
                                        <input className="input" value={amountOfResponder} onChange={(event) => {setAmountOfResponder(event.target.value)}} name="Amount of Volunteer / Responders" type="number" placeholder=" "/>
                                        <label for="Amount of Volunteer / Responders" className="label">Amount of Responders</label>
                                    </div>
                                </Col>
                            </Row>
                            <Row>
                                <Col>
                                    <div className="field">
                                        <input className="input" value={timeArrived} onChange={(event) => {setTimeArrived(event.target.value)}} name="TimeArrived" type="time" placeholder=" "/>
                                        <label for="TimeArrived" className="label">Time Arrived</label>
                                    </div>
                                </Col>
                                <Col>
                                    <div className="field">
                                        <input className="input" value={timeLeft} onChange={(event) => {setTimeLeft(event.target.value)}} name="TimeLeft" type="time" placeholder=" "/>
                                        <label for="TimeLeft" className="label">Time Left</label>
                                    </div>
                                </Col>
                            </Row>
                        </div>
                    }
                    <Row>
                        <Col>
                            <div className="field more-border">
                                <textarea className="input" value={description} onChange={(event) => {setDescription(event.target.value)}} name="MoreInfo" placeholder=" "/>
                                <label for="MoreInfo" className="label">Description ...</label>
                            </div>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <Dropzone accept={'image/\*'} style={{ minWidth: "500px" }} onChange={updateFiles} value={pictures}>
                                {pictures.map((picture, key)=>{
                                    return(<FileItem {...picture} onDelete={removeFile} preview info key={picture.id}/>)
                                })}
                            </Dropzone>
                        </Col>
                    </Row>
                </Container>
            </div>
            <Navbar fixed="bottom" bg="light">
                <Container>
                    <h4>When finished you will be allowed to click Submit</h4>
                    <Nav className="ms-auto">
                        <Button className="float-right" onClick={()=>SubmitIncident()} disabled={submitQuery} variant="success">Submit</Button>
                    </Nav>
                </Container>
            </Navbar>
        </div>
    )
}

export default FileReport;