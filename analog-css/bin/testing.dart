void main(List<String> args) {
  String output = 'ab#{cde}fghijk';

  output = output.replaceAll('#{cde}', 'CDE');
  print(output);
}