import 'dart:io';

import 'package:analog_css/src/template_parser.dart';
import 'package:analog_css/src/generator.dart';
import 'package:analog_css/src/markup_parser.dart';
import 'package:analog_css/src/template_class.dart';
import 'package:analog_css/src/utils.dart';

List<String> getMarkupFiles(Iterable files) {
  List<String> markupFiles = [];
  for (File file in files) {
    String fileName = file.path.split('/')[file.path.split('/').length - 1];

    List<String> splitFileName = fileName.split('.');
    String ext = splitFileName[splitFileName.length -1];
    if (ext == 'html' || ext == 'php') {
      markupFiles.add(file.path);
    }
  }

  return markupFiles;
}

List<String> getTemplateFiles(Iterable files) {
  List<String> templateFiles = [];
  for (File file in files) {
    String fileName = file.path.split('/')[file.path.split('/').length - 1];
    List<String> splitFileName = fileName.split('.');
    String ext = splitFileName[splitFileName.length -1];
    if (ext == 'scss' || ext == 'css') {
      templateFiles.add(file.path);
    }
  }

  return templateFiles;
}


void main(List<String> argv) async {
  final dir = Directory('./');
  

  while (true) {
    final List<FileSystemEntity> entities = dir.listSync().toList();
    final Iterable<File> files = entities.whereType<File>();

    List<String> markupFiles = getMarkupFiles(files);
    List<String> templateCssFiles = getTemplateFiles(files);

    List<String> generatedClasses = [];
    List<String> userClassNames = getClassesFromFiles(markupFiles);

    List<TemplateClass> templateClasses = TemplateParser().getTemplateClassesFromFiles(templateCssFiles);
    
    for (String userClass in userClassNames) {
        for (TemplateClass templateClass in templateClasses) {
          Generator generator = Generator(templateClass);

          List<String> matchedClasses = generator.findMatchingCssClasses(userClassNames);
          for (String className in matchedClasses) {
            String generatedClass = generator.generateAnalogClass(className);
            if (!generatedClasses.contains(generatedClass)) {
              generatedClasses.add(generatedClass);
            }
          }
        }
    }

    writeFile('output.css', '');
    for (String _class in generatedClasses) {
      appendFile('output.css', _class);
    }
    
    await Future.delayed(Duration(seconds: 1));
  }
  
}