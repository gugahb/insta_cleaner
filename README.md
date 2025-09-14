# 🧹 Instagram Cleaner

<div align="center">
  <h3>🤖 Ferramenta automatizada para limpeza inteligente de seguidores no Instagram</h3>
  <p>Analisa perfis e remove seguidores inativos, spam e contas suspeitas de forma automatizada</p>
  
  ![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
  ![Playwright](https://img.shields.io/badge/Playwright-Latest-green.svg)
  ![License](https://img.shields.io/badge/License-MIT-yellow.svg)
</div>

---

## 📋 Funcionalidades

### 🎯 **Análise Inteligente**
- ✅ **Perfis inativos** - Identifica contas sem atividade
- ✅ **Poucos posts** - Remove usuários com menos de 10 publicações
- ✅ **Razão suspeita** - Detecta contas que seguem muito mais do que têm seguidores
- ✅ **Filtro por nome** - Remove perfis com padrões específicos (ex: "sorte")

### 🛠️ **Automação Avançada**
- 🔄 **Processamento em lote** - Analisa milhares de seguidores automaticamente
- 💾 **Sistema de cache** - Evita re-análise de perfis já verificados  
- 📊 **Logs detalhados** - Registra todas as ações para auditoria
- 🚫 **Auto-remoção** - Remove da lista usuários que não existem mais

### 🖥️ **Interface Amigável**
- 📋 **Menu interativo** - Navegação simples e intuitiva
- 🔍 **Feedback em tempo real** - Acompanhe o progresso das operações
- ⚡ **Processamento rápido** - Otimizado para grandes volumes

---

## 🚀 Instalação

### Pré-requisitos
- 🐍 **Python 3.8+**
- 🌐 **Google Chrome** (para automação web)

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/insta_cleaner.git
cd insta_cleaner
```

### 2️⃣ Instale as dependências
```bash
pip install -r app/requirements.txt
```

### 3️⃣ Configure o Playwright
```bash
playwright install chromium
```

---

## 🎮 Como Usar

### 🏃‍♂️ **Execução**
```bash
cd app
python main.py
```

### 📋 **Menu Principal**
```
📋 MENU
1 - Verificar perfis inativos e autorizar remoção
2 - Remover seguidores com nome contendo 'sorte'  
3 - Remover seguidores listados em remover_depois.json
4 - Sair
```

### 🔑 **Primeiro Uso**
1. Execute o programa
2. Faça login manualmente no Instagram (incluindo 2FA se habilitado)
3. As credenciais ficam salvas localmente para próximas execuções

---

## 📁 Estrutura do Projeto

```
insta_cleaner/
├── 🐳 docker-compose.yml    # Containerização
├── 📝 README.md            # Documentação  
├── 🚫 .gitignore          # Arquivos ignorados
└── 📱 app/
    ├── 🚀 main.py         # Ponto de entrada
    ├── 🌐 browser.py      # Gerenciamento do navegador
    ├── 🔍 remover.py      # Lógica de análise e remoção
    ├── 📊 processar_csv_seguidores.py  # Processamento de dados
    ├── 🏷️ analisados.py   # Cache de perfis analisados
    ├── 🗂️ remover_depois.py # Gerenciamento de listas
    ├── 🛠️ utils.py        # Utilitários diversos
    └── 📋 requirements.txt # Dependências
```

---

## 🔧 Configuração Avançada

### 📊 **Critérios de Remoção**
O sistema utiliza os seguintes critérios para identificar perfis suspeitos:

- **Posts insuficientes**: < 10 publicações
- **Razão seguindo/seguidores**: > 4:1  
- **Perfis inativos**: Sem atividade recente
- **Nomes suspeitos**: Contém palavras como "sorte"

### 🎛️ **Personalização**
Você pode ajustar os critérios editando as constantes em `remover.py`:
```python
MIN_POSTS = 10              # Mínimo de posts
MAX_FOLLOWING_RATIO = 4     # Razão máxima seguindo/seguidores
```

---

## 🐳 Docker

### 🏗️ **Build e execução**
```bash
docker-compose up --build
```

### 📋 **Variáveis de ambiente**
Crie um arquivo `.env` (opcional):
```env
DISPLAY=:0  # Para interface gráfica no Linux
```

---

## ⚠️ Avisos Importantes

### 🚨 **Termos de Uso do Instagram**
- ✅ Use com responsabilidade e moderação
- ✅ Respeite os limites de rate do Instagram  
- ✅ Não use para spam ou ações maliciosas
- ❌ Este projeto é apenas para fins educacionais

### 🔒 **Privacidade**
- 🔐 Suas credenciais ficam salvas **apenas localmente**
- 🚫 **Nenhum dado** é enviado para servidores externos
- 💾 Todos os arquivos de dados estão no `.gitignore`

### ⚖️ **Responsabilidade**
- 👤 **Você é responsável** pelo uso desta ferramenta
- 📋 Certifique-se de cumprir os **Termos de Serviço** do Instagram
- 🛡️ Use apenas em **sua própria conta**

---

## 🤝 Contribuição

### 🐛 **Reportar Bugs**
Abra uma [issue](https://github.com/seu-usuario/insta_cleaner/issues) com:
- Descrição detalhada do problema
- Passos para reproduzir
- Screenshots (se aplicável)

### 💡 **Sugestões**
- Fork o projeto
- Crie uma branch para sua feature
- Commit suas mudanças
- Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## ❤️ Agradecimentos

- 🎭 [Playwright](https://playwright.dev/) - Automação web moderna
- 🐍 [Python](https://python.org/) - Linguagem de programação
- 📸 [Instagram](https://instagram.com/) - Plataforma social

---

<div align="center">
  <p>⭐ Se este projeto foi útil, deixe uma estrela!</p>
  <p>💬 Dúvidas? Abra uma issue!</p>
</div>
