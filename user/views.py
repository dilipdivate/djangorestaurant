
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.dispatch.dispatcher import receiver

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
# from .decorators import user_not_authenticated
from .tokens import account_activation_token

# from .models import Profile
# from .forms import CustomUserCreationForm, ProfileForm

# from .utils import searchProfiles, paginateProfiles

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from user.models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

# # Create your views here.
# def loginUser(request):
#     page = 'login'

#     if request.user.is_authenticated:
#         return redirect('profiles')

#     if request.method == 'POST':
#         username = request.POST['username'].lower()
#         password = request.POST['password']

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'Username does not exist')

#         user = authenticate(request, me=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect(request.GET['next'] if 'next' in request.GET else 'account')

#         else:
#             messages.error(request, 'Username Or Password is incorrect')

#     return render(request, 'user/login_register.html')


# def logoutUser(request):
#     logout(request)
#     messages.info(request, 'User was logged out')
#     return redirect('login')


# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def registerUser(request):
#     user = User.objects.get()
#     # user = request.user.profile
#     data = request.data

#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


# def registerUser(request):
#     page = 'register'
#     form = CustomUserCreationForm()


#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()

#             # messages.success(request, 'User account was created')
#             # return render(request, 'user/login_register.html', context)
#             login(request, user)
#             return redirect('edit-account')
#         else:
#             messages.success(
#                 request, 'An error has occurred during registration')

#     context = {'page': page, 'form': form}
#     return render(request, 'user/login_register.html', context)


# def profiles(request):
#     profiles, search_query = searchProfiles(request)

#     custom_range, profiles = paginateProfiles(request, profiles, 3)

#     context = {"profiles": profiles, "search_query": search_query,
#                "custom_range": custom_range}

#     return render(request, 'user/profiles.html', context)


# def userProfile(request, pk):
#     profile = Profile.objects.get(id=pk)

#     # topSkills = profile.skill_set.exclude(description__exact="")

#     # otherSkills = profile.skill_set.filter(description="")

#     # context = {'profile': profile, 'topSkills': topSkills,
#     #            'otherSkills': otherSkills}

#     context = {'profile': profile}

#     return render(request, 'user/user-profile.html', context)


# @login_required(login_url="login")
# def userAccount(request):
#     profile = request.user.profile

#     # skills = profile.skill_set.all()
#     # projects = profile.project_set.all()

#     # context = {'profile': profile, 'skills': skills, 'projects': projects}
#     context = {'profile': profile}

#     return render(request, 'user/account.html', context)


# @login_required(login_url='login')
# def editAccount(request):
#     profile = request.user.profile
#     form = ProfileForm(instance=profile)

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'user/profile_form.html', context)


# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    # To exclude from authentication
    authentication_classes = ()
    permission_classes = ()
    # token = Token.objects.get(user=user).key
    # data['token'] = token
    serializer_class = UserSerializer


class UserUsList(APIView):
    queryset = User.objects.all()
    # To exclude from authentication
    authentication_classes = ()
    permission_classes = ()
    # token = Token.objects.get(user=user).key
    # data['token'] = token
    serializer_class = LoginSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(email=email, username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView2(APIView):
    """This api will handle login and return token for authenticate user."""

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            print(email, username, password)
            user = authenticate(request, email=email,
                                username=username, password=password)
            print("Dilip1:", user)
            if user is not None:
                """We are reterving the token for authenticated user."""
                token = Token.objects.get(user=user)
                response = {
                    "status": status.HTTP_200_OK,
                    "message": "success",
                    "data": {
                        "Token": token.key
                    }
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid Email or Password",
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "bad request",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('homepage')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(
            request, f'Problem sending email to {to_email}, check if you typed it correctly.')
