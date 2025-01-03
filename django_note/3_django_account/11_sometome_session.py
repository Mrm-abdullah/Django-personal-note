from django.shortcuts import render

def perform_once_daily(request):
    current_date = request.session.get('current_date')

    if current_date != str(datetime.now().date()):
        # প্রথম ক্লিক হওয়া বাটনের ক্ষেত্রে আপনি করতে চান কী করবেন, এখানে কোড লিখুন

        # উদাহরণস্বরূপ, একটি ডাটাবেসে কিছু তথ্য সংরক্ষণ করা হচ্ছে
        # আপনি এটি আপনার প্রজেক্টের প্রয়োজনীয় অপারেশনের সাথে পরিবর্তন করুন

        # এখানে আপনি কাজের জন্য প্রয়োজনীয় কোড লিখতে পারেন

        # কাজটি সম্পন্ন হওয়ার পর বর্তমান তারিখটি সেশনে সেট করুন
        request.session['current_date'] = str(datetime.now().date())

    return render(request, 'perform_once_daily.html')

from django.shortcuts import render
from datetime import datetime

def perform_once_daily(request):
    current_date = request.session.get('current_date')

    if current_date is None or current_date.date() != datetime.now().date():
        # প্রথম ক্লিক হওয়া বাটনের ক্ষেত্রে আপনি করতে চান কী করবেন, এখানে কোড লিখুন

        # উদাহরণস্বরূপ, একটি ডাটাবেসে কিছু তথ্য সংরক্ষণ করা হচ্ছে
        # আপনি এটি আপনার প্রজেক্টের প্রয়োজনীয় অপারেশনের সাথে পরিবর্তন করুন

        # কাজটি সম্পন্ন হওয়ার পর বর্তমান তারিখটি সেশনে সেট করুন
        request.session['current_date'] = datetime.now()

    return render(request, 'perform_once_daily.html')
