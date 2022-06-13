import 'dart:io';


String readFile(String path) {
  File file = File(path);
  return file.readAsStringSync();
}

void appendFile(String path, String contents) {
  File file = File(path);
  file.writeAsStringSync(contents, mode: FileMode.append);
}


