#from random import sample


import json

from django.core.serializers import serialize
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import A, Q,U,Quiz


def list_Qs(request):
    Q_qs = Q.objects.all()

    Q_list = []
    for q in Q_qs:
        Q_list.append(
            {
                "question": q.question,
                "category": q.category,
                "answer" : str(q.answer)}
        )
    return JsonResponse(Q_list, safe=False)


@csrf_exempt
def edit_Q(request, id):
    if request.method == "GET":
        q = Q.objects.filter(id=id).values().first()

        return JsonResponse(q, safe=False)
    elif request.method == "PUT":
        data = json.loads(request.body)
        q = get_object_or_404(Q, id=id)
        q.question = data.get("question", q.question)
        q.answer = data.get("answer", q.answer.choice)
        q.category = data.get("category", q.category)
        q.save()
        return JsonResponse({"status": "Updated!"})

    return JsonResponse({"status": "Oops!", "error": "method error"})


@csrf_exempt
@require_http_methods(["POST"])
def create_Q(request):
    data = json.loads(request.body)
    question = data.get("question", None)
    answer = data.get("answer", None)
    category = data.get("category", None)
    if A.objects.filter(choice=answer).values() :
        print("answer founded")
    else:
        create_A(request)
    if question and answer and category:
        As = A.objects.filter(choice=answer).first()
        if As:
            q_obj = Q(question=question, category=category, answer=As)
            q_obj.save()
            return JsonResponse({"status":"201"})
        else:
            raise PermissionDenied
    else:
        return JsonResponse({"error": "you miss some fields"})


def create_A(request):
    data = json.loads(request.body)
    choice = data.get("answer", None)
    category = data.get("category", None)
    a_obj = A(choice=choice, category=category)
    a_obj.save()
    #return JsonResponse({"status": "201"})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_Q (request, id):
    q = get_object_or_404(Q, id=id)
    try:
        q.delete()
        return JsonResponse({"status": "204"})
    except IntegrityError as e:
        return JsonResponse({"error": str(e)})


@require_http_methods(["GET","POST"])
@csrf_exempt
def create_quiz(request,name):
    if request.method == "GET":
        if U.objects.filter(name=name).values():
            print("user founded")
        else:
            create_U(name)
        quiz_list=[]
        for tag in ["pol","sprt","eco","cul","soc"]:
            qs = Q.objects.filter(category=tag).order_by('?').values('id', 'question')[:4]
            for q in qs:
                quiz_list.append(q.get('id'))
        user = U.objects.filter(name=name).first()
        listQ =quiz_list
        a_obj =Quiz(user=user, listQ=listQ)
        a_obj.save()

        return JsonResponse(list(Q.objects.filter(id__in=listQ).values()),safe=False)

    if request.method == "POST":
        data = json.loads(request.body)
        quiz=Quiz.objects.filter(name=name).values().first()
        score=0
        for answer,id in request.answers,quiz.listQ:
            if answer == id:
                score+=1
        q = get_object_or_404(Quiz, user__name=name)
        q.score = score
        q.save()
        return JsonResponse({"status": "score Updated!"})


#@require_http_methods(["GET"])
def create_U (name):
    u_obj = U(name=name)
    u_obj.save()
    return JsonResponse({"status": "201"})

