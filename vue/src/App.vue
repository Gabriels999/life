<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld/>
    <div v-for="item, index_row in matriz" :key="index_row" class="flex">
      <div v-for="item, index_col in matriz[index_row]" :key="index_col">
        <CelulaLife :row="index_row" :col="index_col" @update-life="updateCelula($event)" :item="item"/>
      </div>
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import CelulaLife from './components/CelulaLife'

export default {
  name: 'App',
  components: {
    HelloWorld,
    CelulaLife
  },
  data() {
    return {
      cols: 4,
      rows: 4,
      matriz: [
        [1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
      ],
      alive: false
    }
  },
  methods: {
    init(){

    },
    updateCelula(event){
      if (event[2] == 0){
        this.matriz[event[0]][event[1]] = 1
        console.log(this.matriz[event[0]][event[1]] = 1)
        debugger
      } else {
        this.matriz[event[0]][event[1]] = 0
      }
      //this.matriz[row][column] = newValue
      //this.$forceUpdate()
    }
  },
  watch:{
    matriz(){
      return this.matriz
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.flex {
  display: flex;
}
</style>
