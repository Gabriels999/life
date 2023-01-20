export function updateCell(matriz, evento) {
    if (evento[2] == 0) {
        matriz[evento[0]][evento[1]] = 1;
    } else {
        matriz[evento[0]][evento[1]] = 0;
    }
}
