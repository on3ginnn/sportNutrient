import { Button, Nav, Navbar } from "react-bootstrap"
import { Link, useNavigate } from "react-router-dom";
import { authRoutes, publicRoutes } from "../config/routes";
import { observer } from "mobx-react";
import { userStore } from "../stores/UserStore";
import {motion} from 'framer-motion';
const Header = observer(() => {
    const navigate = useNavigate();
    const logout = ()=>{
        userStore.logout();
            navigate('/login');
    }
    return (
        <Navbar bg="dark" variant="dark" className="p-2 mb-2">
            <Navbar.Brand>
                <motion.h1 initial={{opacity:0}} animate={{opacity:1}} transition={{duration:.8}}>Это лого</motion.h1>
                </Navbar.Brand>
            <Nav className="ms-auto">
                {
                    userStore.accessToken.length!=0 &&

                        authRoutes.map((el, i) => <Nav.Link key={i} as={Link} to={el.path}>{el.name}</Nav.Link>) && <Button variant="danger" onClick={logout}>Выйти</Button>
                }
                        
                {userStore.accessToken.length==0 && publicRoutes.map((el, i) => <Nav.Link key={i} as={Link} to={el.path}>{el.name}</Nav.Link>)}
            </Nav>
        </Navbar>
    )
})
export default Header;