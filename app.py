import serial
import time

# Configure a porta (mude 'COM3' para a porta que aparece no seu Gerenciador de Dispositivos)
# No Linux, geralmente é algo como '/dev/ttyUSB0' ou '/dev/ttyS0'
porta = '/dev/ttyUSB0' 

try:
    ser = serial.Serial(porta, 9600, timeout=1)
    time.sleep(2) # Aguarda a conexão estabilizar
    
    mensagem_enviada = b"Ola Mundo Serial"
    
    # Limpa os buffers
    ser.reset_input_buffer()
    
    # Envia os dados
    print(f"Enviando: {mensagem_enviada.decode()}")
    ser.write(mensagem_enviada)
    
    # Lê os dados de volta
    mensagem_recebida = ser.read(len(mensagem_enviada))
    
    if mensagem_recebida == mensagem_enviada:
        print("SUCESSO: O teste de loopback funcionou! O cabo está íntegro.")
    else:
        print(f"FALHA: Recebido '{mensagem_recebida.decode()}' (Pode haver mau contato ou o jumper está ausente).")

    ser.close()

except serial.SerialException as e:
    print(f"Erro ao abrir a porta: {e}")