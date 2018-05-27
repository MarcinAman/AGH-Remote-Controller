import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """
    Capture and convert voice to text
    Note that it is using google API

    :param recognizer: instance of sr.Recogniser()
    :param microphone: instance of sr.Microphone() for capturing voice
    :return:
    """
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        response = recognizer.recognize_google(audio, language='pl-PL')
    except sr.RequestError:
        raise ConnectionError
    except sr.UnknownValueError:
        raise IOError
    return response


def get_text_from_speech():
    """
    High level interface to capture and convert voice (from Microphone) to text
    :return: text made from voice or exception if it was not possible
    """
    r = sr.Recognizer()
    mic = sr.Microphone()

    try:
        response = recognize_speech_from_mic(r, mic)
    except IOError:
        raise IOError
    except ConnectionError:
        raise ConnectionError

    return response
