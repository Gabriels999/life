<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld/>
    <div v-for="item, index_row in matriz" :key="index_row" class="flex">
      <div v-for="item, index_col in matriz[index_row]" :key="index_col">
        <CelulaLife :row="index_row" :col="index_col" @update-life="updateCelula($event)" :state="item"/>
      </div>
    </div>
    <button @click="init">Jogar</button>
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
        [1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,1,0],
        [0,0,0,1,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
      ],
      novaMatriz: [],
      alive: false
    }
  },
  methods: {
    init(){
      this.matriz = this.geraNovaMatriz(this.matriz)
      return this.matriz
    },
    updateCelula(event){
      if (event[2] == 0){
        this.matriz[event[0]][event[1]] = 1
      } else {
        this.matriz[event[0]][event[1]] = 0
      }
    },
    verificaVizinhos(matriz, x, y){
      let possiveisVizinhos = [
        [-1,-1], [-1,0], [-1,1],
        [0,-1], [0,1],
        [1,-1], [1,0] [1,1]      
      ]
        let vizinhos = []
        let abacaxi = possiveisVizinhos.forEach((i)=>{
          console.log(x+i[0], y+i[1])
          if (i[0] + x >= 0 && i[1] + y >= 0){
            vizinhos.push([matriz[x+i[0]][y+i[1]]])
            console.log('foi')
          }
        })
      return 0 // FAZER A CONTAGEM
    },
    geraNovaMatriz(matriz){
      this.novaMatriz = [
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
      ]
      for(let i = 0; i < matriz.length; i++){
        for(let j = 0; j < matriz[i].length; j++){
          const vizinhosVivos = this.verificaVizinhos(matriz, i, j)
          if (matriz[i][j] == 1){
            if (vizinhosVivos < 2 || vizinhosVivos > 3){
              this.novaMatriz[i][j] = 0
            }
            else {
              this.novaMatriz[i][j] = 1
            }
          }
          else {
            if (vizinhosVivos == 3){
              this.novaMatriz[i][j] = 1
            }
            else {
              this.novaMatriz[i][j] = 0
            }
          }
        }
      }
      return this.novaMatriz
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
