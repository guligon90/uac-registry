# Base imports
from enum import Enum


class BaseEnum(Enum):
    """Base enumeration class with an auxiliary
    method for building the choices for the
    DB address fields"""
    @classmethod
    def choices(cls):
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


def format_address(address):
    """
    Logradouro Rua, Número
    Complemento - Bairro
    Cidade - Estado
    CEP

    More info:
    https://www.correios.com.br/enviar-e-receber/precisa-de-ajuda/como-enderecar-cartas-e-encomendas
    """
    formatted_cep = format_postal_code(address.postal_code)
    number = address.number if address.number is not None else 's/n'
    formatted_address = f'{address.public_place} {address.name}, {number}\n'

    if address.additional_info and address.district:
        formatted_address += f'{address.additional_info} - {address.district}\n'
    elif address.additional_info and not address.district:
        formatted_address += f'{address.additional_info}\n'
    elif address.district and not address.additional_info:
        formatted_address += f'{address.district}\n'

    formatted_address += f'{address.city} - {address.state}\n{formatted_cep}'

    return formatted_address
