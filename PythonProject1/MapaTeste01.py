from datetime import datetime


# Classe para representar o veículo
class Veiculo:
    def __init__(self, tipo, hora_entrada):
        self.tipo = tipo  # Tipo do veículo: 'moto', 'carro', 'camionete'
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


# Função para pegar a hora e garantir que o formato seja válido
def obter_hora(mensagem):
    while True:
        try:
            hora_str = input(mensagem)
            hora = datetime.strptime(hora_str, '%H:%M')
            return hora
        except ValueError:
            print("Formato inválido. Por favor, insira a hora no formato HH:MM (24h).")


# Função principal
def main():
    print("Bem-vindo ao sistema de gerenciamento do estacionamento\nUniCesumar Parking")

    # Pergunta pelo tipo de veículo
    tipo_veiculo = input("Qual o tipo de veículo? (moto, carro, camionete): ").lower()

    # Verifica se o tipo de veículo é válido
    if tipo_veiculo not in ['moto', 'carro', 'camionete']:
        print("Tipo de veículo inválido. Por favor, insira 'moto', 'carro' ou 'camionete'.")
        return

    # Pergunta pela hora de entrada
    hora_entrada = obter_hora("Digite a hora de entrada (formato HH:MM): ")

    # Pergunta pela hora de saída
    hora_saida = obter_hora("Digite a hora de saída (formato HH:MM): ")

    # Verifica se a hora de saída é maior que a hora de entrada
    if hora_saida <= hora_entrada:
        print("A hora de saída não pode ser anterior à hora de entrada.")
        return

    # Cria o veículo e calcula o valor
    veiculo = Veiculo(tipo_veiculo, hora_entrada)
    veiculo.hora_saida = hora_saida
    valor = veiculo.calcular_valor()

    # Exibe o valor a ser pago
    print(f"Valor a ser pago pelo veículo ({tipo_veiculo}): R${valor:.2f}")


# Chama a função principal
if __name__ == "__main__":
    main()
