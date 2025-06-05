# teste_robo.py
from econdo_bot import criar_liberacao_econdo  # Importe conforme o local do seu código

if __name__ == "__main__":
    link = criar_liberacao_econdo(
        nome="Teste Local",
        data_checkin="2024-06-10",
        data_checkout="2024-06-12"
    )
    print("LINK GERADO:", link)
