from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
# Create your views here.

def home(request):
    """
    메인 페이지
    """
    3/0
    return render(request, 'index.html')

def QnA(request):
    """
    Q&A 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'poop/question_list.html', context)

def detail(request, question_id):
    """
    Q&A 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'poop/question_detail.html', context)

def answer_create(request, question_id):
    """
    Q&A 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('poop:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'poop/question_detail.html', context)

def question_create(request):
    """
    Q&A 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('poop:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'poop/question_form.html', context)

