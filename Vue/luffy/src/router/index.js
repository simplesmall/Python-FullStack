import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)
import Home from '@/components/Home/Home'

export default new Router({
  // 路由组件使用
  //1.创建路由组件  2,配置路由信息  3,在router-link中使用
  routes: [
    {
      path:'/',
      redirect:{name:"Home"}
    },
    {
      path:'/home',
      name:'Home',
      component: Home
    },
  ]
})
