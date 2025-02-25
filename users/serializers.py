import stripe
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        # fields = ("email", "avatar", "phone_number",)
        fields = "__all__"


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentSessionRetrieveSerializer(ModelSerializer):
    status = SerializerMethodField()

    class Meta:
        model = User
        fields = ("status",)

    def get_status(self, obj):
        return stripe.checkout.Session.retrieve(
            obj.session_id,
        )
