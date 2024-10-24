from django.shortcuts import render, redirect
from .models import Player

def game_home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # Check if player exists
        player, created = Player.objects.get_or_create(name=name)
        request.session['player_id'] = player.id  # Save player id in session
        return redirect('game:game_play')
    
    # If a player has played before, retrieve their names
    players = Player.objects.all()
    return render(request, 'game/game_home.html', {'players': players})

def game_play(request):
    player_id = request.session.get('player_id')
    if not player_id:
        return redirect('game:game_home')  # Ensure player has a name
    
    player = Player.objects.get(id=player_id)
    return render(request, 'game/game_play.html', {'player': player})


def save_score(request):
    if request.method == 'POST':
        player_id = request.session.get('player_id')
        score = int(request.POST.get('score'))
        player = Player.objects.get(id=player_id)

        # Update the player's score if it's higher than the previous score
        if score > player.score:
            player.score = score
            player.save()

    return redirect('game:leaderboard')


def leaderboard(request):
    players = Player.objects.all().order_by('-score')  # Order by highest score
    return render(request, 'game/leaderboard.html', {'players': players})
