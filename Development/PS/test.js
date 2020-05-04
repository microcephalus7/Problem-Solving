const number = Number(prompt());

for (i = 1; i <= number; i++) {
  for (j = 1; j <= i; j++) {
    document.write("*");
  }
  document.write("\n");
}
