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
        }
    }
    async profileUser(){
        try {
            const response = await UserService.profile();
            console.log(response);
        } catch (error) {
            
        }
    }
    async loginUser(data){
        try {
            const response = await UserService.login(data);
            const { access, refresh } = response.data.tokens;

            localStorage.setItem('accessToken', access);
            localStorage.setItem('refreshToken', refresh);
            
            console.log(localStorage);
            // const [cookies, setCookie, removeCookie] = useCookies(['cookie-name']);
            
        } catch (error) {
            
        }
    }
    logout(){
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
    }
}
export let userStore = new UserStore();