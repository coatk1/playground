from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, Http404
# from django.template import loader

from .models import Question


def index(request):

    # Get first 5 questions by date.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # Separate them by comma.
    # output = ', '.join([q.question_text for q in latest_question_list])

    # Load template.
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    # return HttpResponse("Hello, world. You're at the polls index.")
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    # Try to get the question.
    # try:
    #     question = Question.objects.get(pk=question_id)

    # Raise Exception if it does not exist.
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)

    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):

    response = "You're looking at the results of question %s."

    return HttpResponse(response % question_id)


def vote(request, question_id):

    return HttpResponse("You're voting on question %s." % question_id)
