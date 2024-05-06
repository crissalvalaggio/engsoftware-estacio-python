class Veiculo:
    def __init__(self, velocidade_maxima, km_por_litro):
        self.velocidade_maxima = VelocidadeMaxima(velocidade_maxima)
        self.km_por_litro = KmPorLitro(km_por_litro)

class VelocidadeMaxima:
    def __init__(self, velocidade_maxima):
        self.valor = velocidade_maxima

class KmPorLitro:
    def __init__(self, km_por_litro):
        self.valor = km_por_litro

# Exemplo de uso das classes
meu_carro = Veiculo(180, 12)  # Velocidade máxima de 180 km/h, 12 km por litro
print("Velocidade máxima do carro:", meu_carro.velocidade_maxima.valor, "km/h")
print("Consumo de combustível do carro:", meu_carro.km_por_litro.valor, "km por litro")