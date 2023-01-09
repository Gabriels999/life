import atualiza from '../../src/service/matriz'


const matriz1 = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 0, 0],
]

describe('Atualiza celula', () => {
    it('verifica atualizacao da celula (0, 0)', () => {
        const evento1 = [0, 0, 0]
        atualiza.updateCelula(matriz1, evento1)
        expect(matriz1[0][0]).toBe(1)
    })
    it('verifica atualizacao da celula (1, 0)', () => {
        const evento2 = [1, 0, 1]
        atualiza.updateCelula(matriz1, evento2)
        expect(matriz1[1][0]).toBe(0)
    })
})