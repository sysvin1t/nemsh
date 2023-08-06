install:
  @echo "installing nemsh"
  install -Dm755 main.py /usr/bin/nemsh
  install -Dm755 main.py /bin/nemsh

uninstall:
  @echo "removing nemsh"
  rm /usr/bin/nemsh
  rm /bin/nemsh
