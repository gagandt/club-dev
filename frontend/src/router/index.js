import Vue from 'vue'
import VueRouter from 'vue-router'
import Auth from '@/components/pages/Auth'

import Events from '@/views/Events.vue'

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
  },
  {
    path: '/events',
    name: 'Events',
    component: Events
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
