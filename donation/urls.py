from django.urls import path, include
from donation import views
app_name = 'donation'

urlpatterns = [
    path('donate_money/',views.donatemoneyview,name='donatemoney'),
    path('donate_valuables/',views.donatevaluablesview,name='donate_valuables'),
    path('donation_done/',views.donation_completedview,name='completed'),
    path('requestplaced/',views.donation_completedview,name='request_placed'),
    path('paypal_home/<int:tid>/<int:amount>/<str:orphanage_id1>/',views.paypal_home,name='inprogress'),
    path('paypal_return/',views.paypal_return),
    path('paypal_cancel/',views.paypal_cancel),
    path('paypal/',include('paypal.standard.ipn.urls')),
#    path('facebook/',views.facebookview,name='facebook'),
    path('social/',views.socialview,name='social'),
    path('Accepted/',views.acceptedview,name='accepted'),
    path('Rejected/',views.rejectedview,name='rejected'),
    path('history/',views.historyview,name='history'),

]