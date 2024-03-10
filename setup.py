import setuptools

setuptools.setup(
    name='delivery',
    version='1.0.0',
    author='karim@gheddache.com',
    description='Predire le temps de livraison',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn==1.3",
        "pandas==2.1.2"
    ]
)