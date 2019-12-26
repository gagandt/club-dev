import Vue from 'vue'
import VueRouter from 'vue-router'
import Auth from '@/views/Auth'

import Events from '@/views/Events.vue'
import About from '@/views/About.vue'

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
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
