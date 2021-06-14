from unittest.mock import Mock
import pytest

from empresa import Pessoa, Funcionario, Programador, Estagiario, Vendedor, Empresa, EmpresaCreationError

# -----------------------
# Testes da classe Pessoa
# -----------------------

def test_cria_pessoa():
    try:
        p = Pessoa("João", 20)
    except:
        raise AssertError("Erro ao criar um objeto da classe Pessoa.")
    else:
        assert hasattr(p, "nome"), "Não existe o atributo público nome."
        assert hasattr(p, "idade"), "Não existe o atributo público idade."
        assert hasattr(p, "aniversario"), ("Não existe o método público",
                "aniversario.")

@pytest.mark.parametrize("nome", [5, 6.1, True, [], {}, ()])
def test_cria_pessoa_nome_type_error(nome):
    try:
        p = Pessoa(nome, 20)
    except TypeError:
        pass
    except Exception:
        raise AssertionError("Não levanta TypeError para nome.")
    else:
        raise AssertionError("Criou um objeto da classe Pessoa com nome que",
                "não é string.")

def test_cria_pessoa_nome_value_error():
    try:
        p = Pessoa("", 20)
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para nome.")
    else:
        raise AssertionError("Criou um objeto da classe Pessoa com nome vazio.")

@pytest.mark.parametrize("idade", [5.6, "21", [], {}, ()])
def test_cria_pessoa_idade_type_error(idade):
    try:
        p = Pessoa("João", idade)
    except TypeError:
        pass
    except Exception:
        raise AssertionError("Não leventa TypeError para idade.")
    else:
        raise AssertionError("Criou um objeto da classe Pessoa com idade que",
            "não é inteira.")

@pytest.mark.parametrize("idade", [-1, -80, -100])
def test_cria_pessoa_idade_value_error(idade):
    try:
        p = Pessoa("João", idade)
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para idade.")
    else:
        raise AssertionError("Criou um objeto da classe Pessoa com uma idade",
                "negativa.")

def test_pessoa_altera_nome():
    p = Pessoa("João", 20)
    try:
        p.nome = "Maria"
    except AttributeError:
        pass
    else:
        raise AssertionError("O atributo nome da classe Pessoa tem um método",
                "setter.")

def test_pessoa_altera_idade():
    p = Pessoa("João", 20)
    try:
        p.idade = 25
    except AttributeError:
        pass
    else:
        raise AssertionError("O atributo idade de Pessoa tem um método",
                "setter.")

def test_pessoa_aniversario():
    p = Pessoa("João", 20)
    try:
        p.aniversario()
    except:
        raise AssertionError("Não é possível chamar o método aniversário",
                "de Pessoa.")
    else:
        assert p.idade == 21, ("O método aniversário de Pessoa não está",
                "incrementando a idade")

# ----------------------------
# Testes da classe Funcionario
# ----------------------------

def test_cria_funcionario():
    try:
        f = Funcionario("João", 20, "jsilva@gmail.com", 44)
    except NotImplementedError:
        pass
    else:
        raise AssertionError("Criou um objeto da classe abstrata Funcionario.")

# ----------------------------
# Testes da classe Programador
# ----------------------------

def test_cria_programador():
    try:
        p = Programador("João", 20, "jsilva@gmail.com", 30)
    except:
        raise AssertionError("Erro ao criar um objeto da classe Programador.")
    else:
        assert hasattr(p, "nome"), "Não existe o atributo público nome."
        assert hasattr(p, "idade"), "Não existe o atributo público idade."
        assert hasattr(p, "email"), "Não existe o atributo público email."
        assert hasattr(p, "carga_horaria"), ("Não existe o atributo público",
                "carga_horaria.")
        assert hasattr(p, "aniversario"), ("Não existe o método público",
                "aniversário")
        assert hasattr(p, "calcula_salario"), ("Não existe o método público",
                "calcula_salario.")
        assert hasattr(p, "aumenta_salario"), ("Não existe o método público",
                "aumenta_salario.")

@pytest.mark.parametrize("email", [5, 5.6, True, [], {}, ()])
def test_programador_email_type_error(email):
    try:
        p = Programador("João", 20, email, 30)
    except TypeError:
        pass
    except Exception:
        raise AssertionError("Não levanta TypeError para email.")
    else:
        raise AssertionError("Criou um objeto da classe Programador com email",
                "que não é string.")

