# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.


def calcular_area_base():
    raio = float(input("Digite o raio do circulo:"))
    area = 3.14*raio**2
    return area

area = calcular_area_base()
print(f"A area desse circulo e {area}")

print('Vamos calcula a do cilidro agora..')


def _volume_cilindro():
    
    altura = float(input("Digite a altura:"))
    volume = area *altura
    return volume

volume= _volume_cilindro()

print(f"O volume do seu cilindro e {volume}")

