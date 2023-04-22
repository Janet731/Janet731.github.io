'''
use machine learning to classify audio files
'''
import os

def getAudioFiles():
    '''
    get the audio files
    '''
    return 0

def getFeatures(audioFiles):
    '''
    get the MFCC features
    '''
    return 0

def getLabels(audioFiles):
    '''
    get the labels
    '''
    return 0

def trainModel(features, labels):
    '''
    train the model
    '''
    return 0

def main():
    # get the audio files
    audioFiles = getAudioFiles()

    # get the features
    features = getFeatures(audioFiles)

    # get the labels
    labels = getLabels(audioFiles)

    # train the model
    trainModel(features, labels)

if __name__ == "__main__":
    main()