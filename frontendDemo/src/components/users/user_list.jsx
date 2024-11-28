import { Alert, Container } from "react-bootstrap"
import {userStore} from '../../stores/UserStore';
import {observer} from 'mobx-react';
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const UserList = observer(()=>{
    const navigate = useNavigate();

    const [users,setUsers] = useState();

    useEffect(() => {
        async function fetchUser(){
            await userStore.userList().then(res=>{
                console.log(res);
                // для выхода в случае если пользователь не аутентифицирован
                if (res === undefined) {
                    userStore.logout();
                    navigate("/login");
                }
                console.log(res.status);
                setUsers(res);
            });
        }
        fetchUser();
        console.log(users);

    }, [])
    return(
        <Container>
            {
                console.log(users)
            }


        </Container>
    )
})
export default UserList;