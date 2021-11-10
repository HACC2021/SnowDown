import React, {useState, useEffect, useCallback, useMemo} from 'react';
import {useHistory, useLocation } from 'react-router-dom';
import {GoogleMap, useJsApiLoader, Marker, Rectangle} from '@react-google-maps/api';
import { LinkContainer } from 'react-router-bootstrap';
import {Container, Row, Col, Table, Pagination} from 'react-bootstrap';
import Filter from 'react-searchable-filter';
import axios from "axios";
import './Home.scss';
import 'react-searchable-filter/dist/index.css';


const Home = () => {

    const [Reoprts, setReports] = useState([])
    const [subAnimal, setSubAnimal] = useState([])
    const [animal, setAnimal] = useState([])
    const [filter, setFilter] = useState({})
    const [, setMarkerMount] = useState()
    const history = useHistory()
    const { search } = useLocation();
    const [pagNum, setPagNum] = useState([])
    const [currentPag, setCurrentPag] = useState(String(1))
    const query = useMemo(() => new URLSearchParams(search), [search]);
    const pag = query.get("pagination")


    useEffect(() => {
        if(!pag){
            history.push('/user?pagination=1')
        }
        if(pag){
            setCurrentPag(pag)
        }
        let queryed = `query data{
            PaginatedReport(pagination:${JSON.stringify(String(currentPag))}`
        if (filter.StartDate){
            queryed += `, StartDate:${JSON.stringify(filter.StartDate)}`
        }
        if (filter.EndDate){
            queryed += `, EndDate:${JSON.stringify(filter.EndDate)}`
        }
        if (filter.TicketNumber){
            queryed += `, TicketNumber:${JSON.stringify(filter.TicketNumber)}`
        }
        if (filter.Animal){
            queryed += `, Animal:${JSON.stringify(filter.Animal)}`
        }
        if (filter.SpecificAnimal){
            queryed += `, SpecificAnimal:${JSON.stringify(filter.SpecificAnimal)}`
        }
        queryed += `){
            paginationNum
            AmountOfPagination
            data{
              Date
              Time
              TicketNumber
              location
              lat
              lng
              Top
              Bottom
              Left
              Right
              animalType{
                subAnimal
                acronym
              }
            }
          }
          allSubanimals{
              subAnimal
          }
          allAnimals{
              animal
          }
        }`
        axios({
            url:'/api/',
            method: 'post',
            data: {
                query: queryed
            }
        }).then((results) => {
            let Animal = []
            let subAnimal = []
            results.data.data.allAnimals.forEach((x)=>{
                Animal.push(x.animal.replace(/ /g, ""))
            })
            results.data.data.allSubanimals.forEach((x)=>{
                subAnimal.push(x.subAnimal.replace(/ /g, ""))
            })
            setReports(results.data.data.PaginatedReport.data)
            setSubAnimal(subAnimal)
            setAnimal(Animal)
            let Pagen = []
            for (var i = 0; i<results.data.data.PaginatedReport.AmountOfPagination; i++){
                let b = i+1
                Pagen.push(b)
            }
            console.log(Pagen)
            setPagNum(Pagen)
        })
    }, [query, history, currentPag, filter])
    const submitHandler = (x) => {
        let filterData = {}
        x.forEach((x) => {
            filterData[x.filterBy]=x.values[0]
        })
        setFilter(filterData)
    }
    const [libraries] = useState(["places"])

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
        height: '600px',
    };
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
        {
            filterBy: 'TicketNumber',
            values: [],
            description: 'Ticket number of incident'
        },
        {
            filterBy: 'Animal',
            values: animal,
            description: 'Filter by animal'
        },
        {
            filterBy: 'SpecificAnimal',
            values: subAnimal,
            description: 'Filter by Specific animal'
        },
    ]
    const markerOnLoad = useCallback((marker) => {
        setMarkerMount(marker)
    }, [])
    const [center] = useState({lat: 21.439542579000033, lng:-157.94363192999998});
    return(
        <Container>
            <Row>
                <Col>
                {isLoaded && <GoogleMap
                    mapContainerStyle={containerStyle}
                    center={center}
                    zoom={7}
                    options={MapHandling}>
                        {Reoprts.map((info)=>{
                            console.log('yelp')
                            return(
                                <div>
                                    <Marker position={{lat:parseFloat(info.lat), lng:parseFloat(info.lng)}} onClick={()=>{history.push("/user/report/"+info.TicketNumber)}} onLoad={markerOnLoad}/>
                                    <Rectangle onClick={()=>{history.push("/user/report/"+info.TicketNumber)}} onload bounds={{north:parseFloat(info.Top), south:parseFloat(info.Bottom), east:parseFloat(info.Right), west:parseFloat(info.Left)}}/>
                                </div>
                            )
                        })}
                    </GoogleMap>}
                </Col>
            </Row>
            <Row>
                <Col className='Filter'>
                    <Filter options={data} onSubmit={submitHandler} placeholder='Filter Reports'/>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Table striped bordered hover size="sm">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Time</th>
                                <th>Ticket Number</th>
                                <th>Location</th>
                                <th>Animal</th>
                            </tr>
                        </thead>
                        <tbody>
                            {Reoprts.map((data)=>{
                                return(
                                    <LinkContainer to={"/user/report/"+data.TicketNumber}>
                                        <tr>
                                            <td>{data.Date}</td>
                                            <td>{data.Time}</td>
                                            <td>{data.TicketNumber}</td>
                                            <td>{data.location}</td>
                                            <td>{data.animalType.subAnimal}</td>
                                        </tr>
                                    </LinkContainer>
                                )
                            })}
                        </tbody>
                    </Table>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Pagination>
                        {pagNum.map((x)=>{
                            console.log(currentPag)
                            return(
                            <LinkContainer to={"/user?pagination="+x}>
                                <Pagination.Item key={x} active={String(x)===String(currentPag)}>
                                    {x}
                                </Pagination.Item>
                            </LinkContainer>)
                        })}
                    </Pagination>
                </Col>
            </Row>
        </Container>
    )
}

export default Home;