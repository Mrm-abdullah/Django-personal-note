# return redirect('account:recherge2',pk=requ_id.pk)
return redirect('room', rom=room, usern=username)
path('/<str:rom>/?username=/<str:usern>', views.checkview, name='room'),