@pytest.mark.parametrize("email", ["jsilva", "1@@", "!", "-j@"])
def test_programador_email_value_error(email):
    try:
        p = Programador("João", 20, email, 30) 
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para email.")
    else:
        raise AssertionError("Criou um objeto da classe Programador com email",
                "inválido.")

@pytest.mark.parametrize("carga_horaria", [10, 19, -5, 41, 50])
def test_programador_carga_horaria_value_error(carga_horaria):
    try:
        p = Programador("João", 20, "jsilva@gmail.com", carga_horaria)
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para carga_horaria.")
    else:
        raise AssertionError("Criou um objeto da classe Programador com",
                "carga_horaria inválida.")

@pytest.mark.parametrize("carga_horaria", [10, 19, -5, 41, 50])
def test_programador_altera_carga_horaria_value_error(carga_horaria):
    p = Programador("João", 20, "jsilva@gmail.com", 30)
    try:
        p.carga_horaria = carga_horaria
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para carga_horaria.")
    else:
        raise AssertionError("Criou um objeto da classe Programador com",
                "carga_horaria inválida.")

@pytest.mark.parametrize("carga_horaria", [20, 25, 30, 35, 40])
def test_programador_calcula_salario(carga_horaria):
    p = Programador("João", 20, "jsilva@gmail.com", carga_horaria)
    assert p.calcula_salario() == carga_horaria * 4.5 * 35, ("O cálculo do",
            "salário está incorreto.")

def test_programador_aumenta_salario():
    p = Programador("João", 20, "jsilva@gmail.com", 30)
    salario_antigo = p.calcula_salario()
    p.aumenta_salario()
    salario_novo = p.calcula_salario()
    assert salario_novo == salario_antigo * 1.05, ("O método calcula_salario",
            "não está aumentando o salário corretamente.")

# ---------------------------
# Testes da classe Estagiário
# ---------------------------

def test_cria_estagiario():
    try:
        e = Estagiario("João", 20, "jsilva@gmail.com", 20)
    except:
        raise AssertionError("Erro ao criar um objeto da classe Estagiário.")
    else:
        assert hasattr(e, "nome"), "Não existe o atributo público nome."
        assert hasattr(e, "idade"), "Não existe o atributo público idade."
        assert hasattr(e, "email"), "Não existe o atributo público email."
        assert hasattr(e, "carga_horaria"), ("Não existe o atributo público",
                "carga_horaria.")
        assert hasattr(e, "aniversario"), ("Não existe o método público",
                "aniversário")
        assert hasattr(e, "calcula_salario"), ("Não existe o método público",
                "calcula_salario.")
        assert hasattr(e, "aumenta_salario"), ("Não existe o método público",
                "aumenta_salario.")

@pytest.mark.parametrize("email", [5, 5.6, True, [], {}, ()])
def test_estagiario_email_type_error(email):
    try:
        e = Estagiario("João", 20, email, 30)
    except TypeError:
        pass
    except Exception:
        raise AssertionError("Não levanta TypeError para email.")
    else:
        raise AssertionError("Criou um objeto da classe Estagiario com email",
                "que não é string.")

@pytest.mark.parametrize("email", ["jsilva", "1@@", "!", "-j@"])
def test_estagiario_email_value_error(email):
    try:
        e = Estagiario("João", 20, email, 30) 
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para email.")
    else:
        raise AssertionError("Criou um objeto da classe Estagiario com email",
                "inválido.")

@pytest.mark.parametrize("carga_horaria", [10, 15, -5, 31, 50])
def test_estagiario_carga_horaria_value_error(carga_horaria):
    try:
        e = Estagiario("João", 20, "jsilva@gmail.com", carga_horaria)
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para carga_horaria.")
    else:
        raise AssertionError("Criou um objeto da classe Estagiario com",
                "carga_horaria inválida.")

@pytest.mark.parametrize("carga_horaria", [10, 15, -5, 31, 50])
def test_estagiario_altera_carga_horaria_value_error(carga_horaria):
    e = Estagiario("João", 20, "jsilva@gmail.com", 20)
    try:
        e.carga_horaria = carga_horaria
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para carga_horaria.")
    else:
        raise AssertionError("Criou um objeto da classe Estagiario com",
                "carga_horaria inválida.")

@pytest.mark.parametrize("carga_horaria", [16, 20, 25, 30])
def test_estagiario_calcula_salario(carga_horaria):
    e = Estagiario("João", 20, "jsilva@gmail.com", carga_horaria)
    assert e.calcula_salario() == carga_horaria * 4.5 * 15.5 + 250, ("O",
            "cálculo do salário está incorreto.")

