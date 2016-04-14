from melissadata import Personator
from random import randint

m = Personator("V6moZUuxCRHXnaLEG2oPm2==QAdUZpxMasAIb7FnHhE8xB==")
response = m.verify_address(addr1="1030 Windham Rd 14", city="Simcoe", province="ON", country="Canada", postal="N3Y4K6", recordID=randint(0, 9999999999999999999999999))

print(response)
print(m.addr1)
