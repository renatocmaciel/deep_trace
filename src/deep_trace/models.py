from pydantic import BaseModel, RootModel
from typing import List, Optional, Any



class SocialMedia(BaseModel):
    linkedin: Optional[str]
    instagram: Optional[str]
    facebook: Optional[str]

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
    title: str
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
    mentions: List[BaseModel]
    legal_verification: List[LegalVerificationItem]
    social_media_images: ImageCollection
    observations_and_data_reconciliation: List[ObservationItem]
