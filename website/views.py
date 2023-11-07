from django.shortcuts import render


def home(request):
    language_list = "html+markup+css+clike+javascript+c+csharp+cpp+css+python+r"
    language_list = sorted(language_list.split("+"))

    context = {
        "languages": language_list,
    }

    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        context = {
            "languages": language_list,
            "lang": lang,
            "code": code,
        }

    return render(request, "home.html", context)