def test_estagiario_aumenta_salario():
    e = Estagiario("João", 20, "jsilva@gmail.com", 20)
    salario_antigo = e.calcula_salario()
    e.aumenta_salario()
    salario_novo = e.calcula_salario()
    assert salario_novo == 15.5 * 1.05 * 20 * 4.5 + 250, ("O método",
            "calcula_salario não está aumentando o salário corretamente.")

# -------------------------
# Testes da classe Vendedor
# -------------------------

def test_cria_vendedor():
    try:
        v = Vendedor("João", 20, "jsilva@gmail.com", 30)
    except:
        raise AssertionError("Erro ao criar um objeto da classe Vendedor")
    else:
        assert hasattr(v, "nome"), "Não existe atributo público nome."
        assert hasattr(v, "idade"), "Não existe atributo público idade."
        assert hasattr(v, "email"), "Não existe o atributo público email."
        assert hasattr(v, "carga_horaria"), ("Não existe o atributo público",
                "carga_horaria.")
        assert hasattr(v, "visitas"), "Não existe o atributo público visitas."
        assert hasattr(v, "aniversario"), ("Não existe o método público",
                "aniversario")
        assert hasattr(v, "calcula_salario"), ("Não existe o método público",
                "calcula_salario.")
        assert hasattr(v, "aumenta_salario"), ("Não existe o método público",
                "aumenta_salario.")
        assert hasattr(v, "realizar_visita"), ("Não existe o método público",
                "realizar_visita.")
        assert hasattr(v, "zerar_visitas"), ("Não existe o método público",
                "zerar_visitas.")

@pytest.mark.parametrize("email", [5, 5.6, True, [], {}, ()])
def test_vendedor_email_type_error(email):
    try:
        v = Vendedor("João", 20, email, 30)
    except TypeError:
        pass
    except Exception:
        raise AssertionError("Não levanta TypeError para email.")
    else:
        raise AssertionError("Criou um objeto da classe Vendedor com email",
                "que não é string.")

@pytest.mark.parametrize("email", ["jsilva", "1@@", "!", "-j"])
def test_vendedor_email_value_error(email):
    try:
        v = Vendedor("João", 20, email, 30) 
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para email.")
    else:
        raise AssertionError("Criou um objeto da classe Vendedor com email",
                "inválido.")

@pytest.mark.parametrize("carga_horaria", [10, 14, -5, 46, 50])
def test_vendedor_carga_horaria_value_error(carga_horaria):
    try:
        v = Vendedor("João", 20, "jsilva@gmail.com", carga_horaria)
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para carga_horaria.")
    else:
        raise AssertionError("Criou um objeto da classe Vendedor com",
                "carga_horaria inválida.")

@pytest.mark.parametrize("carga_horaria", [10, 14, -5, 46, 50])
def test_vendedor_altera_carga_horaria_value_error(carga_horaria):
    v = Vendedor("João", 20, "jsilva@gmail.com", 30)
    try:
        v.carga_horaria = carga_horaria
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para carga_horaria.")
    else:
        raise AssertionError("Criou um objeto da classe Vendedor com",
                "carga_horaria inválida.")

@pytest.mark.parametrize("carga_horaria", [15, 20, 25, 30, 35, 40, 45])
def test_vendedor_calcula_salario(carga_horaria):
    v = Vendedor("João", 20, "jsilva@gmail.com", carga_horaria)
    assert v.calcula_salario() == (30 * 4.5 * carga_horaria + 350 +
        v.visitas * 30), "O cálculo do salário está incorreto."

def test_vendedor_aumenta_salario():
    v = Vendedor("João", 20, "jsilva@gmail.com", 30)
    salario_antigo = v.calcula_salario()
    v.aumenta_salario()
    salario_novo = v.calcula_salario()
    assert salario_novo == 30 * 1.05 * 30 * 4.5 + 350 + v.visitas * 30, ("O ", 
            "método calcula_salario não está aumentando o salário ",
            "corretamente.")

@pytest.mark.parametrize("n_visitas", [5.6, "8", [], (), {}])
def test_vendedor_realizar_visita_type_error(n_visitas):
    v = Vendedor("João", 20, "jsilva@gmail.com", 30)
    try:
        v.realizar_visita(n_visitas)
    except TypeError:
        pass
    except Exception:
        raise AssertionError("Não levanta TypeError para n_visitas.")
    else:
        raise AssertionError("Alterou visitas com n_visitas não inteiro.")

