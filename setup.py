from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name="msid",
        packages=find_packages(),
        install_requires=['numpy', 'scipy']
    )
