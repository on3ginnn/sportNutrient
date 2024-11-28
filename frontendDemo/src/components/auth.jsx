import { Button, Col, Container, Form, Row } from "react-bootstrap"
import { useState } from "react";
import {userStore} from '../stores/UserStore';
import {observer} from 'mobx-react';
import { useNavigate } from "react-router-dom";
const Auth = observer(()=>{
    const [data,setData] = useState({
        username:'',
        password:''
    });
    const navigate = useNavigate();
    const handleChange = (ev)=>{
        const {name,value} = ev.target;
        setData(prevState=>({
            ...prevState,
            [name]:value
        }));
    }

    const submitForm = async (ev)=>{
        ev.preventDefault();
        await userStore.loginUser(data).then(()=>{
            navigate('/profile');
        });

    }
    return(
        <Container>
            <h1>Авторизация</h1>
            <Form onSubmit={submitForm}>
                <Form.Group>
                    <Form.Label>Логин</Form.Label>
                    <Form.Control type="text" name="username" value={data.username} onChange={handleChange}/>
                </Form.Group>
                <Form.Group>
                    <Form.Label>Пароль</Form.Label>
                    <Form.Control type="password" name="password" value={data.password} onChange={handleChange}/>
                </Form.Group>
                <Row>
                    <Col md={6}>
                        <Button variant="success" type="submit">Авторизация</Button>
                    </Col>
                </Row>
            </Form>
        </Container>
    )
})
export default Auth;