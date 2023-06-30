from django.shortcuts import render

def recommendation_view(request):
    music_recommendations = ["Song 1", "Song 2", "Song 3"]
    task_recommendations = ["Task 1", "Task 2", "Task 3"]

    context = {
        'music_recommendations': music_recommendations,
        'task_recommendations': task_recommendations
    }

    return render(request, 'recommendation.html', context)
