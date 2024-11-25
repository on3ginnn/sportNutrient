import {makeAutoObservable} from 'mobx';
import UserService from '../services/UserService';

class UserStore{
    isAuth = localStorage.getItem('auth') || false;
    token = localStorage.getItem('accessToken') || '';
    constructor(){
        makeAutoObservable(this);
    }
    async addUser(data){
        try {
            const response = await UserService.create(data);
            console.log(response);
        } catch (error) {
            console.log(error);
        }
    }
    async profileUser(data){
        try {
            const response = await UserService.profile(data);
            console.log(response);
        } catch (error) {
            console.log(error);
        }
    }
    async loginUser(data){
        try {
            const response = await UserService.login(data);
            localStorage.setItem('accessToken',response.data.tokens.refresh);
            localStorage.setItem('auth',true);
            
            console.log(localStorage)
            // const [cookies, setCookie, removeCookie] = useCookies(['cookie-name']);
            
        } catch (error) {
            console.log(error);
        }
    }
    logout(){
        localStorage.removeItem('accessToken');
        localStorage.removeItem('auth');
    }
}
export let userStore = new UserStore();