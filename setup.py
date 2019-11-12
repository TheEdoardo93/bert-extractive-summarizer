from setuptools import setup
from setuptools import find_packages

setup(name='bert-extractive-summarizer',
      version='0.2.1',
      description='Extractive Text Summarization with BERT (multi-linguals BERT models too!)',
      keywords = ['bert', 'pytorch', 'machine learning', 'deep learning', 'extractive summarization', 'summary'],
      long_description=open("README.md", "r", encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      url='https://github.com/TheEdoardo93/bert-extractive-summarizer',
      download_url='https://github.com/dmmiller612/bert-extractive-summarizer/archive/master.zip',
      author='Edoardo Casiraghi',
      author_email='edoardo.casiraghi.93@gmail.com',
      install_requires=['numpy==1.16.3', 'torch==1.0.1', 'spacy==2.1.3', 'transformers==2.1.1', 'Cython==0.29.10', 'tqdm==4.32.2', 'neuralcoref==4.0', 'argparse', 'scikit-learn'],
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
