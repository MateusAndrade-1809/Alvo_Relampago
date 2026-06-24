from dataclasses import dataclass, field

from src.config import TEMPO_LIMITE, VIDAS_INICIAIS


@dataclass
class Alvo:
    x: float = 0
    y: float = 0
    tamanho: str = "medio"
    surgiu_em: int = 0
    velocidade_x: float = 0
    velocidade_y: float = 0


@dataclass
class ItemEspecial:
    ativo: bool = False
    x: int = 0
    y: int = 0
    surgiu_em: int = 0
    proximo_surgimento: int = 0

    def ativar(self, x, y, agora):
        self.ativo = True
        self.x = x
        self.y = y
        self.surgiu_em = agora

    def desativar(self):
        self.ativo = False
        self.x = 0
        self.y = 0
        self.surgiu_em = 0


@dataclass
class Estatisticas:
    acertos: int = 0
    erros: int = 0
    coracoes: int = 0
    ampulhetas: int = 0

    @property
    def total_cliques(self):
        return self.acertos + self.erros + self.coracoes + self.ampulhetas

    @property
    def precisao(self):
        cliques_em_alvos = self.acertos + self.erros
        if cliques_em_alvos == 0:
            return 0
        return round(self.acertos / cliques_em_alvos * 100)


@dataclass
class EstadoJogo:
    pontos: int = 0
    vidas: int = VIDAS_INICIAIS
    tempo_restante: int = TEMPO_LIMITE
    inicio: int = 0
    tela: str = "inicio"
    mensagem: str = ""
    alvo: Alvo = field(default_factory=Alvo)
    coracao: ItemEspecial = field(default_factory=ItemEspecial)
    ampulheta: ItemEspecial = field(default_factory=ItemEspecial)
    estatisticas: Estatisticas = field(default_factory=Estatisticas)

