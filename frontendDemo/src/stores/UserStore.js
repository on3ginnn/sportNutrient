import {makeAutoObservable} from 'mobx';
import UserService from '../services/UserService';

class UserStore{
    isAuth = localStorage.getItem('auth') || false;
    token = localStorage.getItem('token') || '';
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
    async loginUser(data){
        try {
            const response = await UserService.login(data);
            localStorage.setItem('token',response.data.token);
            localStorage.setItem('auth',true);
            console.log(response);
        } catch (error) {
            console.log(error);
        }
    }
    logout(){
        localStorage.removeItem('token');
        localStorage.removeItem('auth');
    }
}
export let userStore = new UserStore();