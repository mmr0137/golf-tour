from django.shortcuts import render

# Create your views here.
from django.views import generic
from golfer.models import Golfer, TournGolfer, GolferRoundScores
from tournament.models import Tournament
from golf_course.models import GolfCourse, Hole

# First view
# List golfers from home page hyperlinks navigation panel

class GolferListView(generic.ListView):
    model = Golfer
    template_name = 'golfer/golfer_list.html'
    context_object_name = 'golfers'
    
    
class GolferDetailView(generic.DetailView):
    model = Golfer
    template_name = 'golfer/golfer_detail.html'
    
    # override the get_context_data to return the context_object_name
    def get_context_data(self, **kwargs):
        # how to get the context dictionary
        context = super(GolferDetailView, self).get_context_data(**kwargs)
        
        # use the golfer object that was clicked by the user
        golfer = self.get_object()
        
        # use the golfer object to get the rest of the context
        context['golfer'] = golfer
        context['scores'] = GolferRoundScores.getTournScoresByGolfer(golfer.golfer_id)
        
        return context
        
class GolferRoundScoresView(generic.DetailView):
    model = TournGolfer
    template_name = 'golfer/golfer_round_scores.html'
    
    # Override get_context_data method
    def get_context_data(self, **kwargs):
        # Get context dictionary
        context = super(GolferRoundScoresView, self).get_context_data(**kwargs)
        
        # Use the TournGolfer object
        tourn_golfer = self.get_object()
        
        # Pull tourn_golfer into a local variable
        tg_id = self.kwargs.get('pk')
        
        # Retrieve queryset list of GolferRoundScores objects, filtered only to get
        # GolferRoundScores objects whose TournGolfer id is equal to TournGolfer id
        # that was retrieved from the id above
        scores = GolferRoundScores.objects.filter(grs_tourn_golfer_id = tg_id)
        
        # Get the Tournament object
        tournament = Tournament.objects.filter(pk=tourn_golfer.tg_tourn.tourn_id).get()
        
        # Get the GolfCourse object
        golf_course = GolfCourse.objects.filter(pk=tournament.tourn_course.course_id).get()
        
        # Get the list of Hole objects
        holes = Hole.objects.filter(hole_course_id=golf_course.course_id)
        
        # Add results to the context dictionary
        context['tourn_golfer'] = tourn_golfer
        context['golf_course'] = golf_course
        context['scores'] = scores
        context['holes'] = holes
        
        # Return context dictionary
        return context
        
        
        
