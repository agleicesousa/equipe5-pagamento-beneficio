import unittest

from blockchain import BlockchainSimulada
from modelos import EntidadePagadora
from pagamento import PagamentoBeneficio


class TestPagamentoBeneficio(unittest.TestCase):
    def setUp(self) -> None:
        self.blockchain = BlockchainSimulada()
        self.pagamento = PagamentoBeneficio(self.blockchain)

    def test_estado_sem_atestado_pode_transferir(self) -> None:
        self.assertTrue(self.pagamento.pode_transferir(EntidadePagadora.ESTADO, "B001"))

    def test_fundo_de_pensao_sem_atestado_pode_transferir(self) -> None:
        self.assertTrue(
            self.pagamento.pode_transferir(EntidadePagadora.FUNDO_DE_PENSAO, "B001")
        )

    def test_estado_com_atestado_do_oraculo_nao_pode_transferir(self) -> None:
        self.blockchain.registrar_atestado("B002", "ORACULO")
        self.assertFalse(self.pagamento.pode_transferir(EntidadePagadora.ESTADO, "B002"))

    def test_fundo_com_atestado_do_oraculo_nao_pode_transferir(self) -> None:
        self.blockchain.registrar_atestado("B002", "ORACULO")
        self.assertFalse(
            self.pagamento.pode_transferir(EntidadePagadora.FUNDO_DE_PENSAO, "B002")
        )

    def test_entidade_nao_autorizada_nao_pode_transferir(self) -> None:
        self.assertFalse(self.pagamento.pode_transferir(EntidadePagadora.OUTRA, "B001"))

    def test_atestado_de_outra_fonte_nao_bloqueia_transferencia(self) -> None:
        self.blockchain.registrar_atestado("B003", "OUTRA_FONTE")
        self.assertTrue(self.pagamento.pode_transferir(EntidadePagadora.ESTADO, "B003"))

    def test_atestado_de_outro_beneficiario_nao_bloqueia(self) -> None:
        self.blockchain.registrar_atestado("B002", "ORACULO")
        self.assertTrue(self.pagamento.pode_transferir(EntidadePagadora.ESTADO, "B001"))

    def test_identificador_vazio_nao_pode_transferir(self) -> None:
        self.assertFalse(self.pagamento.pode_transferir(EntidadePagadora.ESTADO, ""))

    def test_identificador_so_com_espacos_nao_pode_transferir(self) -> None:
        self.assertFalse(self.pagamento.pode_transferir(EntidadePagadora.ESTADO, "   "))

    def test_identificador_invalido_nao_pode_transferir(self) -> None:
        self.assertFalse(self.pagamento.pode_transferir(EntidadePagadora.ESTADO, None))

    def test_falha_na_consulta_bloqueia_transferencia(self) -> None:
        class BlockchainIndisponivel:
            def existe_atestado_obito_do_oraculo(self, id_beneficiario: str) -> bool:
                raise ConnectionError("Blockchain indisponível")

        pagamento = PagamentoBeneficio(BlockchainIndisponivel())
        self.assertFalse(pagamento.pode_transferir(EntidadePagadora.ESTADO, "B001"))


if __name__ == "__main__":
    unittest.main()
