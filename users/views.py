from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer, PaymentSessionRetrieveSerializer
from users.services import strip_create_product, strip_create_price, strip_create_sessions


class UserCreateAPIView(generics.CreateAPIView):
    """Реализация представления создания уроков через generic. CreateAPIView"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(serializer.validated_data["password"])
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Реализация представления просмотра всех уроков через generic. ListAPIView"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Реализация представления просмотра одного урока через generic. ListAPIView"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Реализация представления изменения урока через generic. UpdateAPIView"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Реализация представления удаления урока через generic. DestroyAPIView"""

    queryset = User.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    """Реализация представления создания оплаты через generic. CreateAPIView"""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        print(payment.course, payment.lesson)
        if payment.course is not None:
            product = strip_create_product(payment.course.title)
        elif payment.lesson is not None:
            product = strip_create_product(payment.lesson.title)

        price = strip_create_price(product, payment.amount)
        session_id, payment_link = strip_create_sessions(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class PaymentSessionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSessionRetrieveSerializer
    queryset = Payment.objects.all()


class PaymentListAPIView(ListAPIView):
    """Реализация представления оплаты курса/урока через ViewSet (полный crud)"""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["payment_method"]
    ordering_fields = ["date_pay"]
    filterset_fields = ["lesson", "course"]
