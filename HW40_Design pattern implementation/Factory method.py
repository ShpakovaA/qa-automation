import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

"""
SerializerFactory formats product configuration txt file to the one of the implemented formats (xml, json)
"""


class AbstractSerializer(ABC):
    @abstractmethod
    def serializer(self, file_name):
        pass

    def _file_data_to_dict(self, file):
        dict_ = {}
        with open(file, "r") as f:
            for line in f:
                key, value = line.strip().split(None, 1)
                dict_[key] = value.strip()
        return dict_


class JsonSerializer(AbstractSerializer):
    def serializer(self, file_name):
        dict_ = super()._file_data_to_dict(file_name)
        new_file = file_name + ".json"
        with open(new_file, "w") as f2:
            json.dump(dict_, f2, indent=1)


class XMLSerializer(AbstractSerializer):

    def serializer(self, file_name):
        dict_ = super()._file_data_to_dict(file_name)

        data = ET.Element("ProductInfo")
        for k, v in dict_.items():
            element = ET.SubElement(data, k)
            element.text = v
        xml_data = ET.tostring(data)

        new_file = file_name + ".xml"
        with open(new_file, "wb") as f2:
            f2.write(xml_data)


class SerializerFactory:
    def __init__(self):
        self.serializer_mapping = {'json': JsonSerializer,
                                   'xml': XMLSerializer}

    def get_serializer(self, format_):
        try:
            format_from_mapping = self.serializer_mapping.get(format_)()
        except TypeError:
            print("Format is not implemented")
        else:
            return format_from_mapping


file = "Product info"
serializer = SerializerFactory()

try:
    xml = serializer.get_serializer("xml")
    xml.serializer(file)
    json_ = serializer.get_serializer("json")
    json_.serializer(file)
    other = serializer.get_serializer("other")
    other.serializer(file)
except AttributeError:
    print("Unable to serialize file with no implemented format")

