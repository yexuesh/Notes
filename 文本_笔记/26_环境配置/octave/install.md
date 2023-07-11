# install

官网: https://octave.org/

官网教程: https://wiki.octave.org/Octave_for_GNU/Linux#Distribution_independent

```sh
# apt
apt install octave
apt install liboctave-dev  # development files

# snap
snap install octave
# or If you want to use a nightly snapshot build of the development branch of Octave, install from the edge channel
snap install --edge octave

# yum
yum install epel-release
yum install octave
yum install octave-devel  # development files

# Anaconda
 conda create --name octave
 conda activate octave
 conda install -c conda-forge octave

# Docker
docker pull docker.io/gnuoctave/octave:8.2.0
``` 

