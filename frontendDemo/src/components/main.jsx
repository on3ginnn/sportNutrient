import {Routes,Route} from 'react-router-dom';
import { authRoutes, publicRoutes } from '../config/routes';
import { observer } from 'mobx-react';
import { userStore } from '../stores/UserStore';

const Main = observer(()=>{

    return(
        <Routes>
            {!userStore.isAuth && publicRoutes.map((el,i)=><Route key={i} path={el.path} Component={el.component}/>)}
            {userStore.isAuth && authRoutes.map((el,i)=><Route key={i} path={el.path} Component={el.component}/>)}
        </Routes>
    )
})
export default Main;