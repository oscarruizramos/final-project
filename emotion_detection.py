from emotion_detection import EmotionDetection

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using the EmotionDetection function.

    Parameters:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: The emotion detection results.
    """
    response = EmotionDetection(text_to_analyze)
    return response
