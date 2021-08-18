def funcao(semitom):
    notasMaiores = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]  # 11 tons
    notasMenores = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]  # 11 tons
    valor = ''

    # senitons maiores, no caso, utilizando sustenidos
    if semitom >= 0:
        if semitom > 10:
            index = 0
            valor = ''
            frequencia = 440 * (2 ** (semitom  / 12))  # indica a frequencia em Hz
            frequenciaArredondada = round(frequencia, 4)
            for n in range(semitom + 1):   # percorre as notas de forma circular
                valor = notasMaiores[index - 2]
                index += 1
                if index == 11:
                    index = 0
            # usando o dó como exemplo # a referência
            frequenciaArredondada = round(frequencia, 4)
            print(f'A nota é : {valor} e a frequência é: {frequenciaArredondada} Hz')
        else:
            # usando o lá como exemplo # a referência
            frequencia = 440 * (2 ** (semiton / 12) ) #  indica a frequencia em Hz
            frequenciaArredondada = round(frequencia, 4)
            print(f'A nota é :{notasMaiores[semiton]} e a frequência é: {frequenciaArredondada} Hz')

    # semitons menores, no caso, usando b mol
    elif semitom < 0:
        if  (-1 * semitom) > 10:
            index = 0
            frequencia = 440 * (2 ** (semitom  / 12))  # indica a frequencia em Hz
            frequenciaArredondada = round(frequencia, 4)
            for n in range(semitom * -1 + 1):   # percorre as notas de forma circular
                valor = notasMenores[nu - 2]
                index += 1
                if index == 11:
                    index = 0
            # usando o dó como exemplo # a referência
            frequenciaArredondada = round(frequencia, 4)
            print(f'A nota é : {valor} e a frequência é: {frequenciaArredondada} Hz')
        else:
            frequencia = 440 * (2 ** (semitom  / 12) ) # indica a frequencia em Hz
            frequenciaArredondada = round(frequencia, 4)
            inverso = notasMenores  # inverte o vetor para que -1 torne-se ré b, que é o tom abaixo do dó
            print(f'A nota é : {inverso[semitom]} e a frequência é: {frequenciaArredondada} Hz')


if __name__ == '__main__':
    semiton = int(input('Informe o semitom: '))
    funcao(semiton)
