import 'bootstrap/dist/css/bootstrap.min.css';
import {Container} from 'react-bootstrap';
import Header from './components/header';
import Main from './components/main';
import { BrowserRouter } from 'react-router-dom';

function App() {

  return (
    <BrowserRouter>
    <Container fluid>
      <Header/>
      <Main/>
    </Container>
    </BrowserRouter>

  )
}

export default App
