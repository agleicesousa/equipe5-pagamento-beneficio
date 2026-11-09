from typing import Protocol
from modelos import AtestadoObito


class ConsultaBlockchain(Protocol):
    def existe_atestado_obito_do_oraculo(self, id_beneficiario: str) -> bool:
        ...


class BlockchainSimulada:
    def __init__(self) -> None:
        self._atestados: list[AtestadoObito] = []

    def registrar_atestado(self, id_beneficiario: str, emissor: str) -> None:
        self._atestados.append(AtestadoObito(id_beneficiario, emissor))

    def existe_atestado_obito_do_oraculo(self, id_beneficiario: str) -> bool:
        return any(
            atestado.id_beneficiario == id_beneficiario
            and atestado.emissor == "ORACULO"
            for atestado in self._atestados
        )
