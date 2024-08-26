from sqlalchemy import Table, Column, Integer, ForeignKey, String, Boolean, Enum
from sqlalchemy.orm import relationship
from src.core.database import Base

# Association table for doctor-patient relationships
doctor_patient_association = Table(
    'doctor_patient',
    Base.metadata,
    Column('doctor_id', Integer, ForeignKey('users.id')),
    Column('patient_id', Integer, ForeignKey('users.id'))
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum('woman', 'doctor', name='user_roles'), nullable=False)
    days_pregnant = Column(Integer, nullable=True)
    num_of_pregnancies = Column(Integer, nullable=False)
    num_of_failed_pregnancies = Column(Integer, nullable=False)
    first_time_pregnancy = Column(Boolean, nullable=False)
    prev_failed_pregnancies = Column(Boolean, nullable=False)
    med_conditions = Column(Enum('diabetes', 'high blood pressure', 'asthma',
                                 'fertility issues', 'mental health conditions',
                                 'obesity', 'other', name='med_conditions_enum'), nullable=False)

    # Self-referential many-to-many relationship for doctors and patients
    patients = relationship(
        'User',
        secondary=doctor_patient_association,
        primaryjoin=id == doctor_patient_association.c.doctor_id,
        secondaryjoin=id == doctor_patient_association.c.patient_id,
        backref='doctors'
    )
