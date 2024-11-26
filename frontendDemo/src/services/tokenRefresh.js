import axios from 'axios';
import AuthService from './UserService';

// Создаем экземпляр Axios
const api = axios.create({
    baseURL: '/api',
});

// Перехватчик для обработки ошибок авторизации
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            try {
                // Обновляем accessToken
                const newAccessToken = await AuthService.refreshToken();
                originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
                return api.request(originalRequest);
            } catch (err) {
                console.error('Не удалось обновить токен:', err.message);
                AuthService.logout();
            }
        }

        return Promise.reject(error);
    }
);

export default api;