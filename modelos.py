from dataclasses import dataclass
from enum import Enum


class EntidadePagadora(Enum):
    ESTADO = "Estado"
    FUNDO_DE_PENSAO = "Fundo de Pensão"
    OUTRA = "Outra entidade"


@dataclass(frozen=True)
class AtestadoObito:
    id_beneficiario: str
    emissor: str
