from .models import Basket

class BasketMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        basket_id = request.session.get('basket_id')
        if basket_id:
            basket = Basket.objects.get(id=basket_id)

        else:
            basket = Basket.objects.create()

        if request.user.is_authenticated:
            if not basket.owner:

                request.user.baskets.filter(status=Basket.Status.OPEN).update(status=Basket.Status.CLOSE)
                basket.owner = request.user
                basket.save()

        request.session['basket_id'] = basket.id
        request.basket = basket


        response = self.get_response(request)


        return response