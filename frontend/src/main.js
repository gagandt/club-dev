import Vue from 'vue';
import App from './App.vue';
import Vuetify from "vuetify";
import vuetify from './plugins/vuetify';
import "vuetify/dist/vuetify.min.css";
import router from './router';
import VueSession from 'vue-session';
import axios from 'axios';
import VueSweetalert2 from '../node_modules/vue-sweetalert2';


Vue.config.productionTip = false;
Vue.use(Vuetify);
Vue.use(VueSession);
Vue.use(VueSweetalert2);


const base = axios.create({
  baseURL: 'http://localhost:8000'
});

Vue.prototype.$http = base;

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app');
