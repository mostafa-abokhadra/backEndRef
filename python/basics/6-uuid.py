"""
        UUID, Universal Unique Identifier, is a python library which helps in generating random
        objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of
        time, Computer hardware (MAC etc.).
"""
import uuid
print(uuid.uuid1())
"""
    generate the random id using MAC address and time component.
    so it compromise the privacy as it uses MAC address
"""
print(uuid.uuid4()) # don't use mac address so better for privacy