from time import sleep

# XML class (Legacy / Incompatible)
class Xml():
    def __init__(self, xmldata: str):
        self._xmldata = xmldata  # fixed attribute

    def getXmldata(self):
        return self._xmldata

# Target Class (expects JSON)
class DataAnalytics_Tool():
    def __init__(self, argJSONdata: str):
        self._jsondata = argJSONdata

    def analyseData(self):
        print("⭕ Analysing data: ", self._jsondata)
        sleep(1)
        print("✅ Analysis completed.")

# Adapter class to convert XML to JSON-like structure
class XmlToJsonAdapter(DataAnalytics_Tool):
    def __init__(self, xml: Xml):
        # convert XML to fake JSON (simulating transformation)
        converted = f'{{"converted_from_xml": "{xml.getXmldata()}"}}'
        super().__init__(converted)

# Client class
class Client():
    def processData(self, tool: DataAnalytics_Tool):
        tool.analyseData()


# Client side using the tool (it should not change the process of using our tool)
if __name__ == "__main__":
    # sample XML data
    to_analyse_data_xml = Xml("!! Sample XML data !!")

    # Adapter used to convert and pass XML as JSON
    # Instead of the tool itself, we make object of Adapter and pass the data the same
    analysis_tool = XmlToJsonAdapter(to_analyse_data_xml)

    # Client processes data with analytics tool
    client_xyz = Client()
    client_xyz.processData(analysis_tool)
