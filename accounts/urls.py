from django.urls import path
from .views import account, profile, recommendation

app_name = "accounts"

urlpatterns = [
    # 계정 생성 및 인증
    path("signup/", account.SignUpView.as_view(), name="signup"),
    path("login/", account.LoginView.as_view(), name="login"),
    path("logout/", account.LogoutView.as_view(), name="logout"),
    path("current-user/", account.CurrentUserView.as_view(), name="current_user"),
    path(
        "change-password/", account.PasswordChangeView.as_view(), name="change_password"
    ),
    # 계정 관리
    path("deactivate/", account.UserDeactivateView.as_view(), name="user_deactivate"),
    path("delete/", account.UserDeleteView.as_view(), name="user_delete"),
    path(
        "request-reactivation/",
        account.RequestReactivationView.as_view(),
        name="request_reactivation",
    ),
    path(
        "activate/<uidb64>/<token>/",
        account.ActivateAccountView.as_view(),
        name="activate_account",
    ),
    # 프로필 관련
    path(
        "profile/<str:username>/",
        profile.ProfileDetailView.as_view(),
        name="profile_detail",
    ),
    path("profile/", profile.ProfileUpdateView.as_view(), name="profile_update"),
    path(
        "privacy-settings/<str:username>/",
        profile.PrivacySettingsView.as_view(),
        name="privacy_settings",
    ),
    path("follow/<int:pk>/", profile.FollowView.as_view(), name="follow"),
    path("unfollow/<int:pk>/", profile.UnfollowView.as_view(), name="unfollow"),
    # 프로필 검색
    path("search/", profile.ProfileSearchView.as_view(), name="profile_search"),
    # 친구 추천
    path(
        "recommend/",
        recommendation.FriendRecommendationView.as_view(),
        name="friend_recommendation",
    ),
]
