from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
  __tablename__ = 'customers'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  reservations = relationship('Reservation', back_populates='customer')

  def __init__(self, name):
    self.name = name

# Room class
class Room(Base):
  __tablename__ = 'rooms'

  id = Column(Integer, primary_key=True)
  number = Column(Integer)
  capacity = Column(Integer)
  reservations = relationship('Reservation', back_populates='room')

  def __init__(self, number, capacity):
    self.number = number
    self.capacity = capacity


class Reservation(Base):
  __tablename__ = 'reservations'

  id = Column(Integer, primary_key=True)
  customer_id = Column(Integer, ForeignKey('customers.id'))
  room_id = Column(Integer, ForeignKey('rooms.id'))
  check_in = Column(String)
  check_out = Column(String)

  customer = relationship('Customer', back_populates='reservations')
  room = relationship('Room', back_populates='reservations')

  def __init__(self, customer, room, check_in, check_out):
    self.customer = customer
    self.room = room
    self.check_in = check_in
    self.check_out = check_out


