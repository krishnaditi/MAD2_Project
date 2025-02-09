import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import HelloWorld from '../components/HelloWorld.vue'
import RegisterPage from '../components/RegisterPage.vue'

const routes = [
    {
        path: '/',
        name: 'HelloWorldPage',
        component: HelloWorld
    },

    {
        path: '/login',
        name: 'LoginPage',
        component: LoginPage
    },

    {
        path: '/register',
        name: 'RegisterPage',
        component: RegisterPage
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router