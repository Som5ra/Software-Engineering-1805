import Vue from 'vue'
import Router from 'vue-router'
import VueRouter from 'vue-router'
import Login from './views/Login.vue'
import Home from './views/Home.vue'
import List from './components/list.vue'
import Mvideo from './components/mvideo.vue'
import Museum from './components/museum.vue'
import News from './components/news.vue'
import Evideo from './components/evideo.vue'
import Cvideo from './components/cvideo.vue'
import Exhibition from './components/exhibition.vue'
import Score from './components/score.vue'
import Collection from './components/collection.vue'
import Updown from './components/updown.vue'
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {path:'/',redirect:'/login'
    },
    {path:'/login',component:Login
    },
    {
      path:'/home',component:Home,
      children: [
        {path:'/list',component:List},
        {path:'/mvideo',component:Mvideo},
        {path:'/museum',component:Museum},
        {path:'/news',component:News},
        {path:'/evideo',component:Evideo},
        {path:'/cvideo',component:Cvideo},
        {path:'/exhibition',component:Exhibition},
        {path:'/score',component:Score},
        {path:'/collection',component:Collection},
        {path:'/updown',component:Updown}
      ]
    }
  ]
})
//挂载路由导航守卫
router.beforeEach((to,from,next)=>{
  //to将要访问的路径
  //from代表从哪个路径跳转来
  //next是一个函数，表示放行
  if(to.path==='/login') return next()
  const tokenstr = window.sessionStorage.getItem('token')
  if(!tokenstr) return next('/login')
  next()
})
export default router