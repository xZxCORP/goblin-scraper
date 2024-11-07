from typing import Literal, Optional
from pydantic import BaseModel


class VehicleForm(BaseModel):
    nom: Optional[str]
    prenom: str | None = None
    numeroFormule: str
    immat: str
    siren: str | None = None
    raison_sociale: str | None = None
    vin: str | None = None
    type: Literal["pro", "particulier"] = "particulier"
