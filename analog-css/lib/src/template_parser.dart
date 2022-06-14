import '../src/utils.dart';
import 'package:analog_css/src/template_class.dart';

class TemplateParser {
  String getClassNameFromLine(String line) {
    String className = '';
    List<String> chars = line.split('');
    for (int i = 0; i < chars.length; i++) {
		String char = chars[i];
		if (char == '{' && chars[i - 1] != '#') break;
			
		className += char;
    }

    return className;
  }
        
  bool isClassDefLine(line) {
      return line != "" && line[0] == ".";
  }

  List<TemplateClass> getTemplateClassesFromFile(String file) {
    String fileContents = readFile(file);
	List<TemplateClass> templateClasses = [];

    // If parse_class is True, that means the program found a CSS class name, 
    // so it should grab all the properties under it (in that class)
    
    bool parseClass = false;
    
    String currentClassProperties = '';
    String currentClassName = '';

    for (String line in fileContents.split("\n")) {
        // This means the program found a CSS class
        if (isClassDefLine(line)) {
          // Since the program found a CSS class, set parse_class to True so next 
          // itteration start adding the class properties to the current_class_properties list """
          parseClass = true;
          currentClassName = getClassNameFromLine(line);
          continue;
        }
            

        if (parseClass) {
          for (String char in line.split('\n')) {
            if (char == "}") {
				TemplateClass templateClass = TemplateClass(currentClassName, currentClassProperties);
				templateClasses.add(templateClass);

                // Reset the current class attributes to nothing
                currentClassProperties = "";
                currentClassName = "";

                parseClass = false;
                break;
            }

            currentClassProperties += char;
          }
        }
    }
    
    return templateClasses;
  }

  List<TemplateClass> getTemplateClassesFromFiles(List<String> files) {
    List<TemplateClass> templateClasses = [];

    for (String file in files) {
      List<TemplateClass> tempClasses = getTemplateClassesFromFile(file);
	  for (TemplateClass tempClass in tempClasses) {
		  templateClasses.add(tempClass);
	  }
    }

    return templateClasses;
  }
}


