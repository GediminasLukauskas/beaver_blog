from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Camp, CampInstance, ChildrenCamp, Reservation, CampReview, Score
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfilisUpdateForm, CampReviewForm, ReservationForm, ScoreForm
from django.urls import reverse
from django.views import View
from django.utils import timezone


# ------------------ žaidimas ------------------

@login_required
def score_view(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            points = form.cleaned_data['points']
            if 'round' not in request.session:
                request.session['round'] = 1
                request.session['points'] = [points]
                request.session['intermediate_sum'] = points
            else:
                round_number = request.session['round']
                points_list = request.session['points']
                points_list.append(points)
                request.session['points'] = points_list
                request.session['intermediate_sum'] = request.session.get('intermediate_sum', 0) + points
                if round_number >= 4:
                    total_points = sum(points_list)
                    Score.objects.get_or_create(user=request.user, points=total_points)
                    del request.session['round']
                    del request.session['points']
                    del request.session['intermediate_sum']
                    return redirect('score_results')
                else:
                    request.session['round'] = round_number + 1
            return redirect('score_view')
    else:
        form = ScoreForm()

    user_scores = Score.objects.filter(user=request.user).order_by('-points')
    if user_scores.exists() and user_scores.first().points is not None:
        user_rank = user_scores.filter(points__gte=user_scores.first().points).count()
    else:
        user_rank = 0

    global_scores = Score.objects.exclude(user=request.user).order_by('-points')
    if user_scores.exists() and user_scores.first().points is not None:
        global_rank = global_scores.filter(points__gte=user_scores.first().points).count()
    else:
        global_rank = 0

    top_scores = Score.objects.order_by('-points')[:50]

    return render(request, 'score.html', {
        'form': form,
        'user_scores': user_scores,
        'user_rank': user_rank,
        'global_scores': global_scores,
        'global_rank': global_rank,
        'top_scores': top_scores,
        'intermediate_sum': request.session.get('intermediate_sum', 0),
    })

def score_results(request):
    all_scores = Score.objects.all().order_by('-points')
    user_score = Score.objects.filter(user=request.user).order_by('-created_at').first()

    if user_score and user_score in all_scores:
        user_rank = list(all_scores).index(user_score) + 1
    else:
        user_rank = None

    context = {
        'all_scores': all_scores,
        'user_score': user_score,
        'user_rank': user_rank
    }

    return render(request, 'score_results.html', context)

# -----------------------------------------------------------

@login_required
def reserve_campsite(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            # Patikriname, ar toks eksempliorius jau yra rezervuotas
            if Reservation.objects.filter(camp_instance=reservation.camp_instance, check_in__lt=reservation.check_out, check_out__gt=reservation.check_in).exists():
                messages.warning(request, 'Ši stovyklavietė jau užimta pasirinktu laiku.')
                return redirect('reserve-campsite')
            reservation.save()
            messages.success(request, 'Jūsų registracija sėkminga')
            return redirect('my-reservation')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

def calendar(request):
    now = timezone.now()
    reserved_camps = Reservation.objects.filter(check_out__gte=now).order_by('check_in')
    num_camp = Camp.objects.all().count()
    num_instances = CampInstance.objects.all().count()
    num_instances_available = CampInstance.objects.filter(status__exact='g').count()
    num_childrenCamp = ChildrenCamp.objects.all().count()

    context = {
        'num_camp': num_camp,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_childrenCamp': num_childrenCamp,
        'reserved_camps': reserved_camps,
    }

    return render(request, 'calendar.html', context=context)


@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user, check_out__gte=timezone.now())
    return render(request, 'myreservation.html', {'reservations': reservations})

def loaned_camps_by_user_list_view(request):
    queryset = CampInstance.objects.filter(consumer=request.user).filter(status__exact='p').order_by('due_back')
    context = {
        'object_list': queryset,
    }
    return render(request, 'myreservation.html', context=context)

# ---------------Registracija į stovyklavietes ---------------
def camps (request):
    camps = Camp.objects.all()
    context = {
        'camps': camps
    }
    return render(request, 'camps.html', context=context)

def camp_detail(request, camp_id):
    if request.method == 'POST':
        camp = get_object_or_404(Camp, pk=camp_id)
        content = request.POST['comment']
        review = CampReview(camp=camp, reviewer=request.user, content=content )
        review.save()
        return redirect('camp', camp_id)
    camp = get_object_or_404(Camp, pk=camp_id)
    print(dir(camp))
    reviews = CampReview.objects.filter(camp=camp).all()
    context = {
        'camp': camp,
        'reviews': reviews

    }
    return render(request, 'camp.html', context)

# ---------------Registracija į vaikų stovyklas ---------------
def children_camp_list (request):
    camps = ChildrenCamp.objects.all()
    context = {
        'camps': camps
    }
    return render(request, 'camps.html', context=context)

def children_camp_detail(request, camp_id):
    if request.method == 'POST':
        camp = get_object_or_404(ChildrenCamp, pk=camp_id)
        content = request.POST['comment']
        review = CampReview(camp=camp, reviewer=request.user, content=content )
        review.save()
        return redirect('camp', camp_id)
    camp = get_object_or_404(ChildrenCamp, pk=camp_id)
    print(dir(camp))
    reviews = CampReview.objects.filter(camp=camp).all()
    context = {
        'camp': camp,
        'reviews': reviews

    }
    return render(request, 'children_camp_detail.html', context)

# ---------------Registracija į Suaugusiuju stovyklas ---------------

# -------------------------------------------------------------

@login_required
def profilis(request):
    return render(request, 'profilis.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis.html', context)

