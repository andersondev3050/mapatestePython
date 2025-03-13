from datetime import datetime

# Classe para representar o veículo
class Veiculo:
    print(input('Tipo do veículo: '))
    print(input('Hora da entrada: '))
    print(input('Hora da saída: '))
    print(input('Valor pago R$: '))

    # Tipo do veículo: 'moto', 'carro', 'camionete'
    def __init__(self, tipo, hora_entrada):
        self.tipo = tipo
        self.hora_entrada = hora_entrada
        self.hora_saida = None
        self.valor_pago = 0

    def calcular_valor(self):
        # Calcular o tempo de permanência em minutos
        tempo_permanencia = (self.hora_saida - self.hora_entrada).total_seconds() / 60

        # Calcular valor com base no tempo de permanência
        if tempo_permanencia <= 15:
            self.valor_pago = 0
        elif tempo_permanencia <= 60:
            self.valor_pago = 1.50
        else:
            horas_adicionais = (tempo_permanencia - 60) // 60
            self.valor_pago = 1.50 + (horas_adicionais * 1.00)

        return self.valor_pago


# Classe para representar o estacionamento
class Estacionamento:
    def __init__(self):

        self.veiculos = []
        self.total_arrecadado = 0
        self.veiculos_isentos = 0
        self.contagem_tipo = {'moto': 0, 'carro': 0, 'camionete': 0}

    def registrar_entrada(self, tipo):
        hora_entrada = datetime.now()
        veiculo = Veiculo(tipo, hora_entrada)
        self.veiculos.append(veiculo)
        self.contagem_tipo[tipo] += 1

    def registrar_saida(self, veiculo, hora_saida):
        veiculo.hora_saida = hora_saida
        valor = veiculo.calcular_valor()
        self.total_arrecadado += valor
        if valor == 0:
            self.veiculos_isentos += 1
        return valor

    def mostrar_relatorio(self):
        print(f"Total arrecadado: R${self.total_arrecadado:.2f}")
        print(f"Veículos isentos: {self.veiculos_isentos}")
        for tipo, quantidade in self.contagem_tipo.items():
            print(f"{tipo.capitalize()}s estacionados: {quantidade}")


# Função principal
def main():
    estacionamento = Estacionamento()

    # Exemplo de registros
    estacionamento.registrar_entrada('carro')
    estacionamento.registrar_entrada('moto')

    # Simulando uma saída de veículo
    hora_saida = datetime.now()
    valor = estacionamento.registrar_saida(estacionamento.veiculos[0], hora_saida)
    print("Valor a pagar pelo veículo: R${valor:.2f}")

    estacionamento.mostrar_relatorio()


# Chama a função principal
if __name__ == "__main__":
    main()
