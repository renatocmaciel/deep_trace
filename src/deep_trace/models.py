from pydantic import BaseModel
from typing import List, Optional
from typing import List, Optional
from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "OK"

class SocialMedia(BaseModel):
    linkedin: Optional[str] = None
    instagram: Optional[str] = None
    facebook: Optional[str] = None
    tiktok: Optional[str] = None
    github: Optional[str] = None

class SocietaryStatusItem(BaseModel):
    company: str
    cnpj: str
    source: str

class InterestItem(BaseModel):
    interest: str
    description: str
    source: List[str]

class MentionItem(BaseModel):
    mention: str
    description: str
    source: List[str]

class LegalVerificationItem(BaseModel):
    legal_mention: str
    description: str
    source: List[str]

class ObservationItem(BaseModel):
    observation: str
    description: str
    source: List[str]

class EscavadorData(BaseModel):
    data: str
    description: str
    source: List[str]

class BasicInfo(BaseModel):
    linkedin_profile_photo: str
    name: str
    position: str
    location: str
    profile_link: str

class DeepSearchInfo(BaseModel):
    email: str
    social_media: SocialMedia
    societary_status: List[SocietaryStatusItem]
    mentions: List[MentionItem]
    interests: List[InterestItem]
    legal_verification: List[LegalVerificationItem]
    escavador_data: List[EscavadorData]

class ImageCollection(BaseModel):
    social_media_images: List[str]

class ImageAnalysis(BaseModel):
    age_range: str
    gender: str
    marital_status: str
    interests: List[InterestItem]
    people_descriptions: List[ObservationItem]

class Profile(BaseModel):
    title: Optional[str] = None
    full_name: str
    phone: str
    email: str
    age_range: str
    gender: str
    marital_status: str
    approximate_location: str
    profession: str
    current_company: str
    social_media: SocialMedia
    societary_status: List[SocietaryStatusItem]
    interests: List[InterestItem]
    mentions: List[MentionItem]
    legal_verification: List[LegalVerificationItem]
    social_media_images: ImageCollection
    observations_and_data_reconciliation: List[ObservationItem]

# class Profile(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     title: Optional[str] = Field(default=None)  # Allow NULL values
#     full_name: str
#     phone: str
#     email: Optional[str] = Field(default=None)
#     age_range: Optional[str] = Field(default=None)
#     gender: Optional[str] = Field(default=None)
#     marital_status: Optional[str] = Field(default=None)
#     approximate_location: str
#     profession: Optional[str] = Field(default=None)
#     current_company: Optional[str] = Field(default=None)
#     social_media: dict = Field(sa_column=Column(JSON))
#     societary_status: list = Field(sa_column=Column(JSON))
#     interests: list = Field(sa_column=Column(JSON))
#     mentions: list = Field(sa_column=Column(JSON))
#     legal_verification: list = Field(sa_column=Column(JSON))
#     social_media_images: dict = Field(sa_column=Column(JSON))
#     observations_and_data_reconciliation: list = Field(sa_column=Column(JSON))