@pytest.mark.parametrize("n_visitas", [-10, -1, 11, 20, 100])
def test_vendedor_realizar_visita_value_error(n_visitas):
    v = Vendedor("João", 20, "jsilva@gmail.com", 30)
    try:
        v.realizar_visita(n_visitas)
    except ValueError:
        pass
    except Exception:
        raise AssertionError("Não levanta ValueError para n_visitas.")
    else:
        raise AssertionError("Alterou visitas com n_visitas inválido.")

def test_vendedor_zerar_visitas():
    v = Vendedor("João", 20, "jsilva@gmail.com", 30)
    v.realizar_visita(5)
    v.zerar_visitas()
    assert v.visitas == 0, "O método zerar_visitas não zera as visitas."

# ------------------------
# Testes da classe Empresa
# ------------------------

def test_cria_empresa():
    try:
        e = Empresa("Macrosft", "08194332000124", "Software",
                [Programador("João", 20, "jsilva@gmail.com", 30)])
    except:
        raise AssertionError("Erro ao criar objeto da classe Empresa.")
    else:
        assert hasattr(e, "nome"), "Não existe o atributo público nome."
        assert hasattr(e, "cnpj"), "Não existe o atributo público cnpj."
        assert hasattr(e, "area_atuacao"), ("Não existe o atributo público",
                "area_atuacao.")
        assert hasattr(e, "equipe"), "Não existe o atributo público equipe."
        assert hasattr(e, "contrata"), "Não existe o método público contrata."
        assert hasattr(e, "folha_pagamento"), ("Não existe o método público",
                "folha_pagamento.")
        assert hasattr(e, "dissidio_anual"), ("Não existe o método público",
                "dissidio_anual.")
        assert hasattr(e, "listar_visitas"), ("Não existe o método público",
                "listar_visitas.")
        assert hasattr(e, "zerar_visitas_vendedores"), ("Não existe o método",
                "público zerar_visitas_vendedores.")

@pytest.mark.parametrize("nome", [5, 5.6, True, [], (), {}])
def test_empresa_nome(nome):
    try:
        e = Empresa(nome, "08194332000124", "Software",
                [Programador("João", 20, "jsilva@gmail.com", 30)])
    except EmpresaCreationError:
        pass
    except Exception:
        raise AssertionError("Não levanta EmpresaCreationError para nome.")
    else:
        raise AssertionError("Criou um objeto da classe Empresa com nome",
                "inválido.")

@pytest.mark.parametrize("cnpj", [5, 5.6, True, [], (), {}])
def test_empresa_cnpj(cnpj):
    try:
        e = Empresa("Macrosoft", cnpj, "Software",
                [Programador("João", 20, "jsilva@gmail.com", 30)])
    except EmpresaCreationError:
        pass
    except Exception:
        raise AssertionError("Não levanta EmpresaCreationError para cnpj.")
    else:
        raise AssertionError("Criou um objeto da classe Empresa com cnpj",
                "inválido.")

@pytest.mark.parametrize("area_atuacao", [5, 5.6, True, [], (), {}])
def test_empresa_area_atuacao(area_atuacao):
    try:
        e = Empresa("Macrosoft", "08194332000124", area_atuacao,
                [Programador("João", 20, "jsilva@gmail.com", 30)])
    except EmpresaCreationError:
        pass
    except Exception:
        raise AssertionError("Não levanta EmpresaCreationError para",
                "area_atuacao.")
    else:
        raise AssertionError("Criou um objeto da classe Empresa com",
                "area_atuacao inválida.")

@pytest.mark.parametrize("equipe", [[Pessoa("Maria", 20)], [5, 6, 7],
    [Vendedor("José", 30, "jsantos@gmail.com", 30), Pessoa("Maria", 20)]])
def test_empresa_equipe(equipe):
    try:
        e = Empresa("Macrosoft", "08194332000124", "Software", equipe)
    except EmpresaCreationError:
        pass
    except Exception:
        raise AssertionError("Não levanta EmpresaCreationError para equipe.")
    else:
        raise AssertionError("Criou um objeto da classe Empresa com equipe",
                "inválida.")

