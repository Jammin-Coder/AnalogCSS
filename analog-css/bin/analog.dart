import 'package:analog_css/src/utils.dart';
import 'package:analog_css/src/template_parser.dart';

void main() {
  Map<String, String> classes = TemplateParser('input.css').getClasses();

  for (String className in classes.keys) {
    String properties = classes[className]!;
    print('Class name: $className');
    print('Properties:\n$properties');
  }
}