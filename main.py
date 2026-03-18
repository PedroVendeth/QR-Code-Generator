import qrcode
import os

def gerar_qrcode(dados, nome_arquivo):
    # cria um abjeto chamado qr, que é uma instãncia da classe QRCODE do módulo QRcode
    qr = qrcode.QRCode(
        version=1, # versão do QR code, ajustável para aumentar ou diminuir o tamanho do código
        error_correction=qrcode.constants.ERROR_CORRECT_L, # o nível de correção de erros, que pode ser L (baixo) ou H (alto);
        box_size=10, # o tamanho de cada caixa do QR code em pixels
        border=4, # Largura da borda do QR code em caixas (padrão é 4)
    )

    qr.add_data(dados) # vai Adicionar os dados ao objeto QR code.
    qr.make(fit=True) # vai gerar o QR code com base nos dados fornecidos e fazer o ajuste automático do tamanho do código.
    img = qr.make_image(fill_color="black", back_color="white") # vai criar uma imagem do QR code, onde fill_color é a cor dos pixels do código e back_color é a cor de fundo da imagem.
    img.save(nome_arquivo + ".png") # vai salvar a imagem do QR code em um arquivo com o nome especificado e formatado como png;
    
def limpar_tela():
    os.system('cls')

if __name__ == "__main__":
    while True:
        dados = input("Informe o link a ser convertido em QR code: ").strip() # vai solicitar ao usuário que informe o link a ser convertido em QR code. O Strip() foi usado para remover espaços em branco no início e no final da string.
        nome_arquivo = input("informe o nome do arquivo para salvar o QR code: ").strip()
        if not dados or not nome_arquivo:
            limpar_tela()
            print("Dados ou nome do arquivo não podem estar vazios. Tente novamente!\n")  
        elif os.path.exists(nome_arquivo + ".png"):
            limpar_tela()
            print(f"Arquivo {nome_arquivo}.png já existe. Por favor escolha outro nome de arquivo.\n")
        else:
            gerar_qrcode(dados, nome_arquivo)
            print(f"QR code gerado e salvo como {nome_arquivo}.png")
            break
        
        