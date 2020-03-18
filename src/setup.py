import setuptools

setuptools.setup(
    name                            = "orquestra",
    packages                        = setuptools.find_namespace_packages(include=['orquestra.*']),
    package_dir                     = {
        "" : "python"
    },
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
