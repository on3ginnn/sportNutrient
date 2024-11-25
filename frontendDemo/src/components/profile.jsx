import { Alert, Container } from "react-bootstrap"
import {userStore} from '../stores/UserStore';
import {observer} from 'mobx-react';

const Profile = observer(()=>{
    return(
        <Container>
            { userStore.token }
            { userStore.profileUser() }
        </Container>
    )
})
export default Profile;