<template>
  <button class="box" :class="{ alive: state }" @click="changeState"></button>
</template>

<script>
export default {
  props: {
    state: 0,
  },
  methods: {
    changeState() {
      // this.$emit("update-life", (this.row, this.col));
      if (this.state == 1) {
        this.state = 0;
      } else {
        this.state = 1;
      }
    },
  },
};
</script>

<style>
.box {
  display: inline-block;
  border: 1px solid gray;
  padding: 8px;
  color: white;
  background-color: grey;
  margin: 2px;
}
.alive {
  color: green;
  background-color: green;
}
</style>
