# melissadata
A Python interface for MelissaData JSON API

Currently only supports the MelissaData Personator.

## Installation
`pip install git+https://github.com/gregmccoy/melissadata.git`

## Example
```python
m = Personator("<License Token>")

response = m.verify_address(addr1="123 Test St", city="Fakevile", province="ON", country="Canada", postal="L2Y4J6")

#The Personator Object now contains the standardized data
print(m.addr1 + m.city + m.province)

#Reponse contains a list of codes returned by melissa data see <a href="http://wiki.melissadata.com/index.php?title=Result_Codes">http://wiki.melissadata.com/index.php?title=Result_Codes</a>
print(response)
```
