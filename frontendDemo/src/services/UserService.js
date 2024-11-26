import axios from 'axios';

export default class UserService{
    static async refreshToken() {
        try {
            const refreshToken = localStorage.getItem('refreshToken');
            if (!refreshToken) {
                console.error("Refresh token отсутствует.");
                return null;
            }

            const response = await axios.post('/api/auth/token/refresh/', {
                refresh: refreshToken,
            });
            console.log(response.data);
            const { access } = response.data;
            localStorage.setItem('accessToken', access);
            return access;
        } catch (error) {
            console.error("Ошибка обновления токена:", error.response?.data || error.message);
            return null;
        }
    }
    static async create(data){
        try {
            const response = await axios.post('/api/auth/register/',data);
            return response;
        } catch (error) {
            console.log(error.response.data.message);
        }
    }
    static async login(data){
        try {
            const response = await axios.post('/api/auth/login/',data);
            return response;
        } catch (error) {
            console.log(error.response.data.message);
        }
    }
    static async profile() {
        try {
            const response = await axios.get('/api/auth/profile/', {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                }
            });
            console.log(response.data);
            return response.data;
        } catch (error) {
            console.error(error.response.data.message);
            if (error.response.status === 401) {
                console.error('Требуется повторный вход в систему');
            }
        }
    }
}