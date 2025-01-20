import qrcode

def gerar_qr_code(texto):
    # Cria o QR Code
    qr = qrcode.QRCode(
        version=1,  # O tamanho do QR Code (1 é o menor)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
        box_size=10,  # Tamanho de cada caixa (pixel)
        border=4,  # Tamanho da borda
    )

    qr.add_data(texto)
    qr.make(fit=True)

    # Cria uma imagem do QR Code
    img = qr.make_image(fill='black', back_color='white')
    return img

def salvar_qr_code(img, nome_arquivo):
    # Salva a imagem em um arquivo
    img.save(nome_arquivo)

def main():
    texto = input("Digite o texto ou URL para gerar o QR Code: ")
    img = gerar_qr_code(texto)
    salvar_qr_code(img, "qrcode.png")
    print("QR Code gerado e salvo como 'qrcode.png'.")

if __name__ == "__main__":
    main()
