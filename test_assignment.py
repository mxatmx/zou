import sys
import os
from pprint import pprint

# Ensure we can import zou
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from zou.app import create_app, db
from zou.app.models.person import Person, SoftwarePersonLink
from zou.app.models.software import Software
from zou.app.services import persons_service

app = create_app()

with app.app_context():
    person = Person.query.first()
    software = Software.query.first()
    
    if not person:
        print("No person found.")
        sys.exit(0)
        
    if not software:
        print("No software found. Creating a test software...")
        software = Software(name="Test Software", short_name="TS")
        db.session.add(software)
        db.session.commit()

    print(f"Testing assignment for Person: {person.first_name} ({person.id}) and Software: {software.name} ({software.id})")
    
    # Check existing links
    existing = SoftwarePersonLink.query.filter_by(person_id=person.id).all()
    print(f"Existing links before: {existing}")
    
    # Try the service method
    try:
        res = persons_service.add_software_to_person(person.id, software.id)
        print("Service returned:", res)
    except Exception as e:
        print("Error during add_software_to_person:", e)
        
    # Check if the DB committed it
    links_after = SoftwarePersonLink.query.filter_by(person_id=person.id).all()
    print(f"Existing links after (direct query): {links_after}")
    
    # Check GET service method
    softwares = persons_service.get_software_for_person(person.id)
    print("get_software_for_person returns:", softwares)
    
    print("Done")
