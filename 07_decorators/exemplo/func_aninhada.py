def media_acumulada():
    valores = []  # valores que serao chamadas dentro da funcao interna!!!!!

    def calcula_media(valor):
      valores.append(valor)
      return sum(valores)/len(valores)

    return calcula_media   
