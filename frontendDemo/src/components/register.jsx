import { Button, Col, Container, Form, Row } from "react-bootstrap"
import { useState } from "react";
import {userStore} from '../stores/UserStore';
import {observer} from 'mobx-react';
import { useNavigate } from "react-router-dom";
const Register = observer(()=>{
    const navigate = useNavigate();
    const [data,setData] = useState({
        username:'',
        email:'',
        password:''
    });
    const handleChange = (ev)=>{
        const {name,value} = ev.target;
        setData(prevState=>({
            ...prevState,
            [name]:value
        }));
    }

    const submitForm = async (ev)=>{
        ev.preventDefault();
        if(await userStore.addUser(data)){
            navigate('/login');
        }
    }
    return(
        <Container>
            <h1>Регистрация</h1>
            <Form onSubmit={submitForm}>
            <Form.Group>
                    <Form.Label>Логин</Form.Label>
                    <Form.Control type="text" name="username" value={data.username} onChange={handleChange}/>
                </Form.Group>
                <Form.Group>
                    <Form.Label>Почта</Form.Label>
                    <Form.Control type="text" name="email" value={data.email} onChange={handleChange}/>
                </Form.Group>
                <Form.Group>
                    <Form.Label>Пароль</Form.Label>
                    <Form.Control type="password" name="password" value={data.password} onChange={handleChange}/>
                </Form.Group>
                <Row>
                    <Col md={6}>
                        <Button variant="success" type="submit">Зарегаться</Button>
                    </Col>
                </Row>
            </Form>
        </Container>
    )
})
export default Register;