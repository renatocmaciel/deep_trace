from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class ProfileDBModel(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, autoincrement=True)
    context = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=True)
    age_range = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    marital_status = Column(String, nullable=True)
    approximate_location = Column(String, nullable=True)
    profession = Column(String, nullable=True)
    current_company = Column(String, nullable=True)

    social_media = Column(JSONB, nullable=True)
    societary_status = Column(JSONB, nullable=True)
    interests = Column(JSONB, nullable=True)
    mentions = Column(JSONB, nullable=True)
    legal_verification = Column(JSONB, nullable=True)
    social_media_images = Column(JSONB, nullable=True)
    observations_and_data_reconciliation = Column(JSONB, nullable=True)

    def to_dict(self):
        """Convert SQLAlchemy object to dictionary format for compatibility."""
        return {
            "title": self.title,
            "full_name": self.full_name,
            "phone": self.phone,
            "email": self.email,
            "age_range": self.age_range,
            "gender": self.gender,
            "marital_status": self.marital_status,
            "approximate_location": self.approximate_location,
            "profession": self.profession,
            "current_company": self.current_company,
            "social_media": self.social_media,
            "societary_status": self.societary_status,
            "interests": self.interests,
            "mentions": self.mentions,
            "legal_verification": self.legal_verification,
            "social_media_images": self.social_media_images,
            "observations_and_data_reconciliation": self.observations_and_data_reconciliation,
        }
