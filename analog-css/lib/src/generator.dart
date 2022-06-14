import 'package:analog_css/src/template_class.dart';


class Generator {
  TemplateClass templateClass;
  List<int> parameterPostitions = [];

  List<String> classNameComponents = [];
  int componentCount = 0;
  int parameterCount = 0;

  Generator(this.templateClass) {
    classNameComponents = templateClass.name.split('-');
    parameterPostitions = getPrameterPositions();

    componentCount = classNameComponents.length;
    parameterCount = parameterPostitions.length;
  }

  List<int> getPrameterPositions() {
    List<int> positions = [];
    List<String> components = templateClass.name.split('-');

    for (int i = 0; i < components.length; i++) {
      String component = components[i];
      if (componentIsParam(component)) positions.add(i);
    }

    return positions;
  }

  int getParamCount() {
    return getPrameterPositions().length;
  }

  List<String>? getExpectedParams() {
    var expectedParams = <String>[];

    for (String component in classNameComponents) {
      if (componentIsParam(component)) {
        if (expectedParams.contains(component)) {
          print('Duplicate parameters in ${templateClass.name}');
          return null;
        }

        expectedParams.add(component);
      }
    }

    return expectedParams;
  }

  Map<String, String> getMappedParams(String cssClass) {
    Map<String, String> paramMap = {};
    List<String> cssClassComponents = cssClass.split('-');
    for (int pos in parameterPostitions) {
      String param = classNameComponents[pos];
      paramMap[param] = cssClassComponents[pos];
    }
    
    return paramMap;
  }

  bool componentIsParam(String component) {
    return component[0] == '#' && component[1] == '{';
  }

  bool statementMatchesAnalogClass(String cssClassName) {
    List<String> cssClassComponents = cssClassName.split('-');
    List<String> templateClassComponents = templateClass.name.split('-');

    // Incorrect length
    if (cssClassComponents.length != templateClassComponents.length) return false;

    int i = 0;
    for (String component in cssClassComponents) {
      String templateComponent = templateClassComponents[i];
      if (
        component != templateComponent 
        && !componentIsParam(templateComponent)
        ) return false;
      i++;
    }
    
    return true;
  }

  List<String> findMatchingCssClasses(List<String> classNamesToCompare) {
    List<String> matchedClasses = [];
    for (String cssClass in classNamesToCompare) {
      if (!statementMatchesAnalogClass(cssClass)) continue;
      matchedClasses.add(cssClass);
    }

    return matchedClasses;
  }


  String generateAnalogClass(String cssClass) {
    String output = '.$cssClass {\n';

    for (String propName in templateClass.propMap.keys) {
      String? propValue = templateClass.getProperty(propName);
      output += '\t$propName: $propValue;';
    }

    output += '\n}\n';
    
    Map<String, String> paramMap = getMappedParams(cssClass);
    for (String paramName in paramMap.keys) {
      String paramValue = paramMap[paramName]!.trim();

      RegExp pattern = RegExp(r'' + paramName);

      print(output.replaceAll(pattern, paramValue));
    }


    return output;

  }
}