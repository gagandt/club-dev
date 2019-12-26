import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Auth from '@/components/pages/Auth'
import AddSong from '@/components/pages/AddSong'
import Events from '@/views/Events.vue'
import GetSong from '@/components/pages/GetSong'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/events',
    name: 'Events',
    component: Events
  },
  {
    path: '/song',
    name: 'AddSong',
    component: AddSong
  },
  {

    path: '/getsong',
    name: 'GetSong',
    component: GetSong
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
