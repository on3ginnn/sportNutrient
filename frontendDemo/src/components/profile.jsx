import { Alert, Container } from "react-bootstrap"
import {userStore} from '../stores/UserStore';
import {observer} from 'mobx-react';
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Profile = observer(()=>{
    const navigate = useNavigate();

    const [user,setUser] = useState();
    // использовать useEffect для запроса один раз при подгрузке страницы
    useEffect(() => {
        async function fetchUser(){
            await userStore.profileUser().then(res=>{
                console.log(res);
                // для выхода в случае если пользователь не аутентифицирован
                if (res === undefined) {
                    userStore.logout();
                    navigate("/login");
                }
                console.log(res.status);
                setUser(res);
            });
        }
        fetchUser();
        console.log(user);

    }, [])
    return(
        <Container>
            {
                console.log(user)
            }

            {/* ожидание подгрузки */}
            {
                !user ? (<p>Loading...</p>) : (<div>
                    <p>{user.username}</p>
                    <p>{user.email}</p>
                </div>)
            }
        </Container>
    )
})
export default Profile;