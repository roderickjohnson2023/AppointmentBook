from abc import ABC, abstractmethod

class Appointment(ABC):
  def __init__(self, title, date, time):
    self.title = title
    self.date = date
    self.time = time
    
  def get_details(self):
    pass

  def reschedule(self, new_date, new_time):
    self.date = new_date
    self.time = new_time
    print(f"Appointment rescheduled to {self.date} at {self.time}")

class MedicalAppointment(Appointment):
  def __init__(self, title, date, time, doctor, location):
    super().__init__(title, date, time)
    self.doctor = doctor
    self.location = location 

  def get_details(self):
    return f"Medical Appointment with {self.doctor} on {self.date} at {self.time}, location: {self.location}"

class BusinessMeeting(Appointment):
  def __init__(self, title, date, time, participants, location):
    super().__init__(title, date, time)
    self.participants = participants
    self.location = location

  def get_details(self):
    return f"Business Meeting on {self.date} at {self.time} with {','.join(self.participants)} at {self.location}"


class AppointmentBook:
  def __init__(self):
    self.appointments = []
  def add_appointment(self, appointment):
    self.appointments.append(appointment)
  def show_appointments(self):
    for appt in self.appointments:
      print(appt.get_details())
  def remove_appointment(self, title):
    self.appointments + [appt for appt in self.appointment if appt.title != title]

if __name__ == "__main__":
  book = AppointmentBook()
  appt1 = MedicalAppointment("Dentist Visit", "2025-02-11", "10:00 AM", "Dr.Smith", "Dental Clinic")
  appt2 = BusinessMeeting("Project Meeting", "2025-02-11", "3:00 PM", ["Alice", "Bob"], "Conference Room")
  book.add_appointment(appt1)
  book.add_appointment(appt2)
  print("Appointments:")
  book.show_appointments()
  appt1.reschedule("2025-02-12", "11:00 AM")
  print("Updated Appointments:")
  book.show_appointments()