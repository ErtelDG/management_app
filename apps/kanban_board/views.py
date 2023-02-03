from django.shortcuts import render


def kanban_board(request):
    return render(request, 'kanban_board/kanban_board.html')