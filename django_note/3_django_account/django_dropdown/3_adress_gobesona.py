""" 
def Member_Address(request):
    if request.method == "POST" or request.method == "post" and request.user.is_authenticated:
        saddress = request.POST['saddress']
        village = request.POST['village']
        village_id = int(village)
        if Village.objects.filter(id=village_id).exists():
            village = Village.objects.get(id=village_id)
            ward = Ward.objects.get(id=village.ward_id)
            union = Union.objects.get(id=ward.union_id)
            upzilla = Upzilla.objects.get(id=union.upzilla_id)
            district = District.objects.get(id=upzilla.district_id)
            division = Division.objects.get(id=district.division_id)

            user = request.user
            if saddress == 'birthplacea':
                if Birthplace_Address.objects.filter(user=user).exists():
                    messages.info(request, 'adress already exit')
                    return redirect('account:profile')
                else:
                    obj = Birthplace_Address(user=user, birth_division=division, birth_district= district, birth_upzilla= upzilla, birth_union=union, birth_ward=ward, birth_village=village, birth_ad_avalable= True )
                    obj.save()
                    messages.info(request, 'Birthplace Address Succesfully save')
                    return redirect('account:profile')
            elif saddress == 'permanenta':
                if Permanent_Address.objects.filter(user=user).exists():
                    messages.info(request, 'Permanent Address already exit')
                    return redirect('account:profile')
                else:
                    obj = Permanent_Address(user=user, permanent_division=division, permanent_district= district, permanent_upzilla= upzilla, permanent_union=union, permanent_ward=ward, permanent_village=village, permanent_ad_avalable= True )
                    obj.save()
                    messages.info(request, ' Permanent Address Succesfully save')
                    return redirect('account:profile')
            elif saddress == 'currenta':
                if Current_Address.objects.filter(user=user).exists():
                    messages.info(request, 'Current Address already exit')
                    return redirect('account:profile')
                else:
                    obj = Current_Address(user=user, currentt_division=division, current_district= district, current_upzilla= upzilla, current_union=union, current_ward=ward, current_village=village, current_ad_avalable= True )
                    obj.save()
                    messages.info(request, 'Birthplace Address Succesfully save')
                    return redirect('account:profile')
            else:
                messages.info(request, 'Address not save')
                return redirect('account:profile')
        else:
            messages.info(request, 'Please select your village, jodi tomar village na thake, admin k message dao')
            return redirect('account:profile')

 """