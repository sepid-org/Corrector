from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(["POST"])
@permission_classes([AllowAny])
def correct(request):
    question = request.data.get('question')
    correct_answer = request.data.get('correct_answer')
    given_answer = request.data.get('given_answer')

    correctness_percentage = 0
    comment = ''

    correct_answer_type = correct_answer.get('answer_type')
    given_answer_type = given_answer.get('answer_type')
    correct_answer_text = correct_answer.get('text')
    given_answer_text = given_answer.get('text')

    print(correct_answer_text, given_answer_text)

    if correct_answer_type == 'SmallAnswer':
        if correct_answer_text == given_answer_text:
            correctness_percentage = 100
            comment = 'بنازم!'
        else:
            comment = 'ای بابا :('
    if correct_answer_type == 'MultiChoiceAnswer':
        if correct_answer_text == given_answer_text:
            correctness_percentage = 100
            comment = 'بنازم!'
        else:
            comment = 'ای بابا :('
    else:
        pass

    return Response(data={'correctness_percentage': correctness_percentage, 'comment': comment})
