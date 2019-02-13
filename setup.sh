# remove old versions of the library
pip uninstall -y pyoptclass
rm -rf aptclass/Pyoptclass.egg-info
rm pyoptclass/pyoptclass/__init__.pyc

#install the library
cd pyoptclass
pip2 install -e .