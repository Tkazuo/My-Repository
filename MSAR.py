import pygetwindow as gw
import pyautogui
import time

# Nome da janela alvo
janela_nome = "METAL SLUG ATTACK RELOADED"  # Substitua pelo título da janela desejada

try:
    print(f"Pressionando 'Enter' apenas enquanto a janela '{janela_nome}' estiver ativa. Pressione Ctrl + C para parar.")

    while True:
        # Obter a janela ativa atualmente
        janela_ativa = gw.getActiveWindowTitle()

        # Verificar se a janela ativa é a desejada
        if janela_ativa and janela_nome in janela_ativa:
            pyautogui.press("enter")  # Pressiona a tecla Enter
            print(f"Pressionando 'Enter' na janela: {janela_ativa}")
        else:
            print(f"A janela ativa é diferente: {janela_ativa}")  # Janela ativa não é a desejada

        time.sleep(1)  # Aguarda 1 segundo antes de verificar novamente
except KeyboardInterrupt:
    print("\nScript encerrado.")
