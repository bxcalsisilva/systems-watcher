from pydantic import BaseModel
from typing import List, Optional


class Location(BaseModel):
    name: str
    city: str
    folder_id: Optional[str] = None
    technologies: List[str]


class Settings:
    root_folder_id: str = "1D8_692LPsTny5RMpvM7X0One3Mv4bp3L"
    technologies: List[str] = ["PERC", "HIT", "CIGS"]
    locations: List[Location] = [
        Location(
            name="PUCP",
            city="Lima",
            folder_id="1DFy80y62O8hY2hec6oKGuxUjOwKRrSZ_",
            technologies=technologies,
        ),
        Location(
            name="UNI",
            city="Lima",
            folder_id="16NsFSIrz3yqu8Z5yvuBAQ6zT47BLIeHw",
            technologies=technologies,
        ),
        Location(
            name="UNTRM",
            city="Chachapoyas",
            folder_id="1HyEhEF1XmfMXAiwIvHVzplDSBEXisTOK",
            technologies=technologies,
        ),
        Location(
            name="UNAJ",
            city="Juliaca",
            folder_id="1INvsEEidJLTTkWIwihwjqFawlJyoRNVe",
            technologies=technologies,
        ),
        Location(
            name="UNJBG",
            city="Tacna",
            folder_id="1HvDySv7lANeVZ5asj4qNUNl3hRYi4ygK",
            technologies=technologies,
        ),
        Location(
            name="UNSA",
            city="Arequipa",
            folder_id="1HmTuEzj-2VyzQ5DjO6GUWxOKWxt5dm1_",
            technologies=technologies,
        ),
    ]
