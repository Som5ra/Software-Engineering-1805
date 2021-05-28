import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'
import router from './router'
import './assets/css/reset.css'
import './assets/fonts/iconfont.css'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import axios from 'axios'
Vue.prototype.axios = axios;
axios.interceptors.request.use(config=>{
  config.headers.Authorization=window.sessionStorage.getItem('token')
  return config
})
Vue.config.productionTip = false

Vue.use(ElementUI);



 
const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)

}

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
