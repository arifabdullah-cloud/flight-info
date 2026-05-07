from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func

from app.db.database import Base


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)

    icao24 = Column(String, index=True)
    callsign = Column(String)
    origin_country = Column(String)

    longitude = Column(Float)
    latitude = Column(Float)

    baro_altitude = Column(Float)
    velocity = Column(Float)

    true_track = Column(Float)
    vertical_rate = Column(Float)

    geo_altitude = Column(Float)

    squawk = Column(String)

    on_ground = Column(Boolean)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
