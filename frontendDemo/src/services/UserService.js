import axios from 'axios';

export default class UserService{
    static async create(data){
        try {
            const response = await axios.post('/api/auth/register/',data);
            return response;
        } catch (error) {
            console.log(error);
        }
    }
    static async login(data){
        try {
            const response = await axios.post('/api/auth/login/',data);
            return response;
        } catch (error) {
            console.log(error);
        }
    }
    static async profile(){
        try {
            const response = await axios.post('/api/auth/profile/',{
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                },
            });
            console.log(response);
            return response;
        } catch (error) {
            console.log(error);
        }
    }
}