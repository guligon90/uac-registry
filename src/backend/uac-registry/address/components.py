# Base imports
from enum import Enum
from typing import Any, Tuple, Text


class BaseEnum(Enum):
    """Base enumeration class with an auxiliary
    method for building the choices for the
    DB address fields"""
    @classmethod
    def choices(cls) -> Tuple[Tuple[str, Any], ...]:
        return tuple((e.name, e.value) for e in cls)


class States(BaseEnum):
    """Brazilian states"""
    # Northern region
    AC = 'Acre'
    AP = 'Amapá'
    AM = 'Amazonas'
    PA = 'Pará'
    RO = 'Rondônia'
    RR = 'Roraima'
    TO = 'Tocantins'

    # Northeast region
    AL = 'Alagoas'
    BA = 'Bahia'
    CE = 'Ceará'
    PB = 'Paraíba'
    PE = 'Pernambuco'
    PI = 'Piauí'
    MA = 'Maranhão'
    RN = 'Rio Grande do Norte'
    SE = 'Sergipe'

    # Southeast region
    ES = 'Espírito Santo'
    MG = 'Minas Gerais'
    RJ = 'Rio de Janeiro'
    SP = 'São Paulo'

    # Midwest region
    DF = 'Distrito Federal'
    GO = 'Goiás'
    MS = 'Mato Grosso do Sul'
    MT = 'Mato Grosso'

    # Southern region
    PR = 'Paraná'
    RS = 'Rio Grande do Sul'
    SC = 'Santa Catarina'


class PublicPlaces(BaseEnum):
    """Abbreviations and names for the most common
    public places (logradouros in portuguese)"""
    AER = 'Aeroporto'
    AL = 'Alameda'
    AV = 'Avenida'
    BC = 'Beco'
    BL = 'Bloco'
    BO = 'Bosque'
    CAM = 'Caminho'
    ESC = 'Escadinha'
    ETC = 'Estação'
    EST = 'Estrada'
    FAZ = 'Fazenda'
    FER = 'Ferrovia'
    GLR = 'Galeria'
    LAD = 'Ladeira'
    LGO = 'Largo'
    LIM = 'Limite'
    LINHA = 'Linha de Transmissão'
    MANG = 'Mangue'
    MAR = 'Margem'
    MT = 'Monte'
    MRO = 'Morro'
    PQ = 'Parque'
    PCA = 'Praça'
    PR = 'Praia'
    PRL = 'Prologamento'
    PAS = 'Passagem'
    RODOVIA = 'Rodovia'
    R = 'Rua'
    SQD = 'Superquadra'
    TR = 'Travessa'
    VD = 'Viaduto'
    VL = 'Vila'

    @classmethod
    def max_len(cls) -> int:
        lengths = [len(e.name) for e in cls]
        return max(lengths)


def format_postal_code(code: str) -> str:
    return f'{code[:2]}.{code[2:5]}-{code[5:9]}'


def format_address(address: dict) -> Text:
    """
    Logradouro Rua, Número
    Complemento - Bairro
    Cidade - Estado
    CEP

    More info:
    https://www.correios.com.br/enviar-e-receber/precisa-de-ajuda/como-enderecar-cartas-e-encomendas
    """
    public_place = address.get('pulic_place')
    name = address.get('name')
    number = address.get('number')
    postal_code = address.get('postal_code')

    formatted_cep = format_postal_code(postal_code)
    formatted_address = f'{public_place} {name}, {number}\n'

    additional_info = address.get('additional_info')
    district = address.get('district')

    if additional_info and district:
        formatted_address += f'{additional_info} - {district}\n'
    elif additional_info and not district:
        formatted_address += f'{additional_info}\n'
    elif district and not additional_info:
        formatted_address += f'{district}\n'

    city = address.get('city')
    state = address.get('state')
    formatted_address += f'{city} - {state}\n{formatted_cep}'

    return formatted_address
