import { Container, Row, Col, Form, Button } from "react-bootstrap"
import { useState } from "react";
import axios from "axios";
const AddCategory = ()=>{
    const [name,setName] = useState('');
    const submitForm =  async (ev)=>{
        ev.preventDefault();
        await axios.post('/api/category/create',{name:name})
        .then(res=>console.log(res.data));
    }
    return(
        <Container>
            <h1>Добавление категории</h1>
            <Form onSubmit={submitForm}>
                <Form.Group>
                    <Form.Label>Название</Form.Label>
                    <Form.Control type="text" value={name} onChange={(ev)=>setName(ev.target.value)}/>
                </Form.Group>
                <Row>
                    <Col md={6}>
                        <Button variant="success" type="submit">Добавить</Button>
                    </Col>
                </Row>
            </Form>
        </Container>
    )
}
export default AddCategory;