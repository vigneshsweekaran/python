from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Answer, QuizAttempt

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        score = 0
        total_questions = quiz.questions.count()
        for question in quiz.questions.all():
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answer.objects.get(pk=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1
        quiz_attempt = QuizAttempt.objects.create(quiz=quiz, score=score)
        return redirect('quiz:quiz_result', attempt_id=quiz_attempt.id)
    return render(request, 'quiz/take_quiz.html', {'quiz': quiz})


def quiz_result(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, pk=attempt_id)
    total_questions = attempt.quiz.questions.count()
    percentage = (attempt.score / total_questions) * 100 if total_questions > 0 else 0
    return render(request, 'quiz/quiz_result.html', {
        'attempt': attempt,
        'total_questions': total_questions,
        'percentage': percentage
    })

