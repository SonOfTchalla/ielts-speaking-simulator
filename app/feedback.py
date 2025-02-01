# Provide feedback to user
def generate_feedback(text, scores):
    feedback = f"""
    Fluency: {scores['fluency']}/10
    Grammar: {scores['grammar']}/10
    Vocabulary: {scores['vocabulary']}/10

    Suggestions:
    - Try to speak more fluently with fewer pauses.
    - Use a wider range of vocabulary.
    - Check your grammar for minor errors.
    """
    return feedback