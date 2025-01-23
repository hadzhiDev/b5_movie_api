from django.shortcuts import redirect


def login_required_custom(func):

    def inner_func(request, *args, **kwargs):
        # print(f'the user is {request.user.is_authenticated}')

        if request.user.is_authenticated and request.user.is_superuser:
            return func(request, *args, **kwargs)
        return redirect('/')

    return inner_func