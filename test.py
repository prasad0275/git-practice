import json
import pprint
import xml.etree.ElementTree as ET
import xmltodict
# import xmltojson

def recur(child):
    # if not isinstance(child, ET.Element):
    #     return print("at end type : ", type(child))
    
    return {
        "attributes": child.attrib,
        "text": child.text,
        "children" : [{x.tag : recur(x) for x in child}]
    }
        

    # return recur(child)

if __name__ == "__main__":
    xml_file_path = "./output.xml"
    json_file_path = "./output.json"
    # convert_xml_to_json(xml_file_path, json_file_path)
    # print(f"Converted {xml_file_path} to {json_file_path}")

    # tree = ET.parse(xml_file_path)
    # root = tree.getroot()
    # doc = {}
    
    # doc[root.tag] = recur(root)

    # pprint.pprint(doc)
    # with open('report.json', 'w') as report:
    #     js = json.dump(doc, report)
    # print(js)

    with open("output.xml") as xml_file:
     
        data_dict = xmltodict.parse(str(xml_file.read()))
               
        with open("data.json", "w") as json_file:
            json_file.write(json.dumps(data_dict))
            # json_file.close()