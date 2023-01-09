import { verificaVizinhos } from '../../src/service/vizinhos'


describe('Vizinhos vivos', () => {
    it('um vizinho vivo abaixo', () => {
        const matriz = [
            [0, 0, 0],
            [1, 0, 1],
            [0, 0, 0],
        ]

        expect(verificaVizinhos(matriz, 0, 0)).toBe(1)
    })

    it("vizinhos vivos embaixo, acima e dos lados", () => {
        const matriz = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        expect(verificaVizinhos(matriz, 1, 1)).toBe(4)
    })

    it("vizinhos vivos embaixo, acima e dos lados", () => {
        const matriz = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1],
        ]
        expect(verificaVizinhos(matriz, 1, 1)).toBe(6)
    })
})