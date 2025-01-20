import os
import typing
import xml.dom.minidom
import xml.etree.ElementTree

def write_checkpoint(fchk: str, content: typing.Union[list[float], list[list[float]]], header: str) -> None:
    """
    Writes the checkpoint data to an XML file.

    This function parses the provided checkpoint file (fchk), retrieves its root element, 
    and is intended to update or modify the XML tree based on the provided content and header.

    Args:
    -----
    fchk (str): The path to the checkpoint file (XML file) to be parsed.
    content (Union[list[float], list[list[float]]]): The content to be written to the XML file.
        This can either be:
        - A list of floats, or
        - A list of lists of floats. The structure of the content will determine how the XML is updated.
    header (str): A header or identifier string to be added or associated with the content in the XML file.
    
    Returns:
    --------
    None: This function does not return a value. It modifies the XML structure and writes it back to the file.
    """
    if not os.path.exists(fchk):
        _root_element = xml.etree.ElementTree.Element("checkpoint")
        _geom_element = xml.etree.ElementTree.SubElement("geometry")
        _dens_element = xml.etree.ElementTree.SubElement("density")
        _tree         = xml.etree.ElementTree.ElementTree(root)
        _tree.write(fchk)
    else:
        _tree = xml.etree.ElementTree.parse(fchk)
        _root = _tree.getroot()
