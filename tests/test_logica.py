from src.funcoes import (
    calcular_pontos,
    clique_acertou_alvo,
    jogador_perdeu,
    limitar_valor,
    tomar_dano,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_tomar_dano():
    """Deve reduzir a quantidade de vidas."""
    assert tomar_dano(3, 1) == 2


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_clique_acertou_alvo_no_centro():
    """Deve acertar quando o clique ocorre no centro do alvo."""
    assert clique_acertou_alvo((100, 100), (100, 100), 35) is True


def test_clique_acertou_alvo_na_borda():
    """Deve acertar quando o clique ocorre exatamente na borda."""
    assert clique_acertou_alvo((135, 100), (100, 100), 35) is True


def test_clique_errou_alvo():
    """Deve errar quando o clique ocorre fora do raio."""
    assert clique_acertou_alvo((140, 100), (100, 100), 35) is False
