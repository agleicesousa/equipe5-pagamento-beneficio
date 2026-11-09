from blockchain import ConsultaBlockchain
from modelos import EntidadePagadora


class PagamentoBeneficio:
    PAGADORES_AUTORIZADOS = {
        EntidadePagadora.ESTADO,
        EntidadePagadora.FUNDO_DE_PENSAO,
    }

    def __init__(self, blockchain: ConsultaBlockchain) -> None:
        self.blockchain = blockchain

    def pode_transferir(
        self, pagador: EntidadePagadora, id_beneficiario: str
    ) -> bool:
        if pagador not in self.PAGADORES_AUTORIZADOS:
            return False

        if not isinstance(id_beneficiario, str) or not id_beneficiario.strip():
            return False

        try:
            ha_atestado = self.blockchain.existe_atestado_obito_do_oraculo(
                id_beneficiario
            )
            return ha_atestado is False
        except Exception:
            return False
