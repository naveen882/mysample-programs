#usage:  $ pkm pack -f  "create_debian.py"
# https://github.com/cloudify-cosmo/cloudify-packager
#http://packman.readthedocs.org/en/latest/
#pip install packman

COMPONENT_PACKAGES_PATH = '/home/user/ui/'  #Destination path where the debian file has to be stored
PACKAGES_PATH = '/home/user/ui' #source path for which the debian package has to be built
PACKAGES = {
    "naveen": {
        "name": "naveen",
        "version": "0.2.2",
        #"source_urls": [
        #    "http://aphyr.com/riemann/riemann_0.2.2_all.deb",
        #],
        #"depends": [
        #    'openjdk-7-jdk'  #Dependencies : if this package is not installed then the debian package will not be installed until te dependency is satisfied
        #],
        "package_path": "{0}/mycomponent/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/mycomponent/ui/".format(PACKAGES_PATH),
	     "bootstrap_script": "{0}/mycomponent/ui/run.sh".format(PACKAGES_PATH), #After installation this script will be run first .Very useful since if any service has to be started. this script will be in the folder where the debian unzips/installs the folders/files
        "src_package_type": "dir",
        "dst_package_type": "deb"
    },
}



