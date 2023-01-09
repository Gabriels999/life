<template>
  <div id="app">
    <h1>Life Game</h1>
    <div class="board">
      <div v-for="(item, index_row) in matriz" :key="index_row" class="flex">
        <div v-for="(item, index_col) in matriz[index_row]" :key="index_col">
          <CelulaLife
            :row="index_row"
            :col="index_col"
            @update-life="updateCelula($event)"
            :state="item"
          />
        </div>
      </div>
    </div>
    <button @click="init">Jogar</button>
  </div>
</template>

<script>
import CelulaLife from "./components/CelulaLife";
import vizinhos from "./service/vizinhos"
import atualizaCelula from "./service/matriz"

export default {
  name: "App",
  components: {
    CelulaLife,
  },
  data() {
    return {
      cols: 4,
      rows: 4,
      matriz: [
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
      ],
      novaMatriz: [],
      alive: false,
    };
  },
  methods: {
    init() {
      this.matriz = this.geraNovaMatriz(this.matriz);
      this.rodaGame(this.matriz);
    },
    rodaGame(matriz) {
      this.matriz = this.geraNovaMatriz(matriz);
      setTimeout(() => {
        this.rodaGame(this.matriz);
      }, 700);
    },
    updateCelula(event) {
      this.matriz = atualizaCelula.updateCelula(this.matriz, event)
    },
    geraNovaMatriz(matriz) {
      this.novaMatriz = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      ];
      for (let i = 0; i < matriz.length; i++) {
        for (let j = 0; j < matriz[i].length; j++) {
          const vizinhosVivos = vizinhos.verificaVizinhos(matriz, i, j);
          if (matriz[i][j] == 1) {
            if (vizinhosVivos < 2 || vizinhosVivos > 3) {
              this.novaMatriz[i][j] = 0;
            } else {
              this.novaMatriz[i][j] = 1;
            }
          } else {
            if (vizinhosVivos == 3) {
              this.novaMatriz[i][j] = 1;
            } else {
              this.novaMatriz[i][j] = 0;
            }
          }
        }
      }
      return this.novaMatriz;
    },
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.flex {
  display: flex;
}
.board {
  margin: 5% 43%;
  width: 20%;
}
</style>
