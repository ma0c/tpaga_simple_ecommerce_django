from django.conf.urls import url

from . import conf

urlpatterns = [

]

from .views import item

urlpatterns += [
    # item
    url(
        '^item/$',
        item.List.as_view(),
        name=conf.ITEM_LIST_URL_NAME
    ),
    url(
        '^item/create/$',
        item.Create.as_view(),
        name=conf.ITEM_CREATE_URL_NAME
    ),
    url(
        '^item/(?P<pk>\d+)/$',
        item.Detail.as_view(),
        name=conf.ITEM_DETAIL_URL_NAME
    ),
    url(
        '^item/(?P<pk>\d+)/update/$',
        item.Update.as_view(),
        name=conf.ITEM_UPDATE_URL_NAME
    ),
    url(
        '^item/(?P<pk>\d+)/delete/$',
        item.Delete.as_view(),
        name=conf.ITEM_DELETE_URL_NAME
    ),
]

from .views import order

urlpatterns += [
    # order
    url(
        '^order/$',
        order.List.as_view(),
        name=conf.ORDER_LIST_URL_NAME
    ),
    url(
        '^order/create/$',
        order.Create.as_view(),
        name=conf.ORDER_CREATE_URL_NAME
    ),
    url(
        '^order/(?P<slug>[\w-]+)/$',
        order.ProtectedDetail.as_view(),
        name=conf.ORDER_DETAIL_URL_NAME
    ),
    url(
        '^order/(?P<slug>[\w-]+)/update/$',
        order.Update.as_view(),
        name=conf.ORDER_UPDATE_URL_NAME
    ),
    url(
        '^order/(?P<slug>[\w-]+)/delete/$',
        order.Delete.as_view(),
        name=conf.ORDER_DELETE_URL_NAME
    ),

    url(
        '^order/(?P<slug>[\w-]+)/checkout/$',
        order.Checkout.as_view(),
        name=conf.ORDER_CHECKOUT_URL_NAME
    ),
    url(
        '^order/(?P<slug>[\w-]+)/confirm/$',
        order.Confirm.as_view(),
        name=conf.ORDER_CONFIRM_URL_NAME
    ),
    url(
        '^order/(?P<slug>[\w-]+)/refund/$',
        order.Refund.as_view(),
        name=conf.ORDER_REFUND_URL_NAME
    ),
]

from .views import main

urlpatterns += [
    url(
        '^$',
        main.Index.as_view(),
        name=conf.MAIN_INDEX

    )
]
