export function verificaVizinhos(matriz, x, y) {
    let possiveisVizinhos = [
        { x: -1, y: -1 },
        { x: -1, y: 0 },
        { x: -1, y: 1 },
        { x: 0, y: -1 },
        { x: 0, y: 1 },
        { x: 1, y: -1 },
        { x: 1, y: 0 },
        { x: 1, y: 1 },
    ];

    let vizinhosVivos = 0;

    possiveisVizinhos.forEach((item) => {
        if (matriz[item.x + x]?.[item.y + y] == 1) {
            vizinhosVivos += 1;
        }
        // if (
        //     i["x"] + x >= 0 &&
        //     i["y"] + y >= 0 &&
        //     i["x"] + x < matriz.length &&
        //     i["y"] + y < matriz[0].length
        // ) {
        //     vizinhos.push({ x: i["x"] + x, y: i["y"] + y });
        // }
    });

    // vizinhos.forEach((i) => {
    //     if (matriz[i["x"]][i["y"]] == 1) {
    //         vizinhosVivos += 1;
    //     }
    // });
    return vizinhosVivos;
}
