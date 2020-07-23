from setuptools import setup


setup(
    name='AAMD',
    packages=['AAMD'],
    version='0.5',
    scripts=['AAMD/amd'],
    description="Employs data science and deep learning to assist therapists treat a common autism symptom that involves interpretation and correlation of facial and speech emotions",
    author='Pranav eranki',
    author_email='pranav.eranki@gmail.com',
    url='https://github.com/PranavEranki/AAMD',
    download_url='https://github.com/PranavEranki/AAMD/tarball/0.1',
    keywords=['data science, emotion recognition, psychology, autism, speech emotion recognition'],  # arbitrary keywords
    classifiers=[],
    install_requires=['SimpleAudioIndexer', 'watson_developer_cloud',
                      'SpeechRecognition', 'matplotlib', 'numpy'],
    license="MIT"
)
