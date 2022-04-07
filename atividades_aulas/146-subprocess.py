import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1'], # Comando
    capture_output=True, # Informa que quer capturar a saida
    text=True, # Saida em modo texto
    check=False
)

saida = proc.stdout
print(saida)
