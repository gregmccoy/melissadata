import requests
import json

class Personator(object):
    """Class for using MelissaData Personator

    Contains methods and attributes to standardize an address
    using Melissa Data

    """
    def __init__(self, custID):
        """__init__

        Defines attributes for Personator Object.

        Args:
                custID (str): ID for Melissa Data account
        """
        self.custID = custID
        self.addr1 = None
        self.addr2 = None
        self.city = None
        self.postal = None
        self.province = None
        self.country = None
        self.name = None
        self.phone = None
        self.recordID = None

    def verify_address(self, addr1="", addr2="", city="", fname="", lname="", phone="", province="", postal="", country="", email="", recordID="", freeform= ""):
        """verify_address

        Builds a JSON request to send to Melissa data. Takes in all needed address info.

        Args:
                addr1 (str):Contains info for Melissa data
                addr2 (str):Contains info for Melissa data
                city (str):Contains info for Melissa data
                fname (str):Contains info for Melissa data
                lname (str):Contains info for Melissa data
                phone (str):Contains info for Melissa data
                province (str):Contains info for Melissa data
                postal (str):Contains info for Melissa data
                country (str):Contains info for Melissa data
                email (str):Contains info for Melissa data
                recordID (str):Contains info for Melissa data
                freeform (str):Contains info for Melissa data

        Returns:
            result, a string containing the result codes from MelissaData
        """
        data = {
            "TransmissionReference": "",
            "CustomerID": self.custID,
            "Actions": "Check",
            "Options": "",
            "Columns": "",
            "Records": [{
                "RecordID": recordID,
                "CompanyName": "",
                "FullName": fname + " " + lname,
                "AddressLine1": addr1,
                "AddressLine2": addr2,
                "Suite": "",
                "City": city,
                "State": province,
                "PostalCode": postal,
                "Country": country,
                "PhoneNumber": phone,
                "EmailAddress": email,
                "FreeForm": freeform,
            }]
        }
        self.country = country
        data = json.dumps(data)
        result = requests.post("https://personator.melissadata.net/v3/WEB/ContactVerify/doContactVerify", data=data)
        result = json.loads(result.text)
        result = self.parse_results(result)
        return result

    def parse_results(self, data):
        """parse_results

        Parses the MelissaData response.

        Args:
                data (dict): Contains MelissaData response

        Returns:
                results, either contains a dict with corrected address info or -1 for an invalid address.
        """
        results = []
        if len(data["Records"]) < 1:
            return -1

        codes = data["Records"][0]["Results"]
        for code in codes.split(","):
            results.append(str(code))

        self.addr1 = data["Records"][0]["AddressLine1"]
        self.addr2 = data["Records"][0]["AddressLine2"]
        self.city = data["Records"][0]["City"]
        self.name = data["Records"][0]["NameFull"]
        self.phone = data["Records"][0]["PhoneNumber"]
        self.province = data["Records"][0]["State"]
        self.postal = data["Records"][0]["PostalCode"]
        self.recordID = data["Records"][0]["RecordID"]
        return results
