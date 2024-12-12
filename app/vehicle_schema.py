import typing


class InfosImport(typing.TypedDict):
    datePremiereImmatEtranger: str
    dateImportFrance: typing.Any
    isImported: bool
    immatriculationOrigine: typing.Any
    codePaysOrigine: typing.Any
    nomPaysOrigine: typing.Any


class Usage(typing.TypedDict):
    listeDesUsages: list
    isAgricole: bool
    isCollection: bool


class Gages(typing.TypedDict):
    hasGages: bool
    informations: list


class Dvs(typing.TypedDict):
    hasDvs: bool
    informations: list


class Suspensions(typing.TypedDict):
    hasSuspensions: bool
    informations: list


class Informations(typing.TypedDict):
    oves: list
    oveis: list
    otcisPv: list
    otcis: list


class Oppositions(typing.TypedDict):
    hasOppositions: bool
    informations: Informations


class SituationAdmin(typing.TypedDict):
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


class Accidents(typing.TypedDict):
    nbSinistres: int
    dateDerniereResolution: typing.Any
    dateDernierSinistre: typing.Any


class Historique(typing.TypedDict):
    opaDate: str
    opaType: str


class PersonnePhysique(typing.TypedDict):
    nomNaissance: str
    prenom: str


class PersonneMorale(typing.TypedDict):
    raisonSociale: str
    siren: str


class Proprietaire(typing.TypedDict):
    personnePhysique: PersonnePhysique
    personneMorale: PersonneMorale
    codePostal: str


class CertificatImmatriculation(typing.TypedDict):
    age: int
    dateEmission: str


class Utac(typing.TypedDict):
    updateDate: str
    status: typing.Any
    ct: list


class SivPhysique(typing.TypedDict):
    nom: str
    prenom: str
    immat: str
    numeroFormule: str


class IncomingQuery(typing.TypedDict):
    SivPhysique: SivPhysique


class Caracteristiques(typing.TypedDict):
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


class Infos(typing.TypedDict):
    nbTitulaires: int
    datePremiereImmatriculationFrance: str
    datePremiereImmatSiv: str
    plaqueImmatriculation: str
    dateConvertionSiv: typing.Any


class Vehicule(typing.TypedDict):
    caracteristiques: Caracteristiques
    infos: Infos
    infosImport: InfosImport
    usage: Usage
    situationAdmin: SituationAdmin
    accidents: Accidents
    historique: list[Historique]


class VehicleRequestOutput(typing.TypedDict):
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
