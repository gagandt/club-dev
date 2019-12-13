import Vue from 'vue'
import App from './App.vue'
import Vuetify from "vuetify";
import vuetify from './plugins/vuetify';
import "vuetify/dist/vuetify.min.css";
import router from './router'
import VueSession from 'vue-session'

Vue.config.productionTip = false
Vue.use(Vuetify);
Vue.use(VueSession)

import axios from 'axios'

const base = axios.create({
  baseURL: 'http://localhost:8000'
})

Vue.prototype.$http = base

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
