import typing
from dataclasses import dataclass


@dataclass
class InfosImport:
    datePremiereImmatEtranger: str
    dateImportFrance: typing.Any
    isImported: bool
    immatriculationOrigine: typing.Any
    codePaysOrigine: typing.Any
    nomPaysOrigine: typing.Any


@dataclass
class Usage:
    listeDesUsages: list
    isAgricole: bool
    isCollection: bool


@dataclass
class Gages:
    hasGages: bool
    informations: list


@dataclass
class Dvs:
    hasDvs: bool
    informations: list


@dataclass
class Suspensions:
    hasSuspensions: bool
    informations: list


@dataclass
class Informations:
    oves: list
    oveis: list
    otcisPv: list
    otcis: list


@dataclass
class Oppositions:
    hasOppositions: bool
    informations: Informations


@dataclass
class SituationAdmin:
    isApteACirculer: bool
    isCiAnnule: bool
    dateAnnulation: typing.Any
    isCiVole: bool
    isDuplicata: bool
    gages: Gages
    isCiPerdu: bool
    dvs: Dvs
    suspensions: Suspensions
    oppositions: Oppositions
    isVehVole: bool


@dataclass
class Accidents:
    nbSinistres: int
    dateDerniereResolution: typing.Any
    dateDernierSinistre: typing.Any


@dataclass
class Historique:
    opaDate: str
    opaType: str


@dataclass
class PersonnePhysique:
    nomNaissance: str
    prenom: str


@dataclass
class PersonneMorale:
    raisonSociale: str
    siren: str


@dataclass
class Proprietaire:
    personnePhysique: PersonnePhysique
    personneMorale: PersonneMorale
    codePostal: str


@dataclass
class CertificatImmatriculation:
    age: int
    dateEmission: str


@dataclass
class Utac:
    updateDate: str
    status: typing.Any
    ct: list


@dataclass
class SivPhysique:
    nom: str
    prenom: str
    immat: str
    numeroFormule: str


@dataclass
class IncomingQuery:
    SivPhysique: SivPhysique


@dataclass
class Caracteristiques:
    marque: str
    nomCommercial: str
    puissanceCv: int
    couleur: str
    tvv: str
    numCnit: str
    typeReception: str
    vin: str
    champF1: int
    champF2: int
    champF3: int
    champG: int
    champG1: int
    categorie: str
    genre: str
    carrosserieCe: str
    carrosserieNationale: str
    numeroReception: str
    cylindree: int
    puissanceNette: int
    energie: str
    nbPlacesAssises: int
    nbPlacesDebout: int
    niveauSonore: int
    vitesseMoteur: int
    co2: int
    pollution: str
    rapportPuissMasse: int


@dataclass
class Infos:
    nbTitulaires: int
    datePremiereImmatriculationFrance: str
    datePremiereImmatSiv: str
    plaqueImmatriculation: str
    dateConvertionSiv: typing.Any


@dataclass
class Vehicule:
    caracteristiques: Caracteristiques
    infos: Infos
    infosImport: InfosImport
    usage: Usage
    situationAdmin: SituationAdmin
    accidents: Accidents
    historique: list[Historique]


@dataclass
class VehicleRequestOutput:
    vehicule: Vehicule
    proprietaire: Proprietaire
    certificatImmatriculation: CertificatImmatriculation
    utac: Utac
    clefAcheteur: str
    validiteClefAcheteur: str
    messageUsager: str
    plaqImmatHash: str
    incomingQuery: IncomingQuery
    dateMiseAJour: str
