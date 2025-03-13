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
    print("Bem-vindo ao sistema de gerenciamento do estacionamento!")

    # Lista para armazenar os veículos registrados
    veiculos_registrados = []
    total_arrecadado = 0
    total_isentos = 0

    while True:
        # Pergunta pelo tipo de veículo
        tipo_veiculo = input("Qual o tipo de veículo? (moto, carro, camionete) ou 'sair' para encerrar: ").lower()

        # Condição de saída do loop
        if tipo_veiculo == 'sair':
            break

        # Verifica se o tipo de veículo é válido
        if tipo_veiculo not in ['moto', 'carro', 'camionete']:
            print("Tipo de veículo inválido. Por favor, insira 'moto', 'carro' ou 'camionete'.")
            continue

        # Pergunta pela hora de entrada
        hora_entrada = obter_hora("Digite a hora de entrada (formato HH:MM): ")

        # Pergunta pela hora de saída
        hora_saida = obter_hora("Digite a hora de saída (formato HH:MM): ")

        # Verifica se a hora de saída é maior que a hora de entrada
        if hora_saida <= hora_entrada:
            print("A hora de saída não pode ser anterior à hora de entrada.")
            continue

        # Cria o veículo e calcula o valor
        veiculo = Veiculo(tipo_veiculo, hora_entrada)
        veiculo.hora_saida = hora_saida
        valor = veiculo.calcular_valor()

        # Adiciona o veículo à lista de veículos registrados
        veiculos_registrados.append(veiculo)
        total_arrecadado += valor

        # Conta os isentos
        if valor == 0:
            total_isentos += 1

        # Exibe o valor a ser pago
        print(f"Valor a ser pago pelo veículo ({tipo_veiculo}): R${valor:.2f}")

    # Exibe o relatório diário ao final (\n)==> Onde houver esse símbolo é quebra de linha.
    print("\nRelatório diário do estacionamento:")
    print(f"Total de veículos registrados: {len(veiculos_registrados)}")
    print(f"Total arrecadado: R${total_arrecadado:.2f}")
    print(f"Total de veículos isentos de pagamento: {total_isentos}")
    print("\nDetalhes dos veículos registrados:")

    for veiculo in veiculos_registrados:
        tempo_permanencia = (veiculo.hora_saida - veiculo.hora_entrada).total_seconds() / 60
        print(
            f"Tipo: {veiculo.tipo.capitalize()} | Tempo de permanência: {tempo_permanencia:.2f} minutos | Valor a pagar: R${veiculo.valor_pago:.2f}")


# Chama a função principal
if __name__ == "__main__":
    main()
# Aqui eu criei um relatório diário para o estacionamento.