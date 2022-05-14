from setuptools import find_packages, setup

setup(
    name='cobolt',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'torch',
        'umap-learn',
        'python-igraph',
        'sklearn',
        'xgboost',
        'pandas',
        'seaborn',
        'leidenalg'
    ],
)
