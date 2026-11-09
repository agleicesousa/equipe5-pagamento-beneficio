from blockchain import BlockchainSimulada
from modelos import EntidadePagadora
from pagamento import PagamentoBeneficio


def demonstracao() -> None:
    blockchain = BlockchainSimulada()
    blockchain.registrar_atestado("B002", emissor="ORACULO")
    blockchain.registrar_atestado("B003", emissor="OUTRA_FONTE")
    pagamento = PagamentoBeneficio(blockchain)

    casos = [
        ("Estado, sem atestado", EntidadePagadora.ESTADO, "B001"),
        ("Fundo de Pensão, sem atestado", EntidadePagadora.FUNDO_DE_PENSAO, "B001"),
        ("Estado, com atestado do Oráculo", EntidadePagadora.ESTADO, "B002"),
        ("Entidade não autorizada", EntidadePagadora.OUTRA, "B001"),
        ("Atestado de outra fonte", EntidadePagadora.ESTADO, "B003"),
    ]

    for descricao, pagador, beneficiario in casos:
        permitido = pagamento.pode_transferir(pagador, beneficiario)
        print(f"{descricao}: {'AUTORIZADO' if permitido else 'BLOQUEADO'}")


if __name__ == "__main__":
    demonstracao()
