def get_post_user(request):
    return Response.objects.filter(response_to__user=request.user)


class ResponseFilter(FilterSet):
    response_to = ModelChoiceFilter(
        queryset=get_post_user
    )

    class Meta:
        model = Response
        fields = {
            'response_to': ['exact']
        }