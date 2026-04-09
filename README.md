🐉 Batalha RPG — Sistema de Combate em Python
---

Um mini‑RPG de batalha em turnos feito em Python, com foco em mecânicas estratégicas, polimorfismo e inimigos com comportamentos únicos.
O jogador enfrenta inimigos aleatórios, cada um com habilidades próprias, enquanto usa ataques, cura e esquiva para sobreviver.

---

## 🎮 Como funciona o jogo
A cada partida:
- Um inimigo aleatório é gerado
- O jogador escolhe entre Atacar, Curar ou Esquivar
- O inimigo responde com seu próprio ataque
- O combate continua até um dos dois morrer
O sistema usa polimorfismo para permitir que cada inimigo tenha sua própria lógica de defesa, tornando cada batalha diferente.
---

## ⚔️ Ações do Jogador
🗡️ Atacar
- O jogador causa um dano aleatório entre 15 e 25.
- O ataque passa pela defesa do inimigo (que pode reduzir, esquivar ou modificar o dano).  

💖 Curar
- O jogador recupera entre 15 e 25 de vida.
- Se estiver sob efeito do buff de esquiva, a cura recebe +50% de bônus.  

⚡ Esquivar
- O jogador tem 50% de chance de evitar completamente o próximo ataque.
- Se a esquiva funcionar, o jogador recebe um buff para o próximo turno:
- +50% de dano no ataque
- +50% de cura
- Se falhar, toma o dano normalmente.  
Essa mecânica cria um sistema de risco/recompensa que deixa o combate mais estratégico.
---

## 👹 Inimigos e suas mecânicas
Cada inimigo herda da classe base Personagens, mas sobrescreve o método defender() para criar comportamentos únicos.   
🟩 Goblin — Esquiva Rápida
- 50% de chance de esquivar automaticamente de ataques.
- Irritante, rápido e imprevisível.  

🟥 Orc — Fúria
- 40% de chance de entrar em fúria ao ser atingido.
- Na fúria:
- Recebe metade do dano
- Seu próximo ataque causa dano dobrado

🟫 Golem — Armadura de Pedra
- Reduz todo dano recebido em 40%.
- Tanque pesado, difícil de derrubar.   
Mais inimigos podem ser adicionados facilmente graças ao uso de polimorfismo.
---

## 🧠 Principais conceitos usados

✔ Polimorfismo  
Cada inimigo implementa sua própria lógica de defesa, permitindo comportamentos únicos sem alterar o código da batalha.  
✔ Encapsulamento  
Cada personagem controla seus próprios atributos e métodos (ataque, cura, defesa).  
✔ Aleatoriedade  
Dano, cura, esquiva e habilidades especiais usam random para tornar cada partida diferente.  
✔ Sistema de Buffs  
A esquiva bem-sucedida concede bônus temporários que afetam o próximo turno do jogador.  

--- 

## 📁 Estrutura do Projeto
BatalhaRPG/  
│  
├── Personagens/  
│   ├── Personagens.py  
│   ├── Jogador.py  
│   ├── Goblin.py  
│   ├── Orc.py  
│   ├── Golem.py  
│   └── RandomEnemy.py  
│  
├── Partida/  
│   └── Partida.py  
│  
└── Main.py  

---

## ▶️ Como executar
- Certifique-se de ter Python 3 instalado.
- Clone o repositório:
git clone https://github.com/oiacmon/BatalhaRPG.git
- Execute o arquivo principal:
python Main.py

---