@pytest.mark.parametrize("novo_funcionario", [int, Pessoa("Maria", 20), [], str])
def test_empresa_contrata_type_error(novo_funcionario):
    e = Empresa("Macrosoft", "08194332000124", "Software",
            [Programador("João", 20, "jsilva@gmail.com", 30)])
    try:
        e.contrata(novo_funcionario)
    except TypeError:
        pass
    except Exception:
        raise AssertionError("Não levanta TypeError para novo_funcionario.")
    else:
        raise AssertionError("Adicionou novo_funcionario inválido à equipe.")

@pytest.mark.parametrize("novo_funcionario",
        [Programador("João", 20, "jsilva@gmail.com", 30),
        Vendedor("José", 30, "jsantos@gmail.com", 30),
        Estagiario("Ana", 18, "ana@gmail.com", 20)])
def teste_empresa_contrata_valido(novo_funcionario):
    e = Empresa("Macrosoft", "08194332000124", "Software",
            [Programador("João", 20, "jsilva@gmail.com", 30)])
    try:
        e.contrata(novo_funcionario)
    except:
        raise AssertionError("Não aceita subtipos de Funcionario")
    else:
        pass

def test_empresa_contrata_adiciona():
    funcionarios = [Programador("João", 20, "jsilva@gmail.com", 30),
            Vendedor("José", 30, "jsantos@gmail.com", 30)]
    e = Empresa("Macrosoft", "08194332000124", "Software", [funcionarios[0]])
    e.contrata(funcionarios[1])
    assert e.equipe == funcionarios, ("O método contrata não está",
            "adicionando novo_funcionario à equipe.")

def test_empresa_folha_pagamento():
    funcionarios = [Programador("João", 20, "jsilva@gmail.com", 30),
            Vendedor("José", 30, "jsantos@gmail.com", 30),
            Estagiario("Ana", 18, "ana@gmail.com", 20)]
    e = Empresa("Macrosoft", "08194332000124", "Software", funcionarios)
    e.equipe[1].realizar_visita(5)
    salario_esperado = ((30 * 4.5 * 35) +
            (30 * 4.5 * 30 + 350 + 30 * 5) +
            (20 * 4.5 * 15.5 + 250))
    assert salario_esperado == e.folha_pagamento(), ("O cálculo de",
            "folha_pagamento está incorreto.")

def test_empresa_dissidio_anual():
    funcionarios = [Programador("João", 20, "jsilva@gmail.com", 30),
            Vendedor("José", 30, "jsantos@gmail.com", 30),
            Estagiario("Ana", 18, "ana@gmail.com", 20)]
    e = Empresa("Macrosoft", "08194332000124", "Software", funcionarios)
    e.equipe[1].realizar_visita(5)
    e.dissidio_anual()
    salario_esperado = ((30 * 4.5 * 35 * 1.05) +
            (30 * 4.5 * 30 * 1.05 + 350 + 30 * 5) +
            (20 * 4.5 * 15.5 * 1.05 + 250))
    assert salario_esperado == e.folha_pagamento(), ("O cálculo de",
            "dissidio_anual está incorreto.")

def test_empresa_listar_visitas():
    funcionarios = [Programador("João", 20, "jsilva@gmail.com", 30),
            Vendedor("José", 30, "jsantos@gmail.com", 30),
            Estagiario("Ana", 18, "ana@gmail.com", 20),
            Vendedor("Maria", 20, "maria@gmail.com", 40)]
    e = Empresa("Macrosoft", "08194332000124", "Software", funcionarios)
    e.equipe[1].realizar_visita(5)
    e.equipe[3].realizar_visita(1)
    lista_visitas_esperada = {"jsantos@gmail.com": 5, "maria@gmail.com": 1}
    assert lista_visitas_esperada == e.listar_visitas(), ("O método",
            "listar_visitas está incorreto.")

def test_zerar_visitas_vendedores():
    funcionarios = [Programador("João", 20, "jsilva@gmail.com", 30),
            Vendedor("José", 30, "jsantos@gmail.com", 30),
            Estagiario("Ana", 18, "ana@gmail.com", 20),
            Vendedor("Maria", 20, "maria@gmail.com", 40)]
    e = Empresa("Macrosoft", "08194332000124", "Software", funcionarios)
    e.equipe[1].realizar_visita(5)
    e.equipe[3].realizar_visita(1)
    e.zerar_visitas_vendedores()
    assert (e.equipe[1].visitas, e.equipe[3].visitas) == (0, 0), ("O método",
            "zerar_visitas_vendedores não está zerando as visitas.")
    


