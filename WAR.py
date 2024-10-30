import random

class WARIA:
    def __init__(self, territorios, tropas, objetivo, continentes):
        """
        Inicializa a IA para o jogo WAR.
        territorios: lista de territórios controlados pela IA
        tropas: dicionário com o número de tropas em cada território
        objetivo: objetivo secreto da IA
        continentes: lista de continentes e bônus associados
        """
        self.territorios = territorios
        self.tropas = tropas
        self.objetivo = objetivo
        self.continentes = continentes  # Exemplo: {"América do Sul": ["Brasil", "Argentina", ...]}
    
    def gerar_movimento(self):
        """
        Gera uma lista de ações para o turno da IA (ataque, reforço, movimentação).
        """
        acoes = []
        
        # Passo 1: Priorizar reforço em territórios vulneráveis
        for territorio in self.territorios:
            if self.is_vulneravel(territorio):
                acoes.append(self.reforcar(territorio))
        
        # Passo 2: Determinar ataques com base em análise de risco
        for territorio in self.territorios:
            if self.deve_atacar(territorio):
                acoes.append(self.atacar(territorio))
        
        return acoes

    def is_vulneravel(self, territorio):
        """
        Determina se um território é vulnerável (vizinhos com tropas adversárias maiores).
        """
        for vizinho in self.get_vizinhos(territorio):
            if vizinho not in self.territorios and self.tropas[vizinho] > self.tropas[territorio]:
                return True
        return False

    def reforcar(self, territorio):
        """
        Reforça o território específico adicionando uma tropa, com prioridade para fronteiras e continentes incompletos.
        """
        self.tropas[territorio] += 1
        return f"Reforço em {territorio}"

    def deve_atacar(self, territorio):
        """
        Avalia se o território deve atacar um vizinho com base na análise de risco.
        Considera o número de tropas e a importância estratégica do vizinho.
        """
        vizinhos_inimigos = [v for v in self.get_vizinhos(territorio) if v not in self.territorios]
        for vizinho in vizinhos_inimigos:
            if self.analisar_risco(territorio, vizinho):
                return True
        return False

    def analisar_risco(self, territorio, vizinho):
        """
        Avalia o risco de um ataque, retornando True se o ataque tiver boas chances de sucesso.
        """
        tropas_ataque = self.tropas[territorio] - 1
        tropas_defesa = self.tropas[vizinho]
        
        return tropas_ataque > tropas_defesa

    def atacar(self, territorio):
        """
        Realiza o ataque a um território vizinho com base em uma decisão estratégica.
        """
        vizinho = self.selecionar_vizinho_estrategico(territorio)
        if vizinho:
          
            if self.analisar_risco(territorio, vizinho):
                self.tropas[territorio] -= 1
                self.tropas[vizinho] -= 1
                return f"Ataque de {territorio} para {vizinho}"
        return None
    
    def selecionar_vizinho_estrategico(self, territorio):
        """
        Seleciona um vizinho estratégico para ataque, priorizando territórios fracos e continentes incompletos.
        """
        vizinhos_inimigos = [v for v in self.get_vizinhos(territorio) if v not in self.territorios]
        
        vizinhos_ordenados = sorted(vizinhos_inimigos, key=lambda x: (self.tropas[x], self.is_continente_importante(x)))
        return vizinhos_ordenados[0] if vizinhos_ordenados else None
    
    def is_continente_importante(self, territorio):
        """
        Verifica se o território pertence a um continente que a IA está tentando completar.
        """
        for continente, territorios in self.continentes.items():
            if territorio in territorios and all(t in self.territorios for t in territorios if t != territorio):
                return True
        return False

    def get_vizinhos(self, territorio):
        """
        Retorna territórios vizinhos ao território especificado.
        """
        
        vizinhos_exemplo = {
            "Brasil": ["Argentina", "Peru"],
            "Argentina": ["Brasil", "Chile"],
            
        }
        return vizinhos_exemplo.get(territorio, [])
