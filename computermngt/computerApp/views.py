from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine, Personnel
from .forms import AddMachineForm, AddPersonnelForm


def index(request) :
    #ajout de la ligne de récupération des machines
    #machines = Machine.objects.all()
    #il existe d'autres moyens de filtrer
    #filtrage par numéro de machine
    #machines = Machine.objects.filter(id=1)
    #filtrage par début de nom
    #machines = Machine.objects.filter(nom_startwith="10")
    #Trier les machines selon un champ particulier
    machines = Machine.objects.order_by('-id')
    personnels = Personnel.objects.all()
    context = {}
    
    return render(request, 'index.html', context)

def machine_list_view(request) :
    machines = Machine.objects.all()
    context={'machines': machines}
    return render(request , 'computerApp/machine_list.html', context)
    
def personnel_list_view(request) :
    personnels = Personnel.objects.all()
    context={'personnels': personnels}
    return render(request, 'computerApp/personnel_list.html', context)
    
def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machine': machine}
    return render(request, 'computerApp/machine_detail.html', context)

def machine_detail_view(request, pk):
    personnel = get_object_or_404(Personnel, id=pk)
    context={'personnel': personnel}
    return render(request, 'computerApp/personnel_detail.html', context)
    
def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(name=form.cleaned_data['name'],
                                reseau=form.cleaned_data['reseau'],
                                id=form.cleaned_data['id'],
                                ip=form.cleaned_data['ip'],
                                type_machine=form.cleaned_data['machine_type']) 
            new_machine.save()
            return redirect('machines')
    else:
        form = AddMachineForm()
    context = {'form': form}
    return render(request, 'computerApp/machine_add.html', context)

    
def personnel_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_personnel = Personnel(nom=form.cleaned_data['nom'],
                                      prenom=form.cleaned_data['prenom'],
                                      id=form.cleaned_data['id'],
                                      machine=form.cleaned_data['machine'])
            new_personnel.save()
            return redirect('personnels')
    else :
        form = AddPersonnelForm ( )
        context = {'form': form}
        return render(request, 'computerApp/personnel_add.html',context)

def index(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    context = {'machines': machines, 'personnels': personnels}
    return render(request, 'index.html', context)

def home(request):
    from .forms import SearchForm
    form = SearchForm(request.GET)  # Récupère les données du formulaire GET
    machines = Machine.objects.all()  # Récupère toutes les machines
    personnels = Personnel.objects.all()  # Récupère tous les personnels
    
    if form.is_valid():
        personnel_name = form.cleaned_data['personnel_name']
        # Effectuer la recherche en utilisant le nom du personnel
        
        # Filtrer les résultats en fonction du nom du personnel
        
    context = {
        'form': form,
        'machines': machines,
        'personnels': personnels,
    }
    
    return render(request, 'index.html', context)
    
def global_context(request):
    from .forms import SearchForm
    form = SearchForm()  # Crée une instance du formulaire de recherche
    return {'search_form': form}  # Retourne le formulaire dans le contexte sous la clé 'search_form'
    

def search_results(request):
    from .forms import SearchForm
    form = SearchForm(request.GET) # Crée une instance du formulaire de recherche avec les données GET
    if form.is_valid(): # Récupère les données 
        personnel_name = form.cleaned_data['personnel_name']
        machine_name = form.cleaned_data['machine_name']
        machine_ip = form.cleaned_data['machine_ip']
        
        # Effectue la recherche en utilisant les données fournies
        
        # Passer les résultats de recherche au contexte
      
    context = {
            'form': form,
        }
    return render(request, 'index.html.html', context)
