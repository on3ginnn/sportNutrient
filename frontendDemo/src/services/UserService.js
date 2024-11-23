import axios from 'axios';

export default class UserService{
    static async create(data){
        try {
            const response = await axios.post('/api/user/create',data);
            return response;
        } catch (error) {
            console.log(error);
        }
    }
    static async login(data){
        try {
            const response = await axios.post('/api/user/login',data);
            return response;
        } catch (error) {
            console.log(error);
        }
    }
}