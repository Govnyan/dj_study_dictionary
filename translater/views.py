from django.shortcuts import render, HttpResponseRedirect

def home(request):
    return render(request, 'index.html')

def read_from_file(request):
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    return render(request, 'dictionary.html', {'list': dict(zip(words1, words2))})

def add_word(request):
    if request.method == 'POST':
        add_to_file(request.POST['word1'], request.POST['word2'])
        return HttpResponseRedirect('/')
    return render(request, 'translate.html')

def add_to_file(word1: str, word2: str):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")

