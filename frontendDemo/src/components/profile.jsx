import { Alert, Container } from "react-bootstrap"
import {userStore} from '../stores/UserStore';
import {observer} from 'mobx-react';

const Profile = observer(()=>{
    // использовать useEffect для запроса один раз при подгрузке страницы
    const userData = () =>{
        userStore.profileUser();
    }
    return(
        <Container>
            { userStore.token }
            { userData() }
        </Container>
    )
})
export default Profile;