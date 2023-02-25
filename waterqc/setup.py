from setuptools import setup, find_packages

setup(
    name='waterqc',
    version='1.0.0',
    description='to predict the fresh water quality',
    packages=['waterqc'],
    package_data={'':["Color.npy","scaler.save","model_0.8708945702948415.pkl"]},
    install_requires=[
        'numpy',
        'pandas',
        'polars',
        'joblib',
        'matplotlib',
        'scikit-learn-intelex',
        'scikit-learn',
        'xgboost==1.5',
        'seaborn'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    include_package_data=True,
    zip_safe=False
)
