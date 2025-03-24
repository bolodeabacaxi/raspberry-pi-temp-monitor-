🌡️ Monitor de Temperatura e Umidade com Raspberry Pi

Este projeto usa um Raspberry Pi e um sensor DHT11/DHT22 para medir temperatura e umidade e exibir os dados em tempo real via Flask.

📌 Funcionalidades

✅ Leitura de temperatura e umidade do sensor DHT11/DHT22
✅ Exibição dos dados via API REST (/data)
✅ Servidor web Flask simples para visualização
✅ Código leve e fácil de expandir

🛠️ Instalação e Uso

1️⃣ Clone o repositório

git clone https://github.com/seu-usuario/raspberry-pi-temp-monitor.git
cd raspberry-pi-temp-monitor

2️⃣ Instale as dependências

pip install -r requirements.txt

3️⃣ Execute o script

python app.py

4️⃣ Acesse os dados no navegador

http://<IP_DO_RASPBERRY>:5000/data

🔌 Conexão do Sensor DHT11/DHT22

![image](https://github.com/user-attachments/assets/07f11c96-2e71-4393-bb64-6feaacdf8429)


🖥️ Exemplo de Resposta da API

{
  "temperature": 24.5,
  "humidity": 60.2
}

📡 Hardware Necessário

Raspberry Pi (qualquer modelo com GPIO)

Sensor DHT11 ou DHT22

Jumpers para conexão
