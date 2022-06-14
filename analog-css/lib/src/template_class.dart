class TemplateClass {
  String name = '';
  Map<String, String> propMap = {};

  TemplateClass(this.name, String properties) {
    if (name[0] == '.') {
      name = name.replaceFirst('.', ''); // Remove '.' from class name if it exists.
    }
    

    for (String propString in properties.split(';')) {
      if (propString.trim() == '') continue;

      // replace the first occurance of ':' so  we can distinguish from
      // any colons used in the property value
      propString = propString.replaceFirst(':', '##COLON##');
      List<String> splitPropString = propString.split('##COLON##');

      String propName = splitPropString[0].trim();
      String propValue = splitPropString[1].trim();

      propMap[propName] = propValue;

    }
  }

  void setProperty(String propName, String propValue) {
    propMap[propValue] = propValue;
  }

  String? getProperty(String propName) {
    return propMap[propName];
  }
}