if pip list --format columns | grep Pyoptclass;
then
	pip uninstall Pyoptclass;
else 
	echo "Instalation not found."
fi


rm -rf pyoptclass/Pyoptclass.egg-info
rm pyoptclass/pyoptclass/*.pyc
rm -rf __pycache__
rm -rf .pytest_cache
rm -rf pyoptclass/pyoptclass/tests/__pycache__

#install the library
cd pyoptclass
pip2 install -e .