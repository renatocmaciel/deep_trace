import os
from sqlalchemy.orm import sessionmaker
from deep_trace.database.model import ProfileDBModel, Base
from sqlalchemy import create_engine
from deep_trace.models import Profile, SocialMedia, SocietaryStatusItem, InterestItem, MentionItem, LegalVerificationItem, ImageCollection, ObservationItem
import os


DATABASE_URL = os.environ["DATABASE_URL"]


sync_engine = create_engine(DATABASE_URL, echo=True, future=True)




SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sync_engine,
)



def save_profile_to_db(profile: Profile, inputs: dict) -> bool:
    """
    Saves a Profile to the database, including the provided context.

    :param profile: Profile Pydantic model
    :param inputs: Dict with "full_name", "phone", and "context"
    """
    db = SessionLocal()
    try:
        profile_db = ProfileDBModel(
            full_name=inputs['full_name'],
            phone=inputs['phone'],
            email=profile.email,
            age_range=profile.age_range,
            gender=profile.gender,
            marital_status=profile.marital_status,
            approximate_location=profile.approximate_location,
            profession=profile.profession,
            current_company=profile.current_company,
            social_media=profile.social_media.dict(),
            societary_status=[item.dict() for item in profile.societary_status],
            interests=[item.dict() for item in profile.interests],
            mentions=[item.dict() for item in profile.mentions],
            legal_verification=[item.dict() for item in profile.legal_verification],
            social_media_images=profile.social_media_images.dict(),
            observations_and_data_reconciliation=[item.dict() for item in profile.observations_and_data_reconciliation],
            context=inputs["context"],
        )

        db.add(profile_db)
        db.commit()
        db.refresh(profile_db)
        return True

    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def search_profile_in_db(inputs: dict) -> Profile:
    """
    Searches for a profile in the database that matches full_name, phone, and context
    and returns a Profile Pydantic model.

    :param inputs: Dict with "full_name", "phone", and "context"
    :return: Profile instance or None
    """
    db = SessionLocal()
    try:
        profile_db = db.query(ProfileDBModel).filter(
            ProfileDBModel.full_name == inputs["full_name"],
            ProfileDBModel.phone == inputs["phone"],
            ProfileDBModel.context == inputs["context"]
        ).first()

        if profile_db is None:
            return None  # No match found

        return Profile(
            full_name=profile_db.full_name,
            phone=profile_db.phone,
            email=profile_db.email,
            age_range=profile_db.age_range,
            gender=profile_db.gender,
            marital_status=profile_db.marital_status,
            approximate_location=profile_db.approximate_location,
            profession=profile_db.profession,
            current_company=profile_db.current_company,
            social_media=(
                SocialMedia(**profile_db.social_media)
                if profile_db.social_media
                else SocialMedia()
            ),
            societary_status=(
                [
                    SocietaryStatusItem(**item)
                    for item in profile_db.societary_status
                ]
                if profile_db.societary_status
                else []
            ),
            interests=(
                [InterestItem(**item) for item in profile_db.interests]
                if profile_db.interests
                else []
            ),
            mentions=(
                [MentionItem(**item) for item in profile_db.mentions]
                if profile_db.mentions
                else []
            ),
            legal_verification=(
                [
                    LegalVerificationItem(**item)
                    for item in profile_db.legal_verification
                ]
                if profile_db.legal_verification
                else []
            ),
            social_media_images=(
                ImageCollection(**profile_db.social_media_images)
                if profile_db.social_media_images
                else ImageCollection(social_media_images=[])
            ),
            observations_and_data_reconciliation=(
                [
                    ObservationItem(**item)
                    for item in profile_db.observations_and_data_reconciliation
                ]
                if profile_db.observations_and_data_reconciliation
                else []
            ),
        )
    finally:
        db.close()
