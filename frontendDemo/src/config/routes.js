import Home from "../components/home";
import Register from "../components/register";
import Auth from "../components/auth";
import Profile from "../components/profile";
import UserList from "../components/users/user_list";
import AddCategory from "../components/categories/add_category";
import Categories from "../components/categories/categories";

export const publicRoutes = [
    {
        name:'Главная',
        path:'/',
        component:Home
    },
    {
        name:'Добавление категории',
        path:'/addcategory',
        component:AddCategory
    },
    {
        name:'Категории',
        path:'/categories',
        component:Categories
    },
    {
        name:'Регистрация',
        path:'/register',
        component:Register
    },
    {
        name:'Авторизация',
        path:'/login',
        component:Auth
    }

];
export const authRoutes = [
    {
        name:'Профиль',
        path:'/profile',
        component:Profile
    },
    {
        name:'Пользователи',
        path:'/users',
        component:UserList
    }
];