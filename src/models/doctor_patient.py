from sqlalchemy import Column, Integer, ForeignKey, Table, UniqueConstraint
from src.core.database import Base

class DoctorPatient(Base):
    __tablename__ = "doctor_patient"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # You can add additional fields here if needed, such as:
    # start_date = Column(Date)
    # notes = Column(String)

    # To ensure a doctor can't be associated with the same patient more than once:
    __table_args__ = (
        UniqueConstraint('doctor_id', 'patient_id', name='unique_doctor_patient'),
    )