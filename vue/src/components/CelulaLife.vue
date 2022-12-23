<template>
    <button :class='{"box":true, "alive":item}' @click="changeState"></button>
</template>

<script>
export default{
    props:{
        row: "",
        col: "",
        item: 0
    },
    methods:{
        changeState(){
            this.$emit('update-life', [this.row, this.col, this.item])
        }
    }
}
</script>

<style>
.box{
    display: inline-block;
    border: 1px solid gray;
    padding: 8px;
    color: white;
    background-color: grey;
    margin: 2px;
}
.alive{
    color: green;
    background-color: green;
}
.dead{
    color: gray;
    background-color: gray;
}
</style>