<template>
  <div>
    我是子组件 {{ getCount }}=====> {{ title }} {{ msg }} =+++++= BUS传值再赋值的value为:{{ name }}
  </div>
</template>

<script>
  export default {
    name: "Son",
    //父往子传值  子组件中接收
    props: ['title', 'msg'],
    data() {
      return {
        paramet: "Hello",
        name: ''
      }
    },
    //<!--    子组件往父组件传值 -->
    // 在父组件中需要的地方 @handler 并接入绑定的方法,接收的参数数据就是此处emit函数后面的数据
    created() {
      this.$emit('handler', this.paramet);

      this.$bus.$on('click', (name) => {
        this.name = name
      })
    },
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
