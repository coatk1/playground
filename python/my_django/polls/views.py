from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Choice, Question


'''
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
'''

class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""

        return Question.objects.order_by('-pub_date')[:5]


'''
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
'''

class DetailView(generic.DetailView):

    model = Question
    template_name = 'polls/detail.html'


'''
def results(request, question_id):

    # response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)

    # return HttpResponse(response % question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

class ResultsView(generic.DetailView):

    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        # Using POST to ensure that data is only altered via a POST call.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):

        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:
        # selected_choice.votes += 1
        # Using F() expressions to avoid race conditions.
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)
