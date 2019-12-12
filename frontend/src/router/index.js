import Vue from 'vue'
import VueRouter from 'vue-router'
import Auth from '@/components/pages/Auth'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router