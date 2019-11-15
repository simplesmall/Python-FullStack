<template>
  <div class="a">
    <h2>我是首页</h2>
    <!--    用子-->
    <!--    <Son />-->

    <Son title="静态的方式传值到子组件" @handler='handleClick'/>
    <hr>
    <Son :msg='msg'/>

    <button @click="bushandler">通过BUS传值</button>
    {{ getCount }}
  </div>
</template>

<script>
  // 局部组件的使用:  声子 挂子  用子
  import Son from './Son'   //在Son.vue中声子
  export default {
    name: "Home",
    data() {
      return {
        msg: "父组件动态传值"
      }
    },
    methods: {
      handleClick(val) {
        // alert(val)
        //  不能直接修改state,为了实现异步的操作,我们通过dispatch分发actions中声明的方法
        // this.$store.dispatch('get_count')
      },

      bushandler() {
        //  为了使用全局BUS,在main.js,中let bus
        this.$bus.$emit('click', 'wusir');
        this.$store.dispatch('get_count')
      }
    },
    components: {
      Son                   //挂子
    },
    // Vuex 之调用[state的获取]
    computed: {
      //默认只有getter
      getCount() {
        return this.$store.state.count
      }
    }
  }
</script>

<style scoped>

</style>